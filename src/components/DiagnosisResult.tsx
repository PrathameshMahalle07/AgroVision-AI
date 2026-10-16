import React, { useState } from 'react';
import {
  CheckCircle2,
  AlertTriangle,
  BookmarkCheck,
  MessageSquare,
  RefreshCw,
  Info,
  Thermometer,
  Droplets,
  Wind,
  ShieldCheck,
  ChevronRight,
  ExternalLink,
} from 'lucide-react';
import { DiagnosisResultData, SeverityLevel } from '../types';

interface DiagnosisResultProps {
  result: DiagnosisResultData;
  imageUrl?: string;
  onSaveToHistory: (result: DiagnosisResultData, imageUri: string) => void;
  isSaved: boolean;
  onAskAssistant: (question?: string) => void;
  onNewScan: () => void;
}

export const DiagnosisResult: React.FC<DiagnosisResultProps> = ({
  result,
  imageUrl,
  onSaveToHistory,
  isSaved,
  onAskAssistant,
  onNewScan,
}) => {
  const [saveSuccess, setSaveSuccess] = useState(isSaved);

  const getSeverityBadge = (severity: SeverityLevel) => {
    switch (severity) {
      case 'None':
        return {
          bg: 'bg-emerald-50 text-emerald-800 border-emerald-200',
          label: 'Healthy / No Severity',
        };
      case 'Low':
        return {
          bg: 'bg-emerald-50 text-emerald-800 border-emerald-200',
          label: 'Low Severity',
        };
      case 'Moderate':
        return {
          bg: 'bg-amber-50 text-amber-800 border-amber-200',
          label: 'Moderate Severity',
        };
      case 'High':
        return {
          bg: 'bg-orange-50 text-orange-800 border-orange-200',
          label: 'High Severity',
        };
      case 'Severe':
        return {
          bg: 'bg-rose-50 text-rose-800 border-rose-200',
          label: 'Critical / Severe',
        };
      default:
        return {
          bg: 'bg-gray-50 text-gray-800 border-gray-200',
          label: severity,
        };
    }
  };

  const badge = getSeverityBadge(result.severity);

  const handleSave = () => {
    onSaveToHistory(result, imageUrl || '');
    setSaveSuccess(true);
  };

  const isNonPlant = result.isPlant === false || result.condition.toLowerCase().includes('non-plant') || result.condition.toLowerCase().includes('inconclusive');

  if (isNonPlant) {
    return (
      <div className="bg-white rounded-2xl border-2 border-amber-300 shadow-md overflow-hidden">
        {/* Non-Plant Notice Banner */}
        <div className="p-6 sm:p-8 bg-amber-50/80 border-b border-amber-200">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div className="space-y-1.5">
              <div className="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-amber-900 bg-amber-200/70 px-2.5 py-1 rounded-md">
                <AlertTriangle className="w-3.5 h-3.5 text-amber-800" />
                <span>Non-Plant Surface Detected</span>
              </div>
              <h3 className="text-2xl sm:text-3xl font-serif font-bold text-[#142C1F] tracking-tight">
                {result.detectedSubject || 'Inanimate / Architectural Surface'}
              </h3>
              <p className="text-xs text-amber-950/80 max-w-xl">
                The computer vision system inspected this image and determined it depicts a wall, floor, or non-botanical object rather than living plant foliage.
              </p>
            </div>

            <div className="bg-white p-4 rounded-xl border border-amber-200 shadow-2xs min-w-[200px]">
              <span className="text-[10px] font-bold uppercase tracking-wider text-[#738576] block">
                Plant Leaf Verification
              </span>
              <span className="text-lg font-bold text-rose-700 block mt-0.5">
                No Foliage Detected
              </span>
              <span className="text-[10px] text-[#718274] block mt-1">
                Zero biological tissue found
              </span>
            </div>
          </div>
        </div>

        <div className="p-6 sm:p-8 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          {imageUrl && (
            <div className="lg:col-span-4 space-y-3">
              <div className="aspect-4/3 rounded-xl overflow-hidden bg-gray-100 shadow-sm border border-[#D5E0D6] relative">
                <img
                  src={imageUrl}
                  alt="Scanned image"
                  className="w-full h-full object-cover"
                />
                <div className="absolute bottom-2 left-2 bg-black/70 text-white text-[10px] px-2 py-0.5 rounded-md">
                  Scanned Image
                </div>
              </div>

              <button
                onClick={onNewScan}
                className="w-full py-2.5 px-4 bg-[#234E35] hover:bg-[#1B3E2A] text-white text-xs font-semibold rounded-xl transition flex items-center justify-center gap-2 cursor-pointer shadow-xs"
              >
                <RefreshCw className="w-3.5 h-3.5" />
                <span>Scan a Real Crop Leaf</span>
              </button>
            </div>
          )}

          <div className="lg:col-span-8 space-y-5">
            <div className="p-4 rounded-xl bg-amber-50/50 border border-amber-200 text-xs text-amber-950 space-y-2">
              <h4 className="font-semibold text-sm text-amber-900 flex items-center gap-2">
                <Info className="w-4 h-4 text-amber-700" />
                <span>Why was no disease diagnosed?</span>
              </h4>
              <p className="leading-relaxed">
                {result.diseaseExplanation}
              </p>
            </div>

            <div>
              <h4 className="text-xs font-bold uppercase tracking-wider text-[#2D5A3C] mb-2">
                Visual Inspection Findings:
              </h4>
              <ul className="space-y-1.5">
                {result.visualSymptoms.map((sym, idx) => (
                  <li key={idx} className="p-2.5 rounded-xl bg-[#F9FAF8] border border-[#E7EDE8] text-xs text-[#2A3B2E] flex items-start gap-2">
                    <span className="w-1.5 h-1.5 rounded-full bg-amber-600 shrink-0 mt-1.5" />
                    <span>{sym}</span>
                  </li>
                ))}
              </ul>
            </div>

            <div>
              <h4 className="text-xs font-bold uppercase tracking-wider text-[#2D5A3C] mb-2">
                How to get an accurate crop diagnosis:
              </h4>
              <ul className="space-y-1.5">
                {result.recommendedActions.map((act, idx) => (
                  <li key={idx} className="text-xs text-[#354839] flex items-start gap-2">
                    <CheckCircle2 className="w-3.5 h-3.5 text-[#2D5A3C] shrink-0 mt-0.5" />
                    <span>{act}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-2xl border border-[#DFE7DF] shadow-md overflow-hidden">
      {/* Top Banner: Diagnosis Overview */}
      <div className="p-6 sm:p-8 bg-[#F8FAF7] border-b border-[#E8EDE8]">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="space-y-1.5">
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-xs font-bold uppercase tracking-wider text-[#355F42] bg-[#E2EDE4] px-2.5 py-1 rounded-md">
                Crop: {result.crop}
              </span>
              <span className={`text-xs font-semibold px-2.5 py-1 rounded-md border ${badge.bg}`}>
                {badge.label}
              </span>
              {result.detectedSubject && (
                <span className="text-xs text-[#5C7060] bg-white border border-[#D5E1D7] px-2 py-0.5 rounded-md">
                  {result.detectedSubject}
                </span>
              )}
            </div>

            <h3 className="text-2xl sm:text-3xl font-serif font-bold text-[#142C1F] tracking-tight">
              {result.condition}
            </h3>

            <p className="text-xs text-[#5D6F61]">
              Diagnostic analysis completed for {result.location || 'Local Field'}
            </p>
          </div>

          {/* Confidence Meter Card */}
          <div className="bg-white p-4 rounded-xl border border-[#DFE7E0] shadow-2xs min-w-[200px] flex items-center justify-between gap-4">
            <div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-[#738576] block">
                Model Confidence
              </span>
              <span className="text-2xl font-serif font-bold text-[#142C1F]">
                {result.confidence}%
              </span>
            </div>

            {/* Visual Gauge Bar */}
            <div className="w-24">
              <div className="w-full bg-[#E5EDE6] h-2.5 rounded-full overflow-hidden">
                <div
                  className={`h-full rounded-full transition-all duration-700 ${
                    result.confidence > 85
                      ? 'bg-[#2E6B43]'
                      : result.confidence > 60
                      ? 'bg-[#D9822B]'
                      : 'bg-rose-500'
                  }`}
                  style={{ width: `${result.confidence}%` }}
                />
              </div>
              <span className="text-[10px] text-[#718274] block mt-1 text-right">
                {result.confidence >= 85 ? 'High Confidence' : 'Moderate Match'}
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content Body */}
      <div className="p-6 sm:p-8 space-y-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          {/* Left Column: Image & Quick Actions */}
          <div className="lg:col-span-4 space-y-4">
            {imageUrl && (
              <div className="aspect-4/3 rounded-xl overflow-hidden bg-[#223528] shadow-sm border border-[#D5E0D6] relative">
                <img
                  src={imageUrl}
                  alt={result.condition}
                  className="w-full h-full object-cover"
                />
                <div className="absolute bottom-2 left-2 bg-black/60 backdrop-blur-xs text-white text-[10px] px-2 py-0.5 rounded-md">
                  In-Field Photo Sample
                </div>
              </div>
            )}

            {/* Action Buttons */}
            <div className="space-y-2 pt-2">
              <button
                onClick={handleSave}
                disabled={saveSuccess}
                className={`w-full py-2.5 px-4 rounded-xl text-xs font-semibold flex items-center justify-center gap-2 transition cursor-pointer ${
                  saveSuccess
                    ? 'bg-[#EAF3EC] text-[#234E35] border border-[#CCDCD0]'
                    : 'bg-[#234E35] hover:bg-[#1B3E2A] text-white shadow-2xs'
                }`}
              >
                <BookmarkCheck className="w-4 h-4" />
                <span>{saveSuccess ? 'Saved to My Crop Health' : 'Save Scan to Timeline'}</span>
              </button>

              <button
                onClick={() => onAskAssistant(`What are the immediate steps for ${result.condition} in ${result.crop}?`)}
                className="w-full py-2.5 px-4 rounded-xl bg-white hover:bg-[#F2F6F3] text-[#234E35] border border-[#CAD8CC] text-xs font-semibold flex items-center justify-center gap-2 transition cursor-pointer"
              >
                <MessageSquare className="w-4 h-4" />
                <span>Ask AI Assistant About This</span>
              </button>

              <button
                onClick={onNewScan}
                className="w-full py-2.5 px-4 text-xs font-medium text-[#576B5C] hover:text-[#142C1F] hover:bg-[#F4F7F4] rounded-xl transition flex items-center justify-center gap-1.5"
              >
                <RefreshCw className="w-3.5 h-3.5" />
                <span>Scan Another Plant</span>
              </button>
            </div>
          </div>

          {/* Right Column: Three Diagnostic Explanations */}
          <div className="lg:col-span-8 space-y-6">
            {/* 1. What We Detected */}
            <div>
              <h4 className="text-sm font-semibold uppercase tracking-wider text-[#2D5A3C] flex items-center gap-2 mb-3">
                <CheckCircle2 className="w-4 h-4 text-[#2D5A3C]" />
                <span>What We Detected</span>
              </h4>
              <p className="text-xs text-[#526356] mb-3">
                Visual pathology indicators identified across leaf blade, veins, and petiole:
              </p>
              <ul className="space-y-2">
                {result.visualSymptoms.map((symptom, idx) => (
                  <li
                    key={idx}
                    className="p-3 rounded-xl bg-[#F9FAF8] border border-[#E7EDE8] text-xs text-[#2A3B2E] flex items-start gap-2.5"
                  >
                    <span className="w-1.5 h-1.5 rounded-full bg-[#2D5A3C] shrink-0 mt-1.5" />
                    <span className="leading-relaxed">{symptom}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* 2. What Is This Disease? */}
            <div className="pt-2">
              <h4 className="text-sm font-semibold uppercase tracking-wider text-[#2D5A3C] flex items-center gap-2 mb-2">
                <Info className="w-4 h-4 text-[#2D5A3C]" />
                <span>What Is This Disease?</span>
              </h4>
              <div className="p-4 rounded-xl bg-[#F6FAF7] border border-[#DDE8DF]">
                <p className="text-xs text-[#2D3E31] leading-relaxed">
                  {result.diseaseExplanation}
                </p>
              </div>
            </div>

            {/* 3. Possible Contributing Factors */}
            <div className="pt-2">
              <h4 className="text-sm font-semibold uppercase tracking-wider text-[#2D5A3C] flex items-center gap-2 mb-2">
                <Thermometer className="w-4 h-4 text-[#2D5A3C]" />
                <span>Possible Contributing Factors</span>
              </h4>
              <p className="text-xs text-[#526356] mb-3">
                Environmental and microclimatic variables that frequently encourage this condition:
              </p>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                {result.contributingFactors.map((factor, idx) => (
                  <div
                    key={idx}
                    className="p-2.5 rounded-xl bg-[#FAFBF9] border border-[#E5EBE5] text-xs text-[#354639] flex items-center gap-2"
                  >
                    <Droplets className="w-3.5 h-3.5 text-[#5C8A6C] shrink-0" />
                    <span>{factor}</span>
                  </div>
                ))}
              </div>

              {/* Crucial Distinguishing Disclaimer as mandated by Prompt */}
              <div className="mt-4 p-3 rounded-xl bg-amber-50/70 border border-amber-200/80 text-[11px] text-amber-900 leading-relaxed flex items-start gap-2">
                <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0 mt-0.5" />
                <div>
                  <span className="font-semibold">Agronomic Context Note:</span> Photographic analysis detects visible leaf damage patterns, but environmental conditions (such as humidity, leaf wetness duration, and soil aeration) govern actual pathogen severity. The observations above describe visual symptoms and known environmental correlates rather than a laboratory culture.
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
