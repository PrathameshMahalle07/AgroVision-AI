import React from 'react';
import {
  Camera,
  LayoutDashboard,
  ShieldCheck,
  CloudSun,
  Activity,
  CheckCircle2,
  Sparkles,
  ArrowRight,
  TrendingDown,
  Layers,
} from 'lucide-react';
import { WeatherData } from '../types';

interface HeroSectionProps {
  onScanClick: () => void;
  onDashboardClick: () => void;
  weather: WeatherData;
}

export const HeroSection: React.FC<HeroSectionProps> = ({
  onScanClick,
  onDashboardClick,
  weather,
}) => {
  return (
    <section className="relative overflow-hidden pt-8 pb-16 lg:pt-14 lg:pb-24 border-b border-[#E7EDE8]">
      {/* Subtle organic background tint */}
      <div className="absolute top-0 right-0 -z-10 w-[550px] h-[550px] bg-[#E8F2EA]/40 rounded-full blur-3xl pointer-events-none transform translate-x-1/3 -translate-y-1/3" />
      <div className="absolute bottom-0 left-0 -z-10 w-[400px] h-[400px] bg-[#F5EEDC]/40 rounded-full blur-3xl pointer-events-none transform -translate-x-1/4 translate-y-1/4" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
          {/* Left Column: Headlines & CTA */}
          <div className="lg:col-span-7 space-y-6">
            {/* Tagline pill */}
            <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-[#EBF3ED] border border-[#D5E3D7] text-xs font-semibold text-[#255238]">
              <span className="w-2 h-2 rounded-full bg-[#2E6F45] animate-pulse"></span>
              <span>Intelligent In-Field Plant Pathology</span>
            </div>

            {/* Main Headline */}
            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-serif font-bold text-[#142C1F] tracking-tight leading-[1.12]">
              Know Your Crop. <br className="hidden sm:inline" />
              <span className="text-[#2D5A3C] italic font-normal">Protect Your Harvest.</span>
            </h1>

            {/* Subheading */}
            <p className="text-base sm:text-lg text-[#4E6153] max-w-2xl leading-relaxed">
              AI-powered crop disease detection, weather intelligence and practical crop-care guidance — all in one place.
            </p>

            {/* Action Buttons */}
            <div className="pt-2 flex flex-col sm:flex-row items-stretch sm:items-center gap-3.5">
              <button
                onClick={onScanClick}
                className="px-6 py-3.5 rounded-xl bg-[#234E35] hover:bg-[#1B3E2A] text-white font-semibold text-sm transition shadow-sm hover:shadow-md flex items-center justify-center gap-2.5 group cursor-pointer"
              >
                <Camera className="w-4 h-4 transition group-hover:scale-110" />
                <span>Scan Your Crop</span>
                <ArrowRight className="w-4 h-4 opacity-70 group-hover:translate-x-1 transition" />
              </button>

              <button
                onClick={onDashboardClick}
                className="px-6 py-3.5 rounded-xl bg-white hover:bg-[#F2F6F3] text-[#234E35] border border-[#CCDCD0] font-semibold text-sm transition shadow-2xs flex items-center justify-center gap-2 cursor-pointer"
              >
                <LayoutDashboard className="w-4 h-4" />
                <span>Explore Dashboard</span>
              </button>
            </div>

            {/* Key trust indicators */}
            <div className="pt-6 grid grid-cols-3 gap-4 border-t border-[#E8EEE9] max-w-lg">
              <div>
                <span className="text-xl sm:text-2xl font-serif font-bold text-[#142C1F] block">AI</span>
                <span className="text-xs text-[#637568] block mt-0.5">Vision Analysis</span>
              </div>
              <div>
                <span className="text-xl sm:text-2xl font-serif font-bold text-[#142C1F] block">240+</span>
                <span className="text-xs text-[#637568] block mt-0.5">Crop Profiles</span>
              </div>
              <div>
                <span className="text-xl sm:text-2xl font-serif font-bold text-[#142C1F] block">7-Day</span>
                <span className="text-xs text-[#637568] block mt-0.5">Microclimate Risk</span>
              </div>
            </div>
          </div>

          {/* Right Column: Hero Visual - Realistic In-Field Crop Analysis Card */}
          <div className="lg:col-span-5 relative">
            <div className="relative mx-auto max-w-md rounded-2xl bg-white p-3.5 shadow-xl border border-[#DFE7E0] transition hover:shadow-2xl">
              {/* Image Frame with crop photo and detection reticle */}
              <div className="relative aspect-4/3 rounded-xl overflow-hidden bg-[#243B2B]">
                <img
                  src="/healthy-crop-hero.jpg"
                  alt="Rows of healthy green crops in a field"
                  className="w-full h-full object-cover object-center filter saturate-95"
                />

                {/* Gentle scanning reticle overlay */}
                <div className="absolute inset-0 bg-radial from-transparent via-transparent to-black/30 pointer-events-none" />

                {/* Subtle scan frame — no fake diagnosis is shown before a real scan. */}
                <div className="absolute inset-[16%] border border-white/55 rounded-xl shadow-sm" />

                {/* Live Analysis Badge */}
                <div className="absolute top-3 left-3 bg-black/65 backdrop-blur-md text-white text-[11px] font-medium px-2.5 py-1 rounded-full flex items-center gap-1.5 border border-white/20">
                  <Activity className="w-3.5 h-3.5 text-[#63D182]" />
                  <span>Computer Vision Active</span>
                </div>

                {/* Weather condition overlay chip */}
                <div className="absolute bottom-3 left-3 bg-white/90 backdrop-blur-md text-[#1E2E22] text-[11px] font-medium px-2.5 py-1 rounded-full flex items-center gap-1.5 shadow-xs border border-white/60">
                  <CloudSun className="w-3.5 h-3.5 text-[#2D5A3C]" />
                  <span>{weather.current.temp}°C • {weather.current.humidity}% Humidity</span>
                </div>
              </div>

              {/* Scan Status Card */}
              <div className="p-3.5 mt-2 bg-[#F9FAF8] rounded-xl border border-[#E7EDE8] space-y-2">
                <div className="flex items-center justify-between gap-3">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-wider text-[#6B7E70]">
                      Ready for analysis
                    </span>
                    <h4 className="text-sm font-serif font-bold text-[#142C1F]">
                      Scan your crop to identify its health
                    </h4>
                  </div>
                  <CheckCircle2 className="w-5 h-5 text-[#2D5A3C] shrink-0" />
                </div>
                <p className="text-[11px] text-[#4E6153] leading-snug">
                  Results are generated from the image you provide — no disease is assumed before a scan.
                </p>
              </div>
            </div>

            {/* Floating micro-card: Risk Conditions */}
            <div className="hidden sm:flex absolute -bottom-5 -left-4 bg-white/95 backdrop-blur-md p-3 rounded-xl border border-[#DFE7E0] shadow-lg max-w-[200px] items-center gap-2.5">
              <div className="w-8 h-8 rounded-lg bg-[#FAF0E4] text-[#A64B00] flex items-center justify-center shrink-0">
                <CloudSun className="w-4 h-4" />
              </div>
              <div>
                <span className="text-[10px] font-bold uppercase text-[#A64B00] block">Spore Risk</span>
                <span className="text-xs font-semibold text-[#142C1F] block">High Moisture Alert</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
