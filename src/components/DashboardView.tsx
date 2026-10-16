import React from 'react';
import {
  Camera,
  Activity,
  CloudSun,
  ShieldAlert,
  ArrowRight,
  TrendingDown,
  Layers,
  MapPin,
  CheckCircle2,
  Calendar,
  AlertTriangle,
} from 'lucide-react';
import { DiagnosisResultData, WeatherData, ScanRecord } from '../types';
import { WeatherIntelligence } from './WeatherIntelligence';
import { RecommendedActions } from './RecommendedActions';
import { AiCropAssistant } from './AiCropAssistant';
import { CropHealthHistory } from './CropHealthHistory';
import { AgriculturalNews } from './AgriculturalNews';

interface DashboardViewProps {
  currentCrop: string;
  latestDiagnosis: DiagnosisResultData;
  latestImage: string;
  weather: WeatherData;
  locationName: string;
  onOpenLocation: () => void;
  onNewScanClick: () => void;
  scans: ScanRecord[];
  onSelectScan: (scan: ScanRecord) => void;
  onClearHistory: () => void;
  onResetDemo: () => void;
  onAskAssistant: (question?: string) => void;
}

export const DashboardView: React.FC<DashboardViewProps> = ({
  currentCrop,
  latestDiagnosis,
  latestImage,
  weather,
  locationName,
  onOpenLocation,
  onNewScanClick,
  scans,
  onSelectScan,
  onClearHistory,
  onResetDemo,
  onAskAssistant,
}) => {
  const hasDiagnosis = latestDiagnosis.condition !== 'No scan yet' && Boolean(latestImage);

  return (
    <div className="space-y-8 pb-16">
      {/* 1. Dashboard Welcome & Status Header */}
      <div className="bg-white rounded-2xl border border-[#DFE7DF] shadow-md p-6 sm:p-8">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="space-y-1.5">
            <div className="flex items-center gap-2">
              <span className="text-xs font-bold uppercase tracking-wider text-[#2D5A3C] bg-[#E5EFE7] px-2.5 py-1 rounded-md">
                Field Health Overview
              </span>
              <button
                onClick={onOpenLocation}
                className="text-xs text-[#526656] hover:text-[#142C1F] flex items-center gap-1 cursor-pointer"
              >
                <MapPin className="w-3.5 h-3.5 text-[#2D5A3C]" />
                <span>{locationName}</span>
              </button>
            </div>
            <h2 className="text-2xl sm:text-3xl font-serif font-bold text-[#142C1F] tracking-tight">
              Good day, Grower. Here is your crop health status.
            </h2>
            <p className="text-xs text-[#526356] max-w-2xl leading-relaxed">
              Active monitoring for <strong>{currentCrop}</strong> fields. Ground telemetry indicates high relative humidity and approaching rain fronts requiring prompt foliar hygiene.
            </p>
          </div>

          <button
            onClick={onNewScanClick}
            className="px-5 py-3 rounded-xl bg-[#234E35] hover:bg-[#1B3E2A] text-white font-semibold text-xs flex items-center justify-center gap-2 transition shadow-xs self-start md:self-auto cursor-pointer"
          >
            <Camera className="w-4 h-4" />
            <span>Scan Another Crop</span>
          </button>
        </div>

        {/* Quick Highlights Summary Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-6 pt-6 border-t border-[#EEF2EE]">
          <div className="p-4 rounded-xl bg-[#F8FAF7] border border-[#E7EDE8]">
            <span className="text-[11px] text-[#637568] uppercase font-semibold block">
              Active Crop
            </span>
            <div className="flex items-center justify-between mt-1">
              <h4 className="text-base font-serif font-bold text-[#142C1F]">
                {currentCrop}
              </h4>
              <span className="text-xl">🌱</span>
            </div>
            <span className="text-[11px] text-[#6F8274] block mt-0.5">
              {hasDiagnosis ? 'Currently monitored' : 'Scan a crop to begin tracking'}
            </span>
          </div>

          <div className="p-4 rounded-xl bg-[#F8FAF7] border border-[#E7EDE8]">
            <span className="text-[11px] text-[#637568] uppercase font-semibold block">
              Latest Diagnosis
            </span>
            <div className="flex items-center justify-between mt-1">
              <h4 className="text-base font-serif font-bold text-[#142C1F]">
                {hasDiagnosis ? latestDiagnosis.condition : 'No scan yet'}
              </h4>
              <span className="text-xs font-semibold px-2 py-0.5 rounded-md bg-[#FCE8D5] text-[#A64B00]">
                {hasDiagnosis ? latestDiagnosis.severity : '—'}
              </span>
            </div>
            <span className="text-[11px] text-[#6F8274] block mt-0.5">
              {hasDiagnosis ? `Confidence: ${latestDiagnosis.confidence}%` : 'Scan a crop to see confidence'}
            </span>
          </div>

          <div className="p-4 rounded-xl bg-[#F8FAF7] border border-[#E7EDE8]">
            <span className="text-[11px] text-[#637568] uppercase font-semibold block">
              Weather Risk Index
            </span>
            <div className="flex items-center justify-between mt-1">
              <h4 className="text-base font-serif font-bold text-rose-700">
                Current Weather Conditions
              </h4>
              <span className="w-2.5 h-2.5 rounded-full bg-rose-500 animate-pulse" />
            </div>
            <span className="text-[11px] text-[#6F8274] block mt-0.5">
              {weather.current.humidity}% humidity • rain upcoming
            </span>
          </div>

          <div className="p-4 rounded-xl bg-[#F8FAF7] border border-[#E7EDE8]">
            <span className="text-[11px] text-[#637568] uppercase font-semibold block">
              Historical Timeline
            </span>
            <div className="flex items-center justify-between mt-1">
              <h4 className="text-base font-serif font-bold text-[#142C1F]">
                {scans.length} Scans Logged
              </h4>
              <Calendar className="w-4 h-4 text-[#2D5A3C]" />
            </div>
            <span className="text-[11px] text-[#6F8274] block mt-0.5">
              Last check: Today
            </span>
          </div>
        </div>
      </div>

      {/* 2. Side-by-Side: Latest Scan Spotlight & Weather Risk Intelligence */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        {/* Latest Scan Card */}
        <div className="lg:col-span-5 bg-white rounded-2xl border border-[#DFE7DF] shadow-md p-6 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="font-serif font-bold text-lg text-[#142C1F]">
              Latest Crop Inspection
            </h3>
            <span className="text-[11px] text-[#2D5A3C] font-semibold bg-[#E7F0E8] px-2.5 py-0.5 rounded-md">
              Primary Diagnostic
            </span>
          </div>

          <div className="aspect-4/3 rounded-xl overflow-hidden bg-gray-100 border border-[#D5E1D7] relative">
            <img
              src={latestImage}
              alt={hasDiagnosis ? latestDiagnosis.condition : 'No scan yet'}
              className="w-full h-full object-cover"
            />
            <div className="absolute top-3 left-3 bg-black/70 backdrop-blur-xs text-white text-[11px] px-2.5 py-1 rounded-md font-medium">
              {latestDiagnosis.crop} • {hasDiagnosis ? latestDiagnosis.condition : 'No scan yet'}
            </div>
          </div>

          <div className="space-y-2 text-xs">
            <div className="flex justify-between items-center py-1 border-b border-[#EEF2EE]">
              <span className="text-[#687C6D]">Condition Detected:</span>
              <strong className="text-[#142C1F]">{hasDiagnosis ? latestDiagnosis.condition : 'No scan yet'}</strong>
            </div>
            <div className="flex justify-between items-center py-1 border-b border-[#EEF2EE]">
              <span className="text-[#687C6D]">Model Confidence:</span>
              <strong className="text-[#234E35]">{latestDiagnosis.confidence}%</strong>
            </div>
            <div className="flex justify-between items-center py-1 border-b border-[#EEF2EE]">
              <span className="text-[#687C6D]">Estimated Severity:</span>
              <span className="font-semibold text-amber-800">{hasDiagnosis ? latestDiagnosis.severity : '—'}</span>
            </div>
          </div>

          <div className="p-3 rounded-xl bg-[#F8FAF7] border border-[#E7EDE8] text-xs text-[#3E5244] leading-relaxed">
            <p className="line-clamp-3">
              {hasDiagnosis ? latestDiagnosis.diseaseExplanation : 'Scan a crop image to receive an image-based diagnosis, weather context and recommended actions.'}
            </p>
          </div>

          <button
            onClick={() => onAskAssistant(hasDiagnosis ? `How does this week's weather affect the ${latestDiagnosis.condition} on my ${latestDiagnosis.crop}?` : 'How should I start monitoring my crop?')}
            className="w-full py-2.5 px-4 rounded-xl bg-[#F2F6F3] hover:bg-[#E5ECE6] text-[#234E35] font-semibold text-xs transition flex items-center justify-center gap-2 cursor-pointer"
          >
            <span>Ask Assistant About This Condition</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>

        {/* Weather Intelligence Module */}
        <div className="lg:col-span-7">
          <WeatherIntelligence
            weather={weather}
            onOpenLocation={onOpenLocation}
            detectedCrop={hasDiagnosis ? latestDiagnosis.crop : undefined}
            detectedCondition={hasDiagnosis ? latestDiagnosis.condition : undefined}
          />
        </div>
      </div>

      {/* 3. Recommended Actions & Cultural Management */}
      <RecommendedActions
        recommendedActions={latestDiagnosis.recommendedActions}
        preventionMeasures={latestDiagnosis.preventionMeasures}
        crop={hasDiagnosis ? latestDiagnosis.crop : undefined}
        condition={hasDiagnosis ? latestDiagnosis.condition : undefined}
      />

      {/* 4. AI Agricultural Assistant & Scan History Split */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        {/* Assistant */}
        <div className="lg:col-span-6">
          <AiCropAssistant
            currentCrop={currentCrop}
            latestDiagnosis={latestDiagnosis}
            locationName={locationName}
            weather={weather}
          />
        </div>

        {/* Health History */}
        <div className="lg:col-span-6">
          <CropHealthHistory
            scans={scans}
            onSelectScan={onSelectScan}
            onClearHistory={onClearHistory}
            onResetDemo={onResetDemo}
          />
        </div>
      </div>

      {/* 5. Agricultural News Bulletins */}
      <AgriculturalNews currentCrop={currentCrop} />
    </div>
  );
};
