#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Appends Spices, Floriculture, Medicinal, and Plantation crops.
Outputs the complete master database directly into /src/data/cropsDatabase.ts
"""

import json
import os

with open('scripts/crops_stage5.json', 'r', encoding='utf-8') as f:
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
# 7. SPICES & CONDIMENTS (24 crops)
# ==========================================
c("sangli-turmeric", "Turmeric (Sangli Rajapuri)", "सांगली राजापुरी हळद (Sangli Halad)", "Curcuma longa", "Spices & Condiments", "🟡",
  "8-9 Months Crop", "Sangli (Turmeric City of India holding GI status), Satara, Kolhapur, Hingoli, Nanded",
  "The sacred golden spice of Maharashtra holding GI status. High curcumin content (3.5 - 5%), vibrant saffron-orange color, medicinal antioxidant power, and long rhizome fingers.",
  "20°C - 32°C (warm humid climate)", "1,200 - 1,400 mm through drip; raised beds mandatory.",
  "Well-drained rich friable clay loam or medium black soil with high organic matter, pH 6.0 - 7.5.",
  [{"stage": "Sprouting", "days": "Days 1-40", "description": "Mother finger rhizomes planted on broad beds; sprouts emerge."},
   {"stage": "Tillering & Foliage", "days": "Days 41-120", "description": "Vigorous broad lanceolate green leaves expand."},
   {"stage": "Rhizome Bulking", "days": "Days 121-210", "description": "Fingers swell accumulating curcumin and essential oils."},
   {"stage": "Harvest & Curing", "days": "Days 211-260", "description": "Leaves yellow and dry completely; rhizomes boiled in perforated pans and sun-cured."}],
  [{"name": "Rhizome Rot (Pythium aphanidermatum)", "symptoms": "Collar region turns soft and water-soaked; foul-smelling rhizome decay.", "riskPeriod": "Water stagnation during heavy monsoon."},
   {"name": "Leaf Blotch (Taphrina maculans)", "symptoms": "Small yellow spots turning into dirty brown patches on both leaf surfaces.", "riskPeriod": "Humid overcast days."}],
  ["Shoot Borer", "Rhizome Scale", "Thrips"],
  ["Plant on broad bed furrows (BBF) to ensure perfect drainage.",
   "Drench with Trichoderma harzianum @ 5g/L at planting and after 60 days.",
   "Use premier varieties: Rajapuri, Phule Swarupa, Salem, or IISR Pratibha."])

c("black-pepper", "Black Pepper (King of Spices)", "काळी मिरी (Kali Miri)", "Piper nigrum", "Spices & Condiments", "⚫",
  "Perennial Woody Vine", "Konkan Coast (Sindhudurg, Ratnagiri), Western Ghats, Kerala, Karnataka",
  "The ancient black gold of India. High-value climbing vine trained on silver oak or areca nut trunks, producing pungent piperine-rich berry spikes.",
  "22°C - 32°C (warm humid tropical rainforest climate)", "2,000 - 3,000 mm.", "Humus-rich acidic red lateritic soils, pH 5.5 - 6.5.",
  [{"stage": "Trailing on Standards", "days": "Years 1-3", "description": "Vines tied to live tree standards with coir rope."},
   {"stage": "Spike Flowering", "days": "June - July", "description": "Pendulous spikes emerge with monsoon rains."},
   {"stage": "Berry Maturation & Harvest", "days": "Dec - March", "description": "Spikes harvested when 1-2 berries turn bright orange-red; sun-dried into black wrinkled pepper."}],
  [{"name": "Quick Wilt / Foot Rot (Phytophthora capsici)", "symptoms": "Sudden blackening of leaves, collar rot, and rapid vine death within 10-14 days.", "riskPeriod": "Heavy continuous southwest monsoon rains."},
   {"name": "Pollu Disease / Anthracnose", "symptoms": "Hollow diseased berries that crumble upon touch.", "riskPeriod": "Cloudy wet spells."}],
  ["Pollu Beetle", "Top Shoot Borer", "Scale Insects"],
  ["Drench base of standards with 1% Bordeaux mixture or Metalaxyl before monsoon onset.",
   "Use renowned high-yielding varieties: Panniyur-1, Panniyur-5, or Subhakara."])

c("green-cardamom", "Green Cardamom (Queen of Spices)", "वेलची / छोटी वेलची (Velchi / Elaichi)", "Elettaria cardamomum", "Spices & Condiments", "🟢",
  "Perennial Evergreen", "Western Ghats cloud forests, Kerala, Karnataka, cool Konkan hilltops",
  "One of the world's most precious aromatic spices. Shade-loving perennial clump yielding triangular green capsules packed with cineole-rich seeds.",
  "15°C - 26°C (cool humid mountain mist)", "1,500 - 2,500 mm.", "Rich forest loam with thick leaf mulch, pH 5.0 - 6.0.",
  [{"stage": "Tillering Clump", "days": "Years 1-2", "description": "Clump produces 15-20 leafy pseudostems."},
   {"stage": "Panicle Emergence", "days": "Annual", "description": "Horizontal or erect flower panicles emerge from base."},
   {"stage": "Capsule Harvest", "days": "Every 20-30 days (Aug-Feb)", "description": "Plump green capsules handpicked and cured in flue pipe curing kilns."}],
  [{"name": "Katte Disease / Mosaic Virus", "symptoms": "Mottled yellow streaks on leaves, stunted pseudostems; banana aphid vector.", "riskPeriod": "Vector activity."},
   {"name": "Azhukal / Capsule Rot (Phytophthora)", "symptoms": "Water-soaked rotting of capsules.", "riskPeriod": "Continuous monsoon mist."}],
  ["Cardamom Thrips (Sciothrips cardamomi)", "Shoot Borer", "Whitefly"],
  ["Maintain 50% evergreen tree shade canopy in plantation.",
   "Spray systemic fungicides before monsoon and cure capsules immediately to retain vibrant green color."])

c("large-cardamom", "Large Cardamom (Badi Elaichi)", "बडी वेलची / मसाला वेलची (Badi Elaichi)", "Amomum subulatum", "Spices & Condiments", "🟤",
  "Perennial Mountain Herb", "Sikkim, Darjeeling, Northeast India",
  "Large dark reddish-brown ribbed capsules with deep camphoraceous smoky aroma, essential in Indian garam masala and biryani.",
  "10°C - 22°C (cool temperate misty mountains)", "2,000 - 3,500 mm.", "Moist forest loam rich in organic leaf mould.",
  [{"stage": "Vegetative Clump", "days": "Years 1-3", "description": "Robust clumps reach 2-3 meters."},
   {"stage": "Basal Flowering", "days": "April - May", "description": "Globose floral heads at ground level."},
   {"stage": "Harvest & Bhatti Curing", "days": "Sept - Nov", "description": "Capsules harvested and cured over slow woodsmoke bhattis."}],
  [{"name": "Chirke Virus", "symptoms": "Mosaic streaks on leaves; aphid vector.", "riskPeriod": "Spring."},
   {"name": "Foorkey Virus", "symptoms": "Bushy stunted shoots.", "riskPeriod": "Aphid vector."}],
  ["Stem Borer"], ["Rogue out viral clumps and maintain organic agroforestry."])

c("clove", "Clove (Lavang)", "लवंग (Lavang)", "Syzygium aromaticum", "Spices & Condiments", "🟤",
  "Perennial Evergreen Tree", "Western Ghats, Coastal Konkan trials, Tamil Nadu, Kerala",
  "Aromatic unopened floral buds rich in therapeutic eugenol oil, harvested for dental pain relief, oral health, and spice blends.",
  "20°C - 30°C", "1,500 - 2,500 mm.", "Rich lateritic and clay loam.",
  [{"stage": "Tree Maturation", "days": "Years 1-7", "description": "Conical evergreen tree."},
   {"stage": "Bud Emergence", "days": "Sept - Oct", "description": "Terminal clusters of buds develop."},
   {"stage": "Harvest", "days": "Dec - Feb", "description": "Harvested by hand when buds turn from green to delicate pink before opening."}],
  [{"name": "Dieback", "symptoms": "Twig drying.", "riskPeriod": "Monsoon."}],
  ["Scale Insects"], ["Dry harvested buds on clean mats in sun until dark brown."])

c("cinnamon-dalchini", "Cinnamon (Dalchini)", "दालचिनी (Dalchini)", "Cinnamomum verum", "Spices & Condiments", "🪵",
  "Perennial Tree", "Konkan Coast (Sindhudurg, Ratnagiri), Western Ghats, Kerala",
  "Fragrant inner tree bark containing cinnamaldehyde, harvested by coppicing and hand-peeling into tight golden-brown quills.",
  "22°C - 32°C", "1,500 - 2,500 mm.", "Sandy loam with organic compost.",
  [{"stage": "Coppicing", "days": "Years 2-3", "description": "Stems cut back to ground to stimulate straight pencil-thick shoots."},
   {"stage": "Bark Peeling", "days": "Monsoon", "description": "Outer rough bark scraped off; sweet inner bark peeled and rolled into telescoping quills."}],
  [{"name": "Leaf Blight", "symptoms": "Necrotic leaf patches.", "riskPeriod": "Rains."}],
  ["Cinnamon Butterfly Caterpillar"], ["Use high-oil varieties like Navashree or Nithyashree."])

c("nutmeg-mace", "Nutmeg & Mace (Jaiphal & Jaipatri)", "जायफळ व जायपत्री (Jaiphal / Jaipatri)", "Myristica fragrans", "Fruits & Horticulture", "🌰",
  "Perennial Tree (Bearing from Year 7)", "Konkan (Sindhudurg, Ratnagiri), Western Ghats, Kerala",
  "Unique double-spice tree: yields aromatic seed (Nutmeg / जायफळ) surrounded by brilliant crimson lacy aril (Mace / जायपत्री).",
  "22°C - 32°C", "1,500 - 2,500 mm.", "Deep moist fertile clay loam.",
  [{"stage": "Dioecious Tree", "days": "Years 1-7", "description": "Grafted bisexual or female trees planted."},
   {"stage": "Fruit Dehiscence", "days": "June - Sept", "description": "Yellow peach-like fruit splits on tree exposing scarlet mace and black shell."}],
  [{"name": "Fruit Rot", "symptoms": "Immature fruit drop.", "riskPeriod": "Monsoon."}],
  ["Scale Insects"], ["Separate mace carefully from nutmeg shell and dry into golden-amber blades."])

c("cumin-jeera", "Cumin (Jeera)", "जिरे (Jeera)", "Cuminum cyminum", "Spices & Condiments", "🌾",
  "Rabi (Winter)", "Gujarat, Rajasthan, North Maharashtra border tracts",
  "Highly sensitive aromatic winter spice with distinct warm earthy cumin aldehyde flavor, essential for Indian cooking.",
  "12°C - 24°C (cool winter with completely dry sunny weather during seed formation; cloudy wet weather is fatal)",
  "200 - 300 mm; 3-4 light irrigations; stop watering at grain fill.", "Well-drained sandy loam with good organic matter, pH 6.8 - 7.8.",
  [{"stage": "Emergence", "days": "Days 1-15", "description": "Slow germination of tiny seeds."},
   {"stage": "Vegetative & Flowering", "days": "Days 16-60", "description": "Delicate feathery canopy; small pinkish-white umbels bloom."},
   {"stage": "Seed Filling & Harvest", "days": "Days 61-100", "description": "Aromatic ribbed mericarps turn greyish-brown; hand-pulled early morning."}],
  [{"name": "Cumin Blight (Alternaria burnsii)", "symptoms": "Dark brown necrotic spots on leaves and stems causing entire plants to blacken and wither overnight.", "riskPeriod": "Cloudy, damp, or drizzling weather during flowering stage."},
   {"name": "Powdery Mildew (Erysiphe heraclei)", "symptoms": "White powdery coating covering umbels.", "riskPeriod": "Warm dry days and cool dewy nights."},
   {"name": "Fusarium Wilt", "symptoms": "Sudden drooping of foliage.", "riskPeriod": "Damp warm soils."}],
  ["Cumin Aphids (Myzus persicae)"],
  ["Spray Mancozeb @ 2.5g/L immediately upon overcast sky warning to prevent catastrophic cumin blight.",
   "Use certified wilt-resistant varieties: GC-4, RZ-209, or RZ-223."])

c("fennel-saunf", "Fennel (Saunf / Badishep)", "बडीशेप / सोप (Badishep / Saunf)", "Foeniculum vulgare", "Spices & Condiments", "🌿",
  "Rabi (Winter)", "North Maharashtra, Gujarat, Rajasthan",
  "Sweet aromatic umbelliferous spice yielding crunchy anethole-rich seeds consumed as digestive mukhwas and culinary seasoning.",
  "15°C - 26°C", "350 - 450 mm.", "Deep fertile loam or black cotton soil.",
  [{"stage": "Vegetative", "days": "Days 1-60", "description": "Dense aromatic feathery foliage."},
   {"stage": "Umbel Flowering", "days": "Days 61-110", "description": "Compound flat golden-yellow umbels bloom."},
   {"stage": "Harvesting", "days": "Days 111-150", "description": "Harvested green for sweet chewing saunf (Lucknowi saunf) or dry golden."}],
  [{"name": "Ramularia Blight", "symptoms": "Brown spots on umbels.", "riskPeriod": "Cloudy winter."},
   {"name": "Powdery Mildew", "symptoms": "White coating.", "riskPeriod": "Dewy mornings."}],
  ["Aphids", "Thrips"], ["Spray Wettable Sulfur @ 2g/L.", "Use Gujarat Fennel-11 or RF-125."])

c("fenugreek-seeds", "Fenugreek Seeds (Methi Dana)", "मेथी दाणे (Methi Dana)", "Trigonella foenum-graecum (Seed)", "Spices & Condiments", "🫘",
  "Rabi", "Marathwada, Western Maharashtra, Rajasthan",
  "Golden-yellow rhombic seeds with characteristic bitter-aromatic taste, renowned for reducing blood sugar and cholesterol.",
  "15°C - 24°C", "300 mm.", "Loamy soil.",
  [{"stage": "Pod Maturity", "days": "Days 60-90", "description": "Beaked pods turn straw-yellow."},
   {"stage": "Harvest", "days": "Days 90-105", "description": "Threshed for hard aromatic seeds."}],
  [{"name": "Downy Mildew", "symptoms": "Yellow leaf patches.", "riskPeriod": "Dew."}],
  ["Aphids"], ["Use Pusa Early Bunching or RMt-1."])

c("coriander-seeds-dhana", "Coriander Seeds (Dhana)", "धने / सुका धना (Dhana)", "Coriandrum sativum (Seed)", "Spices & Condiments", "🌾",
  "Rabi", "Marathwada, Vidarbha, Western Maharashtra, MP",
  "Round ribbed aromatic mericarps ground into essential curry powders and roasted for digestive dhana-dal.",
  "15°C - 25°C", "300 - 400 mm.", "Medium to deep black soils.",
  [{"stage": "Umbel Flowering", "days": "Days 45-75", "description": "White/pinkish umbels."},
   {"stage": "Seed Ripening", "days": "Days 76-110", "description": "Globular fruits turn light brown."}],
  [{"name": "Powdery Mildew", "symptoms": "White powder on umbels.", "riskPeriod": "Dry spells."}],
  ["Aphids"], ["Use grain varieties: Sadhana, Swati, or Hisar Anand."])

c("ajwain-carom", "Ajwain (Carom / Owa)", "ओवा (Owa / Ajwain)", "Trachyspermum ammi", "Spices & Condiments", "🌿",
  "Rabi", "Marathwada, Solapur, Ahmednagar, Gujarat",
  "Tiny greyish-brown ribbed seeds packed with powerful antiseptic thymol oil, renowned for soothing digestive gas, colic, and cough.",
  "15°C - 26°C", "250 - 350 mm.", "Black cotton soil.",
  [{"stage": "Foliage", "days": "Days 1-50", "description": "Feathery aromatic foliage."},
   {"stage": "Umbel Flowering", "days": "Days 51-95", "description": "White compound umbels."},
   {"stage": "Harvest", "days": "Days 96-135", "description": "Umbels harvested when seeds turn brown."}],
  [{"name": "Root Rot", "symptoms": "Wilting.", "riskPeriod": "Excess watering."}],
  ["Aphids"], ["Use Gujarat Ajwain-1, Lam Selection-1."])

c("kalonji-nigella", "Kalonji (Nigella / Black Seed)", "कलोंजी / काळे जिरे (Kalonji)", "Nigella sativa", "Spices & Condiments", "⚫",
  "Rabi", "North Maharashtra, MP, Rajasthan",
  "Sacred triangular matte-black seeds rich in thymoquinone; traditional cure for respiratory wellness and naan bread topping.",
  "14°C - 24°C", "250 - 350 mm.", "Well-drained loam.",
  [{"stage": "Sky-Blue Blossom", "days": "Days 40-70", "description": "Delicate starry blue flowers."},
   {"stage": "Capsule Harvest", "days": "Days 71-110", "description": "Inflated horned capsules yield jet black seeds."}],
  [{"name": "Damping Off", "symptoms": "Seedling decay.", "riskPeriod": "Damp soil."}],
  ["Aphids"], ["Use Azad Kalonji, Pant Krishna."])

c("star-anise", "Star Anise (Chakraphul)", "चक्रफूल (Chakraphul)", "Illicium verum", "Spices & Condiments", "⭐",
  "Perennial Tree", "Northeast India (Arunachal Pradesh), humid Western Ghat trails",
  "Star-shaped woody pericarps containing sweet licorice-like anethole oil, prized in biryanis and Chinese five-spice.",
  "15°C - 26°C", "1,500 - 2,500 mm.", "Acidic rich mountain loams.",
  [{"stage": "Flowering", "days": "March - May", "description": "Yellow-green blossoms."},
   {"stage": "Star Harvest", "days": "Sept - Oct", "description": "Green 8-pointed star fruits harvested and sun-dried."}],
  [{"name": "Leaf Spot", "symptoms": "Brown specks.", "riskPeriod": "Rain."}],
  ["Wood Borers"], ["Air-dry carefully to preserve whole star symmetry."])

c("asafoetida-hing", "Asafoetida (Hing)", "हिंग (Hing)", "Ferula foetida", "Spices & Condiments", "🪵",
  "Cold Desert Perennial", "Ladakh, Lahaul-Spiti (Himachal Pradesh trials by CSIR)",
  "Pungent oleo-gum-resin tapped from massive taproots of wild giant umbelliferous desert fennel, essential for Indian dal tempering.",
  " -5°C to 20°C (extreme cold desert with snow cover)", "Low rainfall; arid mountains.", "Dry sandy scree slopes.",
  [{"stage": "Massive Taproot", "days": "Years 1-4", "description": "Carrot-like fleshy root accumulates resin."},
   {"stage": "Root Incision & Tapping", "days": "Year 5", "description": "Root crown sliced; white milky gum exudes and dries."}],
  [{"name": "Root Rot", "symptoms": "Tuber decay in wet soil.", "riskPeriod": "Rain."}],
  ["Soil Grubs"], ["India's premier import-substitution trial crop in cold Himalayas."])

c("bay-leaf-tejpatta", "Indian Bay Leaf (Tejpatta)", "तेजपत्ता / तमालपत्र (Tejpatta)", "Cinnamomum tamala", "Spices & Condiments", "🍃",
  "Perennial Tree", "Sub-Himalayan hills, Western Ghats, Konkan",
  "Aromatic evergreen tree leaves with three prominent longitudinal veins and warm clove-cinnamon fragrance.",
  "15°C - 28°C", "1,500 mm.", "Mountain soils.",
  [{"stage": "Leaf Harvest", "days": "Annual from Year 5", "description": "Leaves harvested and shade-cured into olive-brown dry leaves."}],
  [{"name": "Leaf Blotch", "symptoms": "Brown patches.", "riskPeriod": "Humid."}],
  ["Caterpillar"], ["Shade-dry leaves to retain volatile oils."])

c("dry-ginger-sonth", "Dry Ginger (Sonth)", "सुंठ (Sonth)", "Zingiber officinale (Cured)", "Spices & Condiments", "🫚",
  "Post-harvest cured", "Satara (Wai), Sangli, Kerala",
  "Peeled, bleached and sun-dried ginger rhizomes yielding concentrated pungent shogaol and zingerone for Ayurvedic remedies and chai masala.",
  "22°C - 32°C", "Post-harvest process.", "Loamy soils.",
  [{"stage": "Harvest & Peeling", "days": "Month 9", "description": "Epidermal skin scraped with bamboo splints."},
   {"stage": "Sun Bleaching & Drying", "days": "8-10 days", "description": "Limed and sun-dried until moisture drops below 10%."}],
  [{"name": "Storage Mold", "symptoms": "White fungus.", "riskPeriod": "Damp storage."}],
  ["Cigarette Beetle"], ["Store with dried neem leaves in moisture-proof containers."])

c("dry-mango-amchur", "Dry Mango Powder (Amchur)", "आमचूर (Amchur)", "Mangifera indica (Green)", "Spices & Condiments", "🥭",
  "Summer Process", "Central India, Maharashtra, UP",
  "Unripened green tart mangoes peeled, sliced, and sun-dried into tangy amchur slices or fine culinary powder.",
  "Summer sun-drying", "N/A", "N/A",
  [{"stage": "Green Fruit Picking", "days": "April", "description": "Sour raw mangoes gathered."},
   {"stage": "Slicing & Sun Drying", "days": "5-7 days", "description": "Sliced and sun-dried crisp on clean mats."}],
  [{"name": "Fungal Blackening", "symptoms": "Mold if rain hits.", "riskPeriod": "Cloudy days."}],
  ["Storage Moths"], ["Ensure bone-dry moisture before pulverizing."])

c("kashmiri-saffron", "Kashmiri Saffron (Kesar)", "केशर (Kashmiri Kesar)", "Crocus sativus", "Spices & Condiments", "🪻",
  "Autumn Bloom (Oct - Nov)", "Pampore (Saffron Bowl of Kashmir holding GI status)",
  "World's most expensive spice holding GI status. Purple-flowered autumn crocus yielding three intense scarlet stigmas rich in crocin, picrocrocin, and safranal.",
  " -10°C to 20°C (cool temperate with snow in winter)", "Rainfed Karewa terraces.", "Deep well-drained calcareous Karewa silt loam, pH 6.8 - 7.8.",
  [{"stage": "Corm Planting", "days": "August - Sept", "description": "Globose corms planted in raised beds."},
   {"stage": "Autumn Bloom Flush", "days": "Oct - Nov", "description": "Lilac-purple flowers burst open at dawn for 15-20 days."},
   {"stage": "Stigma Plucking & Drying", "days": "Daily harvest", "description": "Three blood-red stigmas carefully separated by hand and shade-dried."}],
  [{"name": "Corm Rot (Fusarium oxysporum & Rhizoctonia)", "symptoms": "Sunken brown rot lesions on corms causing yellowing of leaves.", "riskPeriod": "Poorly drained Karewa soil."},
   {"name": "Leaf Blight", "symptoms": "Tip drying.", "riskPeriod": "Humid fog."}],
  ["Corm Mites", "Rodents / Voles"],
  ["Treat corms in Carbendazim @ 2g/L before planting in August.",
   "Install solar dryers for rapid, hygienic saffron stigma desiccation."])

c("allspice-jamaica", "Allspice (Sarva Masala)", "सर्वमसाला (Allspice)", "Pimenta dioica", "Spices & Condiments", "🌿",
  "Perennial Tree", "Western Ghats, Konkan, South India",
  "Miracle spice foliage and berries combining the combined aromas of cinnamon, nutmeg, clove, and black pepper.",
  "20°C - 30°C", "1,500 mm.", "Moist rich loam.",
  [{"stage": "Berry Harvest", "days": "July - Aug", "description": "Green berries picked and sun-dried brown."}],
  [{"name": "Rust", "symptoms": "Leaf spots.", "riskPeriod": "Rains."}],
  ["Caterpillar"], ["Prune to maintain compact harvesting canopy."])

c("vanilla", "Vanilla", "व्हॅनिला (Natural Vanilla)", "Vanilla planifolia", "Spices & Condiments", "🍦",
  "Perennial Climbing Orchid", "Western Ghats shade plantations (Kerala, Karnataka, Konkan)",
  "Exotic climbing orchid producing long aromatic green pods that undergo months of sweating and curing to develop natural vanillin.",
  "22°C - 30°C", "2,000 - 2,500 mm; high humidity.", "Rich organic forest humus.",
  [{"stage": "Vine Training", "days": "Years 1-3", "description": "Trained on live shade trees."},
   {"stage": "Hand Pollination", "days": "Dec - March", "description": "Flowers open for half a day; hand-pollinated with bamboo needle."},
   {"stage": "Pod Harvest & Curing", "days": "Months 7-9 after bloom", "description": "Green pods scalded in hot water and sweated in wool blankets for vanillin crystal formation."}],
  [{"name": "Root & Stem Rot (Fusarium oxysporum f. sp. vanillae)", "symptoms": "Flaccid yellowing of vines and brown water-soaked root death.", "riskPeriod": "Excess rain."}],
  ["Snails", "Grasshoppers"], ["Maintain clean organic leaf mulch and prevent water stagnation."])

c("poppy-seeds-khuskhus", "Poppy Seed (Khuskhus)", "खसखस (Khuskhus)", "Papaver somniferum", "Spices & Condiments", "⚪",
  "Rabi", "Regulated farming tracts in MP, Rajasthan, UP",
  "Tiny creamy-white kidney seeds harvested from mature seed capsules, used for Mughlai gravies, desserts, and soothing sleep.",
  "12°C - 24°C", "350 mm.", "Deep fertile alluvial loam.",
  [{"stage": "Rosette to Bloom", "days": "Days 1-70", "description": "Showy white papery flowers."},
   {"stage": "Capsule Maturity", "days": "Days 71-110", "description": "Hard capsules dry; seeds harvested."}],
  [{"name": "Downy Mildew", "symptoms": "Leaf chlorosis.", "riskPeriod": "Foggy winter."}],
  ["Aphids"], ["Cultivated strictly under Central Narcotics Bureau licensing."])

# ==========================================
# 8. FLORICULTURE & CUT FLOWERS (16 crops)
# ==========================================
c("marigold-zendu", "Marigold (Zendu)", "झेंडू (Zendu / Genda)", "Tagetes erecta", "Floriculture & Flowers", "🏵️",
  "Kharif (Dussehra/Diwali peak), Rabi & Summer", "Pune, Nashik, Ahmednagar, Satara, Solapur",
  "The golden auspicious flower of Maharashtra. Brilliant yellow and orange globose heads used for festive torans, temple offerings, and lutein extraction.",
  "18°C - 30°C", "350 - 450 mm.", "Well-drained loam to clay loam, pH 6.5 - 7.5.",
  [{"stage": "Transplanting & Pinching", "days": "Days 1-30", "description": "Apical bud pinched at 30 days to induce bushy branching and 40-50 blooms per plant."},
   {"stage": "Bud Emergence", "days": "Days 31-50", "description": "Buttons swell at all terminal branch tips."},
   {"stage": "Full Bloom & Plucking", "days": "Days 51-90", "description": "Dense double-petal flowers picked in early mornings for festive markets."}],
  [{"name": "Alternaria Leaf Spot & Flower Blight", "symptoms": "Brown necrotic spots on leaves and petal browning.", "riskPeriod": "Cloudy wet monsoon days."},
   {"name": "Collar Rot (Phytophthora)", "symptoms": "Rotting at ground level.", "riskPeriod": "Waterlogged soil."}],
  ["Red Spider Mites", "Gram Pod Borer (feeding on flower buds)", "Thrips"],
  ["Adopt apical bud pinching at 30 days to double flower yield.",
   "Plant famous hybrids: Maxima Yellow, Pusa Narangi, Pusa Basanti, or Calcutta Orange.",
   "Spray Mancozeb @ 2.5g/L for leaf and flower blight."])

c("french-marigold", "French Marigold (Chhota Zendu)", "छोटा झेंडू / जाफरी झेंडू (French Marigold)", "Tagetes patula", "Floriculture & Flowers", "🏵️",
  "Winter", "Pune, Nashik, urban nurseries",
  "Compact dwarf bushes smothered in bicolour maroon-gold ruffled blossoms; natural nematicide root exudate suppresses root-knot nematodes.",
  "15°C - 26°C", "300 mm.", "Light loam.",
  [{"stage": "Flowering", "days": "Days 35-70", "description": "Smothered in bicolour blooms."}],
  [{"name": "Leaf Blight", "symptoms": "Browning.", "riskPeriod": "Dew."}],
  ["Thrips"], ["Intercrop with tomato or solanaceous crops to kill soil nematodes."])

c("dutch-rose", "Dutch Rose (Cut Flower)", "डच गुलाब (Polyhouse Dutch Rose)", "Rosa hybrida", "Floriculture & Flowers", "🌹",
  "Year-round (Climate Controlled Polyhouse)", "Pune (Talegaon Dabhade is India's Floriculture SEZ Capital), Nashik, Satara",
  "Long-stemmed premium greenhouse cut roses in vibrant red (Top Secret), yellow, white, and peach exported globally for Valentine's Day.",
  "15°C - 26°C (greenhouse cooling pads and misting)", "Drip fertigation with automated EC and pH control.", "Soil or soilless cocopeat / rockwool media, pH 5.5 - 6.5.",
  [{"stage": "Budding on Multiflora Rootstock", "days": "Months 1-3", "description": "Mother plant framework established."},
   {"stage": "Bending & Shoot Induction", "days": "Months 4-6", "description": "Weak shoots bent downward to form photosynthetic lung; stout flower canes emerge."},
   {"stage": "Bud Maturation & Harvesting", "days": "Every 45 days", "description": "Buds harvested at tight color break stage; graded into 40-70 cm stems."}],
  [{"name": "Powdery Mildew (Podosphaera pannosa)", "symptoms": "White powdery talc coating on young shoots, curling leaves and bud distortion.", "riskPeriod": "High humidity inside polyhouse with cool nights (15-20°C)."},
   {"name": "Black Spot (Diplocarpon rosae)", "symptoms": "Circular black spots with fringed margins on leaves causing severe defoliation.", "riskPeriod": "Water droplets on leaves."},
   {"name": "Downy Mildew (Peronospora sparsa)", "symptoms": "Purplish-red angular blotches causing rapid leaf drop.", "riskPeriod": "Cool wet overcast weather."}],
  ["Rose Thrips (Frankliniella occidentalis)", "Red Spider Mite (Tetranychus urticae)", "Aphids", "Caterpillars"],
  ["Burn sulfur in greenhouse sulfur vaporizers at night to prevent powdery mildew spores.",
   "Release predatory mites (Neoseiulus californicus) to control two-spotted red spider mites.",
   "Pulse harvested cut stems in silver thiosulfate (STS) solution to prolong vase life to 14 days."])

c("desi-rose", "Desi Fragrant Rose (Gulab)", "गुलाब / गावरान गुलाब (Desi Gulab)", "Rosa damascena / R. bourboniana", "Floriculture & Flowers", "🌹",
  "Year-round (Winter peak)", "Pune, Alandi, Ahmednagar, Nashik, Haldighati (Rajasthan)",
  "Deeply fragrant damask and desi pink roses cultivated for pure rose water (gulab jal), sweet gulkand, and essential rose otto attar.",
  "16°C - 30°C", "500 - 650 mm.", "Medium black clay to loam.",
  [{"stage": "Winter Pruning", "days": "Oct", "description": "Canes pruned back; root exposed for 3 days."},
   {"stage": "Heavy Bloom Flush", "days": "Nov - March", "description": "Daily harvest of intensely fragrant pink roses at dawn."}],
  [{"name": "Dieback", "symptoms": "Shoots dry downwards from pruned cut.", "riskPeriod": "Post-pruning dampness."}],
  ["Thrips", "Chafer Beetle"], ["Paint pruned cane tips with copper oxychloride paste to prevent dieback."])

c("jasmine-mogra", "Jasmine (Mogra / Arabian Jasmine)", "मोगरा / मल्लिका (Mogra)", "Jasminum sambac", "Floriculture & Flowers", "🌼",
  "Summer (March to July)", "Vasai, Palghar, Thane, Pune, Solapur, Madurai",
  "The fragrant queen of Indian flowers. Snow-white buds woven into traditional hair garlands (gajras) and extracted for exotic perfumery.",
  "22°C - 34°C (warm tropical climate with high light)", "600 - 800 mm; defoliation and water stress in January.", "Well-drained sandy loam or clay loam, pH 6.5 - 7.5.",
  [{"stage": "Annual Pruning & Defoliation", "days": "Jan", "description": "Pruned to 50 cm; leaves stripped to trigger uniform synchronous bud flush."},
   {"stage": "First Watering & Bloom", "days": "Feb - March", "description": "Heavy watering and organic manure awaken white buds."},
   {"stage": "Daily Morning Plucking", "days": "March - July", "description": "Firm white unopened buds plucked before dawn."}],
  [{"name": "Leaf Blight (Alternaria)", "symptoms": "Brown leaf margins.", "riskPeriod": "Rain."}],
  ["Jasmine Budworm (Hendecasis duplifascialis)", "Jasmine Gallery Worm", "White Mite"],
  ["Spray Chlorantraniliprole 18.5 SC @ 3ml/10L for budworm control.",
   "Use famous varieties: Motia, Bela, or Arka Arpan."])

c("chrysanthemum-shewanti", "Chrysanthemum (Shewanti)", "शेवंती (Shewanti)", "Chrysanthemum morifolium", "Floriculture & Flowers", "🌼",
  "Autumn & Winter (Diwali peak)", "Western Maharashtra (Pune, Ahmednagar, Solapur, Satara)",
  "Beloved festive winter flower of Maharashtra available in sunny yellow, pristine white, and purple button heads for garland making.",
  "16°C - 26°C", "350 - 450 mm.", "Rich fertile loam with great aeration.",
  [{"stage": "Sucker / Cutting Planting", "days": "June - July", "description": "Rooted terminal cuttings established."},
   {"stage": "Pinching", "days": "Aug", "description": "Pinched at 4 weeks to induce lateral flower shoots."},
   {"stage": "Flowering & Harvest", "days": "Oct - Dec", "description": "Continuous harvest for Diwali and wedding decor."}],
  [{"name": "Septoria Leaf Spot", "symptoms": "Dark brown spots starting from lower leaves.", "riskPeriod": "Rainy humidity."},
   {"name": "Wilt", "symptoms": "Drooping stems.", "riskPeriod": "Damp soil."}],
  ["Aphids", "Thrips"], ["Use local varieties: Baggi, Raja, Sonali Tara, or Shobha."])

c("tuberose-nishigandha", "Tuberose (Gulchhadi / Nishigandha)", "गुलछडी / निशिगंध (Nishigandha)", "Polianthes tuberosa", "Floriculture & Flowers", "🌸",
  "Year-round bearing (Peak monsoon & winter)", "Pune, Nashik, Thane, Sangli, Satara, Kolhapur",
  "Enchanting night-blooming tuberous flower producing pure white florets with heavenly sweet perfume. Used for garlands and single cut flower spikes.",
  "20°C - 32°C", "600 - 800 mm.", "Well-drained fertile sandy loam to clay loam, pH 6.5 - 7.5.",
  [{"stage": "Bulb Planting", "days": "March - April", "description": "Treated bulbs (2-3 cm diameter) planted on ridges."},
   {"stage": "Spike Emergence", "days": "Months 3-4", "description": "Erect spike reaches 70-100 cm bearing 20-30 florets."},
   {"stage": "Harvesting", "days": "Months 4-24 (ratoon)", "description": "Single type plucked daily; Double type cut as whole spike."}],
  [{"name": "Stem Rot / Sclerotial Wilt (Sclerotium rolfsii)", "symptoms": "Rotting at collar region with white cottony mycelium and mustard-like sclerotia.", "riskPeriod": "Monsoon water stagnation."},
   {"name": "Leaf Blight", "symptoms": "Browning of leaf tips.", "riskPeriod": "Rains."}],
  ["Root Knot Nematode (Meloidogyne incognita)", "Thrips", "Aphids"],
  ["Drench soil with Paecilomyces lilacinus to eradicate damaging root-knot nematodes.",
   "Use university varieties: Phule Rajani, Prajwal, Shringar, or Vaibhav."])

c("gerbera", "Gerbera (Transvaal Daisy)", "जरबेरा (Polyhouse Gerbera)", "Gerbera jamesonii", "Floriculture & Flowers", "🌸",
  "Year-round (Polyhouse)", "Pune, Nashik, Kolhapur, Satara",
  "Vibrant, daisy-like cut flower in red, yellow, orange, and pink, cultivated on raised gravelly beds inside polyhouses.",
  "18°C - 25°C", "Micro-drip; crown must stay dry.", "Porous soil with cocopeat and sand, pH 5.5 - 6.5.",
  [{"stage": "Planting", "days": "Month 1", "description": "Crown kept 1 cm above soil surface."},
   {"stage": "Flower Harvest", "days": "Months 3-30", "description": "Spike plucked at heel when outer 2 whorls of disc florets open."}],
  [{"name": "Foot Rot / Phytophthora", "symptoms": "Sudden crown rot and collapse.", "riskPeriod": "Wet crowns."},
   {"name": "Powdery Mildew", "symptoms": "White foliar dust.", "riskPeriod": "Dry greenhouse air."}],
  ["Whitefly", "Thrips", "Red Spider Mite"], ["Never bury the central crown in soil during planting."])

c("carnation", "Carnation (Cut Flower)", "कार्नेशन (Carnation)", "Dianthus caryophyllus", "Floriculture & Flowers", "🌸",
  "Year-round (Polyhouse)", "Pune, Ooty, Himachal",
  "Classic ruffly cut flower with clove-scented fragrance and long 14-20 day vase life.",
  "14°C - 22°C (cool greenhouse conditions)", "Automated drip.", "Well-aerated sandy loam.",
  [{"stage": "Net Staking", "days": "Month 1-2", "description": "Supported through multi-layered nylon mesh grids."},
   {"stage": "Disbudding", "days": "Month 3-4", "description": "Side buds removed to produce one large central bloom."},
   {"stage": "Harvest", "days": "Months 4-24", "description": "Harvested at paintbrush / cross stage."}],
  [{"name": "Fusarium Wilt", "symptoms": "Vascular yellowing.", "riskPeriod": "High greenhouse heat."}],
  ["Thrips", "Tetranychus Mites"], ["Steam pasteurize greenhouse beds."])

c("gladiolus", "Gladiolus (Sword Lily)", "ग्लॅडिओलस (Gladiolus)", "Gladiolus grandiflorus", "Floriculture & Flowers", "💐",
  "Winter", "Pune, Nashik, Kolhapur, North India",
  "Tall magnificent flower spikes bearing rows of trumpet-shaped flowers in stunning colors, grown from corms.",
  "15°C - 24°C", "350 - 450 mm.", "Loose fertile sandy loam.",
  [{"stage": "Corm Planting", "days": "Oct - Nov", "description": "Corms planted 7-10 cm deep."},
   {"stage": "Spike Emergence", "days": "Days 50-70", "description": "Erect sword-like spike emerges."},
   {"stage": "Spike Harvest", "days": "Days 75-90", "description": "Cut when 1-2 bottom florets show color break."}],
  [{"name": "Fusarium Corm Rot", "symptoms": "Corms rot in storage.", "riskPeriod": "Damp storage."}],
  ["Gladiolus Thrips"], ["Dip corms in Carbendazim solution before planting."])

c("anthurium", "Anthurium (Flamingo Flower)", "अँथुरियम (Anthurium)", "Anthurium andraeanum", "Floriculture & Flowers", "🌺",
  "Year-round (Shade Net)", "Konkan, Western Ghats, South India",
  "Exotic glossy heart-shaped spathes with protruding spadix in vivid red, white, and pink with 30-day vase life.",
  "20°C - 28°C", "High humidity (80%).", "Soilless media: coconut husk chips, charcoal, and brick pieces.",
  [{"stage": "Vegetative", "days": "Continuous", "description": "Glossy spade leaves."},
   {"stage": "Spathe Harvest", "days": "Every 6-8 weeks", "description": "Cut when 50% spadix changes color."}],
  [{"name": "Bacterial Blight (Xanthomonas)", "symptoms": "Yellow V-shaped water-soaked leaf margins.", "riskPeriod": "Warm wet mist."}],
  ["Thrips"], ["Strict hygiene and copper hydroxide sprays."])

c("dendrobium-orchid", "Dendrobium Orchid", "ऑर्किड (Dendrobium Orchid)", "Dendrobium hybrids", "Floriculture & Flowers", "🪻",
  "Year-round", "Konkan (Sindhudurg, Ratnagiri), Kerala, Northeast India",
  "Epiphytic tropical orchid yielding delicate sprays of purple and white flowers with 3-4 week shelf life.",
  "22°C - 30°C", "75-80% humidity.", "Perforated plastic pots filled with charcoal and coconut chips.",
  [{"stage": "Pseudobulb Growth", "days": "Months 1-8", "description": "Canes develop."},
   {"stage": "Spike Bloom", "days": "Annual flushes", "description": "Spikes cut when all but top 1-2 buds open."}],
  [{"name": "Soft Rot (Erwinia)", "symptoms": "Watery blister rot.", "riskPeriod": "Stagnant humid air."}],
  ["Snail / Slugs"], ["Maintain excellent air circulation on nursery benches."])

c("crossandra-aboli", "Crossandra (Aboli)", "आबोली (Aboli)", "Crossandra infundibuliformis", "Floriculture & Flowers", "🏵️",
  "Year-round", "Western Maharashtra, Konkan, South India",
  "Beloved traditional Maharashtrian hair flower. Vibrant coral-orange fan-shaped ruffled petals woven into delicate venis.",
  "22°C - 32°C", "450 mm.", "Well-drained red lateritic loam.",
  [{"stage": "Flowering Spikes", "days": "Continuous", "description": "Four-sided spikes produce daily coral blossoms."}],
  [{"name": "Wilt / Root Rot", "symptoms": "Drooping.", "riskPeriod": "Heavy rain."}],
  ["Nematodes"], ["Drench with neem cake and bio-fungicides."])

c("sacred-lotus-kamal", "Sacred Lotus (Kamal)", "कमळ (Kamal / Lotus)", "Nelumbo nucifera", "Floriculture & Flowers", "🪷",
  "Summer to Monsoon", "Lakes across Maharashtra and India",
  "National flower of India; sacred pink and white blossoms harvested for temple pujas, meditation, and aesthetic wetlands.",
  "22°C - 34°C", "Freshwater pond.", "Rich lake silt.",
  [{"stage": "Bloom", "days": "Morning flower", "description": "Opens at sunrise, closes at afternoon."}],
  [{"name": "Leaf Rot", "symptoms": "Decaying pads.", "riskPeriod": "Polluted water."}],
  ["Caterpillars"], ["Cultivated in natural freshwater ponds."])

c("aster", "Aster (Kamini)", "अॅस्टर (Aster)", "Callistephus chinensis", "Floriculture & Flowers", "🌸",
  "Winter", "Pune, Satara, Nashik",
  "Prolific daisy-like flowers in purple, pink, and white used for loose flower garlands and bouquet fillers.",
  "15°C - 24°C", "350 mm.", "Fertile loam.",
  [{"stage": "Harvest", "days": "Days 60-80", "description": "Fully open flowers plucked."}],
  [{"name": "Blight", "symptoms": "Leaf spots.", "riskPeriod": "Rains."}],
  ["Aphids"], ["Use Kamini, Poornima, or Shashank varieties."])

c("gypsophila", "Gypsophila (Baby's Breath)", "जिप्सोफिला (Baby's Breath)", "Gypsophila paniculata", "Floriculture & Flowers", "🤍",
  "Winter & Polyhouse", "Pune, Ooty, Himachal",
  "Masses of tiny delicate white starry blossoms; premier bouquet filler flower globally.",
  "14°C - 22°C", "350 mm.", "Calcareous sandy loam with high calcium.",
  [{"stage": "Harvest", "days": "Days 75-90", "description": "Cut when 50% starry florets open."}],
  [{"name": "Damping Off", "symptoms": "Stem rot.", "riskPeriod": "Damp soil."}],
  ["Leaf Miner"], ["Use Million Stars or Perfecta varieties."])

# ==========================================
# 9. MEDICINAL & AROMATIC PLANTS (20 crops)
# ==========================================
c("ashwagandha", "Ashwagandha (Indian Ginseng)", "अश्वगंधा (Ashwagandha)", "Withania somnifera", "Medicinal & Aromatic Plants", "🌿",
  "Late Kharif / Rabi", "Marathwada, Ahmednagar, Vidarbha, MP (Neemuch)",
  "Crown jewel of Ayurvedic medicine. Adaptogenic roots packed with withanolides for relieving stress, boosting testosterone, and enhancing longevity.",
  "20°C - 32°C (dry semi-arid climate)", "350 - 450 mm; rainfed once established.", "Light sandy loam or rocky red soil with good drainage, pH 7.0 - 8.0.",
  [{"stage": "Emergence & Branching", "days": "Days 1-45", "description": "Starry hairy branching bush."},
   {"stage": "Green Flower & Orange Berries", "days": "Days 46-120", "description": "Inconspicuous greenish flowers followed by papery calyx enclosing red berries."},
   {"stage": "Root Maturation & Digging", "days": "Days 150-180", "description": "Leaves yellow and berries turn orange-red; deep brittle roots dug with plows."}],
  [{"name": "Seedling Blight / Seed Rot", "symptoms": "Seedling damping off.", "riskPeriod": "Damp wet soil."},
   {"name": "Alternaria Leaf Blight", "symptoms": "Brown leaf spots.", "riskPeriod": "Late monsoon rains."}],
  ["Hadda Beetle (Epilachna)", "Mites", "Aphids"],
  ["Avoid fertile high-nitrogen soils which cause bushy leaves and thin fibrous woody roots.",
   "Use superior high-withanolide varieties: JA-20, Pratap, or Poshita.",
   "Grade dried roots into pencil-thick A-grade brittle white pieces."])

c("holy-basil-tulsi", "Tulsi / Holy Basil (Krishna & Rama Tulsi)", "तुळस (Krishna & Rama Tulsi)", "Ocimum tenuiflorum", "Medicinal & Aromatic Plants", "🌿",
  "Year-round", "Throughout Maharashtra & India",
  "The sacred medicinal queen of Indian herbs. Rich in eugenol and adaptogens; purifies air, boosts respiratory immunity, and relieves cough.",
  "20°C - 35°C", "Rainfed or moderate watering.", "Well-drained loam.",
  [{"stage": "Seedling", "days": "Days 1-25", "description": "Purple or green aromatic shoots."},
   {"stage": "Spike Flowering", "days": "Days 45-75", "description": "Purple inflorescence spikes bloom."},
   {"stage": "Periodic Leaf Harvest", "days": "Monthly", "description": "Tops clipped for tea and herbal formulations."}],
  [{"name": "Leaf Spot", "symptoms": "Brown spots.", "riskPeriod": "Monsoon."}],
  ["Aphids", "Whitefly"], ["Prune flower spikes to keep plants bushy."])

c("citronella", "Citronella (Java Citronella)", "सिट्रोनेला (Citronella)", "Cymbopogon winterianus", "Medicinal & Aromatic Plants", "🌾",
  "Perennial Grass", "Western Maharashtra, Vidarbha, Assam",
  "Clump-forming aromatic grass distilled for pure citronellal essential oil used in natural mosquito repellents and perfumes.",
  "22°C - 35°C", "1,000 - 1,500 mm.", "Fertile loam.",
  [{"stage": "Harvest", "days": "Every 60-75 days", "description": "Canes harvested 15 cm above base for steam distillation."}],
  [{"name": "Leaf Blight", "symptoms": "Tip drying.", "riskPeriod": "Rains."}],
  ["Stem Borer"], ["Use Bio-13 or Mandakini varieties."])

c("palmarosa-rosha", "Palmarosa (Rosha Grass)", "पामारोजा / रोषा गवत (Rosha Grass)", "Cymbopogon martinii", "Medicinal & Aromatic Plants", "🌾",
  "Perennial Grass", "Vidarbha (Melghat forests), Khandesh, Marathwada",
  "Indigenous aromatic grass of Maharashtra hills yielding sweet rose-scented geraniol oil for high-grade international perfumery.",
  "24°C - 35°C", "600 - 800 mm.", "Marginal, rocky, and saline soils.",
  [{"stage": "Harvest at Bloom", "days": "Days 75-90", "description": "Cut at 50% flowering when geraniol content peaks."}],
  [{"name": "Rust", "symptoms": "Brown spots.", "riskPeriod": "Winter."}],
  ["Grasshopper"], ["Use Motia variety (PRC-1, Trishna)."])

c("aloe-vera-korphad", "Aloe Vera (Korphad)", "कोरफड (Korphad / Aloe Vera)", "Aloe barbadensis miller", "Medicinal & Aromatic Plants", "🌵",
  "Perennial Succulent", "Solapur, Ahmednagar, Marathwada arid belts",
  "Drought-hardy fleshy succulent producing clear cooling gel packed with polysaccharides for burns, skincare, and digestion.",
  "24°C - 38°C", "200 - 350 mm; zero tolerance for water stagnation.", "Sandy loam to rocky calcareous soil.",
  [{"stage": "Sucker Planting", "days": "Months 1-3", "description": "Basal suckers established on ridges."},
   {"stage": "Leaf Thickening", "days": "Months 6-12", "description": "Fleshy lanceolate leaves fill with clear gel."},
   {"stage": "Harvest", "days": "Every 2-3 months", "description": "Outer mature 1 kg leaves sliced at base."}],
  [{"name": "Leaf Soft Rot (Bacterial)", "symptoms": "Watery brown rotting of leaf bases.", "riskPeriod": "Water stagnation."}],
  ["Mealybug"], ["Use high aloin varieties: IC-111271 or Thar Kumari."])

c("stevia-sweet-tulsi", "Stevia (Sweet Tulsi)", "गोड तुळस / स्टीव्हिया (Stevia)", "Stevia rebaudiana", "Medicinal & Aromatic Plants", "🌿",
  "Perennial (Harvested 4 times/yr)", "Pune, Satara, Nashik, Marathwada",
  "Zero-calorie natural sweetener crop; leaves are 30-40 times sweeter than cane sugar due to stevioside glycosides, safe for diabetics.",
  "18°C - 32°C", "700 - 900 mm via micro-sprinkler.", "Well-drained sandy loam rich in organic matter, pH 6.0 - 7.5.",
  [{"stage": "Vegetative Flush", "days": "Days 1-70", "description": "Opposite serrated sweet green leaves."},
   {"stage": "Harvest before Bloom", "days": "Day 75", "description": "Canes harvested just as flower buds initiate for highest sweetness."}],
  [{"name": "Septoria Leaf Spot", "symptoms": "Leaf spots.", "riskPeriod": "Humid periods."}],
  ["Aphids"], ["Use varieties: MDS-13 or CIM-Mithi."])

c("shatavari", "Shatavari", "शतावरी (Shatavari)", "Asparagus racemosus", "Medicinal & Aromatic Plants", "🌿",
  "18-24 Months Crop", "Western Ghats, Konkan, Pune, Marathwada",
  "Revered Ayurvedic female tonic and adaptogen. Woody climbing vine producing hundreds of succulent white tuberous roots underground.",
  "20°C - 35°C", "600 - 800 mm.", "Deep loose sandy loam with organic compost.",
  [{"stage": "Root Swelling", "days": "Months 6-18", "description": "Fascicled tuberous roots multiply underground."},
   {"stage": "Digging & Peeling", "days": "Month 18-24", "description": "Roots dug, boiled, and skin peeled to reveal ivory medicinal tubers."}],
  [{"name": "Crown Rot", "symptoms": "Rotting.", "riskPeriod": "Excess rain."}],
  ["Aphids"], ["Plant on deep ridges to facilitate tuber digging."])

c("safed-musli", "Safed Musli", "सफेद मुसळी (Safed Musli)", "Chlorophytum borivilianum", "Medicinal & Aromatic Plants", "🌱",
  "3-4 Months (Kharif)", "Vidarbha, MP, Gujarat border tracts",
  "High-value Ayurvedic revitalizer; produces finger-like tuberous roots rich in saponins, used for vitality and herbal energy tonics.",
  "24°C - 32°C", "600 mm.", "Loose sandy loam with high leaf mould.",
  [{"stage": "Foliage Flush", "days": "Days 1-45", "description": "Sword leaves and white starry flower spikes."},
   {"stage": "Leaf Withering", "days": "Days 90-100", "description": "Foliage dies naturally; tubers mature."},
   {"stage": "Tuber Lifting", "days": "Nov - Dec", "description": "Ivory fascicled roots lifted and sun-dried."}],
  [{"name": "Collar Rot", "symptoms": "Root rot.", "riskPeriod": "Waterlogging."}],
  ["White Grub"], ["Raised bed cultivation with sand and vermicompost."])

c("brahmi-memory-herb", "Brahmi (Memory Herb)", "ब्राह्मी / बाम (Brahmi)", "Bacopa monnieri", "Medicinal & Aromatic Plants", "🌱",
  "Year-round", "Konkan wetlands, stream banks across Maharashtra",
  "Legendary brain-tonic and memory enhancer rich in bacosides; creeping succulent herb thriving in marshy soils.",
  "22°C - 34°C", "Wet waterlogged beds.", "Clay loam and marsh silt.",
  [{"stage": "Trailing Stems", "days": "Continuous", "description": "Leaves harvested every 60-70 days."}],
  [{"name": "Leaf Rot", "symptoms": "Decay.", "riskPeriod": "Stagnant foul water."}],
  ["Grasshopper"], ["Subhiksha variety."])

c("kalmegh-bhuinimba", "Kalmegh (King of Bitters)", "काळमेघ / भुईनिंब (Kalmegh)", "Andrographis paniculata", "Medicinal & Aromatic Plants", "🌿",
  "Kharif", "Vidarbha forest fringes, Konkan, MP",
  "Intensely bitter medicinal herb rich in andrographolide, world-famous for liver protection, jaundice recovery, and viral fever defense.",
  "24°C - 35°C", "500 mm.", "Well-drained loam.",
  [{"stage": "Bloom & Harvest", "days": "Days 90-110", "description": "Cut at 50% flowering when active bitter compounds peak."}],
  [{"name": "Damping Off", "symptoms": "Seedling decay.", "riskPeriod": "Rain."}],
  ["Leaf Miner"], ["Use CIM-Megha variety."])

c("senna-sonamukhi", "Senna (Sonamukhi)", "सोनामुखी / सेना (Sonamukhi)", "Cassia angustifolia", "Medicinal & Aromatic Plants", "🌿",
  "Kharif & Late Kharif", "Solapur, Ahmednagar dry tracts, Gujarat, Rajasthan",
  "Drought-hardy shrub yielding sennosides-rich leaves and flat brown pods for natural laxative and colon detox teas.",
  "25°C - 38°C", "250 - 350 mm.", "Arid marginal gravelly soils.",
  [{"stage": "Leaf Plucking", "days": "Days 90, 120, 150", "description": "Leaves stripped and shade-dried."}],
  [{"name": "Damping Off", "symptoms": "Rot.", "riskPeriod": "Rains."}],
  ["Pod Borer"], ["Use Anand Late Selection or ALFT-2."])

c("isabgol-psyllium", "Isabgol (Psyllium Husk)", "इसबगोल (Isabgol)", "Plantago ovata", "Medicinal & Aromatic Plants", "🌾",
  "Rabi (Winter)", "Gujarat, Rajasthan, North Maharashtra",
  "Premier natural dietary fiber crop; boat-shaped seeds yield pure white mucilaginous husk (Sat Isabgol) for digestive regularity.",
  "15°C - 24°C (completely dry harvest)", "200 - 300 mm.", "Sandy loam with great drainage.",
  [{"stage": "Spike Maturation", "days": "Days 100-120", "description": "Spikes turn yellow-brown; harvested at dawn to prevent shattering."}],
  [{"name": "Downy Mildew", "symptoms": "Leaf spots.", "riskPeriod": "Dewy mornings."}],
  ["Aphids"], ["Use Gujarat Isabgol-1 or GI-2."])

c("vetiver-khus", "Vetiver (Khus / Vala)", "वाळा / खस (Vala / Khus)", "Chrysopogon zizanioides", "Medicinal & Aromatic Plants", "🌾",
  "Perennial Grass", "Konkan, Western Ghats, riverbanks across Maharashtra",
  "Massive fibrous spongy roots hold soil erosion and distill cooling earthy Khus perfume oil, summer cooler mats, and earthen pot aromatics.",
  "22°C - 38°C", "Rainfed.", "All soils, riverbeds.",
  [{"stage": "Root Digging", "days": "Months 15-18", "description": "Roots dug to 2 meters depth; washed and distilled."}],
  [{"name": "Leaf Blight", "symptoms": "Tip drying.", "riskPeriod": "Monsoon."}],
  ["Termites"], ["Use KS-1 or Dharini varieties."])

c("patchouli", "Patchouli", "पचौली (Patchouli)", "Pogostemon cablin", "Medicinal & Aromatic Plants", "🌿",
  "Perennial Shrub", "Western Ghats, Konkan, South India",
  "Aromatic shade-loving shrub whose dried fermented leaves yield legendary patchoulol oil, the deep woody base note of luxury perfumes.",
  "22°C - 30°C", "1,500 mm.", "Rich fertile loam.",
  [{"stage": "Foliage Harvest", "days": "Every 3-4 months", "description": "Top 15 cm leafy shoots harvested."}],
  [{"name": "Root Knot Nematode", "symptoms": "Galls.", "riskPeriod": "Sandy soil."}],
  ["Leaf Caterpillar"], ["Use Johore or CIM-Samarth varieties."])

c("geranium-scented", "Rose Geranium", "जरेनियम (Geranium)", "Pelargonium graveolens", "Medicinal & Aromatic Plants", "🌸",
  "Winter & Spring", "Mahabaleshwar, Pune, Nilgiris hill stations",
  "Deeply aromatic ruffled foliage smelling of fresh roses, distilled for pure rhodinol and geraniol oils.",
  "15°C - 26°C", "600 mm.", "Well-drained mountain soil.",
  [{"stage": "Foliage Cut", "days": "Every 90 days", "description": "Leaves harvested for distillation."}],
  [{"name": "Wilt", "symptoms": "Stem rot.", "riskPeriod": "Excess rain."}],
  ["Root Grubs"], ["Use Bourbon or Algerian varieties."])

c("giloy-guduchi", "Giloy (Guduchi / Amrita)", "गुळवेल / अमृता (Gulvel / Giloy)", "Tinospora cordifolia", "Medicinal & Aromatic Plants", "🌿",
  "Perennial Climbing Vine", "Throughout Maharashtra & India, climbing on neem trees",
  "The elixir of life (Amrita) in Ayurveda. Succulent climbing vine with heart-shaped leaves; stems boost platelet count and immunity against dengue and malaria.",
  "20°C - 35°C", "Rainfed.", "All soil types.",
  [{"stage": "Stem Harvest", "days": "Year-round", "description": "Fleshy grey-barked stems sliced and dried."}],
  [{"name": "Fungal Rot", "symptoms": "Rotting.", "riskPeriod": "Water stagnation."}],
  ["Caterpillar"], ["Neem-growing Giloy (Neem Giloy) possesses the highest medicinal potency."])

c("sarpagandha", "Sarpagandha (Rauvolfia)", "सर्पगंधा (Sarpagandha)", "Rauvolfia serpentina", "Medicinal & Aromatic Plants", "🌿",
  "18-24 Months", "Konkan moist deciduous forests, Western Ghats",
  "Famous root yielding reserpine alkaloid used globally for treating severe hypertension and neuropsychiatric disorders.",
  "20°C - 32°C", "1,500 mm.", "Acidic sandy loam rich in humus.",
  [{"stage": "Root Digging", "days": "Month 24", "description": "Curved yellowish roots dug."}],
  [{"name": "Leaf Blight", "symptoms": "Spots.", "riskPeriod": "Rains."}],
  ["Nematodes"], ["Cultivated under forest shade trees."])

c("shankhpushpi", "Shankhpushpi", "शंखपुष्पी (Shankhpushpi)", "Convolvulus pluricaulis", "Medicinal & Aromatic Plants", "🪻",
  "Perennial Herb", "Dry plains of Maharashtra and Central India",
  "Prostrate trailing herb with blue/white conch-shaped blossoms, renowned memory tonic and anxiety reliever in Ayurveda.",
  "22°C - 35°C", "250 mm.", "Sandy rocky soils.",
  [{"stage": "Harvest", "days": "During Bloom", "description": "Whole plant harvested."}],
  [{"name": "Damping Off", "symptoms": "Rot.", "riskPeriod": "Wet soil."}],
  ["Leaf Hopper"], ["Grows in dry open wastelands."])

c("bhringraj-maka", "Bhringraj (Maka)", "माका / भृंगराज (Bhringraj / Maka)", "Eclipta prostrata", "Medicinal & Aromatic Plants", "🌿",
  "Year-round", "Moist stream banks and ditches across Maharashtra",
  "King of hair care (Keshya) in Ayurveda. Small creeping daisy with white florets; juice stops hair loss and premature greying.",
  "20°C - 32°C", "Moist wet soils.", "Clay loam near watercourses.",
  [{"stage": "Harvest", "days": "Days 45-60", "description": "Flowering shoots cut for Maka hair oil extraction."}],
  [{"name": "Leaf Spot", "symptoms": "Specks.", "riskPeriod": "Monsoon."}],
  ["Aphids"], ["Harvest fresh for boiling with sesame or coconut oil."])

c("neem-medicinal", "Neem (Kadu Neem)", "कडुनिंब (Neem Tree)", "Azadirachta indica", "Medicinal & Aromatic Plants", "🌳",
  "Perennial Tree", "Throughout Maharashtra & India",
  "The village pharmacy of India. Every part (bark, bitter leaves, flowers, seeds) possesses potent antimicrobial, antiviral, and blood-purifying properties.",
  "20°C - 42°C", "Rainfed.", "All soil types.",
  [{"stage": "Leaf & Bark Harvest", "days": "Year-round", "description": "Pruned leaves and twigs used for dental and skin health."}],
  [{"name": "Dieback", "symptoms": "Twig drying.", "riskPeriod": "Monsoon."}],
  ["Tea Mosquito Bug"], ["Sacred village tree requiring zero irrigation."])

# ==========================================
# 10. PLANTATION & AGROFORESTRY (16 crops)
# ==========================================
c("tea-assam", "Tea (Chaha)", "चहा (Assam & Nilgiri Tea)", "Camellia sinensis", "Plantation & Agroforestry", "🍵",
  "Perennial Plantation Bush", "Assam, Darjeeling, Nilgiris, experimental Western Ghats",
  "World's most popular beverage crop. Two tender leaves and a bud hand-plucked every 7-10 days for CTC and orthodox black tea processing.",
  "18°C - 30°C", "1,500 - 2,500 mm.", "Acidic well-drained mountain soil, pH 4.5 - 5.5.",
  [{"stage": "Plucking Flush", "days": "Every 7-10 days", "description": "Two leaves and terminal bud plucked."}],
  [{"name": "Blister Blight (Exobasidium vexans)", "symptoms": "Translucent circular blister lesions on tender leaves.", "riskPeriod": "Heavy continuous monsoon rain and mist."}],
  ["Tea Mosquito Bug", "Red Spider Mite"], ["Spray copper oxychloride for blister blight."])

c("coffee-arabica", "Arabica Coffee", "अरेबिका कॉफी (Arabica Coffee)", "Coffea arabica", "Plantation & Agroforestry", "☕",
  "Perennial Shade Tree", "Chikkamagaluru, Coorg, Wayanad, Nilgiris, Satpura ranges",
  "Premier high-altitude shade-grown specialty coffee yielding sweet aromatic beans with delicate floral notes and balanced acidity.",
  "15°C - 25°C", "1,500 - 2,200 mm.", "Rich fertile volcanic or forest loam.",
  [{"stage": "Blossom Showers", "days": "March - April", "description": "Snowy white fragrant blooms follow first spring rains."},
   {"stage": "Berry Maturation", "days": "Nov - Jan", "description": "Berries turn from green to bright crimson (cherry stage); handpicked."}],
  [{"name": "Coffee Leaf Rust (Hemileia vastatrix)", "symptoms": "Orange powdery pustules on leaf undersides causing severe leaf drop.", "riskPeriod": "Warm wet monsoon."},
   {"name": "Black Rot (Koleroga)", "symptoms": "Hanging leaves bound by white mycelial threads.", "riskPeriod": "Continuous mist."}],
  ["Coffee White Stem Borer (Xylotrechus quadripes)", "Coffee Berry Borer (Hypothenemus hampei)"],
  ["Maintain two-tier shade tree canopy (Dadap and Silver Oak).",
   "Swab main stems with 10% lime wash to prevent white stem borer egg laying."])

c("coffee-robusta", "Robusta Coffee", "रोबस्टा कॉफी (Robusta Coffee)", "Coffea canephora", "Plantation & Agroforestry", "☕",
  "Perennial", "Karnataka, Kerala, Wayanad",
  "Bold, full-bodied coffee crop with higher caffeine content (2.7%) and heavy crema, resilient to rust and lower altitudes.",
  "20°C - 32°C", "1,200 - 2,000 mm.", "Forest loam.",
  [{"stage": "Cherry Harvest", "days": "Jan - March", "description": "Red berries stripped and sun-dried."}],
  [{"name": "Root Rot", "symptoms": "Wilting.", "riskPeriod": "Water stagnation."}],
  ["Shot Hole Borer"], ["Tolerant to rust, ideal for espresso blending."])

c("areca-nut-supari", "Areca Nut (Supari)", "सुपारी (Shrivardhan / Roha Supari)", "Areca catechu", "Plantation & Agroforestry", "🌴",
  "Perennial Palm", "Konkan Coast (Raigad Shrivardhan Rohe supari has GI status!), South India",
  "Slender solitary palm cultivated in coastal Konkan wadis, yielding smooth white-fleshed supari nuts for auspicious occasions and mastication.",
  "22°C - 32°C", "2,000 - 3,500 mm.", "Coastal lateritic and alluvial soils.",
  [{"stage": "Bearing Palm", "days": "Years 6 onwards", "description": "Bunches emerge below feather fronds."},
   {"stage": "Harvest", "days": "Oct - Jan", "description": "Nuts harvested at tender (Chikni) or full ripe stage (Chali)."}],
  [{"name": "Koleroga / Fruit Rot (Phytophthora meadii)", "symptoms": "Rotting and premature shedding of green nuts with white fungal crust.", "riskPeriod": "Heavy continuous monsoon rains."}],
  ["Spindle Bug", "White Mite"], ["Tie polythene or areca leaf sheaths (kotte) over bunches before monsoon onset."])

c("cocoa-chocolate", "Cocoa (Chocolate Tree)", "कोको (Cocoa Tree)", "Theobroma cacao", "Plantation & Agroforestry", "🍫",
  "Perennial Shade Tree", "Intercropped in coconut & arecanut orchards of Konkan and South India",
  "Understory tropical tree bearing colorful ridged pods on trunk and branches; seeds fermented and dried into chocolate nibs.",
  "22°C - 32°C", "1,500 - 2,000 mm.", "Deep fertile loam rich in organic matter.",
  [{"stage": "Cauliflorous Flowering", "days": "Year-round", "description": "Cushions of tiny flowers on bark."},
   {"stage": "Pod Maturity", "days": "5-6 months after bloom", "description": "Pods turn yellow/orange; cracked open for fermentation."}],
  [{"name": "Black Pod Disease (Phytophthora)", "symptoms": "Brown rotting of pods.", "riskPeriod": "Monsoon humidity."}],
  ["Tea Mosquito Bug"], ["Spray 1% Bordeaux mixture before monsoon."])

c("sandalwood-chandan", "Sandalwood (Chandan)", "चंदन (Chandan)", "Santalum album", "Plantation & Agroforestry", "🪵",
  "15-20 Years Perennial", "Marathwada, Western Maharashtra, Karnataka",
  "Sacred partial root parasite producing the world's most fragrant heartwood rich in santalol oil for religious pujas and perfumes.",
  "22°C - 35°C", "600 - 1,000 mm.", "Rocky, gravelly red loam, pH 6.5 - 7.5.",
  [{"stage": "Host Plant Parasitism", "days": "Years 1-3", "description": "Roots attach haustoria to host plants (Shevri, Casuarina, Neem)."},
   {"stage": "Heartwood Formation", "days": "Years 7-15", "description": "Aromatic oil accumulates in central core wood."},
   {"stage": "Uprooting & Harvest", "days": "Years 15-20", "description": "Whole tree uprooted (roots have highest oil content)."}],
  [{"name": "Sandal Spike Disease (Phytoplasma)", "symptoms": "Leaves reduce drastically in size and stand erect like spikes; tree dies in 1-2 years.", "riskPeriod": "Leafhopper vectors."}],
  ["Stem Borer"], ["Always plant primary and secondary host plants (Sesbania and Neem) in 1:2 ratio with sandalwood saplings."])

c("teak-sagwan", "Teak (Sagwan)", "सागवान / साग (Sagwan Teak)", "Tectona grandis", "Plantation & Agroforestry", "🪵",
  "20-25 Years", "Vidarbha (Chandrapur & Gadchiroli Teak holding GI status), Melghat",
  "King of timber trees holding GI status for CP Teak. Impregnable golden-brown heartwood rich in natural tectoquinone preserving wood against termites for centuries.",
  "24°C - 36°C", "1,200 - 2,000 mm.", "Deep alluvial or medium black soils with high calcium.",
  [{"stage": "Sapling & Stump", "days": "Years 1-3", "description": "Root stumps sprout into massive broad-leaved poles."},
   {"stage": "Canopy Thinning", "days": "Years 7, 14", "description": "Silvicultural thinning gives room for prime timber."},
   {"stage": "Timber Felling", "days": "Years 20-30", "description": "Mature logs felled for high-value furniture."}],
  [{"name": "Teak Rust", "symptoms": "Leaf spots.", "riskPeriod": "Post-monsoon."}],
  ["Teak Defoliator (Hyblaea puera)", "Teak Skeletonizer (Eutectona machaeralis)"],
  ["Maintain mixed agroforestry to support natural predator birds."])

c("subabul", "Subabul (Fodder Tree)", "सुबाभूळ (Subabul)", "Leucaena leucocephala", "Plantation & Agroforestry", "🌳",
  "Perennial Fast Growing", "Throughout Maharashtra dairy belts",
  "Super fast-growing leguminous agroforestry tree providing high-protein green forage (24% crude protein) for dairy cattle and biomass energy.",
  "20°C - 38°C", "Rainfed.", "All soil types.",
  [{"stage": "Coppice Harvest", "days": "Every 45-60 days", "description": "Foliage cut for livestock feed."}],
  [{"name": "Gummosis", "symptoms": "Gum ooze.", "riskPeriod": "Rains."}],
  ["Subabul Psyllid (Heteropsylla cubana)"], ["Use psyllid-resistant variety K-636."])

c("eucalyptus-nilgiri", "Eucalyptus (Nilgiri)", "निलगिरी (Nilgiri)", "Eucalyptus tereticornis", "Plantation & Agroforestry", "🌳",
  "5-7 Years Crop", "Western Maharashtra, Vidarbha wastelands",
  "Fastest-growing straight pole tree harvested for paper pulp, rayon, and construction poles.",
  "20°C - 38°C", "400 - 800 mm.", "Well-drained soils.",
  [{"stage": "Poles Harvest", "days": "Year 5", "description": "Tall straight poles felled."}],
  [{"name": "Pink Disease", "symptoms": "Bark crust.", "riskPeriod": "Monsoon."}],
  ["Gall Wasp (Leptocybe invasa)"], ["Use high-yielding clonal varieties: IFGTB-1 to 10."])

c("mahua-tree", "Mahua (Moh)", "मोह / महुआ (Moha Tree)", "Madhuca longifolia", "Plantation & Agroforestry", "🌳",
  "Perennial Forest Tree", "Vidarbha tribal belts (Gadchiroli, Chandrapur), Satpuras",
  "Sacred tribal tree; creamy succulent fallen blossoms collected for traditional syrup and baking; seeds crushed for lighting oil.",
  "24°C - 42°C", "Rainfed.", "Rocky forest soils.",
  [{"stage": "Flower Fall", "days": "March - April", "description": "Fleshy sweet corollas carpet forest floor at dawn."}],
  [{"name": "Fungal Leaf Spot", "symptoms": "Spots.", "riskPeriod": "Monsoon."}],
  ["Bark Caterpillar"], ["Gather fallen flowers on clean swept forest clearings."])

c("shisham-rosewood", "Indian Rosewood (Shisham / Sissoo)", "शिसव / शेशम (Shisham)", "Dalbergia sissoo", "Plantation & Agroforestry", "🪵",
  "20-25 Years", "River valleys of Maharashtra, Punjab, UP",
  "Premier cabinet wood with deep golden-brown grain, exceptional carving strength, and elasticity.",
  "22°C - 36°C", "800 mm.", "Alluvial sandy loams with subsoil moisture.",
  [{"stage": "Growth", "days": "Decades", "description": "Hardwood expands."},
   {"stage": "Felling", "days": "Years 25+", "description": "Prime carving timber."}],
  [{"name": "Shisham Wilt (Fusarium)", "symptoms": "Sudden dying of trees.", "riskPeriod": "Clay soils."}],
  ["Leaf Defoliator"], ["Plant on sandy riverbed soils with high drainage."])

c("khair-catechu", "Khair (Kattha / Catechu)", "खैर / काथ (Khair Tree)", "Senegalia catechu", "Plantation & Agroforestry", "🌳",
  "15-20 Years", "Dry deciduous forests of Khandesh, Marathwada, Vidarbha",
  "Thorny dryland tree; reddish-brown heartwood boiled and crystallized into pure 'Kattha' (काथ) for edible paan and leather tanning.",
  "25°C - 42°C", "Rainfed.", "Rocky, arid, gravelly soils.",
  [{"stage": "Heartwood Extraction", "days": "Years 15+", "description": "Heartwood chipped and boiled in earthen pots for Kattha."}],
  [{"name": "Heart Rot", "symptoms": "Rot in trunk.", "riskPeriod": "Old trees."}],
  ["Wood Borer"], ["Hardy drought-survivor tree."])

c("silver-oak", "Silver Oak (Grevillea)", "सिल्व्हर ओक (Silver Oak)", "Grevillea robusta", "Plantation & Agroforestry", "🌳",
  "10-15 Years", "Coffee and tea estates of Western Ghats, farm bunds across Maharashtra",
  "Tall feathery tree serving as ideal live standard for black pepper vines and shade for coffee; fast-growing farm boundary tree.",
  "15°C - 30°C", "800 - 1,500 mm.", "Well-drained soils.",
  [{"stage": "Growth", "days": "Poles in 5 years", "description": "Provides pepper climbing bark."}],
  [{"name": "Stem Canker", "symptoms": "Lesions.", "riskPeriod": "Monsoon."}],
  ["Termites"], ["Fast growth with high salvage timber value."])

c("banyan-tree", "Sacred Banyan Tree (Vad)", "वड / वटवृक्ष (Vad / Banyan)", "Ficus benghalensis", "Plantation & Agroforestry", "🌳",
  "Centuries Long (Heritage)", "Throughout Maharashtra & India",
  "National tree of India. Massive immortal canopy with aerial prop roots celebrated on Vat Purnima; vital keystone species supporting birds and wildlife.",
  "15°C - 40°C", "Rainfed.", "All soils.",
  [{"stage": "Prop Root Spread", "days": "Decades", "description": "Aerial roots anchor into auxiliary trunks."}],
  [{"name": "Leaf Spot", "symptoms": "Specks.", "riskPeriod": "Rains."}],
  ["Scale Insects"], ["Sacred tree providing perpetual shade."])

c("peepal-tree", "Sacred Fig (Peepal / Pipal)", "पिंपळ / अश्वत्थ (Pimpal / Peepal)", "Ficus religiosa", "Plantation & Agroforestry", "🌳",
  "Centuries Long", "Throughout Maharashtra & India",
  "Sacred Bodhi tree under which Lord Buddha attained enlightenment. Releases oxygen day and night; distinctive heart-shaped leaves with long tapering tail.",
  "15°C - 40°C", "Rainfed.", "Extremely adaptable, even grows in stone masonry.",
  [{"stage": "Canopy Spread", "days": "Centuries", "description": "Rustling heart-shaped leaves."}],
  [{"name": "Sooty Mold", "symptoms": "Black mold.", "riskPeriod": "Humid."}],
  ["Ficus Hopper"], ["Venerated shade tree in every Indian village square."])

c("neem-agroforestry", "Neem (Biopesticide Tree)", "कडुनिंब (Neem Agroforestry)", "Azadirachta indica", "Plantation & Agroforestry", "🌳",
  "Perennial Tree", "Throughout Maharashtra & India",
  "Prime agroforestry shelterbelt tree protecting crops from wind erosion while yielding organic biopesticide seeds.",
  "20°C - 42°C", "Rainfed.", "Dry arid soils.",
  [{"stage": "Tree Maturity", "days": "Years 5+", "description": "Full canopy bearing nimboli."}],
  [{"name": "Dieback", "symptoms": "Twig drying.", "riskPeriod": "Monsoon."}],
  ["Tea Mosquito Bug"], ["Plant on field borders 10 meters apart."])

print(f"Master dataset compiled successfully! Total crops: {len(crops)}")

# Now generate src/data/cropsDatabase.ts
header = """// ==============================================================================
// AgroVision AI — Comprehensive Agricultural Encyclopedia
// Database of 240+ scientifically curated crops across Maharashtra and India
// Includes botanical classification, regional adaptations, phenological stages,
// foliar pathology, entomology, and integrated pest management (IPM) guidelines.
// ==============================================================================

import { CropProfile } from '../types';

export const CROP_CATEGORIES = [
  'All Crops',
  'Maharashtra Specialties',
  'Cereals & Millets',
  'Pulses & Legumes',
  'Oilseeds',
  'Cash & Commercial Crops',
  'Fruits & Horticulture',
  'Vegetables & Tubers',
  'Spices & Condiments',
  'Floriculture & Flowers',
  'Medicinal & Aromatic Plants',
  'Plantation & Agroforestry',
] as const;

export const MAHARASHTRA_REGIONS = [
  'All Regions',
  'Konkan (Coastal)',
  'Western Maharashtra (Desh)',
  'Marathwada',
  'Vidarbha',
  'Khandesh (North Maharashtra)',
  'Pan-India',
] as const;

export const CROPS_DATABASE: CropProfile[] = """

ts_content = header + json.dumps(crops, ensure_ascii=False, indent=2) + ";\n"

with open('src/data/cropsDatabase.ts', 'w', encoding='utf-8') as f:
    f.write(ts_content)

print(f"Wrote {len(crops)} crops directly to src/data/cropsDatabase.ts")
