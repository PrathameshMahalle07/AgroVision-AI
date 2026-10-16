import React from 'react';
import {
  Scissors,
  Wind,
  Droplets,
  Search,
  RotateCcw,
  ShieldCheck,
  Sprout,
  AlertTriangle,
  CheckCircle2,
} from 'lucide-react';

interface RecommendedActionsProps {
  recommendedActions?: string[];
  preventionMeasures?: string[];
  crop?: string;
  condition?: string;
}

export const RecommendedActions: React.FC<RecommendedActionsProps> = ({
  recommendedActions,
  preventionMeasures,
  crop = 'your crop',
  condition = 'the current scan',
}) => {
  // Default practical actions if none provided
  const actions = recommendedActions?.length
    ? recommendedActions
    : [
        'Rescan the affected area with a clear close-up image if symptoms are present.',
        'Monitor the crop for changes in leaf color, spots, wilting, pests, or tissue damage.',
        'Maintain appropriate irrigation and avoid unnecessary leaf wetness.',
        'Check nearby plants for similar visible symptoms.',
        'Use local agricultural guidance before applying any treatment.',
      ];

  const preventions = preventionMeasures?.length
    ? preventionMeasures
    : [
        'Scout crops regularly so new symptoms are detected early.',
        'Maintain good plant spacing and airflow appropriate for the crop.',
        'Keep irrigation practices appropriate for the crop and local climate.',
        'Remove heavily damaged plant material according to local agricultural guidance.',
        'Use locally recommended varieties and integrated crop-management practices.',
      ];

  const getActionIcon = (idx: number) => {
    switch (idx % 5) {
      case 0:
        return <Scissors className="w-4 h-4 text-[#234E35]" />;
      case 1:
        return <Wind className="w-4 h-4 text-[#234E35]" />;
      case 2:
        return <Droplets className="w-4 h-4 text-[#234E35]" />;
      case 3:
        return <Search className="w-4 h-4 text-[#234E35]" />;
      default:
        return <RotateCcw className="w-4 h-4 text-[#234E35]" />;
    }
  };

  return (
    <div className="space-y-6">
      {/* 1. Recommended Actions Section */}
      <div className="bg-white rounded-2xl border border-[#DFE7DF] shadow-md p-6 sm:p-8">
        <div className="flex items-center gap-2 mb-2">
          <div className="w-8 h-8 rounded-lg bg-[#E5EFE7] text-[#234E35] flex items-center justify-center">
            <CheckCircle2 className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-xl sm:text-2xl font-serif font-bold text-[#142C1F] tracking-tight">
              Recommended Actions
            </h3>
            <p className="text-xs text-[#526356]">
              Practical immediate management steps for {crop} ({condition})
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5 mt-6">
          {actions.map((action, idx) => (
            <div
              key={idx}
              className="p-4 rounded-xl bg-[#F9FAF8] border border-[#E7EDE8] hover:border-[#CCDCD0] transition flex items-start gap-3"
            >
              <div className="w-8 h-8 rounded-lg bg-[#EAEFEA] flex items-center justify-center shrink-0 mt-0.5">
                {getActionIcon(idx)}
              </div>
              <div>
                <span className="text-[11px] font-bold text-[#6D8072] uppercase tracking-wider block">
                  Action Step {idx + 1}
                </span>
                <p className="text-xs text-[#2A3B2F] font-medium leading-relaxed mt-0.5">
                  {action}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* 2. Long-term Prevention Section */}
      <div className="bg-white rounded-2xl border border-[#DFE7DF] shadow-md p-6 sm:p-8">
        <div className="flex items-center gap-2 mb-2">
          <div className="w-8 h-8 rounded-lg bg-[#E8F0EA] text-[#234E35] flex items-center justify-center">
            <ShieldCheck className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-xl sm:text-2xl font-serif font-bold text-[#142C1F] tracking-tight">
              Prevention Practices
            </h3>
            <p className="text-xs text-[#526356]">
              Cultural practices to break the disease cycle and protect subsequent seasons
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5 mt-6">
          {preventions.map((prev, idx) => (
            <div
              key={idx}
              className="p-4 rounded-xl bg-[#FAFAF8] border border-[#E6ECE6] flex flex-col justify-between"
            >
              <div className="flex items-center gap-2 mb-2">
                <Sprout className="w-4 h-4 text-[#356345]" />
                <span className="text-xs font-serif font-bold text-[#1E3023]">
                  Method {idx + 1}
                </span>
              </div>
              <p className="text-xs text-[#3E5042] leading-relaxed">
                {prev}
              </p>
            </div>
          ))}
        </div>

        {/* Responsible Treatment & Compliance Notice (Mandated by Prompt #7 & #19) */}
        <div className="mt-6 p-4 rounded-xl bg-[#F6F8F5] border border-[#D8E4D9] text-xs text-[#4E6253] flex items-start gap-3">
          <AlertTriangle className="w-4 h-4 text-amber-700 shrink-0 mt-0.5" />
          <div className="leading-relaxed">
            <strong className="text-[#1E2E22]">Agricultural Safety & Compliance Notice:</strong> When considering bio-fungicides or therapeutic foliar sprays, always consult regional agricultural extension specialists and strictly follow locally approved product labels, application rates, pre-harvest intervals (PHI), and safety instructions. Never apply unverified chemicals without local authorization.
          </div>
        </div>
      </div>
    </div>
  );
};
