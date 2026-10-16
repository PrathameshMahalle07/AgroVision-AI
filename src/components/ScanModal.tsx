import React from 'react';
import { X, CheckCircle2, AlertTriangle, ShieldCheck, Droplets, MapPin, Calendar } from 'lucide-react';
import { ScanRecord } from '../types';

interface ScanModalProps {
  scan: ScanRecord | null;
  onClose: () => void;
  onAskAssistant: (question: string) => void;
}

export const ScanModal: React.FC<ScanModalProps> = ({ scan, onClose, onAskAssistant }) => {
  if (!scan) return null;
  const report = scan.fullReport;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#142C1F]/60 backdrop-blur-xs">
      <div className="bg-white rounded-2xl max-w-3xl w-full shadow-2xl border border-[#DFE7E0] overflow-hidden flex flex-col max-h-[92vh]">
        {/* Modal Header */}
        <div className="p-6 bg-[#F8FAF7] border-b border-[#E8EDE8] flex items-start justify-between">
          <div>
            <div className="flex items-center gap-2 mb-1.5">
              <span className="text-xs font-bold uppercase tracking-wider text-[#2D5A3C] bg-[#E5EFE7] px-2.5 py-0.5 rounded-md">
                Archived Diagnostic Scan
              </span>
              <span className="text-xs text-[#6F8274] flex items-center gap-1">
                <Calendar className="w-3.5 h-3.5" />
                {scan.date} at {scan.time}
              </span>
            </div>
            <h3 className="text-2xl font-serif font-bold text-[#142C1F]">
              {scan.crop} — {scan.condition}
            </h3>
            <p className="text-xs text-[#5D6F61] flex items-center gap-1 mt-1">
              <MapPin className="w-3.5 h-3.5 text-[#2D5A3C]" />
              {scan.location}
            </p>
          </div>

          <button
            onClick={onClose}
            className="p-2 rounded-lg text-[#617466] hover:text-[#142C1F] hover:bg-black/5 transition"
            aria-label="Close report"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-6 overflow-y-auto space-y-6">
          <div className="grid grid-cols-1 sm:grid-cols-12 gap-6 items-start">
            <div className="sm:col-span-4 space-y-3">
              <div className="aspect-4/3 rounded-xl overflow-hidden bg-gray-100 border border-[#D5E1D7]">
                <img
                  src={scan.imageUrl}
                  alt={scan.condition}
                  className="w-full h-full object-cover"
                />
              </div>

              <div className="p-3 bg-[#F8FAF7] rounded-xl border border-[#E7EDE8] space-y-2 text-xs">
                <div className="flex justify-between">
                  <span className="text-[#6D8072]">Severity:</span>
                  <strong className="text-[#142C1F]">{scan.severity}</strong>
                </div>
                <div className="flex justify-between">
                  <span className="text-[#6D8072]">Confidence:</span>
                  <strong className="text-[#234E35]">{scan.confidence}%</strong>
                </div>
              </div>

              <button
                onClick={() => {
                  onClose();
                  onAskAssistant(`Tell me more about the archived ${scan.condition} scan from ${scan.date}.`);
                }}
                className="w-full py-2.5 px-3 bg-[#234E35] hover:bg-[#1B3E2A] text-white rounded-xl text-xs font-semibold transition"
              >
                Ask Assistant About This Scan
              </button>
            </div>

            <div className="sm:col-span-8 space-y-5">
              <div>
                <h5 className="text-xs font-bold uppercase tracking-wider text-[#2D5A3C] mb-1.5">
                  Pathology Explanation
                </h5>
                <p className="text-xs text-[#2E4032] leading-relaxed bg-[#F8FAF7] p-3 rounded-xl border border-[#E7EDE8]">
                  {report.diseaseExplanation}
                </p>
              </div>

              <div>
                <h5 className="text-xs font-bold uppercase tracking-wider text-[#2D5A3C] mb-1.5">
                  Observed Visual Symptoms
                </h5>
                <ul className="space-y-1.5">
                  {report.visualSymptoms.map((sym, idx) => (
                    <li key={idx} className="text-xs text-[#3B4D3F] flex items-start gap-2">
                      <CheckCircle2 className="w-3.5 h-3.5 text-[#2D5A3C] shrink-0 mt-0.5" />
                      <span>{sym}</span>
                    </li>
                  ))}
                </ul>
              </div>

              <div>
                <h5 className="text-xs font-bold uppercase tracking-wider text-[#2D5A3C] mb-1.5">
                  Actionable Steps
                </h5>
                <ul className="space-y-1.5">
                  {report.recommendedActions.map((act, idx) => (
                    <li key={idx} className="text-xs text-[#3B4D3F] flex items-start gap-2">
                      <span className="w-1.5 h-1.5 rounded-full bg-[#2D5A3C] shrink-0 mt-1.5" />
                      <span>{act}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>

        {/* Modal Footer */}
        <div className="p-4 bg-[#F8FAF7] border-t border-[#E8EDE8] flex items-center justify-between text-xs text-[#6F8274]">
          <span>AgroVision AI Archive Record #{scan.id}</span>
          <button
            onClick={onClose}
            className="px-4 py-2 bg-white border border-[#D5E0D6] rounded-xl text-xs font-semibold text-[#142C1F] hover:bg-[#F2F6F3]"
          >
            Close Report
          </button>
        </div>
      </div>
    </div>
  );
};
