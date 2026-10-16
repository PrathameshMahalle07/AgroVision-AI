import { DiagnosisResultData, WeatherData } from '../types';

export interface AssistantContext {
  crop: string;
  condition?: string;
  confidence?: number;
  severity?: string;
  location?: string;
  weather?: {
    temp?: number;
    humidity?: number;
    condition?: string;
    forecastSummary?: string;
  };
}

export async function askCropAssistant(question: string, context: AssistantContext): Promise<string> {
  try {
    const res = await fetch('/api/crop-assistant', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question, context }),
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.error || `Request failed with status ${res.status}`);
    }

    const data = await res.json();
    return data.answer || 'No response generated.';
  } catch (error: any) {
    console.warn('Using client assistant fallback:', error);
    const q = question.toLowerCase();
    if (q.includes('yellow')) {
      return `Leaf yellowing in ${context.crop || 'your crop'} is commonly associated with early fungal lesion development (like the ${context.condition || 'the detected condition'} detected) or nutrient mobilization from older leaves. Ensure leaves stay dry and prune heavily spotted foliage at the base.`;
    }
    if (q.includes('rain') || q.includes('weather')) {
      return `With current humid conditions and upcoming rain, fungal spores reproduce and spread via rain splash. Before rain hits, remove already damaged foliage, verify drainage, and avoid touching wet leaves to prevent cross-contamination.`;
    }
    if (q.includes('spread') || q.includes('prevent')) {
      return `To stop spread: 1) Switch to drip irrigation at ground level; 2) Prune lower leaves to improve airflow; 3) Disinfect pruning tools with 70% alcohol; 4) Mulch around plants to block spore splash from the soil. Consult local agricultural authorities for approved organic or chemical bio-fungicides.`;
    }
    return `For ${context.crop || 'your crop'}, monitor the lower and middle foliage daily. Given current conditions (${context.weather?.temp || 28}°C, ${context.weather?.humidity || 81}% humidity), keep the canopy well-ventilated and ensure pruning tools are sterilized between plants.`;
  }
}
