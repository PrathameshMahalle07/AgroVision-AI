import React from 'react';
import { Sprout, ShieldAlert, Heart, Globe, ExternalLink } from 'lucide-react';

interface FooterProps {
  onNavigate: (tab: any) => void;
}

export const Footer: React.FC<FooterProps> = ({ onNavigate }) => {
  return (
    <footer className="bg-[#142C1F] text-[#D8E6DB] pt-14 pb-10 border-t border-[#234E35]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
        {/* Main Footer Row */}
        <div className="grid grid-cols-1 md:grid-cols-12 gap-8 items-start">
          {/* Brand & Mission */}
          <div className="md:col-span-5 space-y-3">
            <div className="flex items-center gap-2.5">
              <div className="w-9 h-9 rounded-xl bg-[#2D5A3C] flex items-center justify-center text-white">
                <Sprout className="w-5 h-5" />
              </div>
              <span className="text-xl font-serif font-bold text-white tracking-tight">
                AgroVision AI
              </span>
            </div>
            <p className="text-xs text-[#9BB1A0] leading-relaxed max-w-sm">
              Empowering farmers, growers, and agronomists with in-field computer vision pathology, microclimate weather intelligence, and responsible crop management guidance.
            </p>
          </div>

          {/* Quick Navigation Links */}
          <div className="md:col-span-3 space-y-2.5">
            <h5 className="text-xs font-bold uppercase tracking-wider text-white">
              Platform Features
            </h5>
            <ul className="space-y-1.5 text-xs text-[#9BB1A0]">
              <li>
                <button
                  onClick={() => onNavigate('scan')}
                  className="hover:text-white transition cursor-pointer"
                >
                  AI Crop Leaf Scanner
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate('dashboard')}
                  className="hover:text-white transition cursor-pointer"
                >
                  Agricultural Dashboard
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate('crops')}
                  className="hover:text-white transition cursor-pointer"
                >
                  My Crop Health Timeline
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate('insights')}
                  className="hover:text-white transition cursor-pointer"
                >
                  Microclimate Weather Risk
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate('library')}
                  className="hover:text-white transition cursor-pointer"
                >
                  Botanical Crop Library
                </button>
              </li>
            </ul>
          </div>

          {/* Agricultural Data Sources */}
          <div className="md:col-span-4 space-y-2.5">
            <h5 className="text-xs font-bold uppercase tracking-wider text-white">
              Scientific Collaborations & Standards
            </h5>
            <p className="text-xs text-[#9BB1A0] leading-relaxed">
              Telemetry correlated with Open-Meteo microclimate models, University Cooperative Extension IPM guidelines, USDA Agricultural Research Service datasets, and FAO plant health surveillance networks.
            </p>
          </div>
        </div>

        {/* Prominent Trust & Safety Disclaimer Box (Mandated by Prompt #19) */}
        <div className="p-4 rounded-xl bg-[#1C3A29] border border-[#2D5A3C] text-xs text-[#BDD2C2] flex items-start gap-3">
          <ShieldAlert className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
          <div className="space-y-1 leading-relaxed">
            <p className="font-semibold text-white">
              Agricultural Guidance Disclaimer:
            </p>
            <p className="text-[11px] text-[#A5C0AC]">
              "AgroVision AI provides informational guidance and should not replace advice from qualified agricultural professionals or local agricultural authorities. For any foliar treatment, pesticide, or bio-fungicide, growers must verify local agricultural regulations, product registrations, and approved label instructions."
            </p>
          </div>
        </div>

        {/* Bottom copyright row */}
        <div className="pt-6 border-t border-[#234E35] flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-[#78937E]">
          <div>
            © {new Date().getFullYear()} AgroVision AI. Built for modern sustainable agriculture.
          </div>
          <div className="flex items-center gap-4">
            <span>Server-side Computer Vision Engine</span>
            <span>•</span>
            <span>All Data Processed Responsibly</span>
          </div>
        </div>
      </div>
    </footer>
  );
};
