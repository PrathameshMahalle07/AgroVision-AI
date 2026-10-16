import { DiagnosisResultData } from '../types';

export interface DiagnosisRequest {
  imageBase64: string;
  mimeType?: string;
  cropHint?: string;
  location?: string;
  weather?: {
    temp?: number;
    humidity?: number;
    condition?: string;
  };
}

export async function analyzeCropImage(req: DiagnosisRequest): Promise<DiagnosisResultData> {
  const res = await fetch('/api/diagnose-crop', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(req),
  });

  if (!res.ok) {
    const errorJson = await res.json().catch(() => ({}));
    throw new Error(
      errorJson.error || errorJson.details || `Diagnosis failed (Server status ${res.status}). Please try again with a clear plant photo.`
    );
  }

  const data: DiagnosisResultData = await res.json();
  return data;
}
