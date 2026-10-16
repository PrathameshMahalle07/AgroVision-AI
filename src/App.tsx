import React, { useState, useEffect } from 'react';
import { Navbar, NavTab } from './components/Navbar';
import { HeroSection } from './components/HeroSection';
import { CropScanner } from './components/CropScanner';
import { DiagnosisResult } from './components/DiagnosisResult';
import { WeatherIntelligence } from './components/WeatherIntelligence';
import { RecommendedActions } from './components/RecommendedActions';
import { AgriculturalNews } from './components/AgriculturalNews';
import { CropKnowledge } from './components/CropKnowledge';
import { CropHealthHistory } from './components/CropHealthHistory';
import { AiCropAssistant } from './components/AiCropAssistant';
import { DashboardView } from './components/DashboardView';
import { LocationModal } from './components/LocationModal';
import { ScanModal } from './components/ScanModal';
import { Footer } from './components/Footer';
import { AndroidBottomNav } from './components/AndroidBottomNav';
import { AndroidInstallBanner } from './components/AndroidInstallBanner';
import { AndroidInstallModal } from './components/AndroidInstallModal';
import { usePWAInstall } from './hooks/usePWAInstall';

import {
  DiagnosisResultData,
  WeatherData,
  ScanRecord,
} from './types';
import { LocationInfo, POPULAR_AG_REGIONS } from './services/location';
import { fetchWeatherData } from './services/weather';

export default function App() {
  const [activeTab, setActiveTab] = useState<NavTab>('home');
  const [isLocationModalOpen, setIsLocationModalOpen] = useState(false);
  const [inspectedScan, setInspectedScan] = useState<ScanRecord | null>(null);

  // Field location state
  const [currentLocation, setCurrentLocation] = useState<LocationInfo>(POPULAR_AG_REGIONS[0]);

  // Weather data state
  const [weather, setWeather] = useState<WeatherData>({
    location: POPULAR_AG_REGIONS[0].name,
    coordinates: { lat: POPULAR_AG_REGIONS[0].lat, lon: POPULAR_AG_REGIONS[0].lon },
    current: {
      temp: 28,
      tempUnit: '°C',
      humidity: 81,
      windSpeed: 14,
      windUnit: 'km/h',
      rainProbability: 65,
      condition: 'Humid & Overcast',
      icon: 'cloud-rain',
      isRaining: false,
    },
    forecast: [
      { day: 'Today', condition: 'Humid & Showers', tempMax: 28, tempMin: 18, rainProb: 65, humidity: 81, icon: 'cloud-rain' },
      { day: 'Tomorrow', condition: 'Moderate Rain', tempMax: 26, tempMin: 17, rainProb: 80, humidity: 85, icon: 'cloud-rain-heavy' },
      { day: 'Wed', condition: 'Scattered Showers', tempMax: 25, tempMin: 16, rainProb: 55, humidity: 78, icon: 'cloud-drizzle' },
      { day: 'Thu', condition: 'Partly Cloudy', tempMax: 27, tempMin: 15, rainProb: 20, humidity: 62, icon: 'cloud-sun' },
      { day: 'Fri', condition: 'Sunny & Clear', tempMax: 29, tempMin: 16, rainProb: 10, humidity: 55, icon: 'sun' },
      { day: 'Sat', condition: 'Warm & Dry', tempMax: 30, tempMin: 17, rainProb: 5, humidity: 50, icon: 'sun' },
      { day: 'Sun', condition: 'Partly Cloudy', tempMax: 28, tempMin: 16, rainProb: 15, humidity: 58, icon: 'cloud-sun' },
    ],
  });

  // Current crop context
  const [activeCrop, setActiveCrop] = useState<string>('Your crop');

  // No diagnosis is shown until the user actually scans an image.
  const emptyDiagnosis: DiagnosisResultData = {
    isPlant: false,
    detectedSubject: '',
    crop: '',
    condition: 'No scan yet',
    isHealthy: false,
    confidence: 0,
    severity: 'None',
    visualSymptoms: [],
    diseaseExplanation: 'Scan a clear crop or leaf image to generate an AI diagnosis.',
    contributingFactors: [],
    weatherImpactAnalysis: 'Weather-specific disease analysis will appear after a crop is scanned.',
    diseaseRiskEstimate: 'Low',
    recommendedActions: ['Take a clear, close-up photograph of a crop leaf or plant.'],
    preventionMeasures: ['Use good lighting and keep the leaf in focus when scanning.'],
    disclaimer: 'AgroVision AI provides informational guidance and should not replace advice from qualified agricultural professionals or local agricultural authorities.',
  };
  const [latestDiagnosis, setLatestDiagnosis] = useState<DiagnosisResultData>(emptyDiagnosis);
  const [latestImage, setLatestImage] = useState<string>('');
  const [hasScannedInSession, setHasScannedInSession] = useState<boolean>(false);

  // Scan History in localStorage
  const [scans, setScans] = useState<ScanRecord[]>(() => {
    try {
      const saved = localStorage.getItem('agrovision_scans_v2');
      if (saved) {
        return JSON.parse(saved);
      }
    } catch (e) {
      console.warn('Failed reading localStorage scans:', e);
    }
    return [];
  });

  // Persist scans
  useEffect(() => {
    try {
      localStorage.setItem('agrovision_scans_v2', JSON.stringify(scans));
    } catch (e) {
      console.warn('Failed saving scans to localStorage:', e);
    }
  }, [scans]);

  // Update weather whenever location changes
  useEffect(() => {
    let isCancelled = false;
    async function loadWeather() {
      const data = await fetchWeatherData(currentLocation.lat, currentLocation.lon, currentLocation.name);
      if (!isCancelled) {
        setWeather(data);
      }
    }
    loadWeather();
    return () => {
      isCancelled = true;
    };
  }, [currentLocation]);

  // Handle Diagnosis Complete from Scanner
  const handleDiagnosisComplete = (result: DiagnosisResultData, imageUri: string) => {
    setLatestDiagnosis(result);
    setLatestImage(imageUri);
    if (result.isPlant !== false) {
      setActiveCrop(result.crop);
    }
    setHasScannedInSession(true);

    // Only append to history timeline if it's an actual plant specimen
    if (result.isPlant !== false) {
      const now = new Date();
      const newRecord: ScanRecord = {
        id: 'scan-' + Date.now(),
        date: now.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        time: now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        crop: result.crop,
        condition: result.condition,
        confidence: result.confidence,
        severity: result.severity,
        location: currentLocation.name,
        imageUrl: imageUri,
        fullReport: result,
      };

      setScans((prev) => [...prev, newRecord]);
    }

    // Smooth scroll down to result card if on home or scan page
    setTimeout(() => {
      const element = document.getElementById('diagnosis-result-section');
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }, 150);
  };

  const handleSaveToHistory = (result: DiagnosisResultData, imageUri: string) => {
    if (result.isPlant === false) return;
    const exists = scans.some((s) => s.id === result.id);
    if (exists) return;

    const now = new Date();
    const newRecord: ScanRecord = {
      id: 'scan-' + Date.now(),
      date: now.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
      time: now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      crop: result.crop,
      condition: result.condition,
      confidence: result.confidence,
      severity: result.severity,
      location: currentLocation.name,
      imageUrl: imageUri,
      fullReport: result,
    };

    setScans((prev) => [...prev, newRecord]);
  };

  const handleClearHistory = () => {
    setScans([]);
  };

  const handleResetDemoHistory = () => {
    setScans([]);
  };

  const handleOpenScanner = () => {
    setActiveTab('scan');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleOpenDashboard = () => {
    setActiveTab('dashboard');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleAskAssistant = (question?: string) => {
    // If not on dashboard, switch to dashboard or focus on assistant
    setActiveTab('dashboard');
    setTimeout(() => {
      const element = document.getElementById('assistant-section');
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }, 150);
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#FBFBFA]">
      {/* Top Navigation */}
      <Navbar
        activeTab={activeTab}
        onTabChange={(tab) => {
          setActiveTab(tab);
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }}
        location={currentLocation}
        onOpenLocationModal={() => setIsLocationModalOpen(true)}
        totalScansCount={scans.length}
      />

      {/* Main View Container */}
      <main className="flex-1">
        {/* 1. HOME TAB */}
        {activeTab === 'home' && (
          <div className="space-y-12">
            {/* Hero Section */}
            <HeroSection
              onScanClick={handleOpenScanner}
              onDashboardClick={handleOpenDashboard}
              weather={weather}
            />

            {/* In-Page Crop Scanner */}
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              <CropScanner
                onDiagnosisComplete={handleDiagnosisComplete}
                locationName={currentLocation.name}
                weather={weather}
              />
            </div>

            {/* Diagnosis Result only after a real scan */}
            {hasScannedInSession && (
              <div id="diagnosis-result-section" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <DiagnosisResult
                  result={latestDiagnosis}
                  imageUrl={latestImage}
                  onSaveToHistory={handleSaveToHistory}
                  isSaved={scans.some((s) => s.condition === latestDiagnosis.condition && s.crop === latestDiagnosis.crop)}
                  onAskAssistant={handleAskAssistant}
                  onNewScan={handleOpenScanner}
                />
              </div>
            )}

            {/* Weather & Recommendations Duo */}
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                <div className="lg:col-span-6">
                  <WeatherIntelligence
                    weather={weather}
                    onOpenLocation={() => setIsLocationModalOpen(true)}
                    detectedCrop={hasScannedInSession ? latestDiagnosis.crop : undefined}
                    detectedCondition={hasScannedInSession ? latestDiagnosis.condition : undefined}
                  />
                </div>
                {hasScannedInSession && (
                  <div className="lg:col-span-6">
                    <RecommendedActions
                      recommendedActions={latestDiagnosis.recommendedActions}
                      preventionMeasures={latestDiagnosis.preventionMeasures}
                      crop={latestDiagnosis.crop}
                      condition={latestDiagnosis.condition}
                    />
                  </div>
                )}
              </div>
            </div>

            {/* Crop Health Timeline Preview */}
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              <CropHealthHistory
                scans={scans}
                onSelectScan={(scan) => setInspectedScan(scan)}
                onClearHistory={handleClearHistory}
                onResetDemo={handleResetDemoHistory}
              />
            </div>

            {/* Agricultural News Alerts */}
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-12">
              <AgriculturalNews currentCrop={hasScannedInSession ? latestDiagnosis.crop : undefined} />
            </div>
          </div>
        )}

        {/* 2. SCAN TAB */}
        {activeTab === 'scan' && (
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10">
            <CropScanner
              onDiagnosisComplete={handleDiagnosisComplete}
              locationName={currentLocation.name}
              weather={weather}
            />

            {hasScannedInSession && (
              <>
                <div id="diagnosis-result-section">
                  <DiagnosisResult
                    result={latestDiagnosis}
                    imageUrl={latestImage}
                    onSaveToHistory={handleSaveToHistory}
                    isSaved={scans.some((s) => s.condition === latestDiagnosis.condition && s.crop === latestDiagnosis.crop)}
                    onAskAssistant={handleAskAssistant}
                    onNewScan={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
                  />
                </div>

                <RecommendedActions
                  recommendedActions={latestDiagnosis.recommendedActions}
                  preventionMeasures={latestDiagnosis.preventionMeasures}
                  crop={latestDiagnosis.crop}
                  condition={latestDiagnosis.condition}
                />
              </>
            )}
          </div>
        )}

        {/* 3. DASHBOARD TAB */}
        {activeTab === 'dashboard' && (
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <DashboardView
              currentCrop={activeCrop}
              latestDiagnosis={latestDiagnosis}
              latestImage={latestImage}
              weather={weather}
              locationName={currentLocation.name}
              onOpenLocation={() => setIsLocationModalOpen(true)}
              onNewScanClick={handleOpenScanner}
              scans={scans}
              onSelectScan={(scan) => setInspectedScan(scan)}
              onClearHistory={handleClearHistory}
              onResetDemo={handleResetDemoHistory}
              onAskAssistant={handleAskAssistant}
            />
          </div>
        )}

        {/* 4. MY CROPS (HISTORY) TAB */}
        {activeTab === 'crops' && (
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
            <CropHealthHistory
              scans={scans}
              onSelectScan={(scan) => setInspectedScan(scan)}
              onClearHistory={handleClearHistory}
              onResetDemo={handleResetDemoHistory}
            />

            {hasScannedInSession && (
              <div className="pt-4">
                <h3 className="font-serif font-bold text-xl text-[#142C1F] mb-4">
                  Latest Detailed Diagnosis Report
                </h3>
                <DiagnosisResult
                  result={latestDiagnosis}
                  imageUrl={latestImage}
                  onSaveToHistory={handleSaveToHistory}
                  isSaved={true}
                  onAskAssistant={handleAskAssistant}
                  onNewScan={handleOpenScanner}
                />
              </div>
            )}
          </div>
        )}

        {/* 5. INSIGHTS & WEATHER TAB */}
        {activeTab === 'insights' && (
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
            <WeatherIntelligence
              weather={weather}
              onOpenLocation={() => setIsLocationModalOpen(true)}
              detectedCrop={hasScannedInSession ? latestDiagnosis.crop : undefined}
              detectedCondition={hasScannedInSession ? latestDiagnosis.condition : undefined}
            />

            <AgriculturalNews currentCrop={hasScannedInSession ? latestDiagnosis.crop : undefined} />

            <div id="assistant-section">
              <AiCropAssistant
                currentCrop={activeCrop}
                latestDiagnosis={latestDiagnosis}
                locationName={currentLocation.name}
                weather={weather}
              />
            </div>
          </div>
        )}

        {/* 6. CROP LIBRARY TAB */}
        {activeTab === 'library' && (
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <CropKnowledge initialCropId={activeCrop.toLowerCase()} />
          </div>
        )}
      </main>

      {/* Footer */}
      <Footer onNavigate={(tab) => setActiveTab(tab)} />

      {/* Location Modal */}
      <LocationModal
        isOpen={isLocationModalOpen}
        onClose={() => setIsLocationModalOpen(false)}
        currentLocation={currentLocation}
        onSelectLocation={(loc) => setCurrentLocation(loc)}
      />

      {/* Archived Scan Detail Modal */}
      <ScanModal
        scan={inspectedScan}
        onClose={() => setInspectedScan(null)}
        onAskAssistant={handleAskAssistant}
      />
    </div>
  );
}
