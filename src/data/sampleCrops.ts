import { DiagnosisResultData } from '../types';
export { CROPS_DATABASE, CROP_CATEGORIES, MAHARASHTRA_REGIONS } from './cropsDatabase';

// Curated realistic demo samples for instant scanner testing
export interface DemoScanSample {
  id: string;
  name: string;
  crop: string;
  condition: string;
  description: string;
  thumbnailUrl: string;
  mockDiagnosis: DiagnosisResultData;
}

export const DEMO_SCAN_SAMPLES: DemoScanSample[] = [
  {
    id: 'sample-tomato-early-blight',
    name: 'Tomato — Early Blight',
    crop: 'Tomato',
    condition: 'Early Blight',
    description: 'Classic concentric target rings with yellow chlorosis on lower foliage.',
    thumbnailUrl: '/tomato-plant-sample.jpg',
    mockDiagnosis: {
      isPlant: true,
      detectedSubject: 'Tomato Foliage',
      crop: 'Tomato',
      condition: 'Early Blight',
      isHealthy: false,
      confidence: 94,
      severity: 'Moderate',
      visualSymptoms: [
        'Concentric dark brown rings resembling target spots on lower foliage',
        'Yellow chlorotic halos surrounding lesions',
        'Partial defoliation on older branches',
        'Minor dark collar lesions near petiole junctions',
      ],
      diseaseExplanation:
        'Early Blight is a common fungal disease caused by Alternaria solani. It primarily attacks tomatoes and potatoes, starting on older, lower foliage and gradually progressing upward. While manageable if addressed promptly, severe cases can defoliate the plant and reduce fruit yield and quality.',
      contributingFactors: [
        'High relative humidity (> 80%)',
        'Prolonged leaf wetness from morning dew or overhead irrigation',
        'Warm ambient temperatures between 24°C and 30°C',
        'Dense plant canopy restricting airflow',
        'Infected crop residue from previous seasons',
      ],
      weatherImpactAnalysis:
        'Current elevated humidity (81%) and forecasted precipitation will create ideal conditions for fungal spore germination and secondary spread. Immediate canopy management is recommended before rains arrive.',
      diseaseRiskEstimate: 'High',
      recommendedActions: [
        'Prune and carefully destroy severely infected lower leaves (do not compost).',
        'Switch immediately from overhead sprinkling to drip or furrow irrigation to keep leaves dry.',
        'Improve inter-row air circulation by pruning suckers and staking plants upright.',
        'Sterilize pruning shears between cuts using a 70% isopropyl alcohol solution.',
        'Recheck neighbouring plants every 48 hours, especially after rain events.',
      ],
      preventionMeasures: [
        'Practice a minimum 3-year crop rotation avoiding other Solanaceous species.',
        'Apply organic mulch (straw or clean compost) at the plant base to prevent soil-splashing spores.',
        'Select certified disease-resistant or tolerant cultivars for upcoming plantings.',
        'Ensure adequate plant spacing (at least 60 cm between rows) for continuous airflow.',
        'Where preventive sprays are warranted, consult locally registered copper or bio-fungicide labels.',
      ],
      disclaimer:
        'AgroVision AI provides informational guidance based on computer vision patterns. It should not replace in-field agronomic advice or local university extension diagnostics.',
    },
  },
  {
    id: 'sample-corn-rust',
    name: 'Corn — Common Rust',
    crop: 'Corn',
    condition: 'Common Rust',
    description: 'Golden cinnamon-brown pustules erupted across mid-canopy leaves.',
    thumbnailUrl: 'https://images.unsplash.com/photo-1551754655-cd27e38d2076?auto=format&fit=crop&w=600&q=80',
    mockDiagnosis: {
      isPlant: true,
      detectedSubject: 'Maize Leaf',
      crop: 'Corn',
      condition: 'Common Rust',
      isHealthy: false,
      confidence: 91,
      severity: 'Moderate',
      visualSymptoms: [
        'Small, circular to elongate cinnamon-brown uredinial pustules',
        'Pustules ruptured epidermis on both upper and lower leaf surfaces',
        'Yellow chlorotic halos surrounding dense pustule clusters',
        'Lower and middle leaves showing early senescence',
      ],
      diseaseExplanation:
        'Common Rust is caused by the fungus Puccinia sorghi. Rust spores travel on air currents from southern latitudes. When dew or rainfall persists on leaves for over 6 hours at moderate temperatures, spores germinate and form powdery rust pustules.',
      contributingFactors: [
        'Moderate daytime temperatures (16°C - 25°C)',
        'Frequent morning dew persisting past mid-morning',
        'High planting density with restricted ventilation',
        'Susceptible hybrid genetics',
      ],
      weatherImpactAnalysis:
        'Moderate temperatures with cloudy, humid weather favor rapid spore cycling (7-14 day infection cycle). Dry, windy weather will carry spores to adjacent acreage.',
      diseaseRiskEstimate: 'Moderate',
      recommendedActions: [
        'Assess whether disease has reached upper ear leaf canopy before tassel/silking.',
        'Avoid overhead center-pivot irrigation during late afternoons or nights.',
        'Scout 20 plants across 5 representative field points to determine threshold.',
        'Consult regional extension IPM threshold tables before considering fungicide applications.',
      ],
      preventionMeasures: [
        'Select maize hybrids with proven single-gene (Rp) or general field rust resistance.',
        'Plant early in the spring window to avoid peak late-summer spore migrations.',
        'Maintain balanced soil potassium to bolster vascular stalk strength.',
        'Avoid high seeding rates that create enclosed humid micro-climates.',
      ],
      disclaimer:
        'AgroVision AI provides informational guidance and should not replace advice from qualified agricultural professionals or local agricultural authorities.',
    },
  },
  {
    id: 'sample-potato-late-blight',
    name: 'Potato — Late Blight',
    crop: 'Potato',
    condition: 'Late Blight',
    description: 'Dark water-soaked lesions with pale chlorotic border.',
    thumbnailUrl: 'https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&fit=crop&w=600&q=80',
    mockDiagnosis: {
      isPlant: true,
      detectedSubject: 'Potato Foliage',
      crop: 'Potato',
      condition: 'Late Blight',
      isHealthy: false,
      confidence: 96,
      severity: 'High',
      visualSymptoms: [
        'Irregular water-soaked dark brown-to-purplish lesions on leaflets',
        'Pale light-green halo surrounding expanding lesion edges',
        'Delicate white fungal-like sporulation visible on underside of damp leaves',
        'Rapid tissue necrosis with petiole collapse',
      ],
      diseaseExplanation:
        'Late Blight, caused by the oomycete pathogen Phytophthora infestans, is one of the most destructive agricultural plant diseases in human history. Under cool and wet conditions, it can destroy an entire field within 7 to 10 days if left unaddressed.',
      contributingFactors: [
        'Cool temperatures between 15°C and 20°C',
        'Relative humidity consistently exceeding 90%',
        'Fog, prolonged rain, or persistent heavy dew',
        'Presence of infected cull piles or volunteer potatoes nearby',
      ],
      weatherImpactAnalysis:
        'Upcoming rain and cool night temperatures present an urgent high-risk situation. Late blight pathogen can double in volume every 48 hours in saturated air.',
      diseaseRiskEstimate: 'High',
      recommendedActions: [
        'Flag and isolate infected field perimeter immediately.',
        'Destroy severely infected hot spots by flailing or bagging to prevent airborne spore plumes.',
        'Notify neighboring potato and tomato growers so they can inspect their borders.',
        'Ensure rows are well-hilled with loose soil to prevent zoospore washdown into developing tubers.',
        'Consult extension emergency blight alert system for approved regional treatment options.',
      ],
      preventionMeasures: [
        'Plant exclusively certified disease-tested seed potatoes.',
        'Eliminate all cull piles, volunteer potatoes, and nightshade weeds before the season.',
        'Utilize decision support tools (such as BlightCast) to track cumulative risk hours.',
        'Allow vine-kill desiccation 2 to 3 weeks prior to tuber digging to toughen tuber skins.',
      ],
      disclaimer:
        'AgroVision AI provides informational guidance and should not replace advice from qualified agricultural professionals or local agricultural authorities.',
    },
  },
  {
    id: 'sample-healthy-pepper',
    name: 'Bell Pepper — Healthy Foliage',
    crop: 'Bell Pepper',
    condition: 'Healthy',
    description: 'Vibrant green, uniform leaf coloration with zero necrotic lesions.',
    thumbnailUrl: 'https://images.unsplash.com/photo-1563565375-f3fdfdbefa83?auto=format&fit=crop&w=600&q=80',
    mockDiagnosis: {
      isPlant: true,
      detectedSubject: 'Bell Pepper Foliage',
      crop: 'Bell Pepper',
      condition: 'Healthy',
      isHealthy: true,
      confidence: 97,
      severity: 'None',
      visualSymptoms: [
        'Uniform emerald green pigmentation across all leaf blades',
        'Turgid, uncurled foliage with intact leaf margins',
        'Absence of fungal pustules, bacterial specks, or viral mosaic patterns',
        'Healthy apical bud growth with active branching',
      ],
      diseaseExplanation:
        'No symptoms of pathology or active pest distress were detected. The plant exhibits optimal chlorophyll retention, sound cellular turgor, and healthy vegetative architecture.',
      contributingFactors: [
        'Balanced soil moisture and effective drainage',
        'Adequate sunlight and moderate temperature conditions',
        'Sound cultural sanitation practices in the plot',
      ],
      weatherImpactAnalysis:
        'Current weather is favorable for continued healthy growth. Continue monitoring during any incoming precipitation periods.',
      diseaseRiskEstimate: 'Low',
      recommendedActions: [
        'Maintain consistent base watering without wetting leaves.',
        'Continue regular weekly scouting to catch any early symptoms early.',
        'Inspect leaf undersides periodically for early aphid or whitefly colonies.',
        'Maintain light mulch layer to retain soil moisture stability.',
      ],
      preventionMeasures: [
        'Adhere to scheduled balanced fertilization avoiding excess nitrogen.',
        'Sterilize pruning shears between garden maintenance tasks.',
        'Ensure companion plantings encourage beneficial predatory insects.',
      ],
      disclaimer:
        'AgroVision AI provides informational guidance and should not replace advice from qualified agricultural professionals or local agricultural authorities.',
    },
  },
];
