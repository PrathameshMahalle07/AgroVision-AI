#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Appends 56 Fruit & Horticultural crops across Maharashtra and India.
"""

import json

with open('scripts/crops_stage3.json', 'r', encoding='utf-8') as f:
    crops = json.load(f)

def c(cid, name, local, sci, cat, emoji, season, region, desc, temp, water, soil, stages, diseases, pests, prev):
    crops.append({
        "id": cid,
        "name": name,
        "localName": local,
        "scientificName": sci,
        "category": cat,
        "avatarEmoji": emoji,
        "season": season,
        "maharashtraRegion": region,
        "description": desc,
        "optimalTemp": temp,
        "waterRequirement": water,
        "soilPreference": soil,
        "growthStages": stages,
        "commonDiseases": diseases,
        "commonPests": pests,
        "generalPrevention": prev
    })

# ==========================================
# 5. FRUITS & HORTICULTURE (56 crops)
# ==========================================
c("alphonso-mango", "Alphonso Mango (Hapus)", "हापूस आंबा (Ratnagiri Alphonso)", "Mangifera indica", "Fruits & Horticulture", "🥭",
  "Summer (March to June)", "Konkan Coast (Ratnagiri, Sindhudurg, Devgad, Raigad)",
  "The undisputed King of Mangoes holding Geographical Indication (GI). World-renowned for heavenly saffron aroma, fiberless saffron pulp, and exquisite sweetness shaped by coastal sea breezes and lateritic soils.",
  "24°C - 32°C (warm tropical coastal climate with bright sunshine during flowering and fruit development)",
  "900 - 1,200 mm; zero irrigation during winter floral rest period; light protective irrigations during marble-to-egg fruit sizing.",
  "Deep, well-drained red lateritic rocky soils (Jambha) rich in iron and aluminium, pH 5.5 - 7.0.",
  [{"stage": "Vegetative Flush & Floral Rest", "days": "Oct - Nov", "description": "Shoot vegetative flushing ceases; water stress induces floral bud differentiation."},
   {"stage": "Blossoming & Anthesis (Mohor)", "days": "Dec - Feb", "description": "Fragrant pyramidal panicles bloom with thousands of male and hermaphrodite flowers; pollinated by flies and bees."},
   {"stage": "Fruit Set & Pea / Marble Stage", "days": "Feb - March", "description": "Ovaries swell into pea and marble sizes; high physiological fruit drop if weather fluctuates."},
   {"stage": "Maturity & Harvest (Ghada)", "days": "April - June", "description": "Shoulders raise, tapka stage (first fruit drop on tree) indicates full maturity; handpicked with net dapoli harvesters."}],
  [{"name": "Anthracnose (Colletotrichum gloeosporioides)", "symptoms": "Black tear-stain streaks on blossom panicles and dark sunken spots with pink spore masses on ripening fruit.", "riskPeriod": "Unseasonal winter showers or heavy morning coastal fog during flowering."},
   {"name": "Powdery Mildew (Oidium mangiferae)", "symptoms": "White talcum-like coating covering flower panicles causing blossom drop and complete fruit set failure.", "riskPeriod": "Cool cloudy nights with morning dew (10-15°C)."},
   {"name": "Spongy Tissue (Physiological Disorder)", "symptoms": "Internal yellowish-white spongy, sour patch inside ripe pulp with no external blemish.", "riskPeriod": "Convective ground heat radiation during scorching May sunshine."}],
  ["Mango Hopper (Amritodus atkinsoni)", "Fruit Fly (Bactrocera dorsalis)", "Stem Borer (Batocera rufomaculata)", "Thrips", "Gall Midge"],
  ["Spray Imidacloprid 17.8 SL @ 3ml/10L at bud burst to eradicate devastating mango hoppers from inflorescences.",
   "Install Methyl Eugenol pheromone traps @ 10/ha to trap male fruit flies before harvest.",
   "Harvest fruit with 1-2 cm pedicel attached to prevent latex burn (choy) on fruit skin.",
   "Dip harvested mangoes in warm water (52°C for 5 minutes) to eradicate latent anthracnose spores."])

c("kesar-mango", "Kesar Mango", "केसर आंबा (Marathwada / Gir Kesar)", "Mangifera indica", "Fruits & Horticulture", "🥭",
  "Summer (May to July)", "Marathwada (Chhatrapati Sambhajinagar, Jalna, Beed, Latur), Khandesh, Gujarat",
  "The Queen of Mangoes holding GI status. Renowned for intense saffron-orange pulp, high sugar content, rich pulp recovery, and excellent transport shelf life.",
  "25°C - 35°C", "700 - 900 mm; well-scheduled drip irrigation.", "Medium to deep black cotton soils with good drainage.",
  [{"stage": "Flushing & Dormancy", "days": "Nov - Dec", "description": "Canopy resting period."},
   {"stage": "Flowering", "days": "Jan - Feb", "description": "Heavy panicle blossom."},
   {"stage": "Fruit Development", "days": "March - April", "description": "Fruit sizing and pulp sweetening."},
   {"stage": "Harvest", "days": "May - June", "description": "Pick at 80% maturity when fruit shoulders round."}],
  [{"name": "Powdery Mildew", "symptoms": "White powdery panicle coating.", "riskPeriod": "Cloudy winter mornings."},
   {"name": "Bacterial Canker", "symptoms": "Star-shaped cracks on fruit with black bacterial ooze.", "riskPeriod": "Hailstorms and windy summer rains."}],
  ["Mango Hopper", "Fruit Fly", "Thrips"],
  ["Spray Wettable Sulfur @ 2g/L or Hexaconazole @ 1ml/L at 50% bloom.", "Use foam net sleeves to protect fruits."])

c("dasheri-mango", "Dasheri Mango", "दशेरी आंबा (Dasheri)", "Mangifera indica", "Fruits & Horticulture", "🥭",
  "Mid-Season (June)", "North India (Malihabad, UP), Vidarbha, MP",
  "Famous heritage North Indian mango renowned for elongated shape, greenish-yellow skin, fiberless melting sweet pulp, and pleasant aroma.",
  "24°C - 35°C", "800 - 1,000 mm.", "Deep fertile alluvial or medium loam.",
  [{"stage": "Flowering", "days": "Feb - March", "description": "Profuse blooms."},
   {"stage": "Fruit Set", "days": "April - May", "description": "Elongated fruit growth."},
   {"stage": "Harvest", "days": "June", "description": "Handpicked mature fruits."}],
  [{"name": "Malformation", "symptoms": "Compact bunchy floral panicles.", "riskPeriod": "Low winter temperatures."}],
  ["Hopper", "Mealybug"], ["Prune malformed panicles and spray NAA @ 200 ppm in October."])

c("langra-mango", "Langra Mango", "लंगडा आंबा (Langra)", "Mangifera indica", "Fruits & Horticulture", "🥭",
  "Mid-Season (July)", "Varanasi (UP), Bihar, Central India",
  "Celebrated for its distinct bright lime-green skin that stays green even when fully ripe, delivering an unmatched sweet-acid balance.",
  "24°C - 35°C", "900 - 1,100 mm.", "Alluvial clay loam.",
  [{"stage": "Bloom", "days": "March", "description": "Vigorous blossoming."},
   {"stage": "Fruiting", "days": "May - June", "description": "Oval green fruit sizing."},
   {"stage": "Harvest", "days": "July", "description": "Harvested when pulp softens slightly."}],
  [{"name": "Anthracnose", "symptoms": "Dark leaf spots.", "riskPeriod": "Rains."}],
  ["Fruit Fly", "Shoot Borer"], ["Install fruit fly traps and spray copper oxychloride."])

c("totapuri-mango", "Totapuri Mango", "तोतापुरी आंबा (Totapuri)", "Mangifera indica", "Fruits & Horticulture", "🥭",
  "Early Summer", "South India, Maharashtra, Karnataka border",
  "Distinct parrot-beak shaped fruit; the primary mango variety used in India's pulp, juice, and fruit beverage processing industries.",
  "24°C - 35°C", "700 - 1,000 mm.", "Red sandy loam and loams.",
  [{"stage": "Flowering", "days": "Jan - Feb", "description": "Regular annual bearer."},
   {"stage": "Fruit Growth", "days": "March - April", "description": "Curved beak fruit develops."},
   {"stage": "Harvest", "days": "May", "description": "High yield harvested for pulp processing factories."}],
  [{"name": "Sooty Mold", "symptoms": "Black velvety leaf coating following honeydew excretion.", "riskPeriod": "Hopper attack."}],
  ["Mango Hopper"], ["Spray starch solution @ 2% to peel off dry sooty mold."])

c("chausa-mango", "Chausa Mango", "चौसा आंबा (Chausa)", "Mangifera indica", "Fruits & Horticulture", "🥭",
  "Late Summer (July - August)", "North India, Punjab, UP, MP",
  "Extremely sweet late-season table mango with golden yellow skin, juicy aromatic pulp, and zero fiber.",
  "25°C - 36°C", "800 - 1,000 mm.", "Deep fertile loam.",
  [{"stage": "Flowering", "days": "March", "description": "Late blossoming."},
   {"stage": "Fruit Fill", "days": "May - June", "description": "Golden juice accumulates."},
   {"stage": "Harvest", "days": "July - August", "description": "Late season premium market picking."}],
  [{"name": "Fruit Rot", "symptoms": "Decay near stem end.", "riskPeriod": "Monsoon rains."}],
  ["Fruit Fly"], ["Bag fruits on tree using brown paper bags 30 days prior to harvest."])

c("thompson-grapes", "Thompson Seedless Grapes", "थॉम्पसन सीडलेस द्राक्षे (Nashik Grapes)", "Vitis vinifera", "Fruits & Horticulture", "🍇",
  "Late Winter to Summer (Jan to April)", "Nashik (Grape Capital of India), Pune, Solapur, Sangli (Tasgaon)",
  "The crown jewel of Indian viticulture holding GI status for Nashik Valley Wine and Table Grapes. Crisp, amber-green seedless berries prized across Europe and Gulf export markets.",
  "15°C - 32°C (dry sunny climate during berry development and ripening; zero rain during harvest)",
  "500 - 700 mm via micro-drip fertigation; strict water deficit prior to harvest to concentrate sugars.",
  "Well-drained medium black cotton soil, sandy loam, or weathered basaltic red soil, pH 6.5 - 7.8.",
  [{"stage": "Foundation Pruning (Kharif Pruning)", "days": "April - May", "description": "Canes pruned to 1-2 buds to develop fruitful vegetative canes for next winter season."},
   {"stage": "Forward / Fruit Pruning", "days": "Sept - Oct", "description": "Canes pruned to fruitful bud levels (5-8 buds); hydrogen cyanamide applied to break bud dormancy."},
   {"stage": "Inflorescence & Berry Set", "days": "Nov - Dec", "description": "Flower clusters bloom; GA3 (gibberellic acid) dips applied for cluster elongation and berry thinning."},
   {"stage": "Berry Sizing, Veraison & Harvest", "days": "Jan - April", "description": "Berries soften and turn translucent amber; brix reaches 18-20°; handpicked into foam export punnets."}],
  [{"name": "Downy Mildew (Plasmopara viticola)", "symptoms": "Yellowish translucent oil-spots on upper leaf surface with dense white cottony fungal down on undersides.", "riskPeriod": "Continuous monsoon rains or unseasonal winter showers accompanied by leaf wetness >6 hours."},
   {"name": "Powdery Mildew (Uncinula necator)", "symptoms": "Ash-grey powdery coating on berries and leaves; causes berries to crack open exposing seeds.", "riskPeriod": "Warm dry days and cool humid nights (20-25°C)."},
   {"name": "Anthracnose / Bird's Eye Spot (Elsinoe ampelina)", "symptoms": "Sunken circular dark spots with pale grey center and dark purple border on young shoots and berries.", "riskPeriod": "Hot humid rainy periods after April pruning."}],
  ["Thrips (Scirtothrips dorsalis)", "Flea Beetle (Scelodonta strigicollis)", "Mealybug (Maconellicoccus hirsutus)", "Mites"],
  ["Release predator ladybird beetles (Cryptolaemus montrouzieri) @ 1,500/ha to keep mealybugs under biological control.",
   "Apply prophylactic spray of Potassium phosphonate @ 2g/L or Bordeaux mixture 1% prior to cloudy wet spells.",
   "Maintain open canopy architecture on Y-trellis or Bower system to maximize sunlight and air circulation.",
   "Follow strict National Research Centre for Grapes (NRCG) export residue monitoring limits."])

c("sharad-seedless-grapes", "Sharad Seedless Grapes", "शरद सीडलेस काळी द्राक्षे (Sharad Seedless)", "Vitis vinifera", "Fruits & Horticulture", "🍇",
  "Winter to Spring", "Nashik, Sangli, Solapur, Pune",
  "Crisp, elongated black-purple seedless table grapes with sweet juicy pulp and tender edible skin. Excellent domestic and export market value.",
  "16°C - 32°C", "500 - 650 mm.", "Well-drained loam or gravelly black soil.",
  [{"stage": "Pruning", "days": "Oct", "description": "Forward pruning for fruit buds."},
   {"stage": "Berry Set & GA3", "days": "Nov - Dec", "description": "Cluster thinning and sizing."},
   {"stage": "Veraison (Color Change)", "days": "Jan", "description": "Berries transition from green to deep blue-black."},
   {"stage": "Harvest", "days": "Feb - March", "description": "Harvested when brix exceeds 18°."}],
  [{"name": "Downy Mildew", "symptoms": "Oil spots.", "riskPeriod": "Humid spells."},
   {"name": "Berry Cracking", "symptoms": "Skin splitting.", "riskPeriod": "Unseasonal rain during veraison."}],
  ["Thrips", "Mealybug"], ["Apply paper bunch covers to protect black color against bleaching."])

c("tas-a-ganesh-grapes", "Tas-A-Ganesh Grapes", "तास-ए-गणेश द्राक्षे (Tas-A-Ganesh)", "Vitis vinifera", "Fruits & Horticulture", "🍇",
  "Late Winter", "Sangli (Tasgaon), Solapur, Nashik",
  "Superior mutant of Thompson Seedless selected by visionary viticulturist V.P. Patil in Tasgaon. Golden elongated berries with sweet muscat flavor.",
  "15°C - 32°C", "500 - 650 mm.", "Medium black clay to loam.",
  [{"stage": "Vegetative", "days": "May - Sept", "description": "Canopy development."},
   {"stage": "Bloom & Set", "days": "Nov - Dec", "description": "Berry sizing."},
   {"stage": "Harvest", "days": "Feb - April", "description": "Golden translucent berries picked."}],
  [{"name": "Powdery Mildew", "symptoms": "Ashy coating.", "riskPeriod": "Dry cool spells."}],
  ["Flea Beetle"], ["Spray Sulfur 80 WDG @ 2g/L."])

c("flame-seedless-grapes", "Flame Seedless Grapes", "फ्लेम सीडलेस द्राक्षे (Flame Seedless)", "Vitis vinifera", "Fruits & Horticulture", "🍇",
  "Early Season (Jan - Feb)", "Nashik, Sangli, Western Maharashtra",
  "Round, crunchy, bright ruby-red seedless grape with firm texture and refreshing sweet-tart flavor.",
  "16°C - 32°C", "500 - 600 mm.", "Well-drained loams.",
  [{"stage": "Early Veraison", "days": "Dec - Jan", "description": "Vibrant red color accumulation."},
   {"stage": "Harvest", "days": "Jan - Feb", "description": "Early harvest captures high market rates."}],
  [{"name": "Anthracnose", "symptoms": "Bird's eye lesions.", "riskPeriod": "Rain."}],
  ["Thrips"], ["Use ethrel spray at veraison for uniform crimson coloration."])

c("sonaka-grapes", "Sonaka Grapes", "सोनाका लांबट द्राक्षे (Sonaka Grapes)", "Vitis vinifera", "Fruits & Horticulture", "🍇",
  "Feb - April", "Solapur, Sangli, Nashik",
  "Extra-long cylindrical ladyfinger-type seedless green grape mutation bred in Maharashtra, highly prized for dessert elegance and raisin quality.",
  "16°C - 34°C", "500 - 650 mm.", "Black cotton soil with drip.",
  [{"stage": "Berry Elongation", "days": "Dec - Jan", "description": "Berries stretch up to 28-32 mm with GA3."},
   {"stage": "Maturity", "days": "Feb - March", "description": "Pearly green-gold harvest."}],
  [{"name": "Downy Mildew", "symptoms": "Foliar oil spots.", "riskPeriod": "Dewy mornings."}],
  ["Mites"], ["Careful GA3 dipping timing to prevent bunch compactness."])

c("bhagwa-pomegranate", "Bhagwa Pomegranate (Anar)", "भगवा डाळिंब (Solapur Bhagwa)", "Punica granatum", "Fruits & Horticulture", "🍎",
  "Hasth / Mrig / Ambe Bahar (Year-round based on bahar)", "Solapur (Pomegranate Capital of India), Sangli, Nashik, Ahmednagar, Pune",
  "The ruby red marvel of Maharashtra drylands holding GI status. Saffron-red smooth rind, dark crimson juicy arils with soft seeds, high antioxidant content, and unmatched export demand.",
  "25°C - 35°C (arid dry climate with hot days and cool nights during fruit development)",
  "600 - 800 mm through drip irrigation; strict water withholding to induce leaf shedding and synchronous flowering.",
  "Light loamy to medium deep black soil with excellent internal drainage, pH 6.5 - 8.0.",
  [{"stage": "Water Stress & Defoliation (Bahar Induction)", "days": "Day 1-45", "description": "Irrigation stopped for 30-45 days to induce complete leaf fall and rest."},
   {"stage": "First Watering & Flowering", "days": "Day 46-75", "description": "Pruning, heavy watering and bio-fertilizer induce brilliant scarlet vase-shaped flowers."},
   {"stage": "Fruit Set & Aril Development", "days": "Days 76-135", "description": "Round leathery fruits expand; drip fertigation supplies potassium for aril coloration."},
   {"stage": "Coloration & Maturity", "days": "Days 136-180", "description": "Rind turns glossy saffron-red (Bhagwa); metallic sound upon tapping signals harvest maturity."}],
  [{"name": "Bacterial Blight / Telya Disease (Xanthomonas axonopodis pv. punicae)", "symptoms": "Oily black water-soaked spots on leaves and triangular black cracks with gummy exudate on fruits.", "riskPeriod": "Warm cloudy weather (25-35°C) with intermittent rain and high humidity (>70%)."},
   {"name": "Anthracnose / Fruit Spot (Colletotrichum gloeosporioides)", "symptoms": "Circular black spots with yellow margins on fruit rind.", "riskPeriod": "Monsoon showers during Ambe or Mrig bahar."},
   {"name": "Wilt Complex (Ceratocystis fimbriata & Nematodes)", "symptoms": "Sudden yellowing and complete drying of one branch or whole tree; purple-grey wood discoloration.", "riskPeriod": "Continuous wet soil and root nematode injury."}],
  ["Pomegranate Butterfly / Fruit Borer (Virachola isocrates)", "Thrips", "Mealybug", "Stem Borer"],
  ["Bag developing fruits at lemon size with parchment paper bags to completely prevent fruit borer damage.",
   "Spray Copper oxychloride @ 2.5g/L + Streptocycline @ 0.5g/L immediately upon noticing early oily Telya spots.",
   "Drench root zone with Propiconazole @ 2ml/L + Paecilomyces lilacinus to combat Ceratocystis wilt.",
   "Strictly disinfect secateurs with sodium hypochlorite between tree prunings to prevent pathogen spread."])

c("ganesh-pomegranate", "Ganesh Pomegranate", "गणेश डाळिंब (Ganesh Anar)", "Punica granatum", "Fruits & Horticulture", "🍎",
  "Bahar system", "Pune, Ahmednagar, Solapur",
  "Pioneering soft-seeded pomegranate bred by Dr. G.S. Cheema at MPKV. Pinkish-yellow rind with exceptionally sweet pink arils.",
  "22°C - 34°C", "600 - 750 mm.", "Well-drained loams.",
  [{"stage": "Bahar Treatment", "days": "1-30 days", "description": "Stress induced."},
   {"stage": "Flowering", "days": "Days 31-60", "description": "Scarlet bloom."},
   {"stage": "Harvest", "days": "Days 140-160", "description": "Sweet pink arils."}],
  [{"name": "Telya Blight", "symptoms": "Oily spots.", "riskPeriod": "Monsoon."}],
  ["Fruit Borer"], ["Prune infected twigs and burn immediately."])

c("arakta-pomegranate", "Arakta Pomegranate", "आरक्ता डाळिंब (Arakta Anar)", "Punica granatum", "Fruits & Horticulture", "🍎",
  "Bahar system", "Solapur, Marathwada, Western Maharashtra",
  "High-yielding dark red aril variety bred for high juice recovery and attractive table presence.",
  "24°C - 35°C", "600 - 750 mm.", "Medium black soils.",
  [{"stage": "Fruit Development", "days": "Days 60-120", "description": "Ruby aril pigment accumulation."},
   {"stage": "Harvest", "days": "Days 150-170", "description": "Deep red fruits harvested."}],
  [{"name": "Fruit Spot", "symptoms": "Brown specks.", "riskPeriod": "Rain."}],
  ["Thrips"], ["Spray spinosad for thrips control at fruit set."])

c("jalgaon-banana", "Grand Naine Banana (Jalgaon Banana)", "ग्रँड नैन केळी (Jalgaon Banana)", "Musa acuminata", "Fruits & Horticulture", "🍌",
  "Year-round (11-12 months crop cycle)", "Khandesh (Jalgaon is Banana Capital of India), Dhule, Nanded, Kolhapur",
  "The golden fruit of Khandesh holding GI status. High-yielding Cavendish clone produced via tissue culture, yielding massive 25-35 kg bunches with uniform, sweet, export-grade bananas.",
  "25°C - 35°C (high humidity, protected from desiccating hot winds and frost)",
  "1,800 - 2,200 mm; high water feeder requiring drip irrigation every alternate day.",
  "Deep, fertile, well-aerated black clay loam or alluvial silt soil rich in organic matter and potash, pH 6.5 - 7.5.",
  [{"stage": "Planting & Vegetative Growth", "days": "Months 1-5", "description": "Tissue-cultured plantlets establish; pseudo-stem thickens and produces 30-35 massive leaves."},
   {"stage": "Shooting & Bunch Emergence", "days": "Months 7-8", "description": "True stem pushes through pseudostem; terminal inflorescence (kelphul) bends downward exposing hands."},
   {"stage": "Finger Development & De-budding", "days": "Months 8-10", "description": "Fingers curve upward; terminal male bud removed; bunch covered with blue perforated polyethylene sleeve."},
   {"stage": "Bunch Maturation & Harvest", "days": "Months 11-12", "description": "Angles on fingers round off; harvested at 80% maturity for export or local ripening."}],
  [{"name": "Sigatoka Leaf Spot (Mycosphaerella musicola)", "symptoms": "Spindle-shaped chlorotic streaks turning dark brown with grey center, causing massive premature leaf drying.", "riskPeriod": "Warm humid monsoon weather with heavy morning dew (25-30°C)."},
   {"name": "Panama Wilt (Fusarium oxysporum f. sp. cubense)", "symptoms": "Lower leaves turn bright yellow, buckle at petiole base and hang down skirt-like; vascular browning.", "riskPeriod": "Infected suckers and poorly drained acidic soils."},
   {"name": "Banana Bunchy Top Virus (BBTV)", "symptoms": "Leaves become narrow, short, upright and clustered at top like a rosette with dark green dot-dash streaks on veins; aphid vector.", "riskPeriod": "Warm dry spells with high aphid populations."}],
  ["Banana Pseudostem Borer (Odoiporus longicollis)", "Rhizome Weevil", "Banana Aphid (Pentalonia nigronervosa)", "Nematodes"],
  ["Plant exclusively virus-tested certified tissue-cultured Grand Naine plantlets.",
   "Inject pseudostem with Dichlorvos or insert carbofuran granules if pseudostem borer holes appear.",
   "Cover bunches with 6% blue polyethylene sleeves to prevent sunburn, insect scratches, and boost bunch weight by 15%.",
   "Provide bamboo or poly-rope propping support to prevent lodging of heavy bunches during summer storms."])

c("basrai-banana", "Basrai Banana (Dwarf Cavendish)", "बसराई केळी (Basrai Keli)", "Musa acuminata", "Fruits & Horticulture", "🍌",
  "12 months", "Khandesh, Konkan, Western Maharashtra",
  "Traditional dwarf Cavendish banana with wind-resilient short pseudostem and large cylindrical sweet bunches.",
  "24°C - 34°C", "1,800 - 2,000 mm.", "Clay loam to black soil.",
  [{"stage": "Vegetative", "days": "Months 1-6", "description": "Sturdy windproof dwarf trunk."},
   {"stage": "Shooting", "days": "Month 8", "description": "Bunch emergence."},
   {"stage": "Harvest", "days": "Month 11-12", "description": "Large curved sweet fingers."}],
  [{"name": "Sigatoka Leaf Spot", "symptoms": "Cigar burns on leaves.", "riskPeriod": "Humid monsoon."}],
  ["Banana Weevil"], ["Spray propiconazole @ 1ml/L + mineral oil for Sigatoka."])

c("red-banana", "Red Banana (Lal Keli)", "लाल केळी / तांबडी केळी (Red Banana)", "Musa acuminata 'Red Dacca'", "Fruits & Horticulture", "🍌",
  "14-16 months", "Konkan (Vasai, Palghar, Sindhudurg), Tamil Nadu, Kerala",
  "Exotic thick reddish-purple peel banana with creamy pink aromatic pulp, high beta-carotene and vitamin C.",
  "24°C - 32°C", "1,800 - 2,200 mm.", "Coastal fertile loam.",
  [{"stage": "Growth", "days": "Months 1-8", "description": "Tall robust reddish pseudostem."},
   {"stage": "Shooting", "days": "Month 10-12", "description": "Massive purplish inflorescence."},
   {"stage": "Harvest", "days": "Month 14-16", "description": "Plump brick-red bananas mature."}],
  [{"name": "Panama Wilt", "symptoms": "Yellowing leaves.", "riskPeriod": "Wet soils."}],
  ["Aphids"], ["Requires organic manure and long crop cycle."])

c("nagpur-orange", "Nagpur Mandarin Orange (Santra)", "नागपूर संत्रे (Nagpur Santra)", "Citrus reticulata", "Fruits & Horticulture", "🍊",
  "Ambe Bahar (Oct-Jan) / Mrig Bahar (Feb-April)", "Vidarbha (Nagpur is Orange City of India, Amravati, Wardha), Khandesh",
  "The crown of Vidarbha holding GI status. Renowned for easy-peeling loose rind, exquisite sweet-tangy juice, and aromatic zest celebrated nationwide.",
  "22°C - 35°C (sub-tropical dry winter with hot summer; requires cool nights for deep orange peel color)",
  "900 - 1,100 mm; canal and drip irrigation; winter or summer water stress needed to trigger bloom.",
  "Deep, well-aerated light to medium black cotton soil, free from hard subsoil murrum and salinity, pH 6.5 - 7.8.",
  [{"stage": "Stress Period (Bahar Treatment)", "days": "Month 1-1.5", "description": "Water withheld for 30-40 days to induce dormancy and leaf yellowing."},
   {"stage": "Bloom & Anthesis", "days": "Month 2", "description": "First irrigation and fertilizer induce profuse white fragrant blossoms."},
   {"stage": "Fruit Development & Sizing", "days": "Months 3-7", "description": "Green globose hesperidium fruits size; drip delivers potassium and micronutrients."},
   {"stage": "Color Break & Harvest", "days": "Months 8-9", "description": "Rind transitions from green to deep radiant orange as night temperatures fall; hand harvested with clippers."}],
  [{"name": "Citrus Gummosis / Foot Rot (Phytophthora nicotianae)", "symptoms": "Bark cracks on trunk near soil line with profuse golden-brown gum exudation; foliage turns yellow and dies.", "riskPeriod": "Heavy rains and water stagnation around trunk base."},
   {"name": "Citrus Greening / Huanglongbing (Candidatus Liberibacter)", "symptoms": "Mottled yellow asymmetrical leaf chlorosis, vein corking, lopsided bitter fruits with aborted seeds; psyllid vector.", "riskPeriod": "Spring flush with high citrus psylla populations."},
   {"name": "Citrus Canker (Xanthomonas axonopodis pv. citri)", "symptoms": "Raised corky brown crater-like lesions surrounded by yellow chlorotic halo on leaves, twigs, and fruit.", "riskPeriod": "Wind-driven monsoon showers."}],
  ["Citrus Psylla (Diaphorina citri)", "Citrus Leaf Miner (Phyllocnistis citrella)", "Citrus Blackfly", "Fruit Sucking Moth (Eudocima materna)"],
  ["Bud onto Phytophthora-tolerant rootstocks like Rangpur Lime (Citrus limonia).",
   "Paint trunk with Bordeaux paste (1:1:10) up to 2 feet above soil surface twice a year (before and after monsoon).",
   "Control citrus psylla vector using Thiamethoxam 25 WG @ 3g/10L at feather-flush stage.",
   "Install light traps and bait traps (jaggery + malathion) at dusk to destroy destructive nocturnal fruit-sucking moths."])

c("mosambi-sweet-lime", "Mosambi (Sweet Lime)", "मोसंबी (Marathwada Mosambi)", "Citrus sinensis", "Fruits & Horticulture", "🍋",
  "Ambe & Mrig Bahar", "Marathwada (Jalna is Mosambi Capital, Chhatrapati Sambhajinagar, Parbhani), Ahmednagar",
  "The refreshing sweet citrus pride of Marathwada holding GI status. Mild, low-acid, incredibly refreshing thirst-quenching juice.",
  "22°C - 35°C", "800 - 1,000 mm.", "Medium black fertile soils with good drainage.",
  [{"stage": "Bahar Stress", "days": "Dec or May", "description": "Water stress."},
   {"stage": "Flowering", "days": "Jan or June", "description": "Fragrant blossom."},
   {"stage": "Fruit Sizing", "days": "Months 4-7", "description": "Smooth green rind develops."},
   {"stage": "Harvest", "days": "Months 8-9", "description": "Pale yellow skin with sweet juicy vesicles."}],
  [{"name": "Gummosis", "symptoms": "Gum oozing from bark.", "riskPeriod": "Monsoon water stagnation."},
   {"name": "Canker", "symptoms": "Corky spots.", "riskPeriod": "Hail / storms."}],
  ["Citrus Psylla", "Leaf Miner", "Mites"],
  ["Drench root zone with Metalaxyl-Mancozeb @ 2.5g/L for gummosis control.",
   "Spray Streptocycline @ 1g/10L for canker."])

c("acid-lime-kagzi", "Acid Lime (Kagzi Nimbu)", "कागदी लिंबू (Kagzi Nimbu)", "Citrus aurantifolia", "Fruits & Horticulture", "🍋",
  "Year-round bearing", "Ahmednagar (Rahuri, Shrirampur), Solapur, Akola, Western Maharashtra",
  "Indispensable Indian thin-skinned aromatic round juicy lime used for fresh lemonade, pickles, culinary seasoning, and vitamin C.",
  "20°C - 34°C", "700 - 900 mm.", "Light loam to medium black soil.",
  [{"stage": "Flush & Flowering", "days": "3-4 flushes/yr", "description": "Continuous white flowers."},
   {"stage": "Fruit Growth", "days": "Months 3-4", "description": "Smooth thin rind fills with sour juice."},
   {"stage": "Harvest", "days": "Months 5-6", "description": "Picked when fruit turns green-yellow."}],
  [{"name": "Citrus Canker", "symptoms": "Corky craters.", "riskPeriod": "Rainstorms."},
   {"name": "Tristeza Virus", "symptoms": "Stem pitting and vein clearing; aphid vector.", "riskPeriod": "Aphid season."}],
  ["Leaf Miner", "Citrus Butterfly Caterpillar", "Scale Insects"],
  ["Prune canker-infected twigs in May before rains.", "Use Sai Sharbati, Pramalini, or Phule Sharbati varieties."])

c("guava-sardar-l49", "Guava (Sardar L-49 / Lucknow 49)", "पेरू / सरदार लखनौ-४९ (Sardar Peru)", "Psidium guajava", "Fruits & Horticulture", "🍈",
  "Mrig Bahar (Winter crop) / Ambe Bahar", "Western Maharashtra (Pune, Ahmednagar, Satara), Khandesh, Nashik",
  "Premier heavy-yielding guava variety bred in Pune (Ganeshkhind). Rough greenish-yellow skin, creamy white dense pulp, rich in vitamin C and pectin.",
  "20°C - 32°C", "700 - 1,000 mm; hardy and drought tolerant once established.", "Well-drained loamy soil, tolerates salinity and alkaline soils better than most fruits.",
  [{"stage": "Bahar Training & Bending", "days": "April - May", "description": "Branches bent horizontally to stimulate dormant lateral buds into flower shoots."},
   {"stage": "Flowering", "days": "June", "description": "Snow-white flowers with prominent stamens bloom."},
   {"stage": "Fruit Development", "days": "July - Oct", "description": "Globose fruits swell rapidly."},
   {"stage": "Harvest (Winter Peru)", "days": "Nov - Jan", "description": "Crisp sweet winter guavas harvested with high market value."}],
  [{"name": "Guava Wilt (Fusarium oxysporum f. sp. psidii)", "symptoms": "Yellowing and sudden wilting of branches starting on one side; bark splits.", "riskPeriod": "Alkaline clay soils with moisture stagnation."},
   {"name": "Fruit Canker / Anthracnose", "symptoms": "Small brown circular spots turning into rough crater lesions.", "riskPeriod": "Warm wet monsoon."}],
  ["Fruit Fly (Bactrocera correcta)", "Mealybug", "Bark Eating Caterpillar", "Tea Mosquito Bug"],
  ["Adopt branch bending technique in May to double flowering shoots.",
   "Install methyl eugenol fruit fly traps and bag winter guavas with foam nets.",
   "Use Sardar L-49, Allahabad Safeda, or VNR Bihi varieties."])

c("custard-apple-sitaphal", "Custard Apple (Sitaphal)", "सीताफळ (Balanagar Sitaphal)", "Annona squamosa", "Fruits & Horticulture", "🍈",
  "Autumn / Winter (Sept to Dec)", "Marathwada (Beed is Sitaphal hub, Dharashiv/Osmanabad), Pune, Solapur, Ahmednagar dry hills",
  "The sweet jewel of Maharashtra drylands holding GI status. Knobby green fruit filled with rich, creamy, aromatic custardy pulp with delightful caramel sweetness.",
  "22°C - 35°C (tolerates extreme heat and rocky hillsides)", "400 - 650 mm; thrives under low rainfed conditions.",
  "Shallow gravelly rocky soil, hill slopes with excellent drainage, pH 6.0 - 8.0.",
  [{"stage": "Sprouting & Flowering", "days": "May - June", "description": "Fresh green shoots emerge with monsoon; fragrant drooping yellow-green blossoms."},
   {"stage": "Fruit Set & Tuberculate Growth", "days": "July - Sept", "description": "Aggregate fruit (syncarp) expands with knobby segments."},
   {"stage": "Maturation & Harvest", "days": "Oct - Dec", "description": "Areoles broaden and reveal creamy white inter-segment lines; handpicked firm."}],
  [{"name": "Anthracnose / Fruit Rot", "symptoms": "Dark brown dry shrivelled mummified fruits hanging on tree.", "riskPeriod": "Overcast humid monsoon."},
   {"name": "Leaf Spot", "symptoms": "Circular spots.", "riskPeriod": "Rain."}],
  ["Mealybug (Maconellicoccus hirsutus)", "Fruit Borer", "Scale Insects"],
  ["Control mealybugs by drenching trunk base with chlorpyrifos or releasing Cryptolaemus beetles.",
   "Use Balanagar, Phule Purandar, or Anona-2 varieties."])

c("fig-rajewadi-purandar", "Fig (Rajewadi / Purandar Anjeer)", "अंजीर (Purandar Anjeer)", "Ficus carica", "Fruits & Horticulture", "🫐",
  "Spring & Summer (Feb to May)", "Pune (Purandar, Saswad, Rajewadi is Fig Capital of India)",
  "The historic GI-tagged pride of Purandar valley. Bell-shaped violet-bronze figs with sweet luscious pink pulp, rich in calcium and iron.",
  "18°C - 34°C (warm dry summer with zero rainfall during ripening)", "500 - 650 mm; drip irrigation; rain during ripening causes catastrophic fruit splitting.",
  "Deep, well-drained medium black cotton soil or gravelly calcareous loams rich in lime.",
  [{"stage": "Kharif Pruning & Resting", "days": "June - Aug", "description": "Foliage rests during monsoon rains."},
   {"stage": "Sweet Crop Pruning (Meethi Bahar)", "days": "Sept - Oct", "description": "Branches pruned to stimulate fresh fruiting nodes."},
   {"stage": "Syconium Fruit Development", "days": "Nov - Feb", "description": "Unique inverted hollow flower (syconium) swells."},
   {"stage": "Harvesting", "days": "March - May", "description": "Figs soften, neck droops; harvested at daybreak for fresh urban markets."}],
  [{"name": "Fig Rust (Cerotelium fici)", "symptoms": "Small yellowish-brown powdery pustules on leaf undersides causing premature leaf shedding.", "riskPeriod": "Humid post-monsoon weather (Oct-Dec)."},
   {"name": "Anthracnose / Fruit Rot", "symptoms": "Sunken brown spots on fruit.", "riskPeriod": "Unseasonal rainfall."}],
  ["Stem Borer", "Fig Jassids", "Mites", "Fruit Fly"],
  ["Spray Wettable Sulfur @ 2g/L or Mancozeb @ 2.5g/L at first rust symptom in November.",
   "Use famous GI variety Poona Fig / Rajewadi Fig."])

c("strawberry-mahabaleshwar", "Strawberry (Mahabaleshwar Strawberry)", "स्ट्रॉबेरी (Mahabaleshwar Strawberry)", "Fragaria × ananassa", "Fruits & Horticulture", "🍓",
  "Winter to Early Summer (Nov to April)", "Satara (Mahabaleshwar & Panchgani produce 85% of India's strawberries), Wai, Pune hills",
  "The red ruby of Maharashtra hill stations holding GI status. Vibrant crimson conical berries with intense sweet aroma and delightful juiciness cultivated on misty Western Ghat terraces.",
  "14°C - 24°C (cool nights, mild sunny days; frost-sensitive)", "400 - 550 mm through drip; plastic mulch and drip mandatory.",
  "Well-drained rich red lateritic mountain soil rich in organic compost, pH 5.5 - 6.5.",
  [{"stage": "Runner Planting on Silver-Black Mulch", "days": "Sept - Oct", "description": "Cold-stored mother runners planted on raised drip-irrigated beds covered with reflective mulch."},
   {"stage": "Crown Development & Flowering", "days": "Nov - Dec", "description": "Trifoliate leaves spread; five-petaled white flowers bloom; bee-pollinated."},
   {"stage": "Berry Sizing & Crimson Ripening", "days": "Dec - March", "description": "Berries turn from green to white to brilliant ruby red."},
   {"stage": "Daily Morning Harvest", "days": "Dec - April", "description": "Delicately handpicked with stem into cardboard export punnets."}],
  [{"name": "Grey Mold (Botrytis cinerea)", "symptoms": "Soft watery fruit rot covered with dense velvety grey fungal fur.", "riskPeriod": "Cool misty weather, winter rain, or foliage touching damp soil."},
   {"name": "Leaf Spot (Mycosphaerella fragariae)", "symptoms": "Small white spots with deep purple borders on strawberry leaflets.", "riskPeriod": "High humidity and overhead sprinkler wetting."},
   {"name": "Powdery Mildew (Podosphaera aphanis)", "symptoms": "Upward curling of leaf margins with white powdery coating on leaf undersides and young fruit.", "riskPeriod": "Dry warm days and cool humid nights."}],
  ["Two-Spotted Spider Mite (Tetranychus urticae)", "Thrips", "Cutworms", "White Grubs"],
  ["Plant on silver-black plastic mulch to completely prevent fruit contact with wet soil.",
   "Drench bio-agent Trichoderma at planting to prevent crown root rot.",
   "Use premier varieties: Sweet Charlie, Camarosa, Winter Dawn, or Rania.",
   "Spray bio-fungicide Bacillus subtilis or Fenhexamid for grey mold control."])

c("papaya-red-lady", "Papaya (Red Lady 786)", "पपई (Red Lady Papaya)", "Carica papaya", "Fruits & Horticulture", "🍈",
  "Year-round bearing", "Khandesh (Nandurbar, Jalgaon, Dhule), Pune, Sangli, Solapur, Marathwada",
  "High-yielding gynodioecious hybrid producing thick, sweet, deep red-orange flesh with high sugar content (13° Brix) and robust transport shelf life.",
  "22°C - 34°C (sensitive to frost and waterlogging)", "1,200 - 1,500 mm through drip; zero water stagnation.",
  "Deep, rich, friable sandy loam or medium black soil with phenomenal drainage, pH 6.5 - 7.2.",
  [{"stage": "Nursery & Transplanting", "days": "Months 1-2", "description": "60-day seedlings planted on raised mounds."},
   {"stage": "Vegetative Growth & Flowering", "days": "Months 3-5", "description": "Rapid hollow stem elongation; self-fertile bisexual and female blossoms in leaf axils."},
   {"stage": "Fruit Development", "days": "Months 6-8", "description": "Cylindrical heavy fruits crowd upper trunk below leaf canopy."},
   {"stage": "Continuous Harvest", "days": "Months 9-18", "description": "Picked when yellow color breaks at blossom end."}],
  [{"name": "Papaya Ring Spot Virus (PRSV)", "symptoms": "Yellow mosaic mottling on leaves, severe shoe-string leaf distortion, dark green water-soaked oily rings on fruit rind and petioles; aphid vector.", "riskPeriod": "High aphid activity during post-monsoon and early summer."},
   {"name": "Collar Rot / Stem Rot (Pythium aphanidermatum)", "symptoms": "Water-soaked soft rotting at soil line causing top-heavy tree to topple over.", "riskPeriod": "Water stagnation during heavy monsoon."}],
  ["Papaya Mealybug (Paracoccus marginatus)", "Aphids", "Spider Mites"],
  ["Plant border rows of barrier crops (maize or sorghum) to intercept PRSV aphid vectors.",
   "Release parasitoid Acerophagus papayae to achieve 100% biological control of devastating Papaya mealybugs.",
   "Plant on raised ridges to ensure irrigation water never touches tree trunk base."])

c("watermelon", "Watermelon", "कलिंगड / टरबूज (Kalingad)", "Citrullus lanatus", "Fruits & Horticulture", "🍉",
  "Zaid / Summer & Winter", "Western Maharashtra (Pune, Solapur, Satara riverbeds), Marathwada, Khandesh",
  "Thirst-quenching summer vine yielding heavy fruits with crisp, juicy, deep crimson flesh, high lycopene, and sweetness.",
  "24°C - 35°C", "400 - 600 mm via drip fertigation on silver mulch.", "Well-drained sandy loam or riverbed alluvium, pH 6.0 - 7.5.",
  [{"stage": "Emergence & Vine Running", "days": "Days 1-30", "description": "Vigorous trailing vines spread across bed."},
   {"stage": "Flowering & Pollination", "days": "Days 31-50", "description": "Yellow monoecious flowers; morning bee pollination critical."},
   {"stage": "Fruit Sizing", "days": "Days 51-75", "description": "Berries expand rapidly accumulating water and sugars."},
   {"stage": "Harvest Maturity", "days": "Days 76-95", "description": "Tendril near fruit dries completely; ground spot turns buttery yellow; dull thud sound on tapping."}],
  [{"name": "Fusarium Wilt", "symptoms": "Vines wilt unilaterally; vascular browning.", "riskPeriod": "Hot soils."},
   {"name": "Downy Mildew", "symptoms": "Angular yellow patches on leaves.", "riskPeriod": "Morning dew and fog."}],
  ["Fruit Fly", "Thrips", "Aphids", "Red Pumpkin Beetle"],
  ["Use popular icebox hybrids: Sugar Baby, Kiran, Max, or Saraswati.",
   "Install methyl eugenol traps for fruit fly control."])

c("muskmelon-kharbuj", "Muskmelon (Kharbuj)", "खरबूज / चिबूड (Kharbuj)", "Cucumis melo", "Fruits & Horticulture", "🍈",
  "Summer", "Pune, Ahmednagar, Solapur, Marathwada",
  "Aromatic ribbed melon with sweet succulent orange/salmon pulp and intoxicating dessert fragrance.",
  "25°C - 35°C", "350 - 500 mm.", "Sandy loam with great drainage.",
  [{"stage": "Vine Running", "days": "Days 1-25", "description": "Rapid vine growth."},
   {"stage": "Flowering", "days": "Days 26-45", "description": "Bee pollination."},
   {"stage": "Netted Fruit Sizing", "days": "Days 46-70", "description": "Corky net pattern develops on rind."},
   {"stage": "Full Slip Harvest", "days": "Days 71-85", "description": "Stem separates cleanly from fruit upon gentle pressure."}],
  [{"name": "Powdery Mildew", "symptoms": "White coating.", "riskPeriod": "Dry warm days."},
   {"name": "Downy Mildew", "symptoms": "Yellow leaf spots.", "riskPeriod": "Humidity."}],
  ["Fruit Fly", "Whitefly"], ["Use varieties: Madhuras, Hara Madhu, Kundan."])

c("sapota-chikoo-dahanu", "Sapota / Chikoo (Dahanu Gholvad)", "चिकू (Dahanu Gholvad Chikoo)", "Manilkara zapota", "Fruits & Horticulture", "🥔",
  "Year-round bearing (Peak Nov - March)", "Palghar & Thane (Dahanu & Gholvad produce GI-tagged Chikoo), Konkan Coast",
  "The GI-tagged coastal treasure of Maharashtra. Velvety golden-brown round fruits with exceptionally sweet, malty, granulated brown pulp shaped by coastal calcium-rich soils.",
  "22°C - 34°C", "1,200 - 1,800 mm.", "Deep coastal sandy alluvium and lateritic soils.",
  [{"stage": "Continuous Bloom", "days": "3 flushes/yr", "description": "Bell-shaped white flowers in leaf axils."},
   {"stage": "Fruit Development", "days": "Months 4-8", "description": "Slow fruit expansion accumulating milky latex."},
   {"stage": "Harvesting", "days": "Months 9-10", "description": "Scratching skin reveals yellow-green flesh beneath brown scurf."}],
  [{"name": "Leaf Spot (Phaeophleospora indica)", "symptoms": "Circular brown spots with white center on leaves.", "riskPeriod": "Monsoon rains."}],
  ["Chikoo Moth / Leaf Webber", "Bud Borer", "Mealybug"],
  ["Use renowned varieties: Kalipatti, Cricket Ball, or Murabba.",
   "Clean brown scurf and wash fruits in water baths before boxing."])

c("cashew-vengurla", "Cashew (Vengurla Kaju)", "काजू (Vengurla Kaju)", "Anacardium occidentale", "Fruits & Horticulture", "🥜",
  "Harvest: March - May", "South Konkan (Sindhudurg, Ratnagiri, Vengurla is Cashew Research hub), Goa",
  "High-value coastal plantation crop holding GI status. Yields nutritious kidney-shaped cashew nuts and succulent aromatic cashew apples (used for feni).",
  "24°C - 35°C", "1,500 - 2,500 mm; thrives rainfed on sloped hillocks.", "Rocky red lateritic hill soils with good drainage.",
  [{"stage": "Flushing", "days": "Oct - Nov", "description": "Pinkish new shoot flush."},
   {"stage": "Panicle Flowering", "days": "Dec - Feb", "description": "Fragrant terminal panicles."},
   {"stage": "Nut & Apple Maturation", "days": "March - May", "description": "Grey kidney nut forms first; pedicel swells into red/yellow cashew apple."}],
  [{"name": "Dieback / Pink Disease", "symptoms": "Twig withering.", "riskPeriod": "Monsoon."}],
  ["Tea Mosquito Bug (Helopeltis antonii)", "Cashew Stem and Root Borer (Plocaederus ferrugineus)"],
  ["Plant high-yielding Vengurla hybrids: V-4, V-7, V-8, or V-9.",
   "Spray Lambda-cyhalothrin at vegetative flushing and flowering against tea mosquito bug.",
   "Chisel out stem borer grubs from trunk base and paste with coal tar + kerosene."])

c("jackfruit-phanas", "Jackfruit (Phanas)", "फणस (Konkan Phanas)", "Artocarpus heterophyllus", "Fruits & Horticulture", "🍈",
  "Summer (March to July)", "Konkan Coast (Sindhudurg, Ratnagiri, Raigad), Western Ghats",
  "World's largest tree-borne fruit. Distinctive spiky exterior; available as firm crunchy 'Kaapa' (कापा) and soft luscious 'Rasaal' (रसाळ) golden bulbs.",
  "22°C - 35°C", "1,500 - 2,500 mm.", "Deep lateritic alluvium.",
  [{"stage": "Cauliflorous Flowering", "days": "Nov - Jan", "description": "Club-shaped spikes emerge directly from main tree trunk and heavy scaffold branches."},
   {"stage": "Fruit Development", "days": "Feb - April", "description": "Spiky syncarp swells up to 10-25 kg."},
   {"stage": "Ripening & Harvest", "days": "May - July", "description": "Spines flatten; hollow drum sound when tapped; intoxicating fruity aroma."}],
  [{"name": "Rhizopus Fruit Rot", "symptoms": "Soft black fungal whisker decay.", "riskPeriod": "Monsoon rains."}],
  ["Shoot and Fruit Borer", "Spittle Bug"], ["Grow renowned Konkan varieties: Konkan Prolific, Sindhur, or Gumless."])

c("jamun-blackberry", "Jamun (Indian Blackberry)", "जांभूळ (Konkan / Bahadoli Jamun)", "Syzygium cumini", "Fruits & Horticulture", "🫐",
  "Summer (May - June)", "Throughout Maharashtra & India, Konkan, Western Ghats",
  "Sacred, medicinal purple fruit world-famous for controlling diabetes (jamboline glucoside) and purifying blood.",
  "22°C - 36°C", "Rainfed once established.", "Deep alluvial soils and river banks.",
  [{"stage": "Flowering", "days": "March", "description": "Fragrant greenish-white flowers."},
   {"stage": "Fruit Sizing", "days": "April - May", "description": "Green oblong berries transition to pink then deep glossy purple."},
   {"stage": "Harvest", "days": "May - June", "description": "Harvested fresh before monsoon."}],
  [{"name": "Anthracnose", "symptoms": "Dark fruit spots.", "riskPeriod": "Humid spells."}],
  ["Fruit Fly", "Whitefly"], ["Use large-fruited varieties like Bahadoli or Konkan Jamun."])

c("aonla-amla", "Aonla (Indian Gooseberry)", "आवळा (Amla)", "Phyllanthus emblica", "Fruits & Horticulture", "🍈",
  "Winter (Nov - Jan)", "Ahmednagar, Pune, Marathwada, Central India",
  "Revered Ayurvedic rasayana packed with 20 times more Vitamin C than oranges. Hardy tree thriving in drought and alkaline wastelands.",
  "20°C - 38°C", "400 - 600 mm.", "Light, calcareous, and sodic soils.",
  [{"stage": "Flowering", "days": "March - April", "description": "Yellow flowers in leaf axils; embryonic dormancy."},
   {"stage": "Fruit Growth", "days": "July - Oct", "description": "Six-ribbed light green translucent berries expand."},
   {"stage": "Harvest", "days": "Nov - Jan", "description": "Harvested for Chyawanprash, candy, and juice."}],
  [{"name": "Aonla Rust (Ravenelia emblicae)", "symptoms": "Brown pustules on fruit and leaves.", "riskPeriod": "Cloudy post-monsoon weather."}],
  ["Bark Eating Caterpillar", "Gall Midge"], ["Use high-yielding varieties: NA-7, Krishna, Kanchan, or Chakaiya."])

c("ber-indian-plum", "Ber (Indian Jujube)", "बोर (Umran / Gola Bor)", "Ziziphus mauritiana", "Fruits & Horticulture", "🍈",
  "Winter (Dec - Feb)", "Marathwada, Solapur, Ahmednagar dry belts",
  "The king of arid fruits. Thorny, drought-hardy tree producing crisp, sweet, apple-like golden-yellow fruits.",
  "25°C - 40°C", "250 - 450 mm.", "Sandy, rocky, or saline soils.",
  [{"stage": "Pruning", "days": "April - May", "description": "Heavy annual heading back."},
   {"stage": "Bloom", "days": "Sept - Oct", "description": "Small yellow flowers."},
   {"stage": "Harvest", "days": "Dec - Feb", "description": "Crisp golden fruits picked."}],
  [{"name": "Powdery Mildew", "symptoms": "White coating on fruit.", "riskPeriod": "Winter."}],
  ["Ber Fruit Fly (Carpomyia vesuviana)"], ["Use Umran, Gola, or Mehrun varieties."])

c("tamarind-chinch", "Tamarind (Chinch)", "चिंच (Pratishthan Chinch)", "Tamarindus indica", "Fruits & Horticulture", "🫘",
  "Harvest: Jan - April", "Marathwada, Western Maharashtra, South India",
  "Long-lived majestic tree producing tart, pulp-rich brown pods indispensable in Indian sambar, rasam, and chutneys.",
  "25°C - 38°C", "Rainfed.", "Deep alluvium and dry soils.",
  [{"stage": "Flowering", "days": "May - June", "description": "Yellow streaked with red flowers."},
   {"stage": "Pod Maturity", "days": "Jan - April", "description": "Brittle shell cracks revealing sticky dark brown tangy pulp."}],
  [{"name": "Sooty Mold", "symptoms": "Black leaf mold.", "riskPeriod": "Humid periods."}],
  ["Scale Insects"], ["Plant high-pulp grafted varieties: Pratishthan, PKM-1, or Yogeshwari."])

c("royal-delicious-apple", "Apple (Royal Delicious)", "सफरचंद (Royal Delicious Apple)", "Malus domestica", "Fruits & Horticulture", "🍎",
  "Late Summer (Aug - Oct)", "Kashmir Valley, Himachal Pradesh (Shimla, Kullu), Uttarakhand",
  "Premier temperate fruit of India requiring 800-1000 chilling hours below 7°C. Crisp, aromatic red dessert apple.",
  "10°C - 24°C", "1,000 - 1,200 mm.", "Deep fertile mountain loam.",
  [{"stage": "Bud Burst & Pink Bud", "days": "April", "description": "Pink blossoms open."},
   {"stage": "Fruit Set", "days": "May", "description": "Spur fruitlets form; thinning applied."},
   {"stage": "Coloration & Harvest", "days": "Aug - Oct", "description": "Deep red stripes develop."}],
  [{"name": "Apple Scab (Venturia inaequalis)", "symptoms": "Olive-green to black velvety spots on leaves and scabby deformed fruit.", "riskPeriod": "Prolonged wet spring weather."},
   {"name": "Powdery Mildew", "symptoms": "White coating on terminal shoots.", "riskPeriod": "Dry spring."}],
  ["Woolly Apple Aphid (Eriosoma lanigerum)", "San Jose Scale", "Mites"],
  ["Prophylactic spray of Mancozeb or Difenoconazole at pink bud stage for scab prevention."])

c("golden-delicious-apple", "Golden Delicious Apple", "गोल्डन सफरचंद (Golden Delicious)", "Malus domestica", "Fruits & Horticulture", "🍏",
  "Autumn", "Kashmir, Himachal Pradesh",
  "Sweet, juicy, honey-flavored golden-yellow dessert and culinary apple with smooth skin and exceptional aroma.",
  "10°C - 24°C", "1,000 mm.", "Rich mountain loams.",
  [{"stage": "Bloom", "days": "April", "description": "White flowers."},
   {"stage": "Harvest", "days": "Sept - Oct", "description": "Golden skin with sweet crisp flesh."}],
  [{"name": "Apple Scab", "symptoms": "Scab lesions.", "riskPeriod": "Spring rains."}],
  ["Mites"], ["Harvest carefully to avoid skin bruising."])

c("malta-orange", "Malta Sweet Orange", "माल्टा संत्रे (Malta Orange)", "Citrus sinensis", "Fruits & Horticulture", "🍊",
  "Winter", "Punjab, Rajasthan, UP, Himachal foothills",
  "Tight-skinned sweet orange yielding dense aromatic orange juice with rich vitamin C.",
  "18°C - 30°C", "800 - 1,000 mm.", "Deep sandy loam.",
  [{"stage": "Bloom", "days": "March", "description": "Spring blossom."},
   {"stage": "Harvest", "days": "Dec - Feb", "description": "Golden orange globose fruit."}],
  [{"name": "Canker", "symptoms": "Corky lesions.", "riskPeriod": "Stormy rains."}],
  ["Citrus Psylla"], ["Spray copper fungicides before monsoon."])

c("kew-pineapple", "Pineapple (Kew / Queen)", "अननस (Kew Pineapple)", "Ananas comosus", "Fruits & Horticulture", "🍍",
  "Year-round", "Konkan (Sindhudurg, Ratnagiri), Assam, Kerala, West Bengal",
  "Spiky tropical bromeliad yielding giant aromatic golden syncarp rich in bromelain enzyme.",
  "22°C - 32°C", "1,500 - 2,500 mm.", "Acidic sandy loam with high organic matter, pH 4.5 - 5.5.",
  [{"stage": "Vegetative", "days": "Months 1-10", "description": "Spiky rosette."},
   {"stage": "Flowering Induction", "days": "Month 11", "description": "Ethephon applied into heart."},
   {"stage": "Harvest", "days": "Months 15-18", "description": "Base eyes turn golden yellow."}],
  [{"name": "Heart Rot (Phytophthora)", "symptoms": "Central leaf rot.", "riskPeriod": "Waterlogged soil."}],
  ["Pineapple Mealybug"], ["Dip suckers in Bordeaux mixture before planting."])

c("shahi-litchi", "Shahi Litchi", "शाही लिची (Shahi Litchi)", "Litchi chinensis", "Fruits & Horticulture", "🍓",
  "May - June", "Muzaffarpur (Bihar - GI tagged), Dehradun, Punjab",
  "Exquisite translucent juicy aril with divine rose fragrance enclosed in rough pink-red leathery pericarp.",
  "22°C - 34°C (requires mild cool winter without frost followed by warm dry spring)", "1,200 - 1,500 mm.", "Deep rich alluvial calcareous loam.",
  [{"stage": "Flowering", "days": "Feb - March", "description": "Apetalous panicles."},
   {"stage": "Fruit Development", "days": "April - May", "description": "Rapid aril swelling."},
   {"stage": "Harvest", "days": "May - June", "description": "Bright red clusters picked."}],
  [{"name": "Fruit Cracking", "symptoms": "Pericarp splits.", "riskPeriod": "Dry westerly winds followed by rain."}],
  ["Litchi Mite (Eriophyes litchii - Erinose)", "Fruit Borer"], ["Irrigate regularly during summer to prevent fruit cracking."])

c("dragon-fruit-kamalam", "Dragon Fruit (Kamalam)", "ड्रॅगन फ्रूट / कमलम (Dragon Fruit)", "Hylocereus undatus", "Fruits & Horticulture", "🐉",
  "Monsoon to Winter (June to Nov)", "Baramati (Pune), Solapur, Sangli, Gujarat, Marathwada",
  "Climbing night-blooming cactus yielding exotic bright pink fruits with speckled white/red sweet pulp packed with antioxidants.",
  "20°C - 35°C", "500 - 700 mm; low water requirement.", "Well-drained sandy loam or gravelly soil; zero waterlogging.",
  [{"stage": "Trellis Growth", "days": "Year 1", "description": "Triangular fleshy cladodes trained on cement poles with tire ring."},
   {"stage": "Nocturnal Blooming", "days": "Monthly (June-Oct)", "description": "Giant fragrant white flowers bloom for one night."},
   {"stage": "Fruit Maturation", "days": "30-35 days from bloom", "description": "Pink skin with green scales; picked firm."}],
  [{"name": "Stem Canker (Neoscytalidium dimidiatum)", "symptoms": "Sunken yellow-orange spots turning into brown cankers.", "riskPeriod": "Heavy continuous rain."}],
  ["Ants", "Mealybugs"], ["Spray copper hydroxide and prune infected stems."])

c("kokum-ratamba", "Kokum (Ratamba)", "कोकम / रातांबा (Konkan Kokum)", "Garcinia indica", "Fruits & Horticulture", "🫐",
  "March - May", "Konkan (Ratnagiri, Sindhudurg holding GI status), Western Ghats",
  "Endemic Western Ghats fruit yielding ruby-red tangy rinds (amsul) for solkadhi, cooling summer sarbat, and kokum butter.",
  "24°C - 34°C", "2,000 - 3,500 mm.", "Red lateritic coastal soils.",
  [{"stage": "Bloom", "days": "Nov - Feb", "description": "Dioecious fleshy flowers."},
   {"stage": "Fruit Ripening", "days": "March - May", "description": "Globose fruits turn deep dark purple; harvested fresh."}],
  [{"name": "Fruit Rot", "symptoms": "Decay.", "riskPeriod": "Early rains."}],
  ["Leaf Eating Caterpillar"], ["Plant grafted varieties: Konkan Amruta or Konkan Hatis."])

c("karonda-pickle-berry", "Karonda", "करवंद (Karavand)", "Carissa carandas", "Fruits & Horticulture", "🫐",
  "Summer (May - June)", "Konkan, Western Ghats wild forests, throughout Maharashtra",
  "Hardy spiny shrub yielding white-pink berries that turn glossy black; beloved for sour pickles, chutneys, and raw forest snacking.",
  "24°C - 38°C", "Rainfed.", "Rocky, gravelly, marginal soils.",
  [{"stage": "Flowering", "days": "Feb - March", "description": "Fragrant white starry blossoms."},
   {"stage": "Harvest", "days": "May - June", "description": "Berry pickings for pickle or fresh."}],
  [{"name": "Anthracnose", "symptoms": "Spotting.", "riskPeriod": "Rains."}],
  ["Leaf Webber"], ["Use Konkan Bold variety."])

c("wood-apple-kavath", "Wood Apple (Kavath)", "कवठ / कपित्थ (Kavath)", "Limonia acidissima", "Fruits & Horticulture", "🥥",
  "Winter (Nov - Feb)", "Dry zones of Maharashtra, Marathwada, Western Ghat plateaus",
  "Extremely hard woody spherical shell holding aromatic, astringent, brown sticky pulp made into famous Kavath Chutney and Murabba.",
  "22°C - 38°C", "Rainfed.", "Dry arid soils.",
  [{"stage": "Flowering", "days": "April - May", "description": "Small dull red flowers."},
   {"stage": "Harvest", "days": "Nov - Feb", "description": "Hard grey woody shells fall when ripe."}],
  [{"name": "Leaf Spot", "symptoms": "Specks.", "riskPeriod": "Monsoon."}],
  ["Bark Caterpillar"], ["Virtually pest-free dryland fruit."])

c("phalsa", "Phalsa", "फालसा (Phalsa)", "Grewia asiatica", "Fruits & Horticulture", "🫐",
  "Peak Summer (April - May)", "North Maharashtra, Central India, Punjab",
  "Small sweet-tart purple berries renowned for cooling sherbet and anti-heatstroke properties in blazing Indian summers.",
  "25°C - 42°C", "300 - 450 mm.", "All soils.",
  [{"stage": "Annual Pruning", "days": "Jan", "description": "Cut back close to ground."},
   {"stage": "Harvest", "days": "April - May", "description": "Tiny purple berries picked daily."}],
  [{"name": "Rust", "symptoms": "Leaf spots.", "riskPeriod": "Post-harvest rains."}],
  ["Mealybug"], ["Prune in January to 1 meter height to trigger fresh fruiting shoots."])

c("bael-fruit", "Bael (Golden Apple)", "बेलफळ / बेल (Bael)", "Aegle marmelos", "Fruits & Horticulture", "🍈",
  "Summer (March - June)", "Throughout India, forest tracts of Maharashtra",
  "Sacred Shiva tree producing hard-shelled fruits with sweet, aromatic, mucilaginous orange pulp supreme for digestive health and sherbet.",
  "22°C - 40°C", "Rainfed.", "Rocky, saline, and swampy soils.",
  [{"stage": "Flowering", "days": "May", "description": "Fragrant blossoms."},
   {"stage": "Slow Fruit Maturity", "days": "Takes 10-11 months", "description": "Large globose fruit matures next summer."}],
  [{"name": "Fruit Canker", "symptoms": "Shell lesions.", "riskPeriod": "Rain."}],
  ["Leaf Miner"], ["Use improved varieties: Narendra Bael-5, Pant Aparna."])

c("passion-fruit", "Passion Fruit", "पॅशन फ्रूट (Passion Fruit)", "Passiflora edulis", "Fruits & Horticulture", "🫐",
  "Monsoon & Winter", "Western Ghats (Mahabaleshwar, Ooty, Coorg), Northeast India",
  "Vigorous climbing vine yielding aromatic purple/yellow fruits filled with intensely aromatic sweet-tart pulp and edible seeds.",
  "18°C - 28°C", "1,000 - 1,500 mm.", "Well-drained rich mountain loam.",
  [{"stage": "Vine Trellising", "days": "Months 1-6", "description": "Trained on wire trellis."},
   {"stage": "Flowering & Harvest", "days": "Months 7-12", "description": "Stunning purple flowers; fruit harvested when purple skin wrinkles slightly."}],
  [{"name": "Brown Spot (Alternaria passiflorae)", "symptoms": "Sunken brown spots on fruit.", "riskPeriod": "Humid rain."}],
  ["Fruit Fly", "Mites"], ["Spray mancozeb for brown spot control."])

c("kiwi-fruit", "Kiwi Fruit", "किवी (Kiwi)", "Actinidia deliciosa", "Fruits & Horticulture", "🥝",
  "Autumn (Oct - Nov)", "Arunachal Pradesh, Himachal Pradesh, Nilgiris",
  "Temperate dioecious climbing vine producing brown fuzzy berries with vibrant green flesh and black seeds.",
  "12°C - 24°C (requires winter chilling)", "1,200 mm.", "Deep acidic loams.",
  [{"stage": "Bloom", "days": "May", "description": "Male and female vines cross-pollinated."},
   {"stage": "Harvest", "days": "Oct - Nov", "description": "Hard fruits picked for controlled ripening."}],
  [{"name": "Root Rot", "symptoms": "Wilting.", "riskPeriod": "Water stagnation."}],
  ["Armoured Scale"], ["Maintain 1:8 male to female vine ratio on pergolas."])

c("plum-alubukhara", "Plum (Alubukhara)", "आलू बुखार / प्लम (Plum)", "Prunus domestica", "Fruits & Horticulture", "🫐",
  "Early Summer (May - June)", "Himachal Pradesh, Kashmir, Nilgiris",
  "Succulent drupe with smooth reddish-purple skin and juicy sweet-tart pulp with a single hard stone.",
  "12°C - 24°C", "800 - 1,000 mm.", "Well-drained loams.",
  [{"stage": "Bloom", "days": "March", "description": "White blossom canopy."},
   {"stage": "Harvest", "days": "May - June", "description": "Picked firm for market."}],
  [{"name": "Brown Rot (Monilinia)", "symptoms": "Fuzzy brown fruit decay.", "riskPeriod": "Wet pre-harvest."}],
  ["Plum Aphid"], ["Spray captan before harvest."])

c("peach-aadu", "Peach (Aadu)", "आडू / पीच (Peach)", "Prunus persica", "Fruits & Horticulture", "🍑",
  "Early Summer", "Punjab, Himachal, Uttarakhand foothills",
  "Velvety fuzzy skin drupe with yellow-red blush and melting sweet aromatic flesh.",
  "14°C - 26°C", "800 mm.", "Sandy loam with great drainage.",
  [{"stage": "Pink Bloom", "days": "Feb", "description": "Stunning pink flowers."},
   {"stage": "Harvest", "days": "May - June", "description": "Handpicked."}],
  [{"name": "Peach Leaf Curl (Taphrina deformans)", "symptoms": "Leaves thicken, pucker, and turn red-yellow.", "riskPeriod": "Cool wet spring bud swell."}],
  ["Peach Aphid"], ["Apply lime sulfur spray during dormant bud swell."])

c("apricot-khubani", "Apricot (Khubani)", "खुबानी / जर्दाळू (Apricot)", "Prunus armeniaca", "Fruits & Horticulture", "🍑",
  "Summer (May - July)", "Ladakh, Kashmir, Himachal Pradesh",
  "Velvety golden-orange fruit famous for rich dietary fiber, vitamin A, and sun-dried Ladakhi Khubani.",
  "12°C - 25°C", "600 - 800 mm.", "Well-drained gravelly loams.",
  [{"stage": "Blossom", "days": "March", "description": "White flowers."},
   {"stage": "Harvest", "days": "June - July", "description": "Golden fruits picked."}],
  [{"name": "Gummosis", "symptoms": "Gum ooze.", "riskPeriod": "Rain."}],
  ["Chaffer Beetle"], ["Use Halman or New Castle varieties."])

c("sweet-cherry", "Sweet Cherry", "चेरी (Sweet Cherry)", "Prunus avium", "Fruits & Horticulture", "🍒",
  "Summer (May - June)", "Kashmir Valley, Himachal Pradesh",
  "Exquisite glossy ruby-red heart-shaped fruit with sweet crisp flesh and green stem.",
  "10°C - 22°C (high chilling requirement)", "900 mm.", "Deep fertile mountain loam.",
  [{"stage": "White Blossom", "days": "April", "description": "Full white canopy."},
   {"stage": "Harvest", "days": "May - June", "description": "Carefully hand-picked with stems."}],
  [{"name": "Fruit Cracking", "symptoms": "Skin splits.", "riskPeriod": "Rain during harvest."}],
  ["Cherry Fruit Fly"], ["Cover trees with plastic rain shelters during ripening."])

c("pear-nashpati", "Pear (Nashpati / Babgosh)", "नाशपाती / बबूगोशा (Nashpati)", "Pyrus communis / P. pyrifolia", "Fruits & Horticulture", "🍐",
  "Late Summer (July - Sept)", "Himachal Pradesh, Punjab, Kashmir, Nilgiris",
  "Crisp, sweet, gritty-textured fruit available as crisp stone-hard Desi Nashpati and melting soft European Babugosha.",
  "12°C - 26°C", "800 - 1,000 mm.", "Deep clay loam.",
  [{"stage": "Bloom", "days": "March", "description": "White flowers."},
   {"stage": "Harvest", "days": "July - Sept", "description": "Harvested mature green."}],
  [{"name": "Fire Blight (Erwinia amylovora)", "symptoms": "Blackened scorched shoots (shepherd's crook).", "riskPeriod": "Warm wet spring."}],
  ["Pear Psylla"], ["Prune blighted twigs 30 cm below infection mark."])

c("date-palm", "Date Palm (Khajur)", "खजूर (Date Palm)", "Phoenix dactylifera", "Fruits & Horticulture", "🌴",
  "Summer Harvest", "Kutch (Gujarat), Rajasthan desert belts, arid Maharashtra",
  "Desert king tree: 'feet in water and head in fire'. High energy sweet dates harvested fresh (Khelal) or soft dried.",
  "28°C - 42°C (intense heat with zero rain during ripening)", "Micro-irrigation.", "Sandy desert soils, highly salt tolerant.",
  [{"stage": "Pollination", "days": "Feb - March", "description": "Manual pollination of female spadix."},
   {"stage": "Khelal / Doka Harvest", "days": "June - July", "description": "Crisp yellow/red dates harvested before monsoon."}],
  [{"name": "Graphiola Leaf Spot", "symptoms": "Hard black pustules on fronds.", "riskPeriod": "Humid air."}],
  ["Red Palm Weevil", "Rhinoceros Beetle"], ["Use tissue-cultured Barhee or Medjool varieties."])

c("star-fruit-kamrakh", "Star Fruit (Carambola / Kamrakh)", "कमरख / करंबोल (Kamrakh)", "Averrhoa carambola", "Fruits & Horticulture", "⭐",
  "Winter & Summer", "Konkan, Western Ghats, South India",
  "Five-angled translucent green-yellow fruit that reveals perfect star slices when cross-cut; crisp, tart-sweet and refreshing.",
  "22°C - 32°C", "1,200 mm.", "Moist loamy soil.",
  [{"stage": "Bloom", "days": "Lilac flowers", "description": "Clusters on branches."},
   {"stage": "Harvest", "days": "3-4 flushes", "description": "Turn glossy amber-yellow."}],
  [{"name": "Anthracnose", "symptoms": "Brown specks.", "riskPeriod": "Rains."}],
  ["Fruit Fly"], ["Grow Arkin sweet variety."])

print(f"Stage 4 loaded. Total now: {len(crops)}")

with open('scripts/crops_stage4.json', 'w', encoding='utf-8') as f:
    json.dump(crops, f, ensure_ascii=False, indent=2)
