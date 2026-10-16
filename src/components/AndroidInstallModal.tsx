import React from 'react';
import { X, Smartphone, Download, CheckCircle2, ArrowRight, Share2, MoreVertical, PlusSquare, WifiOff } from 'lucide-react';

interface AndroidInstallModalProps {
  isOpen: boolean;
  onClose: () => void;
  onDirectInstall?: () => Promise<boolean>;
  canDirectInstall?: boolean;
}

export const AndroidInstallModal: React.FC<AndroidInstallModalProps> = ({
  isOpen,
  onClose,
  onDirectInstall,
  canDirectInstall = false,
}) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs animate-in fade-in duration-200">
      <div className="bg-white rounded-3xl max-w-md w-full shadow-2xl border border-[#DFE7DF] overflow-hidden flex flex-col max-h-[90vh]">
        {/* Android App Header Card */}
        <div className="p-6 bg-gradient-to-br from-[#142C1F] via-[#234E35] to-[#1A3827] text-white relative">
          <button
            onClick={onClose}
            className="absolute top-4 right-4 p-1.5 rounded-full bg-white/10 hover:bg-white/20 text-white transition cursor-pointer"
            aria-label="Close"
          >
            <X className="w-5 h-5" />
          </button>

          <div className="flex items-center gap-3.5 mb-3">
            <div className="w-14 h-14 rounded-2xl bg-white p-1.5 shadow-md shrink-0 flex items-center justify-center">
              <img
                src="/pwa-192x192.png"
                alt="AgroVision AI App Icon"
                className="w-full h-full rounded-xl object-cover"
              />
            </div>
            <div>
              <div className="inline-flex items-center gap-1 text-[10px] uppercase font-bold tracking-wider bg-emerald-400/20 text-emerald-300 px-2 py-0.5 rounded-md mb-0.5">
                <span>Official Android App (PWA)</span>
              </div>
              <h3 className="text-lg font-serif font-bold leading-tight">
                AgroVision AI
              </h3>
              <p className="text-xs text-emerald-100/80">
                Crop Disease & Weather Intelligence
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3 text-[11px] text-emerald-200/90 pt-1 border-t border-white/10">
            <span className="flex items-center gap-1">
              <span className="text-amber-400 font-bold">4.9 ★</span> (Farm Tested)
            </span>
            <span>•</span>
            <span className="flex items-center gap-1">
              <WifiOff className="w-3 h-3 text-emerald-300" /> Offline Ready
            </span>
            <span>•</span>
            <span>Zero Storage (~2MB)</span>
          </div>
        </div>

        {/* Content Body */}
        <div className="p-6 overflow-y-auto space-y-4 text-xs">
          {/* Direct Android 1-Click Install Button if supported by browser */}
          {canDirectInstall && onDirectInstall ? (
            <div className="space-y-2">
              <button
                onClick={async () => {
                  const installed = await onDirectInstall();
                  if (installed) onClose();
                }}
                className="w-full py-3.5 px-4 rounded-2xl bg-[#234E35] hover:bg-[#183927] text-white font-bold text-sm flex items-center justify-center gap-2 shadow-md transition cursor-pointer"
              >
                <Download className="w-4 h-4" />
                <span>Install on Android Device</span>
              </button>
              <p className="text-[11px] text-center text-[#55695A]">
                Adds an instant launcher icon with native camera integration and full screen view.
              </p>
            </div>
          ) : (
            <div className="p-3.5 rounded-2xl bg-[#F4F8F4] border border-[#D5E2D7] text-[#2C4132] space-y-1">
              <p className="font-semibold text-xs flex items-center gap-1.5 text-[#183927]">
                <Smartphone className="w-4 h-4 text-[#234E35]" />
                How to install on any Android phone:
              </p>
              <p className="text-[11px] text-[#4F6354]">
                Install AgroVision right from Google Chrome, Edge, or Samsung Internet without downloading large APK files:
              </p>
            </div>
          )}

          {/* Android Chrome Instructions */}
          <div className="space-y-3 pt-1">
            <h4 className="font-bold text-[#142C1F] text-xs uppercase tracking-wider flex items-center gap-1.5">
              <span>Android Quick Setup in 2 Taps:</span>
            </h4>

            <div className="space-y-2.5">
              <div className="flex items-start gap-3 p-3 rounded-xl bg-white border border-[#E1EAE2]">
                <div className="w-7 h-7 rounded-lg bg-[#E5EFE7] text-[#234E35] font-bold text-xs flex items-center justify-center shrink-0">
                  1
                </div>
                <div>
                  <p className="font-semibold text-[#183827]">
                    Tap the 3 dots menu <MoreVertical className="w-3.5 h-3.5 inline text-gray-700" />
                  </p>
                  <p className="text-[11px] text-[#55695A] mt-0.5">
                    Located in the top-right corner of Google Chrome or Samsung Internet.
                  </p>
                </div>
              </div>

              <div className="flex items-start gap-3 p-3 rounded-xl bg-white border border-[#E1EAE2]">
                <div className="w-7 h-7 rounded-lg bg-[#E5EFE7] text-[#234E35] font-bold text-xs flex items-center justify-center shrink-0">
                  2
                </div>
                <div>
                  <p className="font-semibold text-[#183827]">
                    Select <span className="underline decoration-[#234E35] font-bold">"Install app"</span> or <span className="underline decoration-[#234E35] font-bold">"Add to Home screen"</span>
                  </p>
                  <p className="text-[11px] text-[#55695A] mt-0.5">
                    The AgroVision leaf icon will appear directly on your Android app drawer.
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Android App Highlights */}
          <div className="pt-3 border-t border-[#E8EEE8] space-y-2">
            <span className="text-[10px] font-bold uppercase tracking-wider text-[#637668] block">
              Native Android App Features Included:
            </span>
            <div className="grid grid-cols-2 gap-2 text-[11px] text-[#34483B]">
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                <span>Instant Camera Shutter</span>
              </div>
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                <span>Real-Time Field GPS</span>
              </div>
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                <span>248 Crops Offline</span>
              </div>
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                <span>No Browser URL Bar</span>
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="p-4 bg-[#F8FAF7] border-t border-[#EEF2EE] flex justify-end">
          <button
            onClick={onClose}
            className="px-5 py-2 rounded-xl bg-[#E4ECE5] hover:bg-[#D5E0D7] text-[#22442E] font-semibold text-xs transition cursor-pointer"
          >
            Got it, Close
          </button>
        </div>
      </div>
    </div>
  );
};
