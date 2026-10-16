import React, { useState } from 'react';
import { Smartphone, Download, X, Sparkles, Check, WifiOff } from 'lucide-react';
import { usePWAInstall } from '../hooks/usePWAInstall';

interface AndroidInstallBannerProps {
  onOpenModal: () => void;
}

export const AndroidInstallBanner: React.FC<AndroidInstallBannerProps> = ({ onOpenModal }) => {
  const { isInstallable, isInstalled, install, isAndroid } = usePWAInstall();
  const [dismissed, setDismissed] = useState(false);

  // If already running standalone or dismissed, do not display
  if (isInstalled || dismissed) return null;

  return (
    <div className="bg-[#142C1F] text-white px-3 sm:px-4 py-2 border-b border-[#234E35] flex items-center justify-between gap-3 text-xs">
      <div className="flex items-center gap-2.5 min-w-0">
        <div className="w-7 h-7 rounded-lg bg-white p-0.5 shrink-0 flex items-center justify-center shadow-xs">
          <img
            src="/pwa-192x192.png"
            alt="App icon"
            className="w-full h-full rounded-md object-cover"
          />
        </div>
        <div className="truncate">
          <span className="font-semibold text-white truncate block sm:inline">
            Get the AgroVision Android App
          </span>
          <span className="text-[11px] text-emerald-300 hidden sm:inline ml-2">
            • Fast camera access, real-time GPS & 248 crops offline
          </span>
        </div>
      </div>

      <div className="flex items-center gap-2 shrink-0">
        {isInstallable ? (
          <button
            onClick={() => install()}
            className="bg-[#2E7A4A] hover:bg-[#25663D] text-white font-semibold px-3 py-1 rounded-lg text-xs flex items-center gap-1.5 transition shadow-xs cursor-pointer"
          >
            <Download className="w-3.5 h-3.5" />
            <span>Install</span>
          </button>
        ) : (
          <button
            onClick={onOpenModal}
            className="bg-[#2E7A4A] hover:bg-[#25663D] text-white font-semibold px-3 py-1 rounded-lg text-xs flex items-center gap-1.5 transition shadow-xs cursor-pointer"
          >
            <Smartphone className="w-3.5 h-3.5" />
            <span>Install App</span>
          </button>
        )}

        <button
          onClick={() => setDismissed(true)}
          className="text-white/60 hover:text-white p-1 rounded-md transition cursor-pointer"
          aria-label="Dismiss banner"
        >
          <X className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};
