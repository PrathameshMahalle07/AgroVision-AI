import React, { useState } from 'react';
import { MapPin, Navigation, Check, X, Search, Globe, Radio, Sparkles } from 'lucide-react';
import { LocationInfo, POPULAR_AG_REGIONS, getCurrentUserLocation } from '../services/location';

interface LocationModalProps {
  isOpen: boolean;
  onClose: () => void;
  currentLocation: LocationInfo;
  onSelectLocation: (loc: LocationInfo) => void;
}

export const LocationModal: React.FC<LocationModalProps> = ({
  isOpen,
  onClose,
  currentLocation,
  onSelectLocation,
}) => {
  const [search, setSearch] = useState('');
  const [regionFilter, setRegionFilter] = useState<'all' | 'maharashtra' | 'india'>('all');
  const [isLocating, setIsLocating] = useState(false);
  const [manualInput, setManualInput] = useState('');
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  if (!isOpen) return null;

  const handleUseMyLocation = async () => {
    setIsLocating(true);
    setErrorMsg(null);
    try {
      const loc = await getCurrentUserLocation();
      onSelectLocation(loc);
      onClose();
    } catch (err: any) {
      setErrorMsg(
        err.message || 'Unable to access GPS location. Please check device location permissions or select an agricultural basin below.'
      );
    } finally {
      setIsLocating(false);
    }
  };

  const handleManualSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!manualInput.trim()) return;

    onSelectLocation({
      name: manualInput.trim(),
      lat: 19.9975,
      lon: 73.7898,
      region: 'Custom Location',
      country: 'India',
    });
    onClose();
  };

  const filteredRegions = POPULAR_AG_REGIONS.filter((r) => {
    const matchesSearch =
      r.name.toLowerCase().includes(search.toLowerCase()) ||
      r.country.toLowerCase().includes(search.toLowerCase()) ||
      r.region.toLowerCase().includes(search.toLowerCase());

    if (!matchesSearch) return false;

    if (regionFilter === 'maharashtra') {
      return r.region.toLowerCase().includes('maharashtra');
    }
    if (regionFilter === 'india') {
      return r.country.toLowerCase().includes('india');
    }
    return true;
  });

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#142C1F]/50 backdrop-blur-xs">
      <div className="bg-white rounded-2xl max-w-xl w-full shadow-2xl border border-[#E4EAE4] overflow-hidden flex flex-col max-h-[92vh]">
        {/* Header */}
        <div className="p-6 border-b border-[#EEF2EE] flex items-start justify-between bg-[#F8FAF7]">
          <div>
            <div className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider text-[#2D5A3C] bg-[#E5EFE7] px-2.5 py-1 rounded-full mb-2">
              <Radio className="w-3.5 h-3.5 text-[#2D5A3C] animate-pulse" />
              <span>Real-Time GPS Location</span>
            </div>
            <h3 className="text-xl font-serif font-bold text-[#1A2E20]">
              Where is your crop located?
            </h3>
            <p className="text-xs text-[#526356] mt-1 leading-relaxed">
              Your real-time GPS coordinates allow AgroVision to pull hyper-local microclimate weather, humidity, and disease pressure models for your specific field.
            </p>
          </div>
          <button
            onClick={onClose}
            className="text-[#6D8072] hover:text-[#1A2E20] p-1.5 rounded-lg hover:bg-black/5 transition cursor-pointer"
            aria-label="Close dialog"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Body */}
        <div className="p-6 overflow-y-auto space-y-5">
          {errorMsg && (
            <div className="p-3.5 text-xs rounded-xl bg-amber-50 border border-amber-200 text-amber-900 flex items-start gap-2.5">
              <span className="font-semibold">Notice:</span>
              <span className="leading-relaxed">{errorMsg}</span>
            </div>
          )}

          {/* Real-Time High-Accuracy GPS Button */}
          <div className="space-y-1.5">
            <button
              onClick={handleUseMyLocation}
              disabled={isLocating}
              className="w-full py-3.5 px-4 rounded-xl bg-[#234E35] hover:bg-[#1B3E2A] text-white font-semibold text-sm flex items-center justify-center gap-2.5 transition shadow-sm disabled:opacity-70 cursor-pointer"
            >
              <Navigation className={`w-4 h-4 ${isLocating ? 'animate-spin' : ''}`} />
              <span>{isLocating ? 'Acquiring high-accuracy GPS coordinates...' : 'Enable Real-Time GPS Location (±5m)'}</span>
            </button>
            <span className="text-[11px] text-[#6E8172] text-center block">
              Uses device satellite/cellular positioning to reverse-geocode your village, taluka & district
            </span>
          </div>

          {/* Divider */}
          <div className="flex items-center gap-3">
            <div className="h-px flex-1 bg-[#E4EAE4]"></div>
            <span className="text-xs font-medium text-[#7D9182] uppercase tracking-wider">Or Select Agricultural Basin</span>
            <div className="h-px flex-1 bg-[#E4EAE4]"></div>
          </div>

          {/* Filter Tabs for Maharashtra and National */}
          <div className="flex items-center gap-1.5 pb-1">
            <button
              onClick={() => setRegionFilter('all')}
              className={`text-xs px-3 py-1.5 rounded-lg font-medium transition cursor-pointer ${
                regionFilter === 'all'
                  ? 'bg-[#234E35] text-white shadow-2xs font-semibold'
                  : 'bg-[#F2F6F3] text-[#4F6254] hover:bg-[#E5ECE6]'
              }`}
            >
              All Basins
            </button>
            <button
              onClick={() => setRegionFilter('maharashtra')}
              className={`text-xs px-3 py-1.5 rounded-lg font-medium transition cursor-pointer ${
                regionFilter === 'maharashtra'
                  ? 'bg-[#234E35] text-white shadow-2xs font-semibold'
                  : 'bg-[#F2F6F3] text-[#4F6254] hover:bg-[#E5ECE6]'
              }`}
            >
              Maharashtra (महाराष्ट्र)
            </button>
            <button
              onClick={() => setRegionFilter('india')}
              className={`text-xs px-3 py-1.5 rounded-lg font-medium transition cursor-pointer ${
                regionFilter === 'india'
                  ? 'bg-[#234E35] text-white shadow-2xs font-semibold'
                  : 'bg-[#F2F6F3] text-[#4F6254] hover:bg-[#E5ECE6]'
              }`}
            >
              Pan-India Hubs
            </button>
          </div>

          {/* Search & Agricultural Regions List */}
          <div>
            <div className="relative mb-2.5">
              <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-[#809585]" />
              <input
                type="text"
                placeholder="Search district, taluka, or basin (e.g., Nashik, Pune, Vidarbha)..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="w-full text-xs py-2 pl-8 pr-3 border border-[#D5E0D6] rounded-xl focus:outline-none focus:border-[#234E35] bg-[#FAFBF9]"
              />
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 max-h-52 overflow-y-auto pr-1">
              {filteredRegions.map((region) => {
                const isSelected = currentLocation.name === region.name;
                return (
                  <button
                    key={region.name}
                    onClick={() => {
                      onSelectLocation(region);
                      onClose();
                    }}
                    className={`text-left p-3 rounded-xl border text-xs transition flex items-center justify-between cursor-pointer ${
                      isSelected
                        ? 'border-[#234E35] bg-[#F2F7F3] text-[#1B3E2A] font-semibold shadow-xs'
                        : 'border-[#E4EAE4] hover:border-[#BED0C1] hover:bg-[#F9FAF8] text-[#334237]'
                    }`}
                  >
                    <div>
                      <p className="font-medium text-[#1E2E22]">{region.name}</p>
                      <p className="text-[11px] text-[#6E8172] flex items-center gap-1 mt-0.5">
                        <Globe className="w-3 h-3 text-[#94A798]" />
                        {region.region}, {region.country}
                      </p>
                    </div>
                    {isSelected && <Check className="w-4 h-4 text-[#234E35] shrink-0" />}
                  </button>
                );
              })}
            </div>
          </div>

          {/* Manual Input Form */}
          <form onSubmit={handleManualSubmit} className="pt-2 border-t border-[#EEF2EE] flex gap-2">
            <input
              type="text"
              placeholder="Or enter custom village, taluka, or city..."
              value={manualInput}
              onChange={(e) => setManualInput(e.target.value)}
              className="flex-1 text-xs py-2 px-3 border border-[#D5E0D6] rounded-xl focus:outline-none focus:border-[#234E35]"
            />
            <button
              type="submit"
              disabled={!manualInput.trim()}
              className="px-4 py-2 bg-[#EAEFEA] hover:bg-[#DCE5DD] text-[#234E35] font-semibold text-xs rounded-xl transition disabled:opacity-50"
            >
              Set
            </button>
          </form>
        </div>

        {/* Footer Note */}
        <div className="px-6 py-3.5 bg-[#F8FAF7] border-t border-[#EEF2EE] text-[11px] text-[#6E8072] flex items-center justify-between">
          <div className="flex items-center gap-1.5">
            <MapPin className="w-3.5 h-3.5 text-[#234E35]" />
            <span>Active: <strong className="text-[#1A2E20]">{currentLocation.name}</strong></span>
            {currentLocation.accuracyMeters && (
              <span className="text-[10px] bg-[#E3EDE5] text-[#234E35] px-1.5 py-0.2 rounded font-mono">
                ±{currentLocation.accuracyMeters}m
              </span>
            )}
          </div>
          <button
            onClick={onClose}
            className="text-xs font-semibold text-[#234E35] hover:underline"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
};
