export type SeverityLevel = 'None' | 'Low' | 'Moderate' | 'High' | 'Severe';
export type RiskLevel = 'Low' | 'Moderate' | 'High';

export interface DiagnosisResultData {
  id?: string;
  timestamp?: string;
  isPlant: boolean;
  detectedSubject?: string;
  crop: string;
  condition: string;
  isHealthy: boolean;
  confidence: number;
  severity: SeverityLevel;
  visualSymptoms: string[];
  diseaseExplanation: string;
  contributingFactors: string[];
  weatherImpactAnalysis: string;
  diseaseRiskEstimate: RiskLevel;
  recommendedActions: string[];
  preventionMeasures: string[];
  disclaimer: string;
  imageUrl?: string;
  location?: string;
}

export interface WeatherDay {
  date?: string;
  day: string;
  condition: string;
  icon: string;
  tempMax: number;
  tempMin: number;
  rainProb: number;
  humidity: number;
}

export interface WeatherData {
  location: string;
  coordinates: {
    lat: number;
    lon: number;
  };
  current: {
    temp: number;
    tempUnit: string;
    humidity: number;
    windSpeed: number;
    windUnit: string;
    rainProbability: number;
    condition: string;
    icon: string;
    isRaining: boolean;
  };
  forecast: WeatherDay[];
}

export interface NewsArticle {
  id: string;
  title: string;
  source: string;
  date: string;
  summary: string;
  cropTag: string;
  diseaseTag: string;
  url: string;
  category: string;
  urgency: 'Low' | 'Medium' | 'High';
}

export interface ScanRecord {
  id: string;
  date: string;
  time: string;
  crop: string;
  condition: string;
  confidence: number;
  severity: SeverityLevel;
  location: string;
  imageUrl: string;
  fullReport: DiagnosisResultData;
}

export interface CropProfile {
  id: string;
  name: string;
  localName?: string;
  scientificName: string;
  category: string;
  avatarEmoji: string;
  season?: string;
  maharashtraRegion?: string;
  description: string;
  optimalTemp: string;
  waterRequirement: string;
  soilPreference: string;
  growthStages: { stage: string; days: string; description: string }[];
  commonDiseases: { name: string; symptoms: string; riskPeriod: string }[];
  commonPests: string[];
  generalPrevention: string[];
}

export interface AssistantMessage {
  id: string;
  sender: 'user' | 'assistant';
  text: string;
  timestamp: string;
}
