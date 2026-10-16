import React, { useState } from 'react';
import {
  CalendarDays,
  Clock,
  MapPin,
  ChevronRight,
  Trash2,
  Eye,
  CheckCircle2,
  AlertTriangle,
  RotateCcw,
  Sparkles,
  ArrowRight,
  GitCompare,
  TrendingUp,
  TrendingDown,
  Minus,
  CheckSquare,
  Square,
  X,
  Droplets,
  Thermometer,
  Layers,
} from 'lucide-react';
import { ScanRecord, SeverityLevel } from '../types';

interface CropHealthHistoryProps {
  scans: ScanRecord[];
  onSelectScan: (scan: ScanRecord) => void;
  onClearHistory: () => void;
  onResetDemo: () => void;
}

export const CropHealthHistory: React.FC<CropHealthHistoryProps> = ({
  scans,
  onSelectScan,
  onClearHistory,
  onResetDemo,
}) => {
  // Comparison selection state: array of 2 scan IDs
  const [isCompareMode, setIsCompareMode] = useState(false);
  const [selectedScanIds, setSelectedScanIds] = useState<string[]>([]);

  const getSeverityPill = (severity: string) => {
    switch (severity) {
      case 'None':
        return 'bg-emerald-50 text-emerald-800 border-emerald-200';
      case 'Low':
        return 'bg-emerald-50 text-emerald-800 border-emerald-200';
      case 'Moderate':
        return 'bg-amber-50 text-amber-800 border-amber-200';
      case 'High':
      case 'Severe':
        return 'bg-rose-50 text-rose-800 border-rose-200';
      default:
        return 'bg-gray-50 text-gray-800 border-gray-200';
    }
  };

  const getSeverityRank = (severity: SeverityLevel): number => {
    switch (severity) {
      case 'None':
        return 0;
      case 'Low':
        return 1;
      case 'Moderate':
        return 2;
      case 'High':
        return 3;
      case 'Severe':
        return 4;
      default:
        return 0;
    }
  };

  // Toggle selection for comparison
  const toggleSelectForCompare = (scanId: string) => {
    setSelectedScanIds((prev) => {
      if (prev.includes(scanId)) {
        return prev.filter((id) => id !== scanId);
      }
      if (prev.length >= 2) {
        // Replace second with new selection
        return [prev[0], scanId];
      }
      return [...prev, scanId];
    });
  };

  const handleStartCompare = () => {
    setIsCompareMode(true);
    if (scans.length >= 2) {
      // Default to first and latest scan to see maximum progression
      setSelectedScanIds([scans[0].id, scans[scans.length - 1].id]);
    } else if (scans.length === 1) {
      setSelectedScanIds([scans[0].id]);
    }
  };

  // Resolve compared objects
  const scanA = scans.find((s) => s.id === selectedScanIds[0]);
  const scanB = scans.find((s) => s.id === selectedScanIds[1]);

  // Determine progression dynamics
  let severityTrend: 'improved' | 'worsened' | 'stable' = 'stable';
  let severityDiff = 0;
  if (scanA && scanB) {
    const rankA = getSeverityRank(scanA.severity);
    const rankB = getSeverityRank(scanB.severity);
    severityDiff = rankB - rankA;
    if (severityDiff > 0) severityTrend = 'worsened';
    else if (severityDiff < 0) severityTrend = 'improved';
    else severityTrend = 'stable';
  }

  return (
    <div className="bg-white rounded-2xl border border-[#DFE7DF] shadow-md p-6 sm:p-8 space-y-6">
      {/* Header & Controls */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-[#E8EDE8]">
        <div>
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider text-[#2D5A3C] bg-[#E5EFE7] px-2.5 py-1 rounded-md mb-2">
            <CalendarDays className="w-3.5 h-3.5" />
            <span>Field Longitudinal Tracking</span>
          </div>
          <h3 className="text-xl sm:text-2xl font-serif font-bold text-[#142C1F] tracking-tight">
            My Crop Health Timeline
          </h3>
          <p className="text-xs text-[#526356]">
            Inspect leaf health and pathogen symptoms over consecutive scouting intervals, or compare two scans side-by-side.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          {scans.length >= 2 && (
            <button
              onClick={() => {
                if (isCompareMode) {
                  setIsCompareMode(false);
                  setSelectedScanIds([]);
                } else {
                  handleStartCompare();
                }
              }}
              className={`text-xs px-3.5 py-2 rounded-xl font-semibold flex items-center gap-1.5 transition cursor-pointer ${
                isCompareMode
                  ? 'bg-[#234E35] text-white shadow-2xs'
                  : 'bg-[#F2F7F3] text-[#234E35] hover:bg-[#E2ECE3] border border-[#CCDCD0]'
              }`}
            >
              <GitCompare className="w-3.5 h-3.5" />
              <span>{isCompareMode ? 'Close Comparison' : 'Compare 2 Scans Side-by-Side'}</span>
            </button>
          )}

          {scans.length > 0 && (
            <button
              onClick={onClearHistory}
              className="text-xs px-3 py-2 rounded-xl border border-rose-200 text-rose-700 hover:bg-rose-50 transition flex items-center gap-1 cursor-pointer"
            >
              <Trash2 className="w-3.5 h-3.5" />
              <span>Clear</span>
            </button>
          )}
        </div>
      </div>

      {/* SIDE-BY-SIDE PROGRESSION COMPARISON VIEW */}
      {isCompareMode && (
        <div className="p-5 sm:p-6 bg-[#F8FAF7] border-2 border-[#234E35]/30 rounded-2xl space-y-6 shadow-sm">
          {/* Comparison Header */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-[#E1EAE2]">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold uppercase tracking-wider text-[#234E35] bg-[#E2EDE4] px-2.5 py-0.5 rounded-md flex items-center gap-1.5">
                  <GitCompare className="w-3 h-3" />
                  Side-by-Side Health Progression
                </span>
                {scanA && scanB && (
                  <span
                    className={`text-xs font-semibold px-2.5 py-0.5 rounded-md flex items-center gap-1 ${
                      severityTrend === 'worsened'
                        ? 'bg-rose-100 text-rose-800 border border-rose-200'
                        : severityTrend === 'improved'
                        ? 'bg-emerald-100 text-emerald-800 border border-emerald-200'
                        : 'bg-blue-100 text-blue-800 border border-blue-200'
                    }`}
                  >
                    {severityTrend === 'worsened' && <TrendingUp className="w-3.5 h-3.5" />}
                    {severityTrend === 'improved' && <TrendingDown className="w-3.5 h-3.5" />}
                    {severityTrend === 'stable' && <Minus className="w-3.5 h-3.5" />}
                    <span>
                      {severityTrend === 'worsened'
                        ? `Pathology Progressed (+${severityDiff} severity level)`
                        : severityTrend === 'improved'
                        ? 'Plant Vigor Improved'
                        : 'Condition Maintained'}
                    </span>
                  </span>
                )}
              </div>
              <p className="text-xs text-[#526356]">
                Comparing earlier baseline inspection against subsequent follow-up scouting.
              </p>
            </div>

            <div className="flex items-center gap-2 text-xs">
              <span className="text-[#687C6D]">Select 2 points in time to inspect:</span>
              <button
                onClick={() => setSelectedScanIds([])}
                className="text-[11px] text-[#234E35] underline hover:text-[#183925]"
              >
                Clear picks
              </button>
            </div>
          </div>

          {/* Selector chips for Scans */}
          <div className="flex flex-wrap gap-2 items-center">
            <span className="text-xs font-semibold text-[#3D5243] mr-1">Timeline Points:</span>
            {scans.map((s) => {
              const isSelectedA = selectedScanIds[0] === s.id;
              const isSelectedB = selectedScanIds[1] === s.id;
              const isSelected = isSelectedA || isSelectedB;
              return (
                <button
                  key={s.id}
                  onClick={() => toggleSelectForCompare(s.id)}
                  className={`text-xs px-3 py-1.5 rounded-xl border transition flex items-center gap-1.5 cursor-pointer ${
                    isSelected
                      ? 'bg-[#234E35] text-white border-[#234E35] font-semibold shadow-xs'
                      : 'bg-white text-[#344839] border-[#D5E1D7] hover:border-[#234E35]'
                  }`}
                >
                  <span>{isSelectedA ? '① Scan A:' : isSelectedB ? '② Scan B:' : '○'}</span>
                  <span>{s.date} — {s.condition}</span>
                </button>
              );
            })}
          </div>

          {/* Two Columns Side by Side */}
          {scanA && scanB ? (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch pt-2">
              {/* Scan A (Earlier / Baseline) */}
              <div className="p-5 bg-white rounded-xl border border-[#DFE7DF] shadow-xs space-y-4 flex flex-col justify-between">
                <div className="space-y-3">
                  <div className="flex items-center justify-between pb-2 border-b border-[#EEF2EE]">
                    <div>
                      <span className="text-[10px] font-bold uppercase tracking-wider text-[#2D5A3C] bg-[#E8F0EA] px-2 py-0.5 rounded">
                        Baseline Scan (Earlier)
                      </span>
                      <h4 className="text-base font-serif font-bold text-[#142C1F] mt-1">
                        {scanA.date} • {scanA.time}
                      </h4>
                    </div>
                    <span className={`text-xs font-semibold px-2.5 py-1 rounded-md border ${getSeverityPill(scanA.severity)}`}>
                      {scanA.severity}
                    </span>
                  </div>

                  {/* Photo */}
                  <div className="aspect-16/10 rounded-lg overflow-hidden bg-gray-100 border border-[#D5E1D7] relative">
                    <img
                      src={scanA.imageUrl}
                      alt={scanA.condition}
                      className="w-full h-full object-cover"
                    />
                    <div className="absolute bottom-2 left-2 bg-black/70 text-white text-[10px] px-2 py-0.5 rounded-md">
                      {scanA.crop} — {scanA.condition}
                    </div>
                  </div>

                  {/* Condition & Confidence */}
                  <div className="space-y-1.5 text-xs">
                    <div className="flex justify-between py-1 border-b border-[#F0F4F0]">
                      <span className="text-[#6D8072]">Condition:</span>
                      <strong className="text-[#142C1F]">{scanA.condition}</strong>
                    </div>
                    <div className="flex justify-between py-1 border-b border-[#F0F4F0]">
                      <span className="text-[#6D8072]">Model Confidence:</span>
                      <strong className="text-[#234E35]">{scanA.confidence}%</strong>
                    </div>
                    <div className="flex justify-between py-1 border-b border-[#F0F4F0]">
                      <span className="text-[#6D8072]">Location:</span>
                      <span className="text-[#4E6153]">{scanA.location}</span>
                    </div>
                  </div>

                  {/* Symptoms Logged */}
                  <div>
                    <span className="text-[11px] font-bold text-[#35523E] block mb-1.5 uppercase tracking-wider">
                      Observed Foliage Symptoms:
                    </span>
                    <ul className="space-y-1">
                      {scanA.fullReport.visualSymptoms.map((sym, idx) => (
                        <li key={idx} className="text-xs text-[#3E5244] flex items-start gap-1.5 leading-snug">
                          <span className="w-1.5 h-1.5 rounded-full bg-[#234E35] shrink-0 mt-1" />
                          <span>{sym}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>

                <button
                  onClick={() => onSelectScan(scanA)}
                  className="w-full py-2 px-3 bg-[#F4F7F4] hover:bg-[#E5ECE6] text-[#234E35] rounded-lg text-xs font-semibold transition"
                >
                  View Full Baseline Report
                </button>
              </div>

              {/* Scan B (Subsequent / Follow-up) */}
              <div className="p-5 bg-white rounded-xl border border-[#DFE7DF] shadow-xs space-y-4 flex flex-col justify-between">
                <div className="space-y-3">
                  <div className="flex items-center justify-between pb-2 border-b border-[#EEF2EE]">
                    <div>
                      <span className="text-[10px] font-bold uppercase tracking-wider text-[#A64B00] bg-[#FAF0E4] px-2 py-0.5 rounded">
                        Follow-up Scan (Subsequent)
                      </span>
                      <h4 className="text-base font-serif font-bold text-[#142C1F] mt-1">
                        {scanB.date} • {scanB.time}
                      </h4>
                    </div>
                    <span className={`text-xs font-semibold px-2.5 py-1 rounded-md border ${getSeverityPill(scanB.severity)}`}>
                      {scanB.severity}
                    </span>
                  </div>

                  {/* Photo */}
                  <div className="aspect-16/10 rounded-lg overflow-hidden bg-gray-100 border border-[#D5E1D7] relative">
                    <img
                      src={scanB.imageUrl}
                      alt={scanB.condition}
                      className="w-full h-full object-cover"
                    />
                    <div className="absolute bottom-2 left-2 bg-black/70 text-white text-[10px] px-2 py-0.5 rounded-md">
                      {scanB.crop} — {scanB.condition}
                    </div>
                  </div>

                  {/* Condition & Confidence */}
                  <div className="space-y-1.5 text-xs">
                    <div className="flex justify-between py-1 border-b border-[#F0F4F0]">
                      <span className="text-[#6D8072]">Condition:</span>
                      <strong className="text-[#142C1F]">{scanB.condition}</strong>
                    </div>
                    <div className="flex justify-between py-1 border-b border-[#F0F4F0]">
                      <span className="text-[#6D8072]">Model Confidence:</span>
                      <strong className="text-[#234E35]">{scanB.confidence}%</strong>
                    </div>
                    <div className="flex justify-between py-1 border-b border-[#F0F4F0]">
                      <span className="text-[#6D8072]">Location:</span>
                      <span className="text-[#4E6153]">{scanB.location}</span>
                    </div>
                  </div>

                  {/* Symptoms Logged */}
                  <div>
                    <span className="text-[11px] font-bold text-[#35523E] block mb-1.5 uppercase tracking-wider">
                      Observed Foliage Symptoms:
                    </span>
                    <ul className="space-y-1">
                      {scanB.fullReport.visualSymptoms.map((sym, idx) => (
                        <li key={idx} className="text-xs text-[#3E5244] flex items-start gap-1.5 leading-snug">
                          <span className="w-1.5 h-1.5 rounded-full bg-[#A64B00] shrink-0 mt-1" />
                          <span>{sym}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>

                <button
                  onClick={() => onSelectScan(scanB)}
                  className="w-full py-2 px-3 bg-[#F4F7F4] hover:bg-[#E5ECE6] text-[#234E35] rounded-lg text-xs font-semibold transition"
                >
                  View Full Follow-up Report
                </button>
              </div>
            </div>
          ) : (
            <div className="p-8 text-center text-xs text-[#6F8274] bg-white rounded-xl border border-dashed border-[#CCDCD0]">
              Please click any two scans from the timeline below to populate the side-by-side progression analysis.
            </div>
          )}

          {/* Pathological Evolution Assessment Summary */}
          {scanA && scanB && (
            <div className="p-4 bg-white rounded-xl border border-[#DCE7DD] space-y-2">
              <h5 className="text-xs font-bold uppercase tracking-wider text-[#234E35] flex items-center gap-2">
                <Sparkles className="w-4 h-4 text-[#2E6B43]" />
                <span>Agronomic Progression Synthesis ({scanA.date} &rarr; {scanB.date})</span>
              </h5>
              <p className="text-xs text-[#3B4E40] leading-relaxed">
                Between <strong>{scanA.date}</strong> and <strong>{scanB.date}</strong>, the crop shifted from <strong>"{scanA.condition}"</strong> ({scanA.severity} severity) to <strong>"{scanB.condition}"</strong> ({scanB.severity} severity).{' '}
                {severityTrend === 'worsened' ? (
                  <span>
                    Foliar pathogen activity intensified over this interval. Moisture events and ambient humidity likely accelerated fungal spore reproduction, moving lesions from initial subtle chlorosis to distinct necrotic target rings. Immediate pruning of affected lower branches and transitioning to soil-line drip irrigation is strongly advised.
                  </span>
                ) : severityTrend === 'improved' ? (
                  <span>
                    Crop health shows positive recovery. Symptoms have receded or stabilization practices have suppressed secondary spore spread. Maintain regular weekly visual scouting.
                  </span>
                ) : (
                  <span>
                    Symptoms have remained steady over this scouting window without substantial outward expansion into the upper vegetative canopy.
                  </span>
                )}
              </p>
            </div>
          )}
        </div>
      )}

      {/* Scans Timeline List */}
      {scans.length === 0 ? (
        <div className="py-12 text-center text-xs text-[#6F8274] space-y-2">
          <p>No recorded crop scans in your timeline yet.</p>
          <p className="text-[11px] text-[#8DA092]">
            Use the scanner above to create your first real crop health record.
          </p>
        </div>
      ) : (
        <div className="relative pl-6 sm:pl-8 space-y-6 before:absolute before:left-3 sm:before:left-4 before:top-3 before:bottom-3 before:w-0.5 before:bg-[#D8E4DA]">
          {scans.map((scan, idx) => {
            const isLatest = idx === scans.length - 1;
            const isSelectedForCompare = selectedScanIds.includes(scan.id);
            const compareIndex = selectedScanIds.indexOf(scan.id);

            return (
              <div key={scan.id} className="relative group">
                {/* Timeline node marker */}
                <div
                  className={`absolute -left-6 sm:-left-8 top-3.5 w-6 h-6 rounded-full border-2 bg-white flex items-center justify-center transition ${
                    isSelectedForCompare
                      ? 'border-[#234E35] bg-[#234E35] text-white ring-4 ring-[#E8F0EA]'
                      : isLatest
                      ? 'border-[#234E35] text-[#234E35] ring-4 ring-[#E8F0EA]'
                      : 'border-[#98AB9C] text-[#98AB9C]'
                  }`}
                >
                  {isSelectedForCompare ? (
                    <span className="text-[10px] font-bold">{compareIndex === 0 ? 'A' : 'B'}</span>
                  ) : (
                    <span className="w-2 h-2 rounded-full bg-current" />
                  )}
                </div>

                {/* Scan Card */}
                <div
                  className={`p-4 sm:p-5 rounded-xl border transition flex flex-col sm:flex-row sm:items-center justify-between gap-4 ${
                    isSelectedForCompare
                      ? 'bg-[#F2F7F3] border-[#234E35] shadow-xs'
                      : 'bg-[#F9FAF8] border-[#E7EDE8] hover:border-[#CCDCD0] hover:shadow-xs'
                  }`}
                >
                  <div className="flex items-start gap-4">
                    {/* Checkbox when in compare mode */}
                    {isCompareMode && (
                      <button
                        onClick={() => toggleSelectForCompare(scan.id)}
                        className="mt-1 text-[#234E35] hover:scale-110 transition cursor-pointer"
                        title="Select for side-by-side comparison"
                      >
                        {isSelectedForCompare ? (
                          <CheckSquare className="w-5 h-5 text-[#234E35]" />
                        ) : (
                          <Square className="w-5 h-5 text-[#91A596]" />
                        )}
                      </button>
                    )}

                    {/* Thumbnail */}
                    <div className="w-16 h-16 sm:w-20 sm:h-20 rounded-lg overflow-hidden bg-gray-100 shrink-0 border border-[#D7E3D8]">
                      <img
                        src={scan.imageUrl}
                        alt={scan.condition}
                        className="w-full h-full object-cover"
                      />
                    </div>

                    <div className="space-y-1">
                      <div className="flex flex-wrap items-center gap-2">
                        <span className="text-xs font-serif font-bold text-[#142C1F]">
                          {scan.date}
                        </span>
                        <span className="text-[10px] text-[#718476] flex items-center gap-1">
                          <Clock className="w-3 h-3" />
                          {scan.time}
                        </span>
                        {isLatest && (
                          <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.2 rounded-full bg-[#234E35] text-white">
                            Latest Scan
                          </span>
                        )}
                        {isSelectedForCompare && (
                          <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.2 rounded-full bg-[#E2EDE4] text-[#234E35]">
                            Comparing ({compareIndex === 0 ? 'Point A' : 'Point B'})
                          </span>
                        )}
                      </div>

                      <h4 className="text-sm font-semibold text-[#1B3021] flex items-center gap-2">
                        <span>{scan.crop} — {scan.condition}</span>
                        <span
                          className={`text-[10px] font-sans font-medium px-2 py-0.5 rounded-md border ${getSeverityPill(
                            scan.severity
                          )}`}
                        >
                          {scan.severity}
                        </span>
                      </h4>

                      <div className="flex items-center gap-3 text-[11px] text-[#55695A] pt-0.5">
                        <span className="flex items-center gap-1">
                          <MapPin className="w-3 h-3 text-[#7B8E80]" />
                          {scan.location}
                        </span>
                        <span>•</span>
                        <span>Confidence: <strong className="text-[#142C1F]">{scan.confidence}%</strong></span>
                      </div>
                    </div>
                  </div>

                  {/* Actions buttons */}
                  <div className="flex items-center gap-2 self-end sm:self-center">
                    <button
                      onClick={() => {
                        if (!isCompareMode) {
                          setIsCompareMode(true);
                          setSelectedScanIds([scan.id]);
                        } else {
                          toggleSelectForCompare(scan.id);
                        }
                      }}
                      className="px-3 py-2 rounded-xl bg-white hover:bg-[#F2F6F3] text-[#2F4A37] border border-[#CCDCD0] text-xs font-medium flex items-center gap-1.5 transition cursor-pointer"
                    >
                      <GitCompare className="w-3.5 h-3.5 text-[#234E35]" />
                      <span>{isSelectedForCompare ? 'Selected' : 'Compare'}</span>
                    </button>

                    <button
                      onClick={() => onSelectScan(scan)}
                      className="px-3.5 py-2 rounded-xl bg-white hover:bg-[#EDF3EE] text-[#234E35] border border-[#CCDCD0] text-xs font-semibold flex items-center gap-1.5 transition cursor-pointer shadow-2xs"
                    >
                      <Eye className="w-3.5 h-3.5" />
                      <span>View Full Report</span>
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
