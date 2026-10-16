import React from 'react';
import {
  CloudSun,
  Droplets,
  Wind,
  CloudRain,
  Sun,
  Cloud,
  Snowflake,
  AlertCircle,
  ShieldCheck,
  TrendingUp,
  MapPin,
  Calendar,
} from 'lucide-react';
import { WeatherData, RiskLevel } from '../types';
import { calculateDiseaseRisk } from '../services/weather';

interface WeatherIntelligenceProps {
  weather: WeatherData;
  onOpenLocation: () => void;
  detectedCrop?: string;
  detectedCondition?: string;
}

export const WeatherIntelligence: React.FC<WeatherIntelligenceProps> = ({
  weather,
  onOpenLocation,
  detectedCrop = 'your crop',
  detectedCondition = 'the current scan',
}) => {
  const riskInfo = calculateDiseaseRisk(weather);

  const getRiskColor = (level: RiskLevel) => {
    switch (level) {
      case 'High':
        return {
          bg: 'bg-rose-50 border-rose-200 text-rose-900',
          badge: 'bg-rose-600 text-white',
          dot: 'bg-rose-500',
          text: 'High Risk Conditions',
        };
      case 'Moderate':
        return {
          bg: 'bg-amber-50 border-amber-200 text-amber-900',
          badge: 'bg-amber-600 text-white',
          dot: 'bg-amber-500',
          text: 'Moderate Risk Conditions',
        };
      case 'Low':
      default:
        return {
          bg: 'bg-emerald-50 border-emerald-200 text-emerald-900',
          badge: 'bg-[#2E6B43] text-white',
          dot: 'bg-emerald-500',
          text: 'Low Risk Conditions',
        };
    }
  };

  const riskStyle = getRiskColor(riskInfo.level);

  // Weather icon selector
  const renderWeatherIcon = (iconName: string, className = 'w-5 h-5') => {
    switch (iconName) {
      case 'sun':
        return <Sun className={`${className} text-amber-500`} />;
      case 'cloud-rain':
      case 'cloud-rain-heavy':
        return <CloudRain className={`${className} text-blue-500`} />;
      case 'cloud-drizzle':
        return <Droplets className={`${className} text-blue-400`} />;
      case 'snowflake':
        return <Snowflake className={`${className} text-cyan-400`} />;
      case 'cloud':
        return <Cloud className={`${className} text-gray-400`} />;
      case 'cloud-sun':
      default:
        return <CloudSun className={`${className} text-amber-600`} />;
    }
  };

  return (
    <div className="space-y-6">
      {/* Top Card: Current Weather & Disease Risk Condition */}
      <div className="bg-white rounded-2xl border border-[#DFE7DF] shadow-md p-6 sm:p-8">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-[#E8EDE8]">
          <div>
            <div className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider text-[#2D5A3C] bg-[#E5EFE7] px-2.5 py-1 rounded-md mb-2">
              <CloudSun className="w-3.5 h-3.5" />
              <span>Weather Intelligence</span>
            </div>
            <h3 className="text-xl sm:text-2xl font-serif font-bold text-[#142C1F] tracking-tight">
              Microclimate & Disease Risk
            </h3>
            <p className="text-xs text-[#526356] mt-0.5">
              Live field atmospheric telemetry linked to {weather.location}
            </p>
          </div>

          <button
            onClick={onOpenLocation}
            className="text-xs font-semibold text-[#234E35] bg-[#EDF3EE] hover:bg-[#E2ECE3] border border-[#CCDCD0] px-3.5 py-2 rounded-xl transition flex items-center gap-1.5 self-start md:self-auto cursor-pointer"
          >
            <MapPin className="w-3.5 h-3.5" />
            <span>Change Location</span>
          </button>
        </div>

        {/* Current Metrics Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 py-6">
          <div className="p-4 rounded-xl bg-[#F8FAF7] border border-[#E7EDE8]">
            <span className="text-[11px] text-[#637568] uppercase font-semibold block">
              Temperature
            </span>
            <div className="flex items-baseline gap-1 mt-1">
              <span className="text-3xl font-serif font-bold text-[#142C1F]">
                {weather.current.temp}
              </span>
              <span className="text-sm font-medium text-[#4E6153]">
                {weather.current.tempUnit}
              </span>
            </div>
            <span className="text-[11px] text-[#6F8274] block mt-1">
              {weather.current.condition}
            </span>
          </div>

          <div className="p-4 rounded-xl bg-[#F8FAF7] border border-[#E7EDE8]">
            <span className="text-[11px] text-[#637568] uppercase font-semibold block">
              Relative Humidity
            </span>
            <div className="flex items-baseline gap-1 mt-1">
              <span className="text-3xl font-serif font-bold text-[#142C1F]">
                {weather.current.humidity}
              </span>
              <span className="text-sm font-medium text-[#4E6153]">%</span>
            </div>
            <span className="text-[11px] text-[#6F8274] block mt-1">
              {weather.current.humidity > 75 ? 'Prolonged dew window' : 'Moderate ambient'}
            </span>
          </div>

          <div className="p-4 rounded-xl bg-[#F8FAF7] border border-[#E7EDE8]">
            <span className="text-[11px] text-[#637568] uppercase font-semibold block">
              Precipitation Probability
            </span>
            <div className="flex items-baseline gap-1 mt-1">
              <span className="text-3xl font-serif font-bold text-[#142C1F]">
                {weather.current.rainProbability}
              </span>
              <span className="text-sm font-medium text-[#4E6153]">%</span>
            </div>
            <span className="text-[11px] text-[#6F8274] block mt-1">
              {weather.current.isRaining ? 'Active rain recorded' : 'Showers in forecast'}
            </span>
          </div>

          <div className="p-4 rounded-xl bg-[#F8FAF7] border border-[#E7EDE8]">
            <span className="text-[11px] text-[#637568] uppercase font-semibold block">
              Wind Velocity
            </span>
            <div className="flex items-baseline gap-1 mt-1">
              <span className="text-3xl font-serif font-bold text-[#142C1F]">
                {weather.current.windSpeed}
              </span>
              <span className="text-sm font-medium text-[#4E6153]">
                {weather.current.windUnit}
              </span>
            </div>
            <span className="text-[11px] text-[#6F8274] block mt-1">
              Spore drift potential
            </span>
          </div>
        </div>

        {/* Section: Disease Risk Conditions (Mandated by Prompt #6) */}
        <div className={`p-5 rounded-xl border ${riskStyle.bg} space-y-3`}>
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div className="flex items-center gap-2.5">
              <span className={`w-3 h-3 rounded-full ${riskStyle.dot} animate-pulse`} />
              <h4 className="font-serif font-bold text-base">
                Disease Risk Conditions: {riskStyle.text}
              </h4>
            </div>
            <span className={`text-[11px] font-bold uppercase tracking-wider px-3 py-1 rounded-md ${riskStyle.badge}`}>
              Risk: {riskInfo.level}
            </span>
          </div>

          <p className="text-xs leading-relaxed">
            "{riskInfo.explanation}"
          </p>

          <div className="pt-2 border-t border-black/10">
            <span className="text-[11px] font-semibold uppercase tracking-wider opacity-80 block mb-1.5">
              Atmospheric Contributing Indicators:
            </span>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              {riskInfo.contributingWeatherPoints.map((point, idx) => (
                <div key={idx} className="text-xs flex items-center gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-current opacity-60 shrink-0" />
                  <span>{point}</span>
                </div>
              ))}
            </div>
          </div>

          <p className="text-[10px] opacity-75 italic pt-1">
            * Informational estimate based on open meteorological models and standard plant epidemiology thresholds.
          </p>
        </div>
      </div>

      {/* 5-7 Day Upcoming Weather Forecast */}
      <div className="bg-white rounded-2xl border border-[#DFE7DF] shadow-md p-6 sm:p-8">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <Calendar className="w-4 h-4 text-[#234E35]" />
            <h4 className="font-serif font-bold text-lg text-[#142C1F]">
              Upcoming Weather (7-Day Forecast)
            </h4>
          </div>
          <span className="text-xs text-[#6F8274]">
            Precipitation & Leaf Moisture Outlook
          </span>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-3">
          {weather.forecast.map((day, idx) => {
            const isToday = idx === 0;
            return (
              <div
                key={day.day + idx}
                className={`p-3.5 rounded-xl border text-center transition ${
                  isToday
                    ? 'bg-[#F2F7F3] border-[#2E6B43] shadow-xs'
                    : 'bg-[#F9FAF8] border-[#E5EDE6] hover:border-[#CCDCD0]'
                }`}
              >
                <span className={`text-xs font-bold block ${isToday ? 'text-[#234E35]' : 'text-[#3E5244]'}`}>
                  {day.day}
                </span>

                <div className="my-2 flex justify-center">
                  {renderWeatherIcon(day.icon, 'w-6 h-6')}
                </div>

                <p className="text-[11px] font-medium text-[#1E2E22] truncate">
                  {day.condition}
                </p>

                <div className="mt-2 text-xs font-semibold text-[#142C1F]">
                  <span>{day.tempMax}°</span>
                  <span className="text-[#889B8C] ml-1 font-normal">{day.tempMin}°</span>
                </div>

                <div className="mt-2 pt-2 border-t border-[#E5EBE5] flex items-center justify-center gap-1 text-[11px] text-blue-700">
                  <Droplets className="w-3 h-3 text-blue-500" />
                  <span>{day.rainProb}%</span>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
