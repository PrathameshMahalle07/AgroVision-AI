import { WeatherData, RiskLevel } from '../types';

export async function fetchWeatherData(lat: number, lon: number, locationName: string): Promise<WeatherData> {
  try {
    const res = await fetch(`/api/weather?lat=${lat}&lon=${lon}&name=${encodeURIComponent(locationName)}`);
    if (!res.ok) {
      throw new Error(`Weather request failed with status: ${res.status}`);
    }
    const data: WeatherData = await res.json();
    return data;
  } catch (err) {
    console.warn('Using client fallback weather data:', err);
    return {
      location: locationName || 'Salinas Valley, CA',
      coordinates: { lat, lon },
      current: {
        temp: 28,
        tempUnit: '°C',
        humidity: 81,
        windSpeed: 14,
        windUnit: 'km/h',
        rainProbability: 65,
        condition: 'Humid & Overcast',
        icon: 'cloud-rain',
        isRaining: false,
      },
      forecast: [
        { day: 'Today', condition: 'Humid & Showers', tempMax: 28, tempMin: 18, rainProb: 65, humidity: 81, icon: 'cloud-rain' },
        { day: 'Tomorrow', condition: 'Moderate Rain', tempMax: 26, tempMin: 17, rainProb: 80, humidity: 85, icon: 'cloud-rain-heavy' },
        { day: 'Wed', condition: 'Scattered Showers', tempMax: 25, tempMin: 16, rainProb: 55, humidity: 78, icon: 'cloud-drizzle' },
        { day: 'Thu', condition: 'Partly Cloudy', tempMax: 27, tempMin: 15, rainProb: 20, humidity: 62, icon: 'cloud-sun' },
        { day: 'Fri', condition: 'Sunny & Clear', tempMax: 29, tempMin: 16, rainProb: 10, humidity: 55, icon: 'sun' },
        { day: 'Sat', condition: 'Warm & Dry', tempMax: 30, tempMin: 17, rainProb: 5, humidity: 50, icon: 'sun' },
        { day: 'Sun', condition: 'Partly Cloudy', tempMax: 28, tempMin: 16, rainProb: 15, humidity: 58, icon: 'cloud-sun' },
      ],
    };
  }
}

/**
 * Calculates disease risk level based on humidity, temperature, and upcoming rain.
 */
export function calculateDiseaseRisk(weather: WeatherData): {
  level: RiskLevel;
  explanation: string;
  contributingWeatherPoints: string[];
} {
  const current = weather.current;
  const forecastRainMax = Math.max(...weather.forecast.slice(0, 3).map((f) => f.rainProb));

  let score = 0;
  const points: string[] = [];

  // Fungal pathogens thrive with relative humidity > 70%
  if (current.humidity >= 80) {
    score += 3;
    points.push(`High current relative humidity (${current.humidity}%) prolongs leaf wetness`);
  } else if (current.humidity >= 65) {
    score += 1;
    points.push(`Moderate humidity (${current.humidity}%) supports spore survival`);
  }

  // Temperature between 20°C and 30°C is the sweet spot for most foliar fungi
  if (current.temp >= 20 && current.temp <= 30) {
    score += 2;
    points.push(`Optimal temperature range (${current.temp}°C) accelerates fungal incubation`);
  }

  // Rainfall expectation creates water splash vectors and canopy moisture
  if (forecastRainMax >= 60 || current.isRaining) {
    score += 3;
    points.push(`Heavy rain probability in near forecast (${forecastRainMax}%) causes spore splash and leaf saturation`);
  } else if (forecastRainMax >= 35) {
    score += 1;
    points.push(`Scattered rain chances (${forecastRainMax}%) will introduce intermittent canopy moisture`);
  }

  if (score >= 6) {
    return {
      level: 'High',
      explanation: 'High humidity and upcoming rainfall create conditions highly favorable for fungal disease development.',
      contributingWeatherPoints: points,
    };
  }

  if (score >= 3) {
    return {
      level: 'Moderate',
      explanation: 'Moderate humidity and warm temperatures create potential conditions for disease spread if leaf surfaces stay wet.',
      contributingWeatherPoints: points,
    };
  }

  return {
    level: 'Low',
    explanation: 'Dry air and clear forecast present unfavorable conditions for most foliar pathogens.',
    contributingWeatherPoints: points.length ? points : ['Low ambient humidity and minimal precipitation expected'],
  };
}
