import React, { useState, useRef, useEffect } from 'react';
import {
  Camera,
  Upload,
  RefreshCw,
  Sparkles,
  AlertTriangle,
  CheckCircle2,
  Image as ImageIcon,
  ArrowRight,
  Maximize2,
  RotateCcw,
  Zap,
} from 'lucide-react';
import { DiagnosisResultData, WeatherData } from '../types';
import { analyzeCropImage } from '../services/diseaseDetection';
import { DEMO_SCAN_SAMPLES, DemoScanSample } from '../data/sampleCrops';

interface CropScannerProps {
  onDiagnosisComplete: (result: DiagnosisResultData, imageUri: string) => void;
  locationName: string;
  weather: WeatherData;
}

const ANALYSIS_STAGES = [
  'Image processing and normalization...',
  'Disease pattern & lesion detection...',
  'Crop taxonomy identification...',
  'Environmental & weather cross-analysis...',
  'Synthesizing diagnostic report...',
];

export const CropScanner: React.FC<CropScannerProps> = ({
  onDiagnosisComplete,
  locationName,
  weather,
}) => {
  // Input mode: 'idle' | 'camera' | 'upload'
  const [mode, setMode] = useState<'idle' | 'camera' | 'upload'>('idle');
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [selectedSample, setSelectedSample] = useState<DemoScanSample | null>(null);
  const [selectedMimeType, setSelectedMimeType] = useState<string>('image/jpeg');
  const [cropHint, setCropHint] = useState<string>('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [currentStageIdx, setCurrentStageIdx] = useState(0);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  // Camera stream state
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const [isCameraActive, setIsCameraActive] = useState(false);
  const [facingMode, setFacingMode] = useState<'environment' | 'user'>('environment');
  const [cameraError, setCameraError] = useState<string | null>(null);

  const fileInputRef = useRef<HTMLInputElement | null>(null);

  // Stop camera on unmount or mode change
  useEffect(() => {
    return () => {
      stopCamera();
    };
  }, []);

  const stopCamera = () => {
    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => track.stop());
      streamRef.current = null;
    }
    setIsCameraActive(false);
  };

  const startCamera = async (facing: 'environment' | 'user' = facingMode) => {
    setCameraError(null);
    setErrorMessage(null);
    stopCamera();

    try {
      const constraints: MediaStreamConstraints = {
        video: {
          facingMode: { ideal: facing },
          width: { ideal: 1280 },
          height: { ideal: 720 },
        },
      };

      const stream = await navigator.mediaDevices.getUserMedia(constraints);
      streamRef.current = stream;

      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.play();
      }
      setIsCameraActive(true);
      setMode('camera');
    } catch (err: any) {
      console.warn('Camera access failed:', err);
      setCameraError(
        'Camera permission was denied or camera is unavailable. You can upload an image or choose one of our sample crops below.'
      );
      setIsCameraActive(false);
    }
  };

  const handleCapturePhoto = () => {
    if (!videoRef.current) return;

    const video = videoRef.current;
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth || 640;
    canvas.height = video.videoHeight || 480;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const dataUrl = canvas.toDataURL('image/jpeg', 0.9);

    stopCamera();
    setSelectedImage(dataUrl);
    setSelectedSample(null);
    setSelectedMimeType('image/jpeg');
    setMode('idle');
  };

  const toggleCameraFacing = () => {
    const nextFacing = facingMode === 'environment' ? 'user' : 'environment';
    setFacingMode(nextFacing);
    startCamera(nextFacing);
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    if (!file.type.match(/image\/(jpeg|jpg|png|webp)/i)) {
      setErrorMessage('Please upload a valid image file (JPG, JPEG, PNG, or WEBP).');
      return;
    }

    if (file.size > 20 * 1024 * 1024) {
      setErrorMessage('Image size is too large (maximum 20MB). Please select a smaller photo.');
      return;
    }

    setErrorMessage(null);
    setSelectedMimeType(file.type);

    const reader = new FileReader();
    reader.onload = (event) => {
      if (typeof event.target?.result === 'string') {
        setSelectedImage(event.target.result);
        setSelectedSample(null);
        stopCamera();
        setMode('idle');
      }
    };
    reader.readAsDataURL(file);
  };

  const handleSelectSample = (sample: DemoScanSample) => {
    stopCamera();
    setSelectedImage(sample.thumbnailUrl);
    setSelectedSample(sample);
    setSelectedMimeType('image/jpeg');
    setCropHint(sample.crop);
    setErrorMessage(null);
    setMode('idle');
  };

  const handleAnalyze = async () => {
    if (!selectedImage) {
      setErrorMessage('Please select or capture a crop photograph first.');
      return;
    }

    setIsAnalyzing(true);
    setErrorMessage(null);
    setCurrentStageIdx(0);

    // Staged progress ticker
    const interval = setInterval(() => {
      setCurrentStageIdx((prev) => {
        if (prev < ANALYSIS_STAGES.length - 1) {
          return prev + 1;
        }
        return prev;
      });
    }, 600);

    try {
      // If user selected one of the preset benchmark samples, use its verified pathology profile
      if (selectedSample && selectedImage === selectedSample.thumbnailUrl) {
        await new Promise((resolve) => setTimeout(resolve, 2000));
        clearInterval(interval);
        setIsAnalyzing(false);
        const result = {
          ...selectedSample.mockDiagnosis,
          location: locationName,
        };
        onDiagnosisComplete(result, selectedImage);
        return;
      }

      // Live image analysis via Gemini 3.8 Flash on server
      const result = await analyzeCropImage({
        imageBase64: selectedImage,
        mimeType: selectedMimeType,
        cropHint: cropHint || undefined,
        location: locationName,
        weather: {
          temp: weather.current.temp,
          humidity: weather.current.humidity,
          condition: weather.current.condition,
        },
      });

      clearInterval(interval);
      setIsAnalyzing(false);
      onDiagnosisComplete(result, selectedImage);
    } catch (err: any) {
      clearInterval(interval);
      setIsAnalyzing(false);
      setErrorMessage(
        err.message || 'Unable to complete crop diagnosis. Please verify your connection or try another photograph.'
      );
    }
  };

  const resetSelection = () => {
    stopCamera();
    setSelectedImage(null);
    setSelectedSample(null);
    setErrorMessage(null);
    setMode('idle');
  };

  return (
    <section id="scanner-section" className="py-12 lg:py-16">
      <div className="max-w-4xl mx-auto px-4 sm:px-6">
        {/* Section Header */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#EBF3ED] text-[#255238] text-xs font-semibold mb-2">
            <Camera className="w-3.5 h-3.5" />
            <span>AI Computer Vision Engine</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-serif font-bold text-[#142C1F] tracking-tight">
            Scan Your Crop
          </h2>
          <p className="text-sm text-[#526356] max-w-lg mx-auto mt-2 leading-relaxed">
            Take a clear photo of an affected leaf, stem, or plant canopy. Our vision model identifies pathologies, estimates severity, and correlates with your local weather.
          </p>
        </div>

        {/* Error message banner */}
        {errorMessage && (
          <div className="mb-6 p-4 rounded-xl bg-rose-50 border border-rose-200 text-rose-900 text-xs flex items-start gap-3">
            <AlertTriangle className="w-4 h-4 text-rose-600 shrink-0 mt-0.5" />
            <div>
              <p className="font-semibold">Diagnostic Notice</p>
              <p className="mt-0.5">{errorMessage}</p>
            </div>
          </div>
        )}

        {/* Main Scanner Container */}
        <div className="bg-white rounded-2xl border border-[#DFE7DF] shadow-md overflow-hidden">
          {/* Active Camera View */}
          {mode === 'camera' && (
            <div className="relative aspect-4/3 sm:aspect-16/10 bg-black flex items-center justify-center overflow-hidden">
              <video
                ref={videoRef}
                playsInline
                autoPlay
                muted
                className="w-full h-full object-cover"
              />

              {/* Viewfinder reticle overlay */}
              <div className="absolute inset-0 pointer-events-none flex items-center justify-center">
                <div className="w-64 h-64 sm:w-80 sm:h-80 border-2 border-white/60 rounded-2xl relative">
                  <div className="absolute -top-1 -left-1 w-6 h-6 border-t-4 border-l-4 border-[#234E35]" />
                  <div className="absolute -top-1 -right-1 w-6 h-6 border-t-4 border-r-4 border-[#234E35]" />
                  <div className="absolute -bottom-1 -left-1 w-6 h-6 border-b-4 border-l-4 border-[#234E35]" />
                  <div className="absolute -bottom-1 -right-1 w-6 h-6 border-b-4 border-r-4 border-[#234E35]" />
                </div>
              </div>

              {/* Camera Controls bar */}
              <div className="absolute bottom-4 inset-x-0 flex items-center justify-center gap-6 px-4">
                <button
                  type="button"
                  onClick={toggleCameraFacing}
                  className="p-3 rounded-full bg-black/60 text-white hover:bg-black/80 transition"
                  title="Switch camera"
                >
                  <RotateCcw className="w-5 h-5" />
                </button>

                <button
                  type="button"
                  onClick={handleCapturePhoto}
                  className="w-16 h-16 rounded-full bg-white border-4 border-[#234E35] flex items-center justify-center shadow-lg active:scale-95 transition cursor-pointer"
                  title="Capture photograph"
                >
                  <div className="w-12 h-12 rounded-full bg-[#234E35]" />
                </button>

                <button
                  type="button"
                  onClick={stopCamera}
                  className="p-3 rounded-full bg-black/60 text-white hover:bg-black/80 transition text-xs font-semibold"
                >
                  Cancel
                </button>
              </div>
            </div>
          )}

          {/* Camera Error banner if denied */}
          {cameraError && mode !== 'camera' && (
            <div className="p-4 bg-amber-50 border-b border-amber-200 text-amber-900 text-xs flex items-center gap-2">
              <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0" />
              <span>{cameraError}</span>
            </div>
          )}

          {/* Selected Image Preview (Ready for Analysis) */}
          {selectedImage && mode !== 'camera' && (
            <div className="p-6">
              <div className="relative aspect-16/10 sm:aspect-16/9 rounded-xl overflow-hidden bg-[#24352A] shadow-inner max-h-[420px]">
                <img
                  src={selectedImage}
                  alt="Selected crop leaf for diagnosis"
                  className="w-full h-full object-contain"
                />

                {/* Scanning line animation during analysis */}
                {isAnalyzing && (
                  <div className="absolute inset-0 pointer-events-none">
                    <div className="absolute inset-x-0 h-1 bg-[#4CE27A] shadow-[0_0_12px_#4CE27A] animate-scan-line" />
                    <div className="absolute inset-0 bg-[#234E35]/15 backdrop-blur-[0.5px]" />
                  </div>
                )}

                {/* Retake / Change image button */}
                {!isAnalyzing && (
                  <button
                    onClick={resetSelection}
                    className="absolute top-3 right-3 bg-black/70 hover:bg-black/90 text-white text-xs font-medium px-3 py-1.5 rounded-lg backdrop-blur-md flex items-center gap-1.5 transition cursor-pointer"
                  >
                    <RefreshCw className="w-3.5 h-3.5" />
                    <span>Change Image</span>
                  </button>
                )}
              </div>

              {/* Progress feedback when analyzing */}
              {isAnalyzing ? (
                <div className="mt-6 p-5 bg-[#F4F8F4] rounded-xl border border-[#DCE8DC] text-center space-y-3">
                  <div className="flex items-center justify-center gap-2 text-[#234E35] font-serif font-bold text-lg">
                    <RefreshCw className="w-5 h-5 animate-spin" />
                    <span>Analyzing your crop...</span>
                  </div>
                  <p className="text-xs text-[#4F6254] font-medium transition">
                    {ANALYSIS_STAGES[currentStageIdx]}
                  </p>
                  <div className="w-full bg-[#E2EBE2] h-2 rounded-full overflow-hidden max-w-md mx-auto">
                    <div
                      className="bg-[#234E35] h-full rounded-full transition-all duration-500 ease-out"
                      style={{
                        width: `${((currentStageIdx + 1) / ANALYSIS_STAGES.length) * 100}%`,
                      }}
                    />
                  </div>
                  <div className="flex justify-between max-w-md mx-auto text-[10px] text-[#788C7D] pt-1">
                    <span>Stage {currentStageIdx + 1} of 5</span>
                    <span>AI Pathology & Weather Correlator</span>
                  </div>
                </div>
              ) : (
                /* Crop Hint & Analyze Button */
                <div className="mt-6 flex flex-col sm:flex-row items-center justify-between gap-4 pt-2 border-t border-[#EDF2EE]">
                  <div className="w-full sm:w-auto flex items-center gap-2">
                    <label htmlFor="crop-select" className="text-xs font-semibold text-[#3E5244] shrink-0">
                      Crop (Optional):
                    </label>
                    <select
                      id="crop-select"
                      value={cropHint}
                      onChange={(e) => setCropHint(e.target.value)}
                      className="text-xs py-2 px-3 bg-[#F7FAF7] border border-[#D5E0D6] rounded-lg text-[#1E2E22] focus:outline-none focus:border-[#234E35]"
                    >
                      <option value="">Auto-Detect Crop (Any of 240+ species)</option>
                      <optgroup label="Maharashtra Key Cash & Food Crops">
                        <option value="Cotton">Cotton (कापूस)</option>
                        <option value="Soybean">Soybean (सोयाबीन)</option>
                        <option value="Sugarcane">Sugarcane (ऊस)</option>
                        <option value="Onion">Onion (कांदा)</option>
                        <option value="Pomegranate">Pomegranate (डाळिंब)</option>
                        <option value="Grapes">Grapes (द्राक्षे)</option>
                        <option value="Banana">Banana (केळी)</option>
                        <option value="Alphonso Mango">Mango (हापूस आंबा)</option>
                        <option value="Turmeric">Turmeric (हळद)</option>
                        <option value="Orange / Citrus">Nagpur Orange (संत्रे)</option>
                        <option value="Jowar / Sorghum">Jowar (ज्वारी)</option>
                      </optgroup>
                      <optgroup label="Major National Crops">
                        <option value="Rice / Paddy">Rice / Paddy (भात/धान)</option>
                        <option value="Wheat">Wheat (गहू)</option>
                        <option value="Corn / Maize">Maize (मका)</option>
                        <option value="Tomato">Tomato (टोमॅटो)</option>
                        <option value="Potato">Potato (बटाटा)</option>
                        <option value="Chilli / Pepper">Chilli / Pepper (मिरची)</option>
                        <option value="Groundnut">Groundnut / Peanut (भुईमूग)</option>
                        <option value="Chickpea / Gram">Chickpea / Chana (हरभरा)</option>
                        <option value="Mustard">Mustard (मोहरी/सरसों)</option>
                        <option value="Tea">Tea (चहा)</option>
                      </optgroup>
                    </select>
                  </div>

                  <button
                    onClick={handleAnalyze}
                    className="w-full sm:w-auto px-8 py-3.5 bg-[#234E35] hover:bg-[#1A3D29] text-white font-semibold text-sm rounded-xl transition shadow-sm hover:shadow-md flex items-center justify-center gap-2 cursor-pointer group"
                  >
                    <Sparkles className="w-4 h-4 text-[#8CE39B]" />
                    <span>Analyze Crop</span>
                    <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition" />
                  </button>
                </div>
              )}
            </div>
          )}

          {/* Empty Selection State: Two Large Options */}
          {!selectedImage && mode !== 'camera' && (
            <div className="p-6 sm:p-10 text-center">
              {/* Two clear buttons */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 max-w-lg mx-auto">
                <button
                  type="button"
                  onClick={() => startCamera('environment')}
                  className="p-6 rounded-xl border-2 border-dashed border-[#BCD0C0] hover:border-[#234E35] bg-[#F9FAF8] hover:bg-[#F2F7F3] transition flex flex-col items-center justify-center gap-3 cursor-pointer group"
                >
                  <div className="w-12 h-12 rounded-full bg-[#E5EFE7] group-hover:bg-[#234E35] text-[#234E35] group-hover:text-white transition flex items-center justify-center">
                    <Camera className="w-6 h-6" />
                  </div>
                  <div>
                    <span className="font-serif font-bold text-sm text-[#142C1F] block">
                      Take Photograph
                    </span>
                    <span className="text-[11px] text-[#637568] block mt-0.5">
                      Use device camera with instant capture
                    </span>
                  </div>
                </button>

                <button
                  type="button"
                  onClick={() => fileInputRef.current?.click()}
                  className="p-6 rounded-xl border-2 border-dashed border-[#BCD0C0] hover:border-[#234E35] bg-[#F9FAF8] hover:bg-[#F2F7F3] transition flex flex-col items-center justify-center gap-3 cursor-pointer group"
                >
                  <div className="w-12 h-12 rounded-full bg-[#E5EFE7] group-hover:bg-[#234E35] text-[#234E35] group-hover:text-white transition flex items-center justify-center">
                    <Upload className="w-6 h-6" />
                  </div>
                  <div>
                    <span className="font-serif font-bold text-sm text-[#142C1F] block">
                      Upload Image
                    </span>
                    <span className="text-[11px] text-[#637568] block mt-0.5">
                      JPG, JPEG, PNG or WEBP (up to 20MB)
                    </span>
                  </div>
                </button>
              </div>

              {/* Hidden file input */}
              <input
                ref={fileInputRef}
                type="file"
                accept="image/jpeg,image/jpg,image/png,image/webp"
                onChange={handleFileUpload}
                className="hidden"
              />

              {/* Helper text & Non-Plant Reminder */}
              <div className="mt-6 max-w-lg mx-auto space-y-2 text-xs text-[#526356]">
                <div className="flex items-center justify-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-[#2D5A3C] shrink-0" />
                  <span>
                    <strong>Best results:</strong> capture a clear, close-up photo of the leaf surface or canopy in good natural lighting.
                  </span>
                </div>
                <div className="p-2.5 rounded-lg bg-[#F5F8F5] border border-[#DEE7DF] text-[11px] text-[#475C4C] text-center">
                  <span>🔬 <strong>Botanical Tissue Filter Active:</strong> AgroVision AI verifies biological chloroplasts and leaf margins. Walls, floors, or non-plant objects are automatically filtered out.</span>
                </div>
              </div>

              {/* Sample Leaf Presets for Quick Testing */}
              <div className="mt-8 pt-6 border-t border-[#EEF3EF]">
                <span className="text-xs font-semibold text-[#5A6D5F] uppercase tracking-wider block mb-3">
                  Or test immediately with a sample crop:
                </span>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-xl mx-auto">
                  {DEMO_SCAN_SAMPLES.map((sample) => (
                    <button
                      key={sample.id}
                      type="button"
                      onClick={() => handleSelectSample(sample)}
                      className="p-2 rounded-xl border border-[#DFE7E0] hover:border-[#234E35] bg-white hover:bg-[#F8FAF8] transition text-left cursor-pointer group"
                    >
                      <div className="aspect-4/3 rounded-lg overflow-hidden bg-gray-100 mb-2">
                        <img
                          src={sample.thumbnailUrl}
                          alt={sample.name}
                          className="w-full h-full object-cover group-hover:scale-105 transition"
                        />
                      </div>
                      <p className="text-[11px] font-bold text-[#142C1F] truncate">{sample.name}</p>
                      <p className="text-[10px] text-[#6C7E70] truncate">{sample.condition}</p>
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </section>
  );
};
