import React, { useState, useMemo } from 'react';
import {
  BookOpen,
  Thermometer,
  Droplets,
  Layers,
  Bug,
  ShieldAlert,
  Sprout,
  CheckCircle2,
  ChevronRight,
  Search,
  Filter,
  MapPin,
  Calendar,
  Sparkles,
  X,
  MessageSquare,
  Globe,
  SlidersHorizontal,
} from 'lucide-react';
import { CROPS_DATABASE, CROP_CATEGORIES, MAHARASHTRA_REGIONS } from '../data/sampleCrops';
import { CropProfile } from '../types';

interface CropKnowledgeProps {
  initialCropId?: string;
  onAskAboutCrop?: (cropName: string) => void;
}

export const CropKnowledge: React.FC<CropKnowledgeProps> = ({
  initialCropId = 'alphonso-mango',
  onAskAboutCrop,
}) => {
  const [selectedCropId, setSelectedCropId] = useState<string>(initialCropId);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('All Crops');
  const [selectedRegion, setSelectedRegion] = useState<string>('All Regions');
  const [selectedSeason, setSelectedSeason] = useState<string>('All Seasons');
  const [isFilterExpanded, setIsFilterExpanded] = useState(false);

  // Popular Maharashtra and Indian crops for instant 1-click access
  const QUICK_CROPS = [
    { id: 'alphonso-mango', label: 'Alphonso Mango', marathi: 'हापूस आंबा', emoji: '🥭' },
    { id: 'thompson-grapes', label: 'Nashik Grapes', marathi: 'द्राक्षे', emoji: '🍇' },
    { id: 'bhagwa-pomegranate', label: 'Bhagwa Pomegranate', marathi: 'भगवा डाळिंब', emoji: '🍎' },
    { id: 'jalgaon-banana', label: 'Jalgaon Banana', marathi: 'ग्रँड नैन केळी', emoji: '🍌' },
    { id: 'nagpur-orange', label: 'Nagpur Orange', marathi: 'नागपूर संत्रे', emoji: '🍊' },
    { id: 'sangli-turmeric', label: 'Sangli Turmeric', marathi: 'सांगली हळद', emoji: '🟡' },
    { id: 'nashik-red-onion', label: 'Nashik Onion', marathi: 'नाशिक कांदा', emoji: '🧅' },
    { id: 'sugarcane', label: 'Sugarcane', marathi: 'ऊस', emoji: '🎋' },
    { id: 'cotton-bt', label: 'BT Cotton', marathi: 'कापूस', emoji: '☁️' },
    { id: 'soybean', label: 'Soybean', marathi: 'सोयाबीन', emoji: '🌱' },
    { id: 'sorghum-jowar', label: 'Maldandi Jowar', marathi: 'मालदांडी ज्वारी', emoji: '🌾' },
    { id: 'strawberry-mahabaleshwar', label: 'Strawberry', marathi: 'स्ट्रॉबेरी', emoji: '🍓' },
  ];

  // Filtering logic
  const filteredCrops = useMemo(() => {
    return CROPS_DATABASE.filter((crop) => {
      // Search text query matches English name, Marathi name, scientific name, or category
      const q = searchQuery.toLowerCase().trim();
      const matchesSearch =
        !q ||
        crop.name.toLowerCase().includes(q) ||
        (crop.localName && crop.localName.toLowerCase().includes(q)) ||
        crop.scientificName.toLowerCase().includes(q) ||
        crop.category.toLowerCase().includes(q) ||
        (crop.maharashtraRegion && crop.maharashtraRegion.toLowerCase().includes(q));

      if (!matchesSearch) return false;

      // Category filter
      if (selectedCategory === 'Maharashtra Specialties') {
        const isMhSpecialty =
          crop.maharashtraRegion?.includes('Konkan') ||
          crop.maharashtraRegion?.includes('Vidarbha') ||
          crop.maharashtraRegion?.includes('Marathwada') ||
          crop.maharashtraRegion?.includes('Western Maharashtra') ||
          crop.maharashtraRegion?.includes('Khandesh') ||
          crop.maharashtraRegion?.includes('Nashik') ||
          crop.maharashtraRegion?.includes('Solapur') ||
          crop.maharashtraRegion?.includes('Pune') ||
          crop.maharashtraRegion?.includes('Sangli') ||
          crop.maharashtraRegion?.includes('Jalgaon') ||
          crop.maharashtraRegion?.includes('Nagpur');
        if (!isMhSpecialty) return false;
      } else if (selectedCategory !== 'All Crops' && crop.category !== selectedCategory) {
        return false;
      }

      // Region filter
      if (selectedRegion !== 'All Regions') {
        const regKeyword = selectedRegion.split(' ')[0].toLowerCase();
        if (!crop.maharashtraRegion?.toLowerCase().includes(regKeyword)) {
          return false;
        }
      }

      // Season filter
      if (selectedSeason !== 'All Seasons') {
        if (!crop.season?.toLowerCase().includes(selectedSeason.toLowerCase())) {
          return false;
        }
      }

      return true;
    });
  }, [searchQuery, selectedCategory, selectedRegion, selectedSeason]);

  // Selected crop entity
  const selectedCrop =
    CROPS_DATABASE.find((c) => c.id.toLowerCase() === selectedCropId.toLowerCase()) ||
    filteredCrops[0] ||
    CROPS_DATABASE[0];

  return (
    <div className="bg-white rounded-2xl border border-[#DFE7DF] shadow-md p-5 sm:p-8 space-y-6">
      {/* Header section with badge and stats */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-5 border-b border-[#E8EDE8]">
        <div>
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider text-[#2D5A3C] bg-[#E5EFE7] px-2.5 py-1 rounded-md mb-2">
            <BookOpen className="w-3.5 h-3.5" />
            <span>Encyclopedia of Maharashtra & India</span>
          </div>
          <h3 className="text-xl sm:text-2xl font-serif font-bold text-[#142C1F] tracking-tight flex items-center gap-2">
            <span>About Your Crop</span>
            <span className="text-xs font-normal px-2.5 py-0.5 rounded-full bg-[#EAF2EC] text-[#224A32] font-sans">
              {CROPS_DATABASE.length} Crops Database
            </span>
          </h3>
          <p className="text-xs text-[#526356] mt-0.5">
            Complete botanical profiles, phenology, climatic tolerances, and plant pathology across Maharashtra & National belts
          </p>
        </div>

        {onAskAboutCrop && (
          <button
            onClick={() => onAskAboutCrop(selectedCrop.name)}
            className="self-start sm:self-auto text-xs px-3.5 py-2 rounded-xl bg-[#234E35] text-white hover:bg-[#1B3E2A] font-semibold transition flex items-center gap-1.5 shadow-2xs cursor-pointer"
          >
            <MessageSquare className="w-3.5 h-3.5" />
            <span>Ask AI about {selectedCrop.name}</span>
          </button>
        )}
      </div>

      {/* Quick shortcuts for famous Maharashtra crops */}
      <div className="space-y-1.5">
        <div className="flex items-center justify-between text-[11px] text-[#607466] font-semibold uppercase tracking-wider">
          <span>Popular Crops of Maharashtra:</span>
          <span>1-Click Quick Select</span>
        </div>
        <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-thin">
          {QUICK_CROPS.map((q) => {
            const isSelected = q.id === selectedCrop.id;
            return (
              <button
                key={q.id}
                onClick={() => setSelectedCropId(q.id)}
                className={`text-xs px-3 py-1.5 rounded-xl font-medium whitespace-nowrap transition flex items-center gap-1.5 cursor-pointer shrink-0 ${
                  isSelected
                    ? 'bg-[#234E35] text-white font-semibold shadow-xs'
                    : 'bg-[#F2F6F3] text-[#334638] hover:bg-[#E5ECE7]'
                }`}
              >
                <span>{q.emoji}</span>
                <span>{q.label}</span>
                <span className="text-[10px] opacity-75">({q.marathi})</span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Search & Filter Toolbar */}
      <div className="space-y-3 p-4 rounded-xl bg-[#F8FAF7] border border-[#E7EDE8]">
        <div className="flex flex-col sm:flex-row sm:items-center gap-2.5">
          {/* Search bar */}
          <div className="relative flex-1">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-[#7C9081]" />
            <input
              type="text"
              placeholder="Search 240+ crops by English, Marathi/Hindi name (e.g. कांदा, हळद, Mango, Cotton, Sugarcane)..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full text-xs py-2.5 pl-9 pr-8 border border-[#CFDCCD] rounded-xl focus:outline-none focus:border-[#234E35] bg-white text-[#1C2C20]"
            />
            {searchQuery && (
              <button
                onClick={() => setSearchQuery('')}
                className="absolute right-2.5 top-1/2 -translate-y-1/2 text-[#7C9081] hover:text-[#1C2C20]"
                aria-label="Clear search"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            )}
          </div>

          {/* Toggle filter drawer button */}
          <button
            onClick={() => setIsFilterExpanded(!isFilterExpanded)}
            className={`text-xs px-3.5 py-2.5 rounded-xl border flex items-center gap-1.5 font-medium transition cursor-pointer shrink-0 ${
              isFilterExpanded || selectedRegion !== 'All Regions' || selectedSeason !== 'All Seasons'
                ? 'bg-[#234E35] text-white border-[#234E35]'
                : 'bg-white text-[#3E5244] border-[#CFDCCD] hover:bg-[#EFF4F0]'
            }`}
          >
            <SlidersHorizontal className="w-3.5 h-3.5" />
            <span>Regional & Seasonal Filters</span>
          </button>
        </div>

        {/* Category Horizontal Filter Pills */}
        <div className="flex items-center gap-1.5 overflow-x-auto pb-1 pt-1 scrollbar-thin">
          {CROP_CATEGORIES.map((cat) => {
            const isSelected = selectedCategory === cat;
            return (
              <button
                key={cat}
                onClick={() => setSelectedCategory(cat)}
                className={`text-xs px-3 py-1.5 rounded-lg whitespace-nowrap transition cursor-pointer shrink-0 font-medium ${
                  isSelected
                    ? 'bg-[#234E35] text-white font-semibold shadow-2xs'
                    : 'bg-white text-[#4A5D4F] border border-[#DEE6DF] hover:bg-[#EFF4F0]'
                }`}
              >
                {cat}
              </button>
            );
          })}
        </div>

        {/* Expandable Advanced Regional & Seasonal Filter */}
        {isFilterExpanded && (
          <div className="pt-3 border-t border-[#E2EAE3] grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
            <div>
              <label className="block text-[11px] font-semibold text-[#546859] mb-1">
                Maharashtra Agro-Climatic Zone:
              </label>
              <select
                value={selectedRegion}
                onChange={(e) => setSelectedRegion(e.target.value)}
                className="w-full py-1.5 px-2.5 border border-[#CFDCCD] rounded-lg bg-white text-[#1C2C20]"
              >
                {MAHARASHTRA_REGIONS.map((reg) => (
                  <option key={reg} value={reg}>
                    {reg}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-[11px] font-semibold text-[#546859] mb-1">
                Cropping Season:
              </label>
              <select
                value={selectedSeason}
                onChange={(e) => setSelectedSeason(e.target.value)}
                className="w-full py-1.5 px-2.5 border border-[#CFDCCD] rounded-lg bg-white text-[#1C2C20]"
              >
                <option value="All Seasons">All Seasons</option>
                <option value="Kharif">Kharif (Monsoon)</option>
                <option value="Rabi">Rabi (Winter)</option>
                <option value="Summer">Summer / Zaid</option>
                <option value="Perennial">Annual / Perennial / Orchard</option>
              </select>
            </div>
          </div>
        )}

        {/* Results Counter & Crop Quick-Picker Grid */}
        <div className="pt-2 flex items-center justify-between text-xs text-[#526356] border-t border-[#E8EEE8]">
          <span className="font-medium">
            Showing <strong className="text-[#1A3324]">{filteredCrops.length}</strong> of{' '}
            {CROPS_DATABASE.length} crops
          </span>
          {(searchQuery || selectedCategory !== 'All Crops' || selectedRegion !== 'All Regions' || selectedSeason !== 'All Seasons') && (
            <button
              onClick={() => {
                setSearchQuery('');
                setSelectedCategory('All Crops');
                setSelectedRegion('All Regions');
                setSelectedSeason('All Seasons');
              }}
              className="text-[#234E35] hover:underline font-semibold cursor-pointer text-[11px]"
            >
              Reset All Filters
            </button>
          )}
        </div>

        {/* Compact scrollable crop picker chips */}
        <div className="flex flex-wrap gap-1.5 max-h-40 overflow-y-auto p-1 bg-white rounded-lg border border-[#E0E8E1]">
          {filteredCrops.map((crop) => {
            const isSelected = crop.id === selectedCrop.id;
            return (
              <button
                key={crop.id}
                onClick={() => setSelectedCropId(crop.id)}
                className={`text-[11px] px-2.5 py-1.5 rounded-lg transition flex items-center gap-1.5 cursor-pointer border ${
                  isSelected
                    ? 'bg-[#234E35] text-white border-[#234E35] font-semibold shadow-2xs'
                    : 'bg-[#FAFBF9] text-[#2C3D31] border-[#E5EDE6] hover:bg-[#EEF4EF] hover:border-[#CCD8CE]'
                }`}
              >
                <span>{crop.avatarEmoji}</span>
                <span className="truncate max-w-[140px]">{crop.name}</span>
                {crop.localName && (
                  <span className={`text-[10px] opacity-75 truncate max-w-[90px] ${isSelected ? 'text-white' : 'text-[#64796B]'}`}>
                    ({crop.localName.split('/')[0].trim()})
                  </span>
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* Selected Crop Profile Header */}
      <div className="p-5 rounded-2xl bg-gradient-to-r from-[#F6FAF6] to-[#FAFBF8] border border-[#E2EAE3] space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-4">
          <div className="flex items-start gap-3.5">
            <div className="w-14 h-14 rounded-2xl bg-white border border-[#D5E1D6] shadow-xs flex items-center justify-center text-3xl shrink-0">
              {selectedCrop.avatarEmoji}
            </div>
            <div>
              <div className="flex flex-wrap items-center gap-2 mb-1">
                <h4 className="text-xl sm:text-2xl font-serif font-bold text-[#142C1F]">
                  {selectedCrop.name}
                </h4>
                {selectedCrop.localName && (
                  <span className="text-sm font-semibold text-[#2D5A3C] bg-[#E7F0E8] px-2.5 py-0.5 rounded-lg">
                    {selectedCrop.localName}
                  </span>
                )}
              </div>
              <p className="text-xs text-[#5D7263] italic">
                {selectedCrop.scientificName} • <span className="font-medium text-[#384D3E]">{selectedCrop.category}</span>
              </p>
            </div>
          </div>

          <div className="flex flex-wrap sm:flex-col items-start sm:items-end gap-1.5 text-xs shrink-0">
            {selectedCrop.season && (
              <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-[#EEF5EF] text-[#295237] font-semibold border border-[#D5E3D7]">
                <Calendar className="w-3 h-3 text-[#295237]" />
                <span>Season: {selectedCrop.season}</span>
              </span>
            )}
            {selectedCrop.maharashtraRegion && (
              <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-[#FFF9EE] text-[#8C5D14] font-medium border border-[#F4E3C1] max-w-sm text-right">
                <MapPin className="w-3 h-3 shrink-0 text-[#8C5D14]" />
                <span className="truncate">{selectedCrop.maharashtraRegion}</span>
              </span>
            )}
          </div>
        </div>

        <p className="text-xs sm:text-sm text-[#384B3E] leading-relaxed max-w-4xl pt-1 border-t border-[#E8EFE8]">
          {selectedCrop.description}
        </p>
      </div>

      {/* Growing Requirements Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-4 rounded-xl bg-[#FAFBF9] border border-[#E7ECE6] flex flex-col justify-between">
          <div>
            <div className="flex items-center gap-2 text-[#234E35] mb-1.5">
              <Thermometer className="w-4 h-4 text-[#D96B27]" />
              <span className="text-xs font-bold uppercase tracking-wider">
                Optimal Temperature
              </span>
            </div>
            <p className="text-xs text-[#2A3E30] font-medium leading-relaxed">
              {selectedCrop.optimalTemp}
            </p>
          </div>
        </div>

        <div className="p-4 rounded-xl bg-[#FAFBF9] border border-[#E7ECE6] flex flex-col justify-between">
          <div>
            <div className="flex items-center gap-2 text-[#234E35] mb-1.5">
              <Droplets className="w-4 h-4 text-[#2E7DA8]" />
              <span className="text-xs font-bold uppercase tracking-wider">
                Water & Irrigation
              </span>
            </div>
            <p className="text-xs text-[#2A3E30] font-medium leading-relaxed">
              {selectedCrop.waterRequirement}
            </p>
          </div>
        </div>

        <div className="p-4 rounded-xl bg-[#FAFBF9] border border-[#E7ECE6] flex flex-col justify-between">
          <div>
            <div className="flex items-center gap-2 text-[#234E35] mb-1.5">
              <Layers className="w-4 h-4 text-[#8C5D14]" />
              <span className="text-xs font-bold uppercase tracking-wider">
                Soil & pH Preference
              </span>
            </div>
            <p className="text-xs text-[#2A3E30] font-medium leading-relaxed">
              {selectedCrop.soilPreference}
            </p>
          </div>
        </div>
      </div>

      {/* Growth Stages Timeline */}
      {selectedCrop.growthStages && selectedCrop.growthStages.length > 0 && (
        <div className="space-y-3">
          <h5 className="text-xs font-bold uppercase tracking-wider text-[#2D5A3C] flex items-center gap-2">
            <Sprout className="w-4 h-4" />
            <span>Growth Stages & Phenological Timeline</span>
          </h5>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
            {selectedCrop.growthStages.map((stage, idx) => (
              <div
                key={idx}
                className="p-3.5 rounded-xl border border-[#E4ECE4] bg-white hover:border-[#BED3C1] transition shadow-2xs"
              >
                <div className="flex items-center justify-between mb-1.5">
                  <span className="w-5 h-5 rounded-full bg-[#E5EFE7] text-[#234E35] font-bold text-[11px] flex items-center justify-center">
                    {idx + 1}
                  </span>
                  <span className="text-[11px] font-semibold text-[#8C5D14] bg-[#FFF8EB] px-2 py-0.5 rounded-md">
                    {stage.days}
                  </span>
                </div>
                <h6 className="text-xs font-bold text-[#142C1F] mb-1">
                  {stage.stage}
                </h6>
                <p className="text-[11px] text-[#55695B] leading-relaxed">
                  {stage.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Disease Vulnerabilities & Common Pests Matrix */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 pt-2">
        {/* Common Diseases */}
        <div className="lg:col-span-2 space-y-3">
          <h5 className="text-xs font-bold uppercase tracking-wider text-[#A33B2E] flex items-center gap-2">
            <ShieldAlert className="w-4 h-4" />
            <span>Common Pathogens & Leaf Diseases</span>
          </h5>

          <div className="space-y-2.5">
            {selectedCrop.commonDiseases.map((disease, idx) => (
              <div
                key={idx}
                className="p-3.5 rounded-xl border border-[#F0DCD7] bg-[#FDF9F8] space-y-1.5"
              >
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1">
                  <span className="text-xs font-bold text-[#912B1E]">
                    {disease.name}
                  </span>
                  <span className="text-[11px] font-medium text-[#7A362B] bg-[#FCECE8] px-2 py-0.5 rounded-md">
                    Risk: {disease.riskPeriod}
                  </span>
                </div>
                <p className="text-xs text-[#523E3A] leading-relaxed">
                  <span className="font-semibold text-[#73352A]">Symptoms: </span>
                  {disease.symptoms}
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* Common Pests */}
        <div className="space-y-3">
          <h5 className="text-xs font-bold uppercase tracking-wider text-[#8A5818] flex items-center gap-2">
            <Bug className="w-4 h-4" />
            <span>Common Insect Pests</span>
          </h5>

          <div className="p-4 rounded-xl border border-[#EFE5D5] bg-[#FDFBF7] space-y-2">
            <p className="text-xs text-[#614D32] leading-relaxed">
              Frequent foliage pests and vectors affecting {selectedCrop.name}:
            </p>
            <div className="flex flex-wrap gap-1.5">
              {selectedCrop.commonPests.map((pest, idx) => (
                <span
                  key={idx}
                  className="text-xs px-2.5 py-1 rounded-lg bg-white border border-[#E4D7C1] text-[#4F3D26] font-medium shadow-2xs"
                >
                  {pest}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Integrated Prevention & Agronomic Practices */}
      {selectedCrop.generalPrevention && selectedCrop.generalPrevention.length > 0 && (
        <div className="p-4 sm:p-5 rounded-xl bg-[#F4F8F4] border border-[#DEECDE] space-y-2.5">
          <h5 className="text-xs font-bold uppercase tracking-wider text-[#234E35] flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-[#234E35]" />
            <span>Recommended Agronomic & Preventive Care for {selectedCrop.name}</span>
          </h5>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-[#304535]">
            {selectedCrop.generalPrevention.map((tip, idx) => (
              <div key={idx} className="flex items-start gap-2">
                <span className="text-[#234E35] font-bold mt-0.5">•</span>
                <span className="leading-relaxed">{tip}</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
