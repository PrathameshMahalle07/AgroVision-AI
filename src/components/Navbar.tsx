import React, { useState } from 'react';
import {
  Sprout,
  Camera,
  LayoutDashboard,
  CalendarDays,
  CloudSun,
  BookOpen,
  MapPin,
  Menu,
  X,
  Sparkles,
  Smartphone,
  Download,
} from 'lucide-react';
import { LocationInfo } from '../services/location';

export type NavTab = 'home' | 'scan' | 'dashboard' | 'crops' | 'insights' | 'library';

interface NavbarProps {
  activeTab: NavTab;
  onTabChange: (tab: NavTab) => void;
  location: LocationInfo;
  onOpenLocationModal: () => void;
  totalScansCount: number;
  onOpenInstallModal?: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  activeTab,
  onTabChange,
  location,
  onOpenLocationModal,
  totalScansCount,
  onOpenInstallModal,
}) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navItems: { id: NavTab; label: string; icon: React.ComponentType<{ className?: string }> }[] = [
    { id: 'home', label: 'Home', icon: Sprout },
    { id: 'scan', label: 'Scan Crop', icon: Camera },
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'crops', label: 'My Crops', icon: CalendarDays },
    { id: 'insights', label: 'Insights & Weather', icon: CloudSun },
    { id: 'library', label: 'Crop Library', icon: BookOpen },
  ];

  const handleNavClick = (tab: NavTab) => {
    onTabChange(tab);
    setMobileMenuOpen(false);
  };

  return (
    <header className="sticky top-0 z-40 bg-[#FBFBFA]/90 backdrop-blur-md border-b border-[#E7EDE8] transition">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-18">
          {/* Logo & Brand */}
          <div className="flex items-center gap-8">
            <button
              onClick={() => handleNavClick('home')}
              className="flex items-center gap-2.5 group text-left cursor-pointer"
            >
              <div className="w-10 h-10 rounded-xl bg-[#234E35] flex items-center justify-center text-white shadow-xs group-hover:bg-[#1B3E2A] transition">
                <Sprout className="w-5 h-5" />
              </div>
              <div>
                <span className="text-lg font-serif font-bold text-[#142C1F] tracking-tight flex items-center gap-1.5">
                  AgroVision <span className="text-xs font-sans font-semibold text-[#3B704C] bg-[#E7F0E8] px-1.5 py-0.5 rounded-md uppercase tracking-wider">AI</span>
                </span>
                <span className="text-[10px] block font-sans text-[#6B7D70] font-medium tracking-wide">
                  Agricultural Intelligence
                </span>
              </div>
            </button>

            {/* Desktop Navigation Links */}
            <nav className="hidden md:flex items-center gap-1">
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = activeTab === item.id;
                return (
                  <button
                    key={item.id}
                    onClick={() => handleNavClick(item.id)}
                    className={`px-3 py-2 rounded-lg text-xs font-semibold transition flex items-center gap-1.5 cursor-pointer ${
                      isActive
                        ? 'bg-[#EAF1EB] text-[#1E432E] shadow-2xs'
                        : 'text-[#4F6254] hover:text-[#142C1F] hover:bg-[#F2F6F3]'
                    }`}
                  >
                    <Icon className={`w-4 h-4 ${isActive ? 'text-[#234E35]' : 'text-[#7A8E7E]'}`} />
                    <span>{item.label}</span>
                    {item.id === 'crops' && totalScansCount > 0 && (
                      <span className="ml-1 text-[10px] px-1.5 py-0.2 rounded-full bg-[#234E35] text-white">
                        {totalScansCount}
                      </span>
                    )}
                  </button>
                );
              })}
            </nav>
          </div>

          {/* Right actions: Location & Action */}
          <div className="flex items-center gap-3">
            {/* Location selector pill */}
            <button
              onClick={onOpenLocationModal}
              className={`flex items-center gap-1.5 text-xs border px-3 py-1.5 rounded-full font-medium transition cursor-pointer max-w-[210px] truncate ${
                location.isGps
                  ? 'text-[#1B4D2E] bg-[#E2EFE5] hover:bg-[#D5E7DA] border-[#97C5A3]'
                  : 'text-[#2A4834] bg-[#EDF3EE] hover:bg-[#E2ECE3] border-[#D7E3D8]'
              }`}
              title={location.isGps ? `GPS Active (±${location.accuracyMeters || 10}m) - Click to change` : 'Click to enable real-time GPS location'}
            >
              {location.isGps ? (
                <span className="relative flex h-2 w-2 shrink-0">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-600"></span>
                </span>
              ) : (
                <MapPin className="w-3.5 h-3.5 text-[#2D5A3C] shrink-0" />
              )}
              <span className="truncate">{location.name}</span>
              {location.isGps && (
                <span className="text-[9px] uppercase tracking-wider font-bold bg-[#234E35] text-white px-1.5 py-0.2 rounded shrink-0">
                  GPS
                </span>
              )}
            </button>

            {/* Android App Button */}
            {onOpenInstallModal && (
              <button
                onClick={onOpenInstallModal}
                className="hidden lg:inline-flex items-center gap-1.5 text-xs text-[#1E482D] bg-[#E7F0E8] hover:bg-[#D9E7DB] border border-[#C5D9C8] px-3 py-1.5 rounded-full font-semibold transition cursor-pointer"
                title="Install Android App / Add to Home screen"
              >
                <Smartphone className="w-3.5 h-3.5 text-[#2D5A3C]" />
                <span>Android App</span>
              </button>
            )}

            {/* Quick scan CTA */}
            <button
              onClick={() => handleNavClick('scan')}
              className="hidden sm:inline-flex items-center gap-2 bg-[#234E35] hover:bg-[#1B3E2A] text-white text-xs font-semibold px-4 py-2 rounded-xl transition shadow-xs cursor-pointer"
            >
              <Camera className="w-3.5 h-3.5" />
              <span>Scan Crop</span>
            </button>

            {/* Mobile menu trigger */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden p-2 rounded-lg text-[#3C4E41] hover:bg-[#EEF3EF] transition"
              aria-label="Toggle navigation menu"
            >
              {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu Dropdown */}
      {mobileMenuOpen && (
        <div className="md:hidden border-t border-[#E7EDE8] bg-white px-4 pt-3 pb-6 space-y-1 shadow-lg">
          <div className="mb-3 px-3 py-2 bg-[#F5F8F5] rounded-xl flex items-center justify-between">
            <span className="text-xs text-[#5C6E61]">Field Location:</span>
            <button
              onClick={() => {
                setMobileMenuOpen(false);
                onOpenLocationModal();
              }}
              className="text-xs font-semibold text-[#234E35] underline"
            >
              {location.name}
            </button>
          </div>

          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => handleNavClick(item.id)}
                className={`w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-xs font-semibold transition ${
                  isActive ? 'bg-[#EAF1EB] text-[#1E432E]' : 'text-[#445548] hover:bg-[#F2F6F3]'
                }`}
              >
                <div className="flex items-center gap-3">
                  <Icon className={`w-4 h-4 ${isActive ? 'text-[#234E35]' : 'text-[#7D9181]'}`} />
                  <span>{item.label}</span>
                </div>
                {item.id === 'crops' && totalScansCount > 0 && (
                  <span className="text-[10px] px-2 py-0.5 rounded-full bg-[#234E35] text-white">
                    {totalScansCount}
                  </span>
                )}
              </button>
            );
          })}

          <div className="pt-2">
            <button
              onClick={() => handleNavClick('scan')}
              className="w-full flex items-center justify-center gap-2 py-3 bg-[#234E35] text-white rounded-xl text-xs font-semibold shadow-xs"
            >
              <Camera className="w-4 h-4" />
              <span>Take New Crop Photo</span>
            </button>
          </div>
        </div>
      )}
    </header>
  );
};
