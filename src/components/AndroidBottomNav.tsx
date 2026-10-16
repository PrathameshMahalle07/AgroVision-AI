import React from 'react';
import {
  Sprout,
  Camera,
  BookOpen,
  CalendarDays,
  CloudSun,
  LayoutDashboard,
} from 'lucide-react';
import { NavTab } from './Navbar';

interface AndroidBottomNavProps {
  activeTab: NavTab;
  onTabChange: (tab: NavTab) => void;
  totalScansCount: number;
}

export const AndroidBottomNav: React.FC<AndroidBottomNavProps> = ({
  activeTab,
  onTabChange,
  totalScansCount,
}) => {
  const triggerHaptic = () => {
    try {
      if (typeof navigator !== 'undefined' && 'vibrate' in navigator) {
        navigator.vibrate?.(12);
      }
    } catch {
      // Haptics optional
    }
  };

  const handleSelect = (tab: NavTab) => {
    triggerHaptic();
    onTabChange(tab);
  };

  return (
    <nav
      className="md:hidden fixed bottom-0 inset-x-0 z-40 bg-[#FBFBFA]/95 backdrop-blur-lg border-t border-[#DFE7DF] pb-[env(safe-area-inset-bottom,0px)] shadow-[0_-4px_20px_rgba(0,0,0,0.06)]"
      aria-label="Mobile Navigation"
    >
      <div className="flex items-center justify-around h-16 px-2 max-w-lg mx-auto relative">
        {/* 1. Home */}
        <button
          onClick={() => handleSelect('home')}
          className={`flex flex-col items-center justify-center flex-1 py-1 transition cursor-pointer ${
            activeTab === 'home' ? 'text-[#1E4D2F]' : 'text-[#637768] hover:text-[#254A32]'
          }`}
        >
          <div
            className={`px-3 py-0.5 rounded-full transition ${
              activeTab === 'home' ? 'bg-[#DDECE0]' : 'bg-transparent'
            }`}
          >
            <Sprout className="w-5 h-5" />
          </div>
          <span className={`text-[10px] tracking-tight mt-0.5 ${activeTab === 'home' ? 'font-bold' : 'font-medium'}`}>
            Home
          </span>
        </button>

        {/* 2. 248 Crops Encyclopedia */}
        <button
          onClick={() => handleSelect('library')}
          className={`flex flex-col items-center justify-center flex-1 py-1 transition cursor-pointer ${
            activeTab === 'library' ? 'text-[#1E4D2F]' : 'text-[#637768] hover:text-[#254A32]'
          }`}
        >
          <div
            className={`px-3 py-0.5 rounded-full transition ${
              activeTab === 'library' ? 'bg-[#DDECE0]' : 'bg-transparent'
            }`}
          >
            <BookOpen className="w-5 h-5" />
          </div>
          <span className={`text-[10px] tracking-tight mt-0.5 ${activeTab === 'library' ? 'font-bold' : 'font-medium'}`}>
            248 Crops
          </span>
        </button>

        {/* 3. CENTER ELEVATED CAMERA SCAN BUTTON (Native Android Style) */}
        <div className="flex flex-col items-center justify-center -mt-6 px-1 relative">
          <button
            onClick={() => handleSelect('scan')}
            className={`w-14 h-14 rounded-full flex items-center justify-center shadow-lg transition transform active:scale-95 cursor-pointer relative ${
              activeTab === 'scan'
                ? 'bg-[#153421] text-white ring-4 ring-[#8CE39B]/60'
                : 'bg-gradient-to-br from-[#2D6A44] to-[#1B3E28] text-white hover:brightness-110 shadow-emerald-950/20'
            }`}
            aria-label="Scan Crop"
          >
            <Camera className="w-7 h-7" />
            <span className="absolute -top-1 -right-1 flex h-3 w-3">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-3 w-3 bg-[#44DF79]"></span>
            </span>
          </button>
          <span className={`text-[10px] tracking-tight mt-1 ${activeTab === 'scan' ? 'font-bold text-[#1E4D2F]' : 'font-semibold text-[#3B5441]'}`}>
            Scan
          </span>
        </div>

        {/* 4. Past Timeline / Scans */}
        <button
          onClick={() => handleSelect('crops')}
          className={`flex flex-col items-center justify-center flex-1 py-1 transition cursor-pointer relative ${
            activeTab === 'crops' ? 'text-[#1E4D2F]' : 'text-[#637768] hover:text-[#254A32]'
          }`}
        >
          <div
            className={`px-3 py-0.5 rounded-full transition relative ${
              activeTab === 'crops' ? 'bg-[#DDECE0]' : 'bg-transparent'
            }`}
          >
            <CalendarDays className="w-5 h-5" />
            {totalScansCount > 0 && (
              <span className="absolute -top-1 -right-1 text-[9px] font-bold bg-[#234E35] text-white w-4 h-4 rounded-full flex items-center justify-center">
                {totalScansCount}
              </span>
            )}
          </div>
          <span className={`text-[10px] tracking-tight mt-0.5 ${activeTab === 'crops' ? 'font-bold' : 'font-medium'}`}>
            Timeline
          </span>
        </button>

        {/* 5. Weather & Insights */}
        <button
          onClick={() => handleSelect('insights')}
          className={`flex flex-col items-center justify-center flex-1 py-1 transition cursor-pointer ${
            activeTab === 'insights' ? 'text-[#1E4D2F]' : 'text-[#637768] hover:text-[#254A32]'
          }`}
        >
          <div
            className={`px-3 py-0.5 rounded-full transition ${
              activeTab === 'insights' ? 'bg-[#DDECE0]' : 'bg-transparent'
            }`}
          >
            <CloudSun className="w-5 h-5" />
          </div>
          <span className={`text-[10px] tracking-tight mt-0.5 ${activeTab === 'insights' ? 'font-bold' : 'font-medium'}`}>
            Weather
          </span>
        </button>
      </div>
    </nav>
  );
};
