export interface LocationInfo {
  name: string;
  lat: number;
  lon: number;
  region: string;
  country: string;
  accuracyMeters?: number;
  isGps?: boolean;
}

export const POPULAR_AG_REGIONS: LocationInfo[] = [
  // Maharashtra Key Agricultural Basins
  { name: 'Nashik (Grapes & Onion Basin), Maharashtra', lat: 19.9975, lon: 73.7898, region: 'Maharashtra', country: 'India' },
  { name: 'Pune (Horticulture & Sugarcane Belt), Maharashtra', lat: 18.5204, lon: 73.8567, region: 'Maharashtra', country: 'India' },
  { name: 'Nagpur (Orange & Cotton Belt), Maharashtra', lat: 21.1458, lon: 79.0882, region: 'Maharashtra', country: 'India' },
  { name: 'Kolhapur (Sugarcane & Jaggery Belt), Maharashtra', lat: 16.705, lon: 74.2433, region: 'Maharashtra', country: 'India' },
  { name: 'Solapur (Pomegranate & Jowar Belt), Maharashtra', lat: 17.6599, lon: 75.9064, region: 'Maharashtra', country: 'India' },
  { name: 'Amravati (Vidarbha Cotton & Soybean), Maharashtra', lat: 20.932, lon: 77.7523, region: 'Maharashtra', country: 'India' },
  { name: 'Jalgaon (Banana Capital of India), Maharashtra', lat: 21.0077, lon: 75.5626, region: 'Maharashtra', country: 'India' },
  { name: 'Sangli (Turmeric & Raisin Belt), Maharashtra', lat: 16.8524, lon: 74.5815, region: 'Maharashtra', country: 'India' },
  { name: 'Ratnagiri (Konkan Alphonso Mango Belt), Maharashtra', lat: 16.9902, lon: 73.312, region: 'Maharashtra', country: 'India' },
  { name: 'Latur (Marathwada Soybean & Pulses), Maharashtra', lat: 18.4088, lon: 76.5604, region: 'Maharashtra', country: 'India' },
  { name: 'Ahmednagar (Dryland Millets & Dairy), Maharashtra', lat: 19.0948, lon: 74.748, region: 'Maharashtra', country: 'India' },
  // National Key Basins across India
  { name: 'Ludhiana, Punjab (Wheat & Rice Bowl)', lat: 30.901, lon: 75.8573, region: 'Punjab', country: 'India' },
  { name: 'Indore, Madhya Pradesh (Soybean & Wheat Plateau)', lat: 22.7196, lon: 75.8577, region: 'Madhya Pradesh', country: 'India' },
  { name: 'Rajkot, Gujarat (Groundnut & Cotton Belt)', lat: 22.3039, lon: 70.8022, region: 'Gujarat', country: 'India' },
  { name: 'Shimla, Himachal Pradesh (Apple Belt)', lat: 31.1048, lon: 77.1734, region: 'Himachal Pradesh', country: 'India' },
  { name: 'Guntur, Andhra Pradesh (Chilli & Tobacco Basin)', lat: 16.3067, lon: 80.4365, region: 'Andhra Pradesh', country: 'India' },
  { name: 'Mysuru, Karnataka (Silk, Ragi & Spices)', lat: 12.2958, lon: 76.6394, region: 'Karnataka', country: 'India' },
  { name: 'Varanasi, Uttar Pradesh (Indo-Gangetic Fertile Plains)', lat: 25.3176, lon: 82.9739, region: 'Uttar Pradesh', country: 'India' },
];

export async function getCurrentUserLocation(): Promise<LocationInfo> {
  return new Promise((resolve, reject) => {
    if (!navigator.geolocation) {
      reject(new Error('GPS Geolocation is not supported by your browser.'));
      return;
    }

    navigator.geolocation.getCurrentPosition(
      async (pos) => {
        const lat = Number(pos.coords.latitude.toFixed(4));
        const lon = Number(pos.coords.longitude.toFixed(4));
        const accuracy = Math.round(pos.coords.accuracy || 0);

        try {
          // 1. Try our backend proxy first to avoid client CORS or rate-limiting
          const backendRes = await fetch(`/api/reverse-geocode?lat=${lat}&lon=${lon}`);
          if (backendRes.ok) {
            const data = await backendRes.json();
            if (data.name) {
              resolve({
                name: data.name,
                lat,
                lon,
                region: data.region || 'Local Farm',
                country: data.country || 'India',
                accuracyMeters: accuracy,
                isGps: true,
              });
              return;
            }
          }
        } catch {
          // Fall through to client reverse geocoding
        }

        try {
          // Free reverse geocoding via OpenStreetMap Nominatim or BigDataCloud
          const res = await fetch(
            `https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lon}&format=json&addressdetails=1`,
            {
              headers: {
                'Accept-Language': 'en',
                'User-Agent': 'AgroVisionAI-CropIntelligence/1.0',
              },
            }
          );

          if (res.ok) {
            const data = await res.json();
            const addr = data.address || {};
            const locality =
              addr.village ||
              addr.town ||
              addr.suburb ||
              addr.city_district ||
              addr.city ||
              addr.county ||
              'Local Farm';
            const district = addr.state_district || addr.county || '';
            const state = addr.state || '';
            const country = addr.country || 'India';

            const parts = [locality, district, state].filter(Boolean);
            const formatted = parts.length > 0 ? parts.slice(0, 2).join(', ') : `${lat}, ${lon}`;

            resolve({
              name: formatted,
              lat,
              lon,
              region: state || district,
              country,
              accuracyMeters: accuracy,
              isGps: true,
            });
            return;
          }
        } catch {
          // Fallback to bigdatacloud if nominatim is slow
          try {
            const bdcRes = await fetch(
              `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${lat}&longitude=${lon}&localityLanguage=en`
            );
            if (bdcRes.ok) {
              const bdcData = await bdcRes.json();
              const city = bdcData.city || bdcData.locality || bdcData.principalSubdivision || 'Local Farm';
              const state = bdcData.principalSubdivision || '';
              const country = bdcData.countryName || 'India';
              const formatted = [city, state].filter(Boolean).join(', ');

              resolve({
                name: formatted || `${lat}, ${lon}`,
                lat,
                lon,
                region: state,
                country,
                accuracyMeters: accuracy,
                isGps: true,
              });
              return;
            }
          } catch {
            // Ignore
          }
        }

        resolve({
          name: `GPS Location (${lat.toFixed(3)}°, ${lon.toFixed(3)}°)`,
          lat,
          lon,
          region: 'Local Field Coordinates',
          country: 'India',
          accuracyMeters: accuracy,
          isGps: true,
        });
      },
      (err) => {
        let msg = 'Unable to acquire GPS coordinates.';
        switch (err.code) {
          case err.PERMISSION_DENIED:
            msg = 'GPS Location permission was denied in your browser settings. Please enable location permissions or choose a regional hub below.';
            break;
          case err.POSITION_UNAVAILABLE:
            msg = 'GPS position is currently unavailable from your device.';
            break;
          case err.TIMEOUT:
            msg = 'GPS location request timed out. Please try again.';
            break;
        }
        reject(new Error(msg));
      },
      {
        enableHighAccuracy: true,
        timeout: 15000,
        maximumAge: 0,
      }
    );
  });
}
