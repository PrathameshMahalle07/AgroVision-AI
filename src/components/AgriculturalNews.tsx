import React, { useState, useEffect } from 'react';
import {
  Newspaper,
  ExternalLink,
  Tag,
  Calendar,
  AlertCircle,
  Filter,
  RefreshCw,
  Building2,
} from 'lucide-react';
import { NewsArticle } from '../types';
import { fetchAgriculturalNews } from '../services/news';

interface AgriculturalNewsProps {
  currentCrop?: string;
}

export const AgriculturalNews: React.FC<AgriculturalNewsProps> = ({ currentCrop = 'all' }) => {
  const [news, setNews] = useState<NewsArticle[]>([]);
  const [selectedFilter, setSelectedFilter] = useState<string>(currentCrop);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    loadNews(selectedFilter);
  }, [selectedFilter]);

  const loadNews = async (crop: string) => {
    setIsLoading(true);
    try {
      const data = await fetchAgriculturalNews(crop);
      setNews(data);
    } catch (err) {
      console.error('Error fetching agricultural news:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const filterOptions = [
    { id: 'all', label: 'All Updates' },
    { id: 'tomato', label: 'Tomato Alerts' },
    { id: 'corn', label: 'Corn / Maize' },
    { id: 'potato', label: 'Potato Watch' },
    { id: 'rice', label: 'Rice' },
    { id: 'general', label: 'General / FAO' },
  ];

  const getUrgencyBadge = (urgency: 'Low' | 'Medium' | 'High') => {
    switch (urgency) {
      case 'High':
        return 'bg-rose-100 text-rose-800 border-rose-200';
      case 'Medium':
        return 'bg-amber-100 text-amber-800 border-amber-200';
      case 'Low':
      default:
        return 'bg-[#E3EDE5] text-[#234E35] border-[#CCDCD0]';
    }
  };

  return (
    <div className="bg-white rounded-2xl border border-[#DFE7DF] shadow-md p-6 sm:p-8">
      {/* Header & Filter Controls */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-[#E8EDE8]">
        <div>
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider text-[#2D5A3C] bg-[#E5EFE7] px-2.5 py-1 rounded-md mb-2">
            <Newspaper className="w-3.5 h-3.5" />
            <span>Official Research & Advisories</span>
          </div>
          <h3 className="text-xl sm:text-2xl font-serif font-bold text-[#142C1F] tracking-tight">
            Latest Agricultural Updates
          </h3>
          <p className="text-xs text-[#526356]">
            Verified outbreak alerts, extension bulletins, and pathology research from reliable institutions
          </p>
        </div>

        {/* Filter Pills */}
        <div className="flex items-center gap-1.5 overflow-x-auto pb-1 sm:pb-0">
          {filterOptions.map((opt) => {
            const isActive = selectedFilter.toLowerCase() === opt.id.toLowerCase();
            return (
              <button
                key={opt.id}
                onClick={() => setSelectedFilter(opt.id)}
                className={`text-xs px-3 py-1.5 rounded-lg font-medium whitespace-nowrap transition cursor-pointer ${
                  isActive
                    ? 'bg-[#234E35] text-white shadow-2xs'
                    : 'bg-[#F2F6F3] text-[#4E6153] hover:bg-[#E5ECE6]'
                }`}
              >
                {opt.label}
              </button>
            );
          })}
        </div>
      </div>

      {/* News Articles Grid */}
      {isLoading ? (
        <div className="py-12 text-center text-xs text-[#6F8274] flex items-center justify-center gap-2">
          <RefreshCw className="w-4 h-4 animate-spin text-[#234E35]" />
          <span>Loading verified agricultural bulletins...</span>
        </div>
      ) : news.length === 0 ? (
        <div className="py-12 text-center text-xs text-[#6F8274]">
          No active alerts found for this filter. Check back shortly.
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          {news.map((item) => (
            <article
              key={item.id}
              className="p-5 rounded-xl bg-[#F9FAF8] border border-[#E7EDE8] hover:border-[#CCDCD0] hover:shadow-xs transition flex flex-col justify-between"
            >
              <div className="space-y-2.5">
                {/* Source & Urgency Header */}
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[11px] font-bold text-[#234E35] flex items-center gap-1">
                    <Building2 className="w-3 h-3 text-[#2D5A3C]" />
                    {item.source}
                  </span>
                  <span
                    className={`text-[10px] font-semibold uppercase px-2 py-0.5 rounded-md border ${getUrgencyBadge(
                      item.urgency
                    )}`}
                  >
                    {item.category}
                  </span>
                </div>

                {/* Title */}
                <h4 className="text-sm font-serif font-bold text-[#142C1F] leading-snug">
                  {item.title}
                </h4>

                {/* Summary */}
                <p className="text-xs text-[#4C5E51] leading-relaxed">
                  {item.summary}
                </p>
              </div>

              {/* Tags and Read Source Action */}
              <div className="pt-4 mt-4 border-t border-[#E8EDE8] flex items-center justify-between gap-2">
                <div className="flex items-center gap-2">
                  <span className="text-[10px] px-2 py-0.5 rounded-md bg-[#EBF1EC] text-[#294E36] font-medium">
                    {item.cropTag}
                  </span>
                  <span className="text-[10px] text-[#788C7D] flex items-center gap-1">
                    <Calendar className="w-3 h-3" />
                    {item.date}
                  </span>
                </div>

                <a
                  href={item.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-xs font-semibold text-[#234E35] hover:text-[#183925] flex items-center gap-1 transition"
                >
                  <span>Read Source</span>
                  <ExternalLink className="w-3 h-3" />
                </a>
              </div>
            </article>
          ))}
        </div>
      )}
    </div>
  );
};
