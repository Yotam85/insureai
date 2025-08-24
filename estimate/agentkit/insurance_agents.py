# estimate/agentkit/insurance_agents.py
from __future__ import annotations

import json
from typing import Optional, Sequence, Any, Dict, Tuple

from agents import Agent
from agents import RunConfig
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

# ──────────────────────────────────────────────────────────────────────
# 1) Peril-specific knowledge bases (edit/extend as you like)
# ──────────────────────────────────────────────────────────────────────
WATER_KNOWLEDGE_BASE = r"""

pertial line items list:
Description | UNIT | Unit Price | RCV (or ACV if different) | Category | Tags | Notes
3 tab - 25 yr. - comp. shingle roofing - w/out felt | SQ | 138.43 | 0.00 | Roofing | shingle,roof | Composition shingles
Remove Tear off, haul and dispose of comp. shingles - 3 tab | SQ | 40.87 | 0.00 | Roofing | tearoff,disposal | Shingle removal & disposal
Roofing felt - 15 lb. | SQ | 18.00 | 0.00 | Roofing | felt,underlayment | Standard felt underlayment
Drip edge | LF | 1.35 | 0.00 | Roofing | flashing,edge | Drip edge installation
Drip edge/gutter apron | LF | 1.48 | 0.00 | Roofing | flashing,gutter | Gutter apron installation
Ice & water shield | SF | 1.02 | 0.00 | Roofing | waterproofing,membrane | Ice & water shield membrane
Roof vent - turtle type - Metal | EA | 35.84 | 36.78 | Roofing | vent,metal | Metal turtle vent
Roof vent - turtle type - Plastic | EA | 31.08 | 31.74 | Roofing | vent,plastic | Plastic turtle vent
Roof vent - turbine type | EA | 80.46 | 83.84 | Roofing | vent,turbine | Spinning turbine vent
R&R Power attic vent cover only - metal | EA | 66.83 | 68.62 | Roofing | vent,attic | Metal attic vent cover
Flashing - pipe jack | EA | 20.85 | 21.19 | Roofing | flashing,pipe | Pipe jack flashing
Flashing - pipe jack - lead | EA | 49.36 | 51.41 | Roofing | flashing,lead | Lead pipe jack flashing
R&R Flashing - pipe jack - split boot | EA | 52.54 | 54.38 | Roofing | flashing,boot | Split boot flashing
Digital satellite system - Detach & reset | EA | 23.78 | 23.78 | Roofing | satellite,reset | Reset satellite dish
Continuous ridge vent - shingle-over style | LF | 5.37 | 0.00 | Roofing | ridgevent,vent | Continuous ridge vent
Ridge cap - composition shingles | LF | 3.19 | 0.00 | Roofing | ridgecap,shingle | Ridge cap shingles
Furnace vent - rain cap and storm collar, 5" | EA | 45.50 | 46.53 | Roofing | vent,furnace | Furnace vent (5”)
Furnace vent - rain cap and storm collar, 8" | EA | 61.74 | 63.75 | Roofing | vent,furnace | Furnace vent (8”)
R&R Exhaust cap - through roof - 6" to 8" | EA | 59.62 | 61.36 | Roofing | vent,exhaust | Exhaust roof cap
Additional charge for high roof (2 stories or greater) | SQ | 9.35 | 0.00 | Roofing | addon,height | High roof charge
Additional charge for steep roof - 7/12 to 9/12 slope | SQ | 21.17 | 0.00 | Roofing | addon,slope | Steep slope charge
Additional charge for steep roof - 10/12 - 12/12 slope | SQ | 33.26 | 0.00 | Roofing | addon,slope | Very steep slope charge
Flashing - rain diverter | EA | 22.94 | 23.48 | Roofing | flashing,diverter | Rain diverter flashing
Valley metal | LF | 3.33 | 0.00 | Roofing | flashing,valley | Valley metal
Valley metal - (W) profile | LF | 4.01 | 0.00 | Roofing | flashing,valley | W-profile valley metal
Chimney flashing - average (32" x 36") | EA | 201.06 | 204.27 | Roofing | flashing,chimney | Standard chimney flashing
Remove Lightning protection system | EA | 161.48 | 161.48 | Roofing | lightning,remove | Remove lightning system
Install Lightning protection system | EA | 1,483.11 | 1,483.11 | Roofing | lightning,install | Install lightning system
R&R Cupola - Wood - Small | EA | 560.10 | 586.16 | Roofing | cupola,wood | Replace/Reset wood cupola
Laminated - comp. shingle roofing - w/out felt | SQ | 153.11 | 0.00 | Roofing | shingle,roof | Laminated shingles
Tear off, haul and dispose of comp. shingles - Laminated | SQ | 52.56 | 0.00 | Roofing | tearoff,disposal | Laminated shingle removal
Roofing felt - 15 lb. | SQ | 18.00 | 0.00 | Roofing | felt,underlayment | Standard felt underlayment
Drip edge | LF | 1.35 | 0.00 | Roofing | flashing,edge | Drip edge installation
Drip edge/gutter apron | LF | 1.48 | 0.00 | Roofing | flashing,gutter | Gutter apron installation
Ice & water shield | SF | 1.02 | 0.00 | Roofing | waterproofing,membrane | Ice & water shield membrane
Roof vent - turtle type - Metal | EA | 35.84 | 36.78 | Roofing | vent,metal | Metal turtle vent
Roof vent - turtle type - Plastic | EA | 31.08 | 31.74 | Roofing | vent,plastic | Plastic turtle vent
Roof vent - turbine type | EA | 80.46 | 83.84 | Roofing | vent,turbine | Spinning turbine vent
R&R Power attic vent cover only - metal | EA | 66.83 | 68.62 | Roofing | vent,attic | Metal attic vent cover
Flashing - pipe jack | EA | 20.85 | 21.19 | Roofing | flashing,pipe | Pipe jack flashing
Flashing - pipe jack - lead | EA | 49.36 | 51.41 | Roofing | flashing,lead | Lead pipe jack flashing
R&R Flashing - pipe jack - split boot | EA | 52.54 | 54.38 | Roofing | flashing,boot | Split boot flashing
Furnace vent - rain cap and storm collar, 5" | EA | 45.50 | 46.53 | Roofing | vent,furnace | Furnace vent (5”)
Furnace vent - rain cap and storm collar, 8" | EA | 61.74 | 63.75 | Roofing | vent,furnace | Furnace vent (8”)
R&R Exhaust cap - through roof - 6" to 8" | EA | 59.62 | 61.36 | Roofing | vent,exhaust | Exhaust roof cap

Example Macro
line_items | unit_code | UNIT_PRICE | TAX | category | tags | notes
R&R Toilet | EA | 541.53 | 19.65 | Plumbing | toilet,replace | Replace standard two-piece incl. wax ring
Drywall remove (damaged up to 2 ft) | SF | 2.25 | 0.00 | Demolition | drywall,remove | Selective demo to studs
Drywall install MR 1/2" | SF | 3.00 | 0.00 | Drywall | drywall,install | Moisture-resistant board
Tape & float L4 | SF | 1.50 | 0.00 | Drywall | drywall,finish | Blend with existing
Prime stain-blocker | SF | 0.60 | 0.00 | Painting | primer,stain | Block water stains
Paint wall (2 coats) | SF | 1.40 | 0.00 | Painting | paint,wall | Color match to nearest break
Antimicrobial treatment | SF | 0.75 | 0.00 | Mitigation | antimicrobial | Treat exposed framing/backing
"""

FIRE_KNOWLEDGE_BASE = r"""
line_items | unit_code | UNIT_PRICE | TAX | category | tags | notes
Soot wipe-down (light) | SF | 0.85 | 0.00 | Cleaning | fire,soot | Light residue removal
HEPA vacuuming | HR | 55.00 | 0.00 | Cleaning | fire,hepa | HEPA vac per hour
Seal odor-block primer | SF | 1.20 | 0.00 | Painting | fire,sealer | Shellac/blocking primer
Deodorize – ozone | DAY | 80.00 | 0.00 | Remediation | fire,odor | Ozone cycle, contained area
"""

WIND_KNOWLEDGE_BASE = r"""
line_items | unit_code | UNIT_PRICE | TAX | category | tags | notes
Shingle reset/replace (architectural) | SQ | 295.00 | 0.00 | Roofing | wind,shingles | Removal, install, nails
Roof felt underlayment | SQ | 45.00 | 0.00 | Roofing | wind,felt | Synthetic
Starter strip | LF | 1.25 | 0.00 | Roofing | wind,starter | Per linear foot
Drip edge | LF | 2.10 | 0.00 | Roofing | wind,edge | Aluminum drip edge

Table index: Roof 1-179, 280-296, 300-365, 490-524                    
Awning 180-184
Water (walls, ceilings, floors 185-198, 199-206, 258-279, 454-457, 458-469
Tree Removal 207-216, 427-443
Deck + Patio 217-219, 297-347,
Fascia 220-231, 253-257, 381-389, 402-411, 418-426, 444-453
Fence 232-238, 
Gutter 239-252
Screen 365-370, window-door- 470-472, 474-489, 525-533
Siding 371-401                    Shed 415-417"			
													
DESCRIPTION | QUANTITY | UNIT | PRICE | TAX | RCV | DEPREC.| ACV		
The following line items are to replace the roof on this structure.																
1. 3 tab - 25 yr. - comp. shingle roofing - w/out felt | 0.00 SQ | 138.43 |0.00 |0.00 |0.00 | 0.00		
2. Remove Tear off, haul and dispose of comp. shingles  | 0.00 SQ |40.87
3. Roofing felt - 15 lb. | 0.00 SQ | 18.00 |0.00 | 0.00 | 0.00 | 0.00		
4. Drip edge | 0.00 LF | 1.35 | 0.00 | 0.00 | 0.00 | 0.00
5. Drip edge/gutter apron | 0.00 LF | 1.48 | 0.00 | 0.00 | 0.00 | 0.00
6. Ice & water shield | 0.00 SF |1.02 | 0.00 | 0.00 | 0.00 | 0.00		
7.  Roof vent - turtle type - Metal | 1.00 EA | 35.84 | 0.94 | 36.78 | 0.00 | 36.78
8.  Roof vent - turtle type - Plastic | 1.00 EA | 31.08 | 0.66 | 31.74 | 0.00 | 31.74
9.  Roof vent - turbine type | 1.00 EA | 80.46 | 3.38 | 83.84 | 0.00 | 83.84
10.  R&R Power attic vent cover only - metal | 1.00 EA | 66.83 | 1.79 | 68.62 | 0.00 | 68.62
11.  Flashing - pipe jack | 1.00 EA | 20.85 | 0.34 | 21.19 | 0.00 | 21.19
12.  Flashing - pipe jack - lead | 1.00 EA | 49.36 | 2.05 | 51.41 | 0.00 | 51.41
13.  R&R Flashing - pipe jack - split boot | 1.00 EA | 52.54 | 1.84 | 54.38 | 0.00 | 54.38 | Typically used for power mast roof penetration.																
14.  Digital satellite system - Detach & reset | 1.00 EA | 23.78 | 0.00 | 23.78 | 0.00 | 23.78
15.  Continuous ridge vent - shingle-over style | 0.00 LF | 5.37 | 0.00 | 0.00 | 0.00 | 0.00
16.  Ridge cap - composition shingles | 0.00 LF | 3.19 | 0.00 | 0.00 | 0.00 | 0.00
17.  Furnace vent - rain cap and storm collar, 5" | 1.00 EA | 45.50	 | 1.03 | 46.53 | 0.00 | 46.53
18.  Furnace vent - rain cap and storm collar, 8" | 1.00 EA | 61.74 | 2.01 | 63.75 | 0.00 | 63.75
19.  R&R Exhaust cap - through roof - 6" to 8" | 1.00 EA | 59.62 | 1.74 | 61.36 | 0.00 | 61.36
20.  Additional charge for high roof (2 stories or greater) | 0.00 SQ | 9.35 | 0.00 | 0.00 | 0.00 | 0.00
21.  Additional charge for steep roof - 7/12 to 9/12 slope | 0.00 SQ | 21.17 | 0.00 | 0.00 | 0.00 | 0.00
22.  Additional charge for steep roof - 10/12 - 12/12 slope | 0.00 SQ | 33.26 | 0.00 | 0.00 | 0.00 | 0.00
23.  Flashing - rain diverter | 1.00 EA | 22.94 | 0.54 | 23.48 | 0.00 | 23.48
24.  Valley metal | 0.00 LF | 3.33 | 0.00 | 0.00 | 0.00 | 0.00
25.  Valley metal - (W) profile | 0.00 LF | 4.01 | 0.00 | 0.00 | 0.00 | 0.00
26.  Chimney flashing - average (32" x 36") | 1.00 EA | 201.06 | 3.21 | 204.27 | 0.00 | 204.27		
27.  Remove Lightning protection system | 1.00 EA | 161.48 | 0.00 | 161.48 | 0.00 | 161.48 | Detach and reset lightning protection system.																
28.  Install Lightning protection system | 1.00 EA  | 1,483.11									0.00		1,483.11		0.00 	1,483.11		
29.  R&R Cupola - Wood - Small                                                   1.00 EA              560.10									26.06		586.16		0.00 	586.16		
30.  Laminated - comp. shingle rfg. - w/out felt                             0.00 SQ               153.11									0.00		0.00		0.00 	0.00		
"31.  Tear off, haul and dispose of comp. shingles -                        0.00 SQ                 52.56
Laminated"									0.00		0.00		0.00 	0.00		
32.  Roofing felt - 15 lb.                                                                  0.00 SQ                 18.00									0.00		0.00		0.00 	0.00		
33.  Drip edge                                                                                  0.00 LF                   1.35									0.00		0.00		0.00 	0.00		
34.  Drip edge/gutter apron                                                             0.00 LF                   1.48									0.00		0.00		0.00 	0.00		
35.  Ice & water shield                                                                    0.00 SF                   1.02									0.00		0.00		0.00 	0.00		
36.  Roof vent - turtle type - Metal                                                 1.00 EA                35.84									0.94		36.78		0.00 	36.78		
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
37.  Roof vent - turtle type - Plastic			1.00 EA				31.08		0.66		31.74		0.00 	31.74		
38.  Roof vent - turbine type			1.00 EA				80.46		3.38		83.84		0.00 	83.84		
39.  R&R Power attic vent cover only - metal			1.00 EA				66.83		1.79		68.62		0.00 	68.62		
40.  Flashing - pipe jack			1.00 EA				20.85		0.34		21.19		0.00 	21.19		
41.  Flashing - pipe jack - lead			1.00 EA				49.36		2.05		51.41		0.00 	51.41		
"42.  R&R Flashing - pipe jack - split boot Typically used for power mast roof penetration. Typically used for power mast roof penetration.
43.  Digital satellite system - Detach & reset"			"1.00 EA
1.00 EA"				"52.54
23.78"		"1.84
0.00"		"54.38
23.78"		"(0.00)
(0.00)"	"54.38
23.78"		
44.  Continuous ridge vent - shingle-over style			0.00 LF				5.37		0.00		0.00		0.00 	0.00		
45.  Ridge cap - composition shingles			0.00 LF				3.19		0.00		0.00		0.00 	0.00		
46.  Furnace vent - rain cap and storm collar, 5"			1.00 EA				45.50		1.03		46.53		0.00 	46.53		
47.  Furnace vent - rain cap and storm collar, 8"			1.00 EA				61.74		2.01		63.75		0.00 	63.75		
48.  R&R Exhaust cap - through roof - 6" to 8"			1.00 EA				59.62		1.74		61.36		0.00 	61.36		
49.  Additional charge for high roof (2 stories or greater)			0.00 SQ				9.35		0.00		0.00		0.00 	0.00		
50.  Additional charge for steep roof - 7/12 to 9/12 slope			0.00 SQ				21.17		0.00		0.00		0.00 	0.00		
51.  Additional charge for steep roof - 10/12 - 12/12 slope			0.00 SQ				33.26		0.00		0.00		0.00 	0.00		
52.  Flashing - rain diverter			1.00 EA				22.94		0.54		23.48		0.00 	23.48		
53.  Valley metal			0.00 LF				3.33		0.00		0.00		0.00 	0.00		
54.  Valley metal - (W) profile			0.00 LF				4.01		0.00		0.00		0.00 	0.00		
55.  Chimney flashing - average (32" x 36")			1.00 EA				201.06		3.21		204.27		0.00 	204.27		
"56.  Remove Lightning protection system Detach and reset lightning protection system. Detach and reset lightning protection system.
57.  Install Lightning protection system"			"1.00 EA
1.00 EA"				"161.48
1,483.11"		"0.00
0.00"		"161.48
1,483.11"		"(0.00)
(0.00)"	"161.48
1,483.11"		
58.  R&R Cupola - Wood - Small			1.00 EA				560.10		26.06		586.16		0.00 	586.16		
The following line items are to repair the XXXXXX slope of the roof damaged by wind.																
59.  R&R Laminated - comp. shingle rfg (per SHINGLE)			12.00 EA				11.55		1.29		139.89		0.00 	139.89		
60.  R&R Roof vent - turtle type - Metal			1.00 EA				42.27		0.94		43.21		0.00 	43.21		
61.  R&R Roof vent - turtle type - Plastic			1.00 EA				37.51		0.66		38.17		0.00 	38.17		
62.  R&R Roof vent - turbine type			1.00 EA				86.89		3.38		90.27		0.00 	90.27		
63.  R&R Ridge cap - composition shingles			12.00 LF				4.48		0.78		54.54		0.00 	54.54		
64.  R&R Continuous ridge vent - shingle-over style			12.00 LF				5.98		2.05		73.81		0.00 	73.81		
65.  R&R Continuous ridge vent - aluminum			12.00 LF				5.93		2.02		73.18		0.00 	73.18		
66.  R&R Flashing - pipe jack			1.00 EA				25.89		0.34		26.23		0.00 	26.23		
67.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
68.  R&R Exhaust cap - through roof - 6" to 8"			1.00 EA				59.62		1.74		61.36		0.00 	61.36		
69.  R&R Furnace vent - rain cap and storm collar, 5"			1.00 EA				53.16		1.03		54.19		0.00 	54.19		
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
70.  R&R Furnace vent - rain cap and storm collar, 6"			1.00 EA				60.11		1.45		61.56		0.00 	61.56		
71.  R&R Furnace vent - rain cap and storm collar, 8"			1.00 EA				69.40		2.01		71.41		0.00 	71.41		
72.  Flue cap			1.00 EA				96.06		4.82		100.88		0.00 	100.88		
73.  R&R Fireplace - chimney chase cover - sheetmetal			1.00 EA				340.90		11.53		352.43		0.00 	352.43		
74.  Remove Additional charge for high roof (2 stories or greater)			2.00 SQ				3.77		0.00		7.54		0.00 	7.54		
75.  Additional charge for high roof (2 stories or greater)			2.00 SQ				9.35		0.00		18.70		0.00 	18.70		
76.  Remove Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ				9.99		0.00		19.98		0.00 	19.98		
77.  Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ				21.17		0.00		42.34		0.00 	42.34		
78.  Remove Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ				15.71		0.00		31.42		0.00 	31.42		
79.  Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ				33.26		0.00		66.52		0.00 	66.52		
80.  Remove Additional charge for steep roof greater than 12/12 slope			2.00 SQ				19.50		0.00		39.00		0.00 	39.00		
81.  Additional charge for steep roof greater than 12/12 slope			2.00 SQ				42.07		0.00		84.14		0.00 	84.14		
The following line items are to repair the XXXXXXX slope of the roof damaged by wind.																
"82.
(per"	R&R 3 tab - 25 yr. - composition shingle roofing SHINGLE)		12.00 EA				11.35		1.14		137.34		0.00 	137.34		
83.	R&R Roof vent - turtle type - Metal		1.00 EA				42.27		0.94		43.21		0.00 	43.21		
84.	R&R Roof vent - turtle type - Plastic		1.00 EA				37.51		0.66		38.17		0.00 	38.17		
85.	R&R Roof vent - turbine type		1.00 EA				86.89		3.38		90.27		0.00 	90.27		
86.	R&R Ridge cap - composition shingles		12.00 LF				4.48		0.78		54.54		0.00 	54.54		
87.	R&R Continuous ridge vent - shingle-over style		12.00 LF				5.98		2.05		73.81		0.00 	73.81		
88.	R&R Continuous ridge vent - aluminum		12.00 LF				5.93		2.02		73.18		0.00 	73.18		
89.	R&R Flashing - pipe jack		1.00 EA				25.89		0.34		26.23		0.00 	26.23		
90.	R&R Flashing - pipe jack - split boot		1.00 EA				52.54		1.84		54.38		0.00 	54.38		
91.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA				59.62		1.74		61.36		0.00 	61.36		
92.	R&R Furnace vent - rain cap and storm collar, 5"		1.00 EA				53.16		1.03		54.19		0.00 	54.19		
93.	R&R Furnace vent - rain cap and storm collar, 6"		1.00 EA				60.11		1.45		61.56		0.00 	61.56		
94.	R&R Furnace vent - rain cap and storm collar, 8"		1.00 EA				69.40		2.01		71.41		0.00 	71.41		
95.	Flue cap		1.00 EA				96.06		4.82		100.88		0.00 	100.88		
96.	R&R Fireplace - chimney chase cover - sheetmetal		1.00 EA				340.90		11.53		352.43		0.00 	352.43		
97.	Remove Additional charge for high roof (2 stories or		2.00 SQ				3.77		0.00		7.54		0.00 	7.54		
greater)																
98.  Additional charge for high roof (2 stories or greater)			2.00 SQ				9.35		0.00		18.70		0.00 	18.70		
99.  Remove Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ				9.99		0.00		19.98		0.00 	19.98		
100.  Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ				21.17		0.00		42.34		0.00 	42.34		
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION                                                                   QUANTITY   UNIT							PRICE		TAX		RCV		DEPREC.	ACV		
101.  Remove Additional charge for steep roof - 10/12 -               2.00 SQ 12/12 slope							15.71		0.00		31.42		0.00 	31.42		
102.  Additional charge for steep roof - 10/12 - 12/12                   2.00 SQ slope							33.26		0.00		66.52		0.00 	66.52		
103.  Remove Additional charge for steep roof greater                  2.00 SQ than 12/12 slope							19.50		0.00		39.00		0.00 	39.00		
104.  Additional charge for steep roof greater than 12/12              2.00 SQ slope							42.07		0.00		84.14		0.00 	84.14		
The following line items are to replace the roof on this structure.																
105.  Laminated - High grd - comp. shingle rfg. - w/out                0.00 SQ felt							183.90		0.00		0.00		0.00 	0.00		
106.  Remove Tear off, haul and dispose of comp.                        0.00 SQ shingles - 3 tab							40.87		0.00		0.00		0.00 	0.00		
107.  Roofing felt - 15 lb.                                                                0.00 SQ							18.00		0.00		0.00		0.00 	0.00		
108.  Drip edge                                                                                0.00 LF							1.35		0.00		0.00		0.00 	0.00		
109.  Drip edge/gutter apron                                                           0.00 LF							1.48		0.00		0.00		0.00 	0.00		
110.  Ice & water shield                                                                  0.00 SF							1.02		0.00		0.00		0.00 	0.00		
111.  Roof vent - turtle type - Metal                                               1.00 EA							35.84		0.94		36.78		0.00 	36.78		
112.  Roof vent - turtle type - Plastic                                              1.00 EA							31.08		0.66		31.74		0.00 	31.74		
113.  Roof vent - turbine type                                                         1.00 EA							80.46		3.38		83.84		0.00 	83.84		
114.  R&R Power attic vent cover only - metal                              1.00 EA							66.83		1.79		68.62		0.00 	68.62		
115.  Flashing - pipe jack                                                                1.00 EA							20.85		0.34		21.19		0.00 	21.19		
116.  Flashing - pipe jack - lead                                                      1.00 EA							49.36		2.05		51.41		0.00 	51.41		
117.  R&R Flashing - pipe jack - split boot                                    1.00 EA							52.54		1.84		54.38		0.00 	54.38		
Typically used for power mast roof penetration.																
118.	Digital satellite system - Detach & reset		1.00 EA				23.78		0.00		23.78		0.00 	23.78		
119.	Continuous ridge vent - shingle-over style		0.00 LF				5.37		0.00		0.00		0.00 	0.00		
120.	Ridge cap - composition shingles		0.00 LF				3.19		0.00		0.00		0.00 	0.00		
121.	Furnace vent - rain cap and storm collar, 5"		1.00 EA				45.50		1.03		46.53		0.00 	46.53		
122.	Furnace vent - rain cap and storm collar, 8"		1.00 EA				61.74		2.01		63.75		0.00 	63.75		
123.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA				59.62		1.74		61.36		0.00 	61.36		
124.	Additional charge for high roof (2 stories or greater)		0.00 SQ				9.35		0.00		0.00		0.00 	0.00		
125.	Additional charge for steep roof - 7/12 to 9/12 slope		0.00 SQ				21.17		0.00		0.00		0.00 	0.00		
"126.
slope"	Additional charge for steep roof - 10/12 - 12/12		0.00 SQ				33.26		0.00		0.00		0.00 	0.00		
127.	Flashing - rain diverter		1.00 EA				22.94		0.54		23.48		0.00 	23.48		
128.	Valley metal		0.00 LF				3.33		0.00		0.00		0.00 	0.00		
129.	Valley metal - (W) profile		0.00 LF				4.01		0.00		0.00		0.00 	0.00		
130.	Chimney flashing - average (32" x 36")		1.00 EA				201.06		3.21		204.27		0.00 	204.27		
131.	Remove Lightning protection system		1.00 EA				161.48		0.00		161.48		0.00 	161.48		
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY		UNIT PRICE				TAX		RCV		DEPREC.	ACV		
Detach and reset lightning protection system.																
132.  Install Lightning protection system			1.00 EA		1,483.11				0.00		1,483.11		0.00 	1,483.11		
133.  R&R Cupola - Wood - Small			1.00 EA		560.10				26.06		586.16		0.00 	586.16		
The following line items are to repair the XXXXXX slope of the roof damaged by wind.																
"134.
(per"	R&R Laminated - High grade - comp. shingle rfg. SHINGLE)		12.00 EA		12.32				1.60		149.44		0.00 	149.44		
135.	R&R Roof vent - turtle type - Metal		1.00 EA		42.27				0.94		43.21		0.00 	43.21		
136.	R&R Roof vent - turtle type - Plastic		1.00 EA		37.51				0.66		38.17		0.00 	38.17		
137.	R&R Roof vent - turbine type		1.00 EA		86.89				3.38		90.27		0.00 	90.27		
138.	R&R Ridge cap - composition shingles		12.00 LF		4.48				0.78		54.54		0.00 	54.54		
139.	R&R Continuous ridge vent - shingle-over style		12.00 LF		5.98				2.05		73.81		0.00 	73.81		
140.	R&R Continuous ridge vent - aluminum		12.00 LF		5.93				2.02		73.18		0.00 	73.18		
141.	R&R Flashing - pipe jack		1.00 EA		25.89				0.34		26.23		0.00 	26.23		
142.	R&R Flashing - pipe jack - split boot		1.00 EA		52.54				1.84		54.38		0.00 	54.38		
143.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA		59.62				1.74		61.36		0.00 	61.36		
144.	R&R Furnace vent - rain cap and storm collar, 5"		1.00 EA		53.16				1.03		54.19		0.00 	54.19		
145.	R&R Furnace vent - rain cap and storm collar, 6"		1.00 EA		60.11				1.45		61.56		0.00 	61.56		
146.	R&R Furnace vent - rain cap and storm collar, 8"		1.00 EA		69.40				2.01		71.41		0.00 	71.41		
147.	Flue cap		1.00 EA		96.06				4.82		100.88		0.00 	100.88		
148.	R&R Fireplace - chimney chase cover - sheetmetal		1.00 EA		340.90				11.53		352.43		0.00 	352.43		
149.	Remove Additional charge for high roof (2 stories		2.00 SQ		3.77				0.00		7.54		0.00 	7.54		
or greater)																
150.  Additional charge for high roof (2 stories or greater)			2.00 SQ		9.35				0.00		18.70		0.00 	18.70		
151.  Remove Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ		9.99				0.00		19.98		0.00 	19.98		
152.  Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ		21.17				0.00		42.34		0.00 	42.34		
153.  Remove Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ		15.71				0.00		31.42		0.00 	31.42		
154.  Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ		33.26				0.00		66.52		0.00 	66.52		
155.  Remove Additional charge for steep roof greater than 12/12 slope			2.00 SQ		19.50				0.00		39.00		0.00 	39.00		
156.  Additional charge for steep roof greater than 12/12 slope			2.00 SQ		42.07				0.00		84.14		0.00 	84.14		
The following line items are to repair the XXXXXX slope of the roof damaged by wind.																
157.  R&R Laminated - Deluxe grd - comp. shingle rfg. (per SHINGLE)			12.00 EA		13.06				1.64		158.36		0.00 	158.36		
158.  R&R Roof vent - turtle type - Metal			1.00 EA		42.27				0.94		43.21		0.00 	43.21		
159.  R&R Roof vent - turtle type - Plastic			1.00 EA		37.51				0.66		38.17		0.00 	38.17		
160.  R&R Roof vent - turbine type			1.00 EA		86.89				3.38		90.27		0.00 	90.27		
161.  R&R Ridge cap - composition shingles			12.00 LF		4.48				0.78		54.54		0.00 	54.54		
																
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY		UNIT PRICE				TAX		RCV		DEPREC.	ACV		
162.  R&R Continuous ridge vent - shingle-over style			12.00 LF		5.98				2.05		73.81		0.00 	73.81		
163.  R&R Continuous ridge vent - aluminum			12.00 LF		5.93				2.02		73.18		0.00 	73.18		
164.  R&R Flashing - pipe jack			1.00 EA		25.89				0.34		26.23		0.00 	26.23		
165.  R&R Flashing - pipe jack - split boot			1.00 EA		52.54				1.84		54.38		0.00 	54.38		
166.  R&R Exhaust cap - through roof - 6" to 8"			1.00 EA		59.62				1.74		61.36		0.00 	61.36		
167.  R&R Furnace vent - rain cap and storm collar, 5"			1.00 EA		53.16				1.03		54.19		0.00 	54.19		
168.  R&R Furnace vent - rain cap and storm collar, 6"			1.00 EA		60.11				1.45		61.56		0.00 	61.56		
169.  R&R Furnace vent - rain cap and storm collar, 8"			1.00 EA		69.40				2.01		71.41		0.00 	71.41		
170.  Flue cap			1.00 EA		96.06				4.82		100.88		0.00 	100.88		
171.  R&R Fireplace - chimney chase cover - sheetmetal			1.00 EA		340.90				11.53		352.43		0.00 	352.43		
172.  Remove Additional charge for high roof (2 stories			2.00 SQ		3.77				0.00		7.54		0.00 	7.54		
or greater)																
173.  Additional charge for high roof (2 stories or greater)			2.00 SQ		9.35				0.00		18.70		0.00 	18.70		
174.  Remove Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ		9.99				0.00		19.98		0.00 	19.98		
175.  Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ		21.17				0.00		42.34		0.00 	42.34		
176.  Remove Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ		15.71				0.00		31.42		0.00 	31.42		
177.  Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ		33.26				0.00		66.52		0.00 	66.52		
178.  Remove Additional charge for steep roof greater than 12/12 slope			2.00 SQ		19.50				0.00		39.00		0.00 	39.00		
179.  Additional charge for steep roof greater than 12/12 slope			2.00 SQ		42.07				0.00		84.14		0.00 	84.14		
The following line items are to replace the awnings on the front, right, back, and left sides of the building.																
180.  R&R Awning - Window/door - Alum./stl. (Oversized)			6.00 LF		78.34				21.60		491.64		0.00 	491.64		
181.  R&R Awning side panels - Alum./steel (Oversized) (PER SET)			1.00 EA		99.62				4.30		103.92		0.00 	103.92		
182.  Awning - Aluminum or steel - Add for each color stripe			2.00 EA		5.50				0.66		11.66		0.00 	11.66		
183.  Haul debris - per pickup truck load - including dump fees			1.00 EA		111.18				0.00		111.18		0.00 	111.18		
184.  Two ladders with jacks and plank (per day)			1.00 DA		104.12				0.00		104.12		0.00 	104.12		
The following line items are to repair water damage to the walls and flooring in this room.																
185.  R&R Batt insulation - 4" - R13 - unfaced batt			0.00 SF		0.73				0.00		0.00		0.00 	0.00		
186.  Drywall replacement per LF - up to 2' tall			0.00 LF		6.93				0.00		0.00		0.00 	0.00		
187.  Seal/prime then paint  (2 coats)			0.00 SF		0.58				0.00		0.00		0.00 	0.00		
188.  R&R Wallpaper			0.00 SF		2.26				0.00		0.00		0.00 	0.00		
189.  R&R Baseboard - 2 1/4"			0.00 LF		2.22				0.00		0.00		0.00 	0.00		
190.  Paint baseboard - one coat			0.00 LF		0.57				0.00		0.00		0.00 	0.00		
																														
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY		UNIT PRICE				TAX		RCV		DEPREC.	ACV		
191.  R&R Vinyl floor covering (sheet goods)			0.00 SF		3.50				0.00		0.00		0.00 	0.00		
192.  R&R Underlayment - 1/4" lauan/mahogany plywood			0.00 SF		1.51				0.00		0.00		0.00 	0.00		
193.  R&R Vanity			3.00 LF		128.12				17.64		402.00		0.00 	402.00		
194.  Sink faucet - Detach & reset			1.00 EA		74.20				0.00		74.20		0.00 	74.20		
195.  P-trap assembly - Detach & reset			1.00 EA		47.28				0.00		47.28		0.00 	47.28		
196.  R&R Angle stop valve			1.00 EA		33.47				0.43		33.90		0.00 	33.90		
197.  Install Claw-foot tub supply lines			1.00 EA		103.13				0.00		103.13		0.00 	103.13		
198.  Toilet - Detach & reset			1.00 EA		151.02				0.27		151.29		0.00 	151.29		
The following line items are to repair water damage to the walls and ceiling in this room.																
199.  R&R Blown-in insulation - 12" depth - R30			10.00 SF		1.89				0.38		19.28		0.00 	19.28		
200.  R&R 5/8" drywall - hung, taped, floated, ready for paint			10.00 SF		2.34				0.34		23.74		0.00 	23.74		
201.  Apply anti-microbial agent to the surface area			10.00 SF		0.20				0.02		2.02		0.00 	2.02		
Application of anti-microbial agent to framing members to inhibit growth.																
202.  Seal the surface area w/latex based stain blocker - one coat			10.00 SF		0.54				0.04		5.44		0.00 	5.44		
203.  Paint  - two coats			0.00 SF		0.88				0.00		0.00		0.00 	0.00		
204.  R&R Acoustic ceiling (popcorn) texture			0.00 SF		1.21				0.00		0.00		0.00 	0.00		
205.  Texture drywall - light hand texture			0.00 SF		0.48				0.00		0.00		0.00 	0.00		
206.  Contents - move out then reset			1.00 EA		50.12				0.00		50.12		0.00 	50.12		
207.  Tree - removal and disposal - per hour including equipment			16.00 HR		70.37				0.00		1,125.92		0.00 	1,125.92		
"This line item is allowance to remove tree from structure so that repairs can be made.
Labor and equipment for 2 person, 8 hours each, to remove tree limbs and debris."																
208.  Crane and operator - 14 ton capacity - 65' extension boom			4.00 HR				171.33		0.00		685.32		0.00 	685.32		
209.  Skid steer loader and operator			4.00 HR				67.58		0.00		270.32		0.00 	270.32		
210.  Boom truck and operator - 20 ton			4.00 HR				106.00		0.00		424.00		0.00 	424.00		
The following line items are to replace the deck on the front, right, back, left side of the house.																
211.  R&R Deck planking - treated lumber (per SF)			0.00 SF				5.72		0.00		0.00		0.00 	0.00		
212.  R&R Deck planking - 5/4" treated lumber, 2 (per SF)			0.00 SF				5.83		0.00		0.00		0.00 	0.00		
213.  R&R Deck planking - Vinyl (per SF)			0.00 SF				9.46		0.00		0.00		0.00 	0.00		
214.  R&R Deck guard rail - treated lumber			10.00 LF				22.78		5.42		233.22		0.00 	233.22		
215.  R&R Deck guard rail - Vinyl			10.00 LF				42.49		15.80		440.70		0.00 	440.70		
216.  Dumpster load - Approx. 20 yards, 4 tons of debris			1.00 EA				420.00		0.00		420.00		0.00 	420.00		
The following line items are to pressure wash and restain the deck on the front, right, back, left side of the house.																
217.  Clean with pressure/chemical spray			1.00 SF				0.21		0.00		0.21		0.00 	0.21		
218.  Stain/finish deck			1.00 SF				0.58		0.01		0.59		0.00 	0.59		
															
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT PRICE						TAX		RCV		DEPREC.	ACV		
219.  Stain/finish deck handrail			1.00 LF                   4.22						0.06		4.28		0.00 	4.28		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
220.  R&R Fascia - metal - 4"			24.00 LF				2.96		1.27		72.31		0.00 	72.31		
221.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
222.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
223.  R&R Fascia - metal - 6"			24.00 LF				3.35		1.71		82.11		0.00 	82.11		
224.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
225.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
226.  R&R Fascia - metal - 8"			24.00 LF				3.65		1.92		89.52		0.00 	89.52		
227.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
228.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the dwelling on the XXXXXXX side of the house.																
229.  R&R Wrap custom fascia with aluminum (PER LF)			24.00 LF				9.92		2.66		240.74		0.00 	240.74		
230.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
231.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to replace the fence on the XXXXXXX side of the house, damaged by XXXXXXXX.																
232.  R&R Wood fence 5'- 6' high - treated			27.00 LF				22.90		15.67		633.97		0.00 	633.97		
233.  R&R Wood gate 5'- 6' high - treated			3.00 LF				30.91		2.71		95.44		0.00 	95.44		
234.  Seal & paint - wood fence/gate			162.00 SF				0.81		3.30		134.52		0.00 	134.52		
235.  R&R Temporary fencing			27.00 LF				5.48		0.00		147.96		0.00 	147.96		
236.  Single axle dump truck - per load - including dump fees			1.00 EA				204.41		0.00		204.41		0.00 	204.41		
The following line items are to pressure wash and restain the fence on the front, right, back, left side of the house.																
237.  Clean with pressure/chemical spray			1.00 SF				0.21		0.00		0.21		0.00 	0.21		
238.  Seal & paint - wood fence/gate			1.00 SF				0.81		0.02		0.83		0.00 	0.83		
"The following line items are to repair wind damage to the gutters and downspouts on the XXXXXXX side of the house.
Depreciation is based on the age and condition of the item.  The gutters are XXXX years old and have a 25 year average useful lifespan.  XX% depreciation withheld."																
239.  R&R Gutter / downspout - aluminum - up to 5"			24.00 LF				4.69		3.31		115.87		0.00 	115.87		
240.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
241.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
GUTTER WIND REPAIR MACROS																
																
																
																
																
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION                                                                   QUANTITY   UNIT PRICE								TAX			RCV        DEPREC.               ACV					
"The following line items are to repair wind damage to the gutters and downspouts on the XXXXXXX side of the house.
Depreciation is based on the age and condition of the item.  The gutters are XXXX years old and have a 25 year average useful lifespan.  XX% depreciation withheld."																
242.  R&R Gutter / downspout - galvanized - up to 5"			12.00 LF				3.91		1.09		48.01		0.00 	48.01		
243.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
244.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
GUTTER WIND REPAIR MACROS																
"The following line items are to repair wind damage to the gutters and downspouts on the XXXXXXX side of the house.
Depreciation is based on the age and condition of the item.  The gutters are XXXX years old and have a 25 year average useful lifespan.  XX% depreciation withheld."																
245.  R&R Gutter / downspout - plastic			12.00 LF				4.18		1.29		51.45		0.00 	51.45		
246.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
247.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to replace the gutters and downspouts on this building.																
"Front:
Gutters - 10LF Downspouts - 10:F"																
"Right:
Gutters - 10LF Downspouts - 10LF"																
"Back:
Gutters - 10LF Downspouts - 10LF"																
"Left:
Gutters - 10LF Downspouts - 10LF"																
248.  R&R Gutter / downspout - aluminum - up to 5"			100.00 LF				4.69		13.80		482.80		0.00 	482.80		
249.  R&R Gutter / downspout - galvanized - up to 5"			100.00 LF				3.91		9.12		400.12		0.00 	400.12		
250.  Prime & paint gutter / downspout			100.00 LF				1.04		1.50		105.50		0.00 	105.50		
251.  R&R Gutter / downspout - plastic			100.00 LF				4.18		10.74		428.74		0.00 	428.74		
252.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the dwelling on the XXXXXXX side of the house.																
253.  R&R Siding - hardboard - sheet			32.00 SF				2.34		2.11		76.99		0.00 	76.99		
254.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
255.  R&R House wrap (air/moisture barrier)			0.00 SF				0.26		0.00		0.00		0.00 	0.00		
256.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
257.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair water damage to the walls and flooring in this room.																
258.  R&R Batt insulation - 4" - R13 - unfaced batt			0.00 SF				0.73		0.00		0.00		0.00 	0.00		
259.  Drywall replacement per LF - up to 2' tall			0.00 LF				6.93		0.00		0.00		0.00 	0.00		
260.  Seal/prime then paint  (2 coats)			0.00 SF				0.58		0.00		0.00		0.00 	0.00		
261.  R&R Wallpaper			0.00 SF				2.26		0.00		0.00		0.00 	0.00		
262.  R&R Baseboard - 2 1/4"			0.00 LF				2.22		0.00		0.00		0.00 	0.00		
263.  Paint baseboard - one coat			0.00 LF				0.57		0.00		0.00		0.00 	0.00		
264.  R&R Vinyl floor covering (sheet goods)			0.00 SF				3.50		0.00		0.00		0.00 	0.00		
265.  R&R Underlayment - 1/4" lauan/mahogany plywood			0.00 SF				1.51		0.00		0.00		0.00 	0.00		
266.  R&R Vanity			3.00 LF				128.12		17.64		402.00		0.00 	402.00		
267.  Sink faucet - Detach & reset			1.00 EA				74.20		0.00		74.20		0.00 	74.20		
268.  Dishwasher - Detach & reset			1.00 EA				168.65		0.00		168.65		0.00 	168.65		
269.  Garbage disposer - Detach & reset			1.00 EA				99.14		0.00		99.14		0.00 	99.14		
270.  Range - gas - Remove & reset			1.00 EA				99.14		0.00		99.14		0.00 	99.14		
271.  Refrigerator - Remove & reset			1.00 EA				27.50		0.00		27.50		0.00 	27.50		
272.  R&R Cabinetry - lower (base) units			5.00 LF				157.12		38.10		823.70		0.00 	823.70		
273.  R&R Cabinetry - upper (wall) units			5.00 LF				114.45		25.30		597.55		0.00 	597.55		
274.  R&R Cabinetry - full height unit			2.00 LF				261.13		26.80		549.06		0.00 	549.06		
275.  R&R Countertop - post formed plastic laminate			15.00 LF				45.05		29.38		705.13		0.00 	705.13		
276.  R&R Countertop - flat laid plastic laminate			15.00 LF				37.63		23.41		587.86		0.00 	587.86		
277.  Add on for undermount sink cutout & polish -			1.00 EA				153.66		0.00		153.66		0.00 	153.66		
double basin																
278.  Add-on for mitered corner (Countertop)				2.00 EA			57.08		0.00		114.16		0.00 	114.16		
279.  Sink - double - Detach & reset				1.00 EA			98.20		0.00		98.20		0.00 	98.20		
The following line items are to repair the roof damaged by wind.																
280.  R&R Modified bitumen roof			1.00 SQ				289.14		5.71		294.85		0.00 	294.85		
281.  R&R Roof vent - turtle type - Metal			1.00 EA				42.27		0.94		43.21		0.00 	43.21		
282.  R&R Roof vent - turtle type - Plastic			1.00 EA				37.51		0.66		38.17		0.00 	38.17		
283.  R&R Roof vent - turbine type			1.00 EA				86.89		3.38		90.27		0.00 	90.27		
284.  R&R Ridge cap - composition shingles			12.00 LF				4.48		0.78		54.54		0.00 	54.54		
285.  R&R Continuous ridge vent - shingle-over style			12.00 LF				5.98		2.05		73.81		0.00 	73.81		
286.  R&R Continuous ridge vent - aluminum			12.00 LF				5.93		2.02		73.18		0.00 	73.18		
287.  R&R Flashing - pipe jack			1.00 EA				25.89		0.34		26.23		0.00 	26.23		
288.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
289.  R&R Exhaust cap - through roof - 6" to 8"			1.00 EA				59.62		1.74		61.36		0.00 	61.36		
290.  R&R Furnace vent - rain cap and storm collar, 5"			1.00 EA				53.16		1.03		54.19		0.00 	54.19		
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
291.  R&R Furnace vent - rain cap and storm collar, 6"			1.00 EA				60.11		1.45		61.56		0.00 	61.56		
292.  R&R Furnace vent - rain cap and storm collar, 8"			1.00 EA				69.40		2.01		71.41		0.00 	71.41		
293.  Flue cap			1.00 EA				96.06		4.82		100.88		0.00 	100.88		
294.  R&R Fireplace - chimney chase cover - sheetmetal			1.00 EA				340.90		11.53		352.43		0.00 	352.43		
295.  Remove Additional charge for high roof (2 stories or greater)			2.00 SQ				3.77		0.00		7.54		0.00 	7.54		
296.  Additional charge for high roof (2 stories or greater)			2.00 SQ				9.35		0.00		18.70		0.00 	18.70		
The following line items are to replace the patio cover on the front, right, back, left sides of the building.																
297.  R&R Patio Cover - Attached - Aluminum - Moderate Load			240.00 SF				11.98		110.45		2,985.65		0.00 	2,985.65		
298.  R&R Patio Cover - Fascia end - Non-guttered			24.00 LF				5.58		3.56		137.48		0.00 	137.48		
299.  R&R Patio Cover - Fascia end - Guttered			20.00 LF				8.18		4.52		168.12		0.00 	168.12		
The following line items are to repaint the deck handrail on the XXXXXXX side of the house.																
300.	Stain/finish deck handrail		24.00 LF				4.22		1.51		102.79		0.00 	102.79		
301.	R&R Metal roofing		100.00 SF				3.61		7.38		368.38		0.00 	368.38		
302.	R&R Ridge cap - metal roofing		10.00 LF				5.23		1.25		53.55		0.00 	53.55		
303.	R&R Power attic vent cover only - metal		1.00 EA				66.83		1.79		68.62		0.00 	68.62		
304.	Flashing - pipe jack		1.00 EA				20.85		0.34		21.19		0.00 	21.19		
305.	Flashing - pipe jack - lead		1.00 EA				49.36		2.05		51.41		0.00 	51.41		
306.	R&R Flashing - pipe jack - split boot		1.00 EA				52.54		1.84		54.38		0.00 	54.38		
307.	Digital satellite system - Detach & reset		1.00 EA				23.78		0.00		23.78		0.00 	23.78		
308.	Ridge / Hip / Rake cap - tile roofing		10.00 LF				9.34		4.15		97.55		0.00 	97.55		
309.	Furnace vent - rain cap and storm collar, 5"		1.00 EA				45.50		1.03		46.53		0.00 	46.53		
310.	Furnace vent - rain cap and storm collar, 8"		1.00 EA				61.74		2.01		63.75		0.00 	63.75		
311.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA				59.62		1.74		61.36		0.00 	61.36		
312.	Additional charge for high roof (2 stories or greater)		10.00 SQ				9.35		0.00		93.50		0.00 	93.50		
313.	Additional charge for steep roof - 7/12 to 9/12 slope		10.00 SQ				21.17		0.00		211.70		0.00 	211.70		
"314.
slope"	Additional charge for steep roof - 10/12 - 12/12		10.00 SQ				33.26		0.00		332.60		0.00 	332.60		
315.	Flashing - rain diverter		1.00 EA				22.94		0.54		23.48		0.00 	23.48		
316.	Valley metal		10.00 LF				3.33		0.98		34.28		0.00 	34.28		
317.	Valley metal - (W) profile		10.00 LF				4.01		1.39		41.49		0.00 	41.49		
318.	Chimney flashing - average (32" x 36")		1.00 EA				201.06		3.21		204.27		0.00 	204.27		
319.	Remove Lightning protection system		1.00 EA				161.48		0.00		161.48		0.00 	161.48		
320.	Install Lightning protection system		1.00 EA				1,483.11		0.00		1,483.11		0.00 	1,483.11		
321.	Remove Tile roofing - Clay - "S" or flat tile		0.00 SQ				140.72		0.00		0.00		0.00 	0.00		
322.	Tile roofing - Clay - "S" or flat tile		0.00 SQ				445.74		0.00		0.00		0.00 	0.00		
323.	Remove Tile roofing - Concrete - "S" or flat tile		0.00 SQ				140.72		0.00		0.00		0.00 	0.00		
324.	Tile roofing - Concrete - "S" or flat tile		0.00 SQ				346.93		0.00		0.00		0.00 	0.00		
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
325.  Ice & water shield			10.00 SF				1.02		0.21		10.41		0.00 	10.41		
326.  Roof vent - turtle type - Metal			1.00 EA				35.84		0.94		36.78		0.00 	36.78		
327.  Roof vent - turtle type - Plastic			1.00 EA				31.08		0.66		31.74		0.00 	31.74		
328.  Roof vent - turbine type			1.00 EA				80.46		3.38		83.84		0.00 	83.84		
329.  R&R Power attic vent cover only - metal			1.00 EA				66.83		1.79		68.62		0.00 	68.62		
330.  Flashing - pipe jack			1.00 EA				20.85		0.34		21.19		0.00 	21.19		
331.  Flashing - pipe jack - lead			1.00 EA				49.36		2.05		51.41		0.00 	51.41		
332.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
333.	Digital satellite system - Detach & reset		1.00 EA				23.78		0.00		23.78		0.00 	23.78		
334.	Ridge / Hip / Rake cap - tile roofing		10.00 LF				9.34		4.15		97.55		0.00 	97.55		
335.	Furnace vent - rain cap and storm collar, 5"		1.00 EA				45.50		1.03		46.53		0.00 	46.53		
336.	Furnace vent - rain cap and storm collar, 8"		1.00 EA				61.74		2.01		63.75		0.00 	63.75		
337.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA				59.62		1.74		61.36		0.00 	61.36		
338.	Additional charge for high roof (2 stories or greater)		10.00 SQ				9.35		0.00		93.50		0.00 	93.50		
339.	Additional charge for steep roof - 7/12 to 9/12 slope		10.00 SQ				21.17		0.00		211.70		0.00 	211.70		
"340.
slope"	Additional charge for steep roof - 10/12 - 12/12		10.00 SQ				33.26		0.00		332.60		0.00 	332.60		
341.	Flashing - rain diverter		1.00 EA				22.94		0.54		23.48		0.00 	23.48		
342.	Valley metal		10.00 LF				3.33		0.98		34.28		0.00 	34.28		
343.	Valley metal - (W) profile		10.00 LF				4.01		1.39		41.49		0.00 	41.49		
344.	Chimney flashing - average (32" x 36")		1.00 EA				201.06		3.21		204.27		0.00 	204.27		
345.	Remove Lightning protection system		1.00 EA				161.48		0.00		161.48		0.00 	161.48		
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
346.  Install Lightning protection system			1.00 EA				1,483.11		0.00		1,483.11		0.00 	1,483.11		
347.  R&R Cupola - Wood - Small			1.00 EA				560.10		26.06		586.16		0.00 	586.16		
CONTINUED - GROUPINGTREESKETCH																
"DESCRIPTION                                                                   QUANTITY   UNIT PRICE
The following line items are to repair the roof damaged by wind."								TAX			RCV        DEPREC.               ACV					
348.  Remove Roll roofing			1.00 SQ				31.91		0.00		31.91		0.00 	31.91		
349.  Roll roofing			1.00 SQ				77.17		3.42		80.59		0.00 	80.59		
350.  R&R Roof vent - turtle type - Metal			1.00 EA				42.27		0.94		43.21		0.00 	43.21		
351.  R&R Roof vent - turtle type - Plastic			1.00 EA				37.51		0.66		38.17		0.00 	38.17		
352.  R&R Roof vent - turbine type			1.00 EA				86.89		3.38		90.27		0.00 	90.27		
353.  R&R Ridge cap - composition shingles			12.00 LF				4.48		0.78		54.54		0.00 	54.54		
354.  R&R Continuous ridge vent - shingle-over style			12.00 LF				5.98		2.05		73.81		0.00 	73.81		
355.  R&R Continuous ridge vent - aluminum			12.00 LF				5.93		2.02		73.18		0.00 	73.18		
356.  R&R Flashing - pipe jack			1.00 EA				25.89		0.34		26.23		0.00 	26.23		
357.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
358.  R&R Exhaust cap - through roof - 6" to 8"			1.00 EA				59.62		1.74		61.36		0.00 	61.36		
359.  R&R Furnace vent - rain cap and storm collar, 5"			1.00 EA				53.16		1.03		54.19		0.00 	54.19		
360.  R&R Furnace vent - rain cap and storm collar, 6"			1.00 EA				60.11		1.45		61.56		0.00 	61.56		
361.  R&R Furnace vent - rain cap and storm collar, 8"			1.00 EA				69.40		2.01		71.41		0.00 	71.41		
362.  Flue cap			1.00 EA				96.06		4.82		100.88		0.00 	100.88		
363.  R&R Fireplace - chimney chase cover - sheetmetal			1.00 EA				340.90		11.53		352.43		0.00 	352.43		
364.  Remove Additional charge for high roof (2 stories			2.00 SQ				3.77		0.00		7.54		0.00 	7.54		
"or greater)
365.  Additional charge for high roof (2 stories or greater)            2.00 SQ                   9.35                0.00               18.70                (0.00)               18.70
The following line items are to replace the screens on the XXXXXXX side of the house."																
366.  R&R Window screen, 1 - 9 SF			1.00 EA				27.79		1.31		29.10		0.00 	29.10		
367.  R&R Window screen, 10 - 16 SF			1.00 EA				35.19		1.76		36.95		0.00 	36.95		
368.  R&R Window screen, 17 - 25 SF			1.00 EA				44.94		2.34		47.28		0.00 	47.28		
369.  R&R Window screen, 26 - 32 SF			1.00 EA				48.84		2.57		51.41		0.00 	51.41		
370.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
"The following line items are to replace the siding on the front, right, back, and left sides of the house.
No damage found to the front, right, back, left side of the house at time of inspection."																
371.  R&R Siding - steel (29 gauge)			0.00 SF				4.61		0.00		0.00		0.00 	0.00		
373.  R&R Siding - aluminum (.024 thickness)			0.00 SF				4.37		0.00		0.00		0.00 	0.00		
374.  R&R Rigid foam insulation board - 1/2"			0.00 SF				0.88		0.00		0.00		0.00 	0.00		
375.  R&R Builder board - 1/2" (composition or fiberboard sheathing)			0.00 SF				1.37		0.00		0.00		0.00 	0.00		
376.  R&R Light/outlet J-block - Vinyl			1.00 EA				18.75		0.61		19.36		0.00 	19.36		
377.  R&R Metal inside corner post			10.00 LF				3.98		0.70		40.50		0.00 	40.50		
378.  R&R Metal outside corner post			10.00 LF				5.27		1.47		54.17		0.00 	54.17		
379.  R&R Clothes dryer vent - installed			1.00 EA				49.77		1.40		51.17		0.00 	51.17		
380.  Dumpster load - Approx. 20 yards, 4 tons of debris			1.00 EA				420.00		0.00		420.00		0.00 	420.00		
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION                                                                   QUANTITY   UNIT PRICE								TAX			RCV        DEPREC.               ACV					
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
381.  R&R Siding - aluminum (.024 thickness)			32.00 SF				4.37		4.90		144.74		0.00 	144.74		
382.  R&R Metal inside corner post			8.00 LF				3.98		0.56		32.40		0.00 	32.40		
383.  R&R Metal outside corner post			8.00 LF				5.27		1.18		43.34		0.00 	43.34		
384.  R&R Metal J trim			24.00 LF				2.82		0.69		68.37		0.00 	68.37		
385.  Metal or Vinyl siding - Detach & reset			100.00 SF				1.32		0.24		132.24		0.00 	132.24		
386.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
387.  R&R House wrap (air/moisture barrier)			0.00 SF				0.26		0.00		0.00		0.00 	0.00		
388.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
389.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repaint the front, right, back, and left sides of the building.																
390.  Seal & paint wood siding			0.00 SF				0.88		0.00		0.00		0.00 	0.00		
391.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
Ladder jacks required for more than two-story elevations.																
The following line items are to replace the siding on the front, right, back, and left sides of the house.																
No damage found to the front, right, back, left side of the house at time of inspection.																
392.  R&R Siding - vinyl			0.00 SF				2.86		0.00		0.00		0.00 	0.00		
393.  R&R Light/outlet J-block - Vinyl			1.00 EA				18.75		0.61		19.36		0.00 	19.36		
394.  R&R Vinyl inside corner post			10.00 LF				3.96		0.68		40.28		0.00 	40.28		
395.  R&R Vinyl outside corner post			10.00 LF				4.51		1.01		46.11		0.00 	46.11		
396.  R&R Clothes dryer vent - installed			1.00 EA				49.77		1.40		51.17		0.00 	51.17		
397.  Dumpster load - Approx. 20 yards, 4 tons of debris			1.00 EA				420.00		0.00		420.00		0.00 	420.00		
The following line items are to repair the siding on the XXXXXX side of the house.																
398.  R&R Siding - vinyl			0.00 SF				2.86		0.00		0.00		0.00 	0.00		
399.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
400.  R&R Wrap wood window frame & trim with aluminum sheet			1.00 EA				143.24		1.95		145.19		0.00 	145.19		
401.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
402.  R&R Soffit - metal			24.00 SF				3.73		2.30		91.82		0.00 	91.82		
403.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
404.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
405.  R&R Soffit - vinyl			24.00 SF				3.48		1.94		85.46		0.00 	85.46		
406.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
																
																
																
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
407.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
408.  R&R Soffit - wood			24.00 SF				3.91		1.86		95.70		0.00 	95.70		
409.  Prime & paint exterior soffit - wood			96.00 SF				1.38		1.96		134.44		0.00 	134.44		
410.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
411.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to replace the shed.																
412.  R&R Storage shed - Metal - Gable type - 10' x 12'			1.00 EA				1,018.14		36.99		1,055.13		0.00 	1,055.13		
413.  Contents - move out then reset			1.00 EA				50.12		0.00		50.12		0.00 	50.12		
414.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to replace the shed.																
415.  Storage shed - Metal - Gable type - 10' x 12'			1.00 EA				1,018.14		25.05		1,043.19		0.00 	1,043.19		
416.  Exterior Structure Installer - per hour - to remove and replace the shed*			7.00 HR				60.04		0.00		420.28		0.00 	420.28		
417.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
418.  R&R Siding - steel (29 gauge)			32.00 SF				4.61		5.36		152.88		0.00 	152.88		
419.  R&R Metal inside corner post			8.00 LF				3.98		0.56		32.40		0.00 	32.40		
420.  R&R Metal outside corner post			8.00 LF				5.27		1.18		43.34		0.00 	43.34		
421.  R&R Metal J trim			24.00 LF				2.82		0.69		68.37		0.00 	68.37		
422.  Metal or Vinyl siding - Detach & reset			100.00 SF				1.32		0.24		132.24		0.00 	132.24		
423.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
424.  R&R House wrap (air/moisture barrier)			0.00 SF				0.26		0.00		0.00		0.00 	0.00		
425.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
426.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair tree damage to the XXXXX slope of the roof on the house.																
427.  R&R 3 tab - 25 yr. - composition shingle roofing (per SHINGLE)			30.00 EA				11.35		2.86		343.36		0.00 	343.36		
428.  R&R Laminated - comp. shingle rfg (per SHINGLE)			30.00 EA				11.55		3.22		349.72		0.00 	349.72		
429.  R&R Laminated - High grade - comp. shingle rfg. (per SHINGLE)			30.00 EA				12.32		4.00		373.60		0.00 	373.60		
430.  R&R Laminated - Deluxe grd - comp. shingle rfg. (per SHINGLE)			30.00 EA				13.06		4.10		395.90		0.00 	395.90		
431.  R&R Ridge cap - composition shingles			24.00 LF				4.48		1.57		109.09		0.00 	109.09		
432.  R&R Ridge cap - High profile - composition shingles			24.00 LF				5.79		3.57		142.53		0.00 	142.53		
																
																
																
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
433.  Roofing felt - 15 lb.			1.00 SQ				18.00		0.36		18.36		0.00 	18.36		
434.  R&R Sheathing - plywood - 1/2" CDX			32.00 SF				1.76		1.32		57.64		0.00 	57.64		
435.  R&R Rafters - 2x8 - Labor only - (using rafter length)			24.00 LF				2.47		0.04		59.32		0.00 	59.32		
Rafter line items are to repair/sister rafters damaged by fallen tree.																
436.  R&R 2" x 8" lumber (1.33 BF per LF)			24.00 LF				2.76		1.38		67.62		0.00 	67.62		
437.  R&R Drip edge			24.00 LF				1.59		0.85		39.01		0.00 	39.01		
The fo																
TREE DEBRIS REMOVAL																
"This is a line item for hauling off only the tree debris that was removed from the house (chopped and dropped) so that repairs can be made.
438.  Tree - removal and disposal - per hour including                  5.00 HR                70.37                0.00             351.85                (0.00)             351.85
equipment
This line item is allowance to haul away tree debris per policy provisions.
Labor and equipment for 2 persons, 4 hours each to remove tree debris from property subject to coverage limit.
439.  Dumpster load - Approx. 20 yards, 4 tons of debris              1.00 EA              420.00                0.00             420.00                (0.00)             420.00
The following line items are to repair the electrical service damaged by fallen trees."																
440.  R&R Meter mast for overhead power - 2" conduit			1.00 EA				392.75		6.12		398.87		0.00 	398.87		
441.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
442.  R&R Meter base and main disconnect - 200 amp			1.00 EA				383.58		9.60		393.18		0.00 	393.18		
443.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
444.  R&R Siding - vinyl			32.00 SF				2.86		2.42		93.94		0.00 	93.94		
445.  R&R Light/outlet J-block - Vinyl			1.00 EA				18.75		0.61		19.36		0.00 	19.36		
446.  R&R Vinyl J-vent			1.00 EA				20.09		0.69		20.78		0.00 	20.78		
447.  R&R Vinyl J trim			24.00 LF				2.79		0.65		67.61		0.00 	67.61		
448.  R&R Vinyl inside corner post			8.00 LF				3.96		0.55		32.23		0.00 	32.23		
449.  R&R Vinyl outside corner post			8.00 LF				4.51		0.81		36.89		0.00 	36.89		
450.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
451.  R&R House wrap (air/moisture barrier)			0.00 SF				0.26		0.00		0.00		0.00 	0.00		
452.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
453.  Haul debris - per pickup truck load - including			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
"dump fees
The following line items are to repair water damage to the walls and flooring in this room."																
454.  R&R Carpet			0.00 SF				2.99		0.00		0.00		0.00 	0.00		
456.  Carpet pad			0.00 SF				0.59		0.00		0.00		0.00 	0.00		
457.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		

CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION                                                                   QUANTITY   UNIT PRICE								TAX			RCV        DEPREC.               ACV					
"===========================================================================
Water mitigation and remediation"																
===========================================================================																
458.  Air mover (per 24 hour period) - No monitoring			1.00 EA				25.22		0.00		25.22		0.00 	25.22		
X air movers for X days																
459.  Dehumidifier (per 24 hour period) - No monitoring			1.00 EA				55.39		0.00		55.39		0.00 	55.39		
X dehumidifier(s) for X days																
460.  Heat drying - thermal air mover - Electric			0.00 DA				180.00		0.00		0.00		0.00 	0.00		
X heater air movers for X days																
461.  Containment Barrier/Airlock/Decon. Chamber			100.00 SF				0.60		0.54		60.54		0.00 	60.54		
462.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.60		0.00		111.60		0.00 	111.60		
463.  Tear out wet drywall, cleanup, bag for disposal			10.00 SF				0.87		0.11		8.81		0.00 	8.81		
464.  Tear out baseboard			0.00 LF				0.34		0.00		0.00		0.00 	0.00		
465.  Baseboard - Detach & reset			0.00 LF				1.38		0.00		0.00		0.00 	0.00		
466.  Water extraction from carpeted floor			0.00 SF				0.44		0.00		0.00		0.00 	0.00		
467.  Tear out wet non-salvageable carpet, cut & bag for disp.			0.00 SF				0.44		0.00		0.00		0.00 	0.00		
468.  Tear out wet carpet pad and bag for disposal			0.00 SF				0.41		0.00		0.00		0.00 	0.00		
469.  Block and pad furniture in room			1.00 EA				34.59		0.07		34.66		0.00 	34.66		
The following line items are to replace the storm windows and doors on the front, right, back, and left sides of the building.																
470.  R&R Storm window - aluminum, 3-11 sf			1.00 EA				106.59		4.61		111.20		0.00 	111.20		
472.  R&R Storm door assembly			1.00 EA				217.74		8.64		226.38		0.00 	226.38		
The following line items are to repair wind damage to the window glass on the XXXXXXX side of the house.																
474.  Reglaze window, 1 - 9 sf			1.00 EA				64.92		2.37		67.29		0.00 	67.29		
475.  Reglaze window, 10 - 16 sf			1.00 EA				115.42		4.21		119.63		0.00 	119.63		
476.  Reglaze window, 17 - 24 sf			1.00 EA				173.08		6.32		179.40		0.00 	179.40		
477.  R&R Glazing bead - Vinyl			24.00 LF				1.29		0.84		31.80		0.00 	31.80		
478.  R&R Glazing bead - Aluminum			24.00 LF				1.16		0.65		28.49		0.00 	28.49		
479.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18	
The following line items are to replace the vinyl windows on the front, right, back, and left sides of the building.																
480.  R&R Vinyl window, single hung, 9-12 sf			1.00 EA				204.83		8.40		213.23		0.00 	213.23		
481.  R&R Vinyl window - double hung, 9-12 sf			1.00 EA				251.74		11.21		262.95		0.00 	262.95		
482.  R&R Vinyl window, picture/fixed, 12-23 sf			1.00 EA				221.89		8.98		230.87		0.00 	230.87		
483.  R&R Vinyl window - casement, 6-8 sf			1.00 EA				271.34		12.39		283.73		0.00 	283.73		
484.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to replace the metal clad wood windows on the front, right, back, and left sides of the building.																
485.  R&R Wood window - single hung, 9-12 sf			1.00 EA				399.80		18.15		417.95		0.00 	417.95		
															
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
486.  R&R Wood window - double hung, 9-12 sf			1.00 EA				457.40		21.61		479.01		0.00 	479.01		
487.  R&R Wood window - picture (fixed), 24-32 sf			1.00 EA				760.19		39.80		799.99		0.00 	799.99		
488.  R&R Wood window - casement, 12-23 sf			1.00 EA				520.44		24.92		545.36		0.00 	545.36		
489.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
490.  R&R Siding - beveled - pine or equal (clapboard)			32.00 SF				4.70		4.72		155.12		0.00 	155.12		
491.  Seal & paint wood siding			0.00 SF				0.88		0.00		0.00		0.00 	0.00		
492.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
493.  R&R House wrap (air/moisture barrier)			0.00 SF				0.26		0.00		0.00		0.00 	0.00		
494.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
495.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
496.  Wood shakes - medium (1/2") hand split			0.00 SQ				343.65		0.00		0.00		0.00 	0.00		
497.  Remove Tear off, haul and dispose of wood shakes/shingles			0.00 SQ				47.04		0.00		0.00		0.00 	0.00		
498.  Drip edge			10.00 LF				1.35		0.35		13.85		0.00 	13.85		
499.  Drip edge/gutter apron			10.00 LF				1.48		0.43		15.23		0.00 	15.23		
500.  Ice & water shield			10.00 SF				1.02		0.21		10.41		0.00 	10.41		
501.  Roof vent - turtle type - Metal			1.00 EA				35.84		0.94		36.78		0.00 	36.78		
502.  Roof vent - turtle type - Plastic			1.00 EA				31.08		0.66		31.74		0.00 	31.74		
503.  Roof vent - turbine type			1.00 EA				80.46		3.38		83.84		0.00 	83.84		
504.  R&R Power attic vent cover only - metal			1.00 EA				66.83		1.79		68.62		0.00 	68.62		
505.  Flashing - pipe jack			1.00 EA				20.85		0.34		21.19		0.00 	21.19		
506.  Flashing - pipe jack - lead			1.00 EA				49.36		2.05		51.41		0.00 	51.41		
507.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
Typically used for power mast roof penetration.																
508.	Digital satellite system - Detach & reset		1.00 EA				23.78		0.00		23.78		0.00 	23.78		
509.	Continuous ridge vent - shingle-over style		10.00 LF				5.37		1.71		55.41		0.00 	55.41		
510.	Sheathing - plywood - 1/2" CDX		32.00 SF				1.36		1.32		44.84		0.00 	44.84		
511.	Ridge cap - composition shingles		10.00 LF				3.19		0.65		32.55		0.00 	32.55		
512.	Furnace vent - rain cap and storm collar, 5"		1.00 EA				45.50		1.03		46.53		0.00 	46.53		
513.	Furnace vent - rain cap and storm collar, 8"		1.00 EA				61.74		2.01		63.75		0.00 	63.75		
514.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA				59.62		1.74		61.36		0.00 	61.36		
515.	Additional charge for high roof (2 stories or greater)		10.00 SQ				9.35		0.00		93.50		0.00 	93.50		
516.	Additional charge for steep roof - 7/12 to 9/12 slope		10.00 SQ				21.17		0.00		211.70		0.00 	211.70		
"517.
slope"	Additional charge for steep roof - 10/12 - 12/12		10.00 SQ				33.26		0.00		332.60		0.00 	332.60		
518.	Flashing - rain diverter		1.00 EA				22.94		0.54		23.48		0.00 	23.48		
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY		UNIT PRICE				TAX		RCV		DEPREC.	ACV		
519.  Valley metal			10.00 LF		3.33				0.98		34.28		0.00 	34.28		
520.  Valley metal - (W) profile			10.00 LF		4.01				1.39		41.49		0.00 	41.49		
521.  Chimney flashing - average (32" x 36")			1.00 EA		201.06				3.21		204.27		0.00 	204.27		
522.  Remove Lightning protection system			1.00 EA		161.48				0.00		161.48		0.00 	161.48		
Detach and reset lightning protection system.																
523.  Install Lightning protection system			1.00 EA		1,483.11				0.00		1,483.11		0.00 	1,483.11		
524.  R&R Cupola - Wood - Small			1.00 EA		560.10				26.06		586.16		0.00 	586.16		
The following line items are to repair wind damage to the door and window wraps on the XXXXXXX side of the house.																
525.  R&R Wrap wood window frame & trim with aluminum sheet			1.00 EA		143.24				1.95		145.19		0.00 	145.19		
526.  R&R Wrap wood window frame & trim with aluminum sheet - Small			1.00 EA		94.54				1.29		95.83		0.00 	95.83		
527.  R&R Wrap wood window frame & trim with aluminum sheet - Large			1.00 EA		191.35				2.38		193.73		0.00 	193.73		
528.  R&R Wrap wood window frame & trim with aluminum sheet - XLarge			1.00 EA		232.45				3.15		235.60		0.00 	235.60		
529.  R&R Custom bent aluminum (PER LF)			12.00 LF		13.30				1.35		160.95		0.00 	160.95		
530.  R&R Wrap wood garage door frame & trim with aluminum (PER LF)			30.00 LF		8.84				3.33		268.53		0.00 	268.53		
531.  R&R Wrap wood post with aluminum (PER LF)			16.00 LF		10.55				1.76		170.56		0.00 	170.56		
532.  R&R Wrap wood door frame & trim with aluminum (PER LF)			16.50 LF		9.74				1.81		162.53		0.00 	162.53		
533.  Haul debris - per pickup truck load - including dump fees			1.00 EA		111.18				0.00		111.18		0.00 	111.18		
Total:  GROUPINGTREESKETCH									1,259.25		65,657.20		0.00	65,657.20		
Labor Minimums Applied																
DESCRIPTION			QUANTITY		UNIT PRICE				TAX		RCV		DEPREC.	ACV		
492.  Awning labor minimum			1.00 EA		6.39				0.00		6.39		0.00 	6.39		
84.  Insulation labor minimum			1.00 EA		84.81				0.00		84.81		0.00 	84.81		
270.  Drywall labor minimum			1.00 EA		243.83				0.00		243.83		0.00 	243.83		
442.  Wallpaper labor minimum			1.00 EA		110.78				0.00		110.78		0.00 	110.78		
268.  Finish carpentry labor minimum			1.00 EA		140.66				0.00		140.66		0.00 	140.66		
438.  Vinyl floor covering labor minimum			1.00 EA		157.18				0.00		157.18		0.00 	157.18		
256.  Framing labor minimum			1.00 EA		30.80				0.00		30.80		0.00 	30.80		
74.  Drywall labor minimum			1.00 EA		288.74				0.00		288.74		0.00 	288.74		
518.  Temporary repair services labor minimum			1.00 EA		46.97				0.00		46.97		0.00 	46.97		
428.  General labor - labor minimum			1.00 EA		17.86				0.00		17.86		0.00 	17.86		
372.  Siding labor minimum			1.00 EA		43.42				0.00		43.42		0.00 	43.42		
455.  Carpet labor minimum			1.00 EA		157.18				0.00		157.18		0.00 	157.18		
																
																
CONTINUED - Labor Minimums Applied																
DESCRIPTION		QUANTITY   UNIT PRICE								TAX	RCV	DEPREC.			ACV	
473.  Door labor minimum		1.00 EA				66.92				0.00	66.92	0.00 			66.92	
Totals:  Labor Minimums Applied										0.00	1,395.54	0.00			1,395.54	
Line Item Totals:  GROUPINGTREESKETCH		1,259.25									67,052.74	0.00        67,052.74				
Coverage		Item Total				%					ACV Total	%				
Dwelling		63,025.80				93.99%					63,025.80	93.99%
Other Structures		4,026.94				6.01%					4,026.94	6.01%				
Contents		0.00				0.00%					0.00	0.00%				
Total		67,052.74				100.00%					67,052.74	100.00%				
"""

ROOF_KNOWLEDGE_BASE = r"""
Table index: Roof 1-179, 280-296, 300-365, 490-524                    
Awning 180-184
Water (walls, ceilings, floors 185-198, 199-206, 258-279, 454-457, 458-469
Tree Removal 207-216, 427-443
Deck + Patio 217-219, 297-347,
Fascia 220-231, 253-257, 381-389, 402-411, 418-426, 444-453
Fence 232-238, 
Gutter 239-252
Screen 365-370, window-door- 470-472, 474-489, 525-533
Siding 371-401                    Shed 415-417"																
DESCRIPTION                                                                   QUANTITY   UNIT PRICE									TAX		RCV		DEPREC.	ACV		
The following line items are to replace the roof on this structure.																
1.  3 tab - 25 yr. - comp. shingle roofing - w/out felt                      0.00 SQ               138.43									0.00		0.00		0.00 	0.00		
"2.  Remove Tear off, haul and dispose of comp. shingles -            0.00 SQ                 40.87
3 tab"									0.00		0.00		0.00 	0.00		
3.  Roofing felt - 15 lb.                                                                    0.00 SQ                 18.00									0.00		0.00		0.00 	0.00		
4.  Drip edge                                                                                    0.00 LF                   1.35									0.00		0.00		0.00 	0.00		
5.  Drip edge/gutter apron                                                               0.00 LF                   1.48									0.00		0.00		0.00 	0.00		
6.  Ice & water shield                                                                      0.00 SF                   1.02									0.00		0.00		0.00 	0.00		
7.  Roof vent - turtle type - Metal                                                   1.00 EA                35.84									0.94		36.78		0.00 	36.78		
8.  Roof vent - turtle type - Plastic                                                  1.00 EA                31.08									0.66		31.74		0.00 	31.74		
9.  Roof vent - turbine type                                                             1.00 EA                80.46									3.38		83.84		0.00 	83.84		
10.  R&R Power attic vent cover only - metal                                1.00 EA                66.83									1.79		68.62		0.00 	68.62		
11.  Flashing - pipe jack                                                                  1.00 EA                20.85									0.34		21.19		0.00 	21.19		
12.  Flashing - pipe jack - lead                                                        1.00 EA                49.36									2.05		51.41		0.00 	51.41		
13.  R&R Flashing - pipe jack - split boot                                      1.00 EA                52.54									1.84		54.38		0.00 	54.38		
Typically used for power mast roof penetration.																
14.  Digital satellite system - Detach & reset                                 1.00 EA                23.78									0.00		23.78		0.00 	23.78		
15.  Continuous ridge vent - shingle-over style                              0.00 LF                   5.37									0.00		0.00		0.00 	0.00		
16.  Ridge cap - composition shingles                                            0.00 LF                   3.19									0.00		0.00		0.00 	0.00		
17.  Furnace vent - rain cap and storm collar, 5"                            1.00 EA                45.50									1.03		46.53		0.00 	46.53		
18.  Furnace vent - rain cap and storm collar, 8"                            1.00 EA                61.74									2.01		63.75		0.00 	63.75		
19.  R&R Exhaust cap - through roof - 6" to 8"                             1.00 EA                59.62									1.74		61.36		0.00 	61.36		
20.  Additional charge for high roof (2 stories or greater)              0.00 SQ                   9.35									0.00		0.00		0.00 	0.00		
21.  Additional charge for steep roof - 7/12 to 9/12 slope              0.00 SQ                 21.17									0.00		0.00		0.00 	0.00		
22.  Additional charge for steep roof - 10/12 - 12/12 slope            0.00 SQ                 33.26									0.00		0.00		0.00 	0.00		
23.  Flashing - rain diverter                                                             1.00 EA                22.94									0.54		23.48		0.00 	23.48		
24.  Valley metal                                                                             0.00 LF                   3.33									0.00		0.00		0.00 	0.00		
25.  Valley metal - (W) profile                                                       0.00 LF                   4.01									0.00		0.00		0.00 	0.00		
26.  Chimney flashing - average (32" x 36")                                  1.00 EA              201.06									3.21		204.27		0.00 	204.27		
27.  Remove Lightning protection system                                      1.00 EA              161.48									0.00		161.48		0.00 	161.48		
Detach and reset lightning protection system.																
28.  Install Lightning protection system                                         1.00 EA           1,483.11									0.00		1,483.11		0.00 	1,483.11		
29.  R&R Cupola - Wood - Small                                                   1.00 EA              560.10									26.06		586.16		0.00 	586.16		
30.  Laminated - comp. shingle rfg. - w/out felt                             0.00 SQ               153.11									0.00		0.00		0.00 	0.00		
"31.  Tear off, haul and dispose of comp. shingles -                        0.00 SQ                 52.56
Laminated"									0.00		0.00		0.00 	0.00		
32.  Roofing felt - 15 lb.                                                                  0.00 SQ                 18.00									0.00		0.00		0.00 	0.00		
33.  Drip edge                                                                                  0.00 LF                   1.35									0.00		0.00		0.00 	0.00		
34.  Drip edge/gutter apron                                                             0.00 LF                   1.48									0.00		0.00		0.00 	0.00		
35.  Ice & water shield                                                                    0.00 SF                   1.02									0.00		0.00		0.00 	0.00		
36.  Roof vent - turtle type - Metal                                                 1.00 EA                35.84									0.94		36.78		0.00 	36.78		
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
37.  Roof vent - turtle type - Plastic			1.00 EA				31.08		0.66		31.74		0.00 	31.74		
38.  Roof vent - turbine type			1.00 EA				80.46		3.38		83.84		0.00 	83.84		
39.  R&R Power attic vent cover only - metal			1.00 EA				66.83		1.79		68.62		0.00 	68.62		
40.  Flashing - pipe jack			1.00 EA				20.85		0.34		21.19		0.00 	21.19		
41.  Flashing - pipe jack - lead			1.00 EA				49.36		2.05		51.41		0.00 	51.41		
"42.  R&R Flashing - pipe jack - split boot Typically used for power mast roof penetration. Typically used for power mast roof penetration.
43.  Digital satellite system - Detach & reset"			"1.00 EA
1.00 EA"				"52.54
23.78"		"1.84
0.00"		"54.38
23.78"		"(0.00)
(0.00)"	"54.38
23.78"		
44.  Continuous ridge vent - shingle-over style			0.00 LF				5.37		0.00		0.00		0.00 	0.00		
45.  Ridge cap - composition shingles			0.00 LF				3.19		0.00		0.00		0.00 	0.00		
46.  Furnace vent - rain cap and storm collar, 5"			1.00 EA				45.50		1.03		46.53		0.00 	46.53		
47.  Furnace vent - rain cap and storm collar, 8"			1.00 EA				61.74		2.01		63.75		0.00 	63.75		
48.  R&R Exhaust cap - through roof - 6" to 8"			1.00 EA				59.62		1.74		61.36		0.00 	61.36		
49.  Additional charge for high roof (2 stories or greater)			0.00 SQ				9.35		0.00		0.00		0.00 	0.00		
50.  Additional charge for steep roof - 7/12 to 9/12 slope			0.00 SQ				21.17		0.00		0.00		0.00 	0.00		
51.  Additional charge for steep roof - 10/12 - 12/12 slope			0.00 SQ				33.26		0.00		0.00		0.00 	0.00		
52.  Flashing - rain diverter			1.00 EA				22.94		0.54		23.48		0.00 	23.48		
53.  Valley metal			0.00 LF				3.33		0.00		0.00		0.00 	0.00		
54.  Valley metal - (W) profile			0.00 LF				4.01		0.00		0.00		0.00 	0.00		
55.  Chimney flashing - average (32" x 36")			1.00 EA				201.06		3.21		204.27		0.00 	204.27		
"56.  Remove Lightning protection system Detach and reset lightning protection system. Detach and reset lightning protection system.
57.  Install Lightning protection system"			"1.00 EA
1.00 EA"				"161.48
1,483.11"		"0.00
0.00"		"161.48
1,483.11"		"(0.00)
(0.00)"	"161.48
1,483.11"		
58.  R&R Cupola - Wood - Small			1.00 EA				560.10		26.06		586.16		0.00 	586.16		
The following line items are to repair the XXXXXX slope of the roof damaged by wind.																
59.  R&R Laminated - comp. shingle rfg (per SHINGLE)			12.00 EA				11.55		1.29		139.89		0.00 	139.89		
60.  R&R Roof vent - turtle type - Metal			1.00 EA				42.27		0.94		43.21		0.00 	43.21		
61.  R&R Roof vent - turtle type - Plastic			1.00 EA				37.51		0.66		38.17		0.00 	38.17		
62.  R&R Roof vent - turbine type			1.00 EA				86.89		3.38		90.27		0.00 	90.27		
63.  R&R Ridge cap - composition shingles			12.00 LF				4.48		0.78		54.54		0.00 	54.54		
64.  R&R Continuous ridge vent - shingle-over style			12.00 LF				5.98		2.05		73.81		0.00 	73.81		
65.  R&R Continuous ridge vent - aluminum			12.00 LF				5.93		2.02		73.18		0.00 	73.18		
66.  R&R Flashing - pipe jack			1.00 EA				25.89		0.34		26.23		0.00 	26.23		
67.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
68.  R&R Exhaust cap - through roof - 6" to 8"			1.00 EA				59.62		1.74		61.36		0.00 	61.36		
69.  R&R Furnace vent - rain cap and storm collar, 5"			1.00 EA				53.16		1.03		54.19		0.00 	54.19		
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
70.  R&R Furnace vent - rain cap and storm collar, 6"			1.00 EA				60.11		1.45		61.56		0.00 	61.56		
71.  R&R Furnace vent - rain cap and storm collar, 8"			1.00 EA				69.40		2.01		71.41		0.00 	71.41		
72.  Flue cap			1.00 EA				96.06		4.82		100.88		0.00 	100.88		
73.  R&R Fireplace - chimney chase cover - sheetmetal			1.00 EA				340.90		11.53		352.43		0.00 	352.43		
74.  Remove Additional charge for high roof (2 stories or greater)			2.00 SQ				3.77		0.00		7.54		0.00 	7.54		
75.  Additional charge for high roof (2 stories or greater)			2.00 SQ				9.35		0.00		18.70		0.00 	18.70		
76.  Remove Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ				9.99		0.00		19.98		0.00 	19.98		
77.  Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ				21.17		0.00		42.34		0.00 	42.34		
78.  Remove Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ				15.71		0.00		31.42		0.00 	31.42		
79.  Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ				33.26		0.00		66.52		0.00 	66.52		
80.  Remove Additional charge for steep roof greater than 12/12 slope			2.00 SQ				19.50		0.00		39.00		0.00 	39.00		
81.  Additional charge for steep roof greater than 12/12 slope			2.00 SQ				42.07		0.00		84.14		0.00 	84.14		
The following line items are to repair the XXXXXXX slope of the roof damaged by wind.																
"82.
(per"	R&R 3 tab - 25 yr. - composition shingle roofing SHINGLE)		12.00 EA				11.35		1.14		137.34		0.00 	137.34		
83.	R&R Roof vent - turtle type - Metal		1.00 EA				42.27		0.94		43.21		0.00 	43.21		
84.	R&R Roof vent - turtle type - Plastic		1.00 EA				37.51		0.66		38.17		0.00 	38.17		
85.	R&R Roof vent - turbine type		1.00 EA				86.89		3.38		90.27		0.00 	90.27		
86.	R&R Ridge cap - composition shingles		12.00 LF				4.48		0.78		54.54		0.00 	54.54		
87.	R&R Continuous ridge vent - shingle-over style		12.00 LF				5.98		2.05		73.81		0.00 	73.81		
88.	R&R Continuous ridge vent - aluminum		12.00 LF				5.93		2.02		73.18		0.00 	73.18		
89.	R&R Flashing - pipe jack		1.00 EA				25.89		0.34		26.23		0.00 	26.23		
90.	R&R Flashing - pipe jack - split boot		1.00 EA				52.54		1.84		54.38		0.00 	54.38		
91.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA				59.62		1.74		61.36		0.00 	61.36		
92.	R&R Furnace vent - rain cap and storm collar, 5"		1.00 EA				53.16		1.03		54.19		0.00 	54.19		
93.	R&R Furnace vent - rain cap and storm collar, 6"		1.00 EA				60.11		1.45		61.56		0.00 	61.56		
94.	R&R Furnace vent - rain cap and storm collar, 8"		1.00 EA				69.40		2.01		71.41		0.00 	71.41		
95.	Flue cap		1.00 EA				96.06		4.82		100.88		0.00 	100.88		
96.	R&R Fireplace - chimney chase cover - sheetmetal		1.00 EA				340.90		11.53		352.43		0.00 	352.43		
97.	Remove Additional charge for high roof (2 stories or		2.00 SQ				3.77		0.00		7.54		0.00 	7.54		
greater)																
98.  Additional charge for high roof (2 stories or greater)			2.00 SQ				9.35		0.00		18.70		0.00 	18.70		
99.  Remove Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ				9.99		0.00		19.98		0.00 	19.98		
100.  Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ				21.17		0.00		42.34		0.00 	42.34		
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION                                                                   QUANTITY   UNIT							PRICE		TAX		RCV		DEPREC.	ACV		
101.  Remove Additional charge for steep roof - 10/12 -               2.00 SQ 12/12 slope							15.71		0.00		31.42		0.00 	31.42		
102.  Additional charge for steep roof - 10/12 - 12/12                   2.00 SQ slope							33.26		0.00		66.52		0.00 	66.52		
103.  Remove Additional charge for steep roof greater                  2.00 SQ than 12/12 slope							19.50		0.00		39.00		0.00 	39.00		
104.  Additional charge for steep roof greater than 12/12              2.00 SQ slope							42.07		0.00		84.14		0.00 	84.14		
The following line items are to replace the roof on this structure.																
105.  Laminated - High grd - comp. shingle rfg. - w/out                0.00 SQ felt							183.90		0.00		0.00		0.00 	0.00		
106.  Remove Tear off, haul and dispose of comp.                        0.00 SQ shingles - 3 tab							40.87		0.00		0.00		0.00 	0.00		
107.  Roofing felt - 15 lb.                                                                0.00 SQ							18.00		0.00		0.00		0.00 	0.00		
108.  Drip edge                                                                                0.00 LF							1.35		0.00		0.00		0.00 	0.00		
109.  Drip edge/gutter apron                                                           0.00 LF							1.48		0.00		0.00		0.00 	0.00		
110.  Ice & water shield                                                                  0.00 SF							1.02		0.00		0.00		0.00 	0.00		
111.  Roof vent - turtle type - Metal                                               1.00 EA							35.84		0.94		36.78		0.00 	36.78		
112.  Roof vent - turtle type - Plastic                                              1.00 EA							31.08		0.66		31.74		0.00 	31.74		
113.  Roof vent - turbine type                                                         1.00 EA							80.46		3.38		83.84		0.00 	83.84		
114.  R&R Power attic vent cover only - metal                              1.00 EA							66.83		1.79		68.62		0.00 	68.62		
115.  Flashing - pipe jack                                                                1.00 EA							20.85		0.34		21.19		0.00 	21.19		
116.  Flashing - pipe jack - lead                                                      1.00 EA							49.36		2.05		51.41		0.00 	51.41		
117.  R&R Flashing - pipe jack - split boot                                    1.00 EA							52.54		1.84		54.38		0.00 	54.38		
Typically used for power mast roof penetration.																
118.	Digital satellite system - Detach & reset		1.00 EA				23.78		0.00		23.78		0.00 	23.78		
119.	Continuous ridge vent - shingle-over style		0.00 LF				5.37		0.00		0.00		0.00 	0.00		
120.	Ridge cap - composition shingles		0.00 LF				3.19		0.00		0.00		0.00 	0.00		
121.	Furnace vent - rain cap and storm collar, 5"		1.00 EA				45.50		1.03		46.53		0.00 	46.53		
122.	Furnace vent - rain cap and storm collar, 8"		1.00 EA				61.74		2.01		63.75		0.00 	63.75		
123.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA				59.62		1.74		61.36		0.00 	61.36		
124.	Additional charge for high roof (2 stories or greater)		0.00 SQ				9.35		0.00		0.00		0.00 	0.00		
125.	Additional charge for steep roof - 7/12 to 9/12 slope		0.00 SQ				21.17		0.00		0.00		0.00 	0.00		
"126.
slope"	Additional charge for steep roof - 10/12 - 12/12		0.00 SQ				33.26		0.00		0.00		0.00 	0.00		
127.	Flashing - rain diverter		1.00 EA				22.94		0.54		23.48		0.00 	23.48		
128.	Valley metal		0.00 LF				3.33		0.00		0.00		0.00 	0.00		
129.	Valley metal - (W) profile		0.00 LF				4.01		0.00		0.00		0.00 	0.00		
130.	Chimney flashing - average (32" x 36")		1.00 EA				201.06		3.21		204.27		0.00 	204.27		
131.	Remove Lightning protection system		1.00 EA				161.48		0.00		161.48		0.00 	161.48		
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY		UNIT PRICE				TAX		RCV		DEPREC.	ACV		
Detach and reset lightning protection system.																
132.  Install Lightning protection system			1.00 EA		1,483.11				0.00		1,483.11		0.00 	1,483.11		
133.  R&R Cupola - Wood - Small			1.00 EA		560.10				26.06		586.16		0.00 	586.16		
The following line items are to repair the XXXXXX slope of the roof damaged by wind.																
"134.
(per"	R&R Laminated - High grade - comp. shingle rfg. SHINGLE)		12.00 EA		12.32				1.60		149.44		0.00 	149.44		
135.	R&R Roof vent - turtle type - Metal		1.00 EA		42.27				0.94		43.21		0.00 	43.21		
136.	R&R Roof vent - turtle type - Plastic		1.00 EA		37.51				0.66		38.17		0.00 	38.17		
137.	R&R Roof vent - turbine type		1.00 EA		86.89				3.38		90.27		0.00 	90.27		
138.	R&R Ridge cap - composition shingles		12.00 LF		4.48				0.78		54.54		0.00 	54.54		
139.	R&R Continuous ridge vent - shingle-over style		12.00 LF		5.98				2.05		73.81		0.00 	73.81		
140.	R&R Continuous ridge vent - aluminum		12.00 LF		5.93				2.02		73.18		0.00 	73.18		
141.	R&R Flashing - pipe jack		1.00 EA		25.89				0.34		26.23		0.00 	26.23		
142.	R&R Flashing - pipe jack - split boot		1.00 EA		52.54				1.84		54.38		0.00 	54.38		
143.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA		59.62				1.74		61.36		0.00 	61.36		
144.	R&R Furnace vent - rain cap and storm collar, 5"		1.00 EA		53.16				1.03		54.19		0.00 	54.19		
145.	R&R Furnace vent - rain cap and storm collar, 6"		1.00 EA		60.11				1.45		61.56		0.00 	61.56		
146.	R&R Furnace vent - rain cap and storm collar, 8"		1.00 EA		69.40				2.01		71.41		0.00 	71.41		
147.	Flue cap		1.00 EA		96.06				4.82		100.88		0.00 	100.88		
148.	R&R Fireplace - chimney chase cover - sheetmetal		1.00 EA		340.90				11.53		352.43		0.00 	352.43		
149.	Remove Additional charge for high roof (2 stories		2.00 SQ		3.77				0.00		7.54		0.00 	7.54		
or greater)																
150.  Additional charge for high roof (2 stories or greater)			2.00 SQ		9.35				0.00		18.70		0.00 	18.70		
151.  Remove Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ		9.99				0.00		19.98		0.00 	19.98		
152.  Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ		21.17				0.00		42.34		0.00 	42.34		
153.  Remove Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ		15.71				0.00		31.42		0.00 	31.42		
154.  Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ		33.26				0.00		66.52		0.00 	66.52		
155.  Remove Additional charge for steep roof greater than 12/12 slope			2.00 SQ		19.50				0.00		39.00		0.00 	39.00		
156.  Additional charge for steep roof greater than 12/12 slope			2.00 SQ		42.07				0.00		84.14		0.00 	84.14		
The following line items are to repair the XXXXXX slope of the roof damaged by wind.																
157.  R&R Laminated - Deluxe grd - comp. shingle rfg. (per SHINGLE)			12.00 EA		13.06				1.64		158.36		0.00 	158.36		
158.  R&R Roof vent - turtle type - Metal			1.00 EA		42.27				0.94		43.21		0.00 	43.21		
159.  R&R Roof vent - turtle type - Plastic			1.00 EA		37.51				0.66		38.17		0.00 	38.17		
160.  R&R Roof vent - turbine type			1.00 EA		86.89				3.38		90.27		0.00 	90.27		
161.  R&R Ridge cap - composition shingles			12.00 LF		4.48				0.78		54.54		0.00 	54.54		
																
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY		UNIT PRICE				TAX		RCV		DEPREC.	ACV		
162.  R&R Continuous ridge vent - shingle-over style			12.00 LF		5.98				2.05		73.81		0.00 	73.81		
163.  R&R Continuous ridge vent - aluminum			12.00 LF		5.93				2.02		73.18		0.00 	73.18		
164.  R&R Flashing - pipe jack			1.00 EA		25.89				0.34		26.23		0.00 	26.23		
165.  R&R Flashing - pipe jack - split boot			1.00 EA		52.54				1.84		54.38		0.00 	54.38		
166.  R&R Exhaust cap - through roof - 6" to 8"			1.00 EA		59.62				1.74		61.36		0.00 	61.36		
167.  R&R Furnace vent - rain cap and storm collar, 5"			1.00 EA		53.16				1.03		54.19		0.00 	54.19		
168.  R&R Furnace vent - rain cap and storm collar, 6"			1.00 EA		60.11				1.45		61.56		0.00 	61.56		
169.  R&R Furnace vent - rain cap and storm collar, 8"			1.00 EA		69.40				2.01		71.41		0.00 	71.41		
170.  Flue cap			1.00 EA		96.06				4.82		100.88		0.00 	100.88		
171.  R&R Fireplace - chimney chase cover - sheetmetal			1.00 EA		340.90				11.53		352.43		0.00 	352.43		
172.  Remove Additional charge for high roof (2 stories			2.00 SQ		3.77				0.00		7.54		0.00 	7.54		
or greater)																
173.  Additional charge for high roof (2 stories or greater)			2.00 SQ		9.35				0.00		18.70		0.00 	18.70		
174.  Remove Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ		9.99				0.00		19.98		0.00 	19.98		
175.  Additional charge for steep roof - 7/12 to 9/12 slope			2.00 SQ		21.17				0.00		42.34		0.00 	42.34		
176.  Remove Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ		15.71				0.00		31.42		0.00 	31.42		
177.  Additional charge for steep roof - 10/12 - 12/12 slope			2.00 SQ		33.26				0.00		66.52		0.00 	66.52		
178.  Remove Additional charge for steep roof greater than 12/12 slope			2.00 SQ		19.50				0.00		39.00		0.00 	39.00		
179.  Additional charge for steep roof greater than 12/12 slope			2.00 SQ		42.07				0.00		84.14		0.00 	84.14		
The following line items are to replace the awnings on the front, right, back, and left sides of the building.																
180.  R&R Awning - Window/door - Alum./stl. (Oversized)			6.00 LF		78.34				21.60		491.64		0.00 	491.64		
181.  R&R Awning side panels - Alum./steel (Oversized) (PER SET)			1.00 EA		99.62				4.30		103.92		0.00 	103.92		
182.  Awning - Aluminum or steel - Add for each color stripe			2.00 EA		5.50				0.66		11.66		0.00 	11.66		
183.  Haul debris - per pickup truck load - including dump fees			1.00 EA		111.18				0.00		111.18		0.00 	111.18		
184.  Two ladders with jacks and plank (per day)			1.00 DA		104.12				0.00		104.12		0.00 	104.12		
The following line items are to repair water damage to the walls and flooring in this room.																
185.  R&R Batt insulation - 4" - R13 - unfaced batt			0.00 SF		0.73				0.00		0.00		0.00 	0.00		
186.  Drywall replacement per LF - up to 2' tall			0.00 LF		6.93				0.00		0.00		0.00 	0.00		
187.  Seal/prime then paint  (2 coats)			0.00 SF		0.58				0.00		0.00		0.00 	0.00		
188.  R&R Wallpaper			0.00 SF		2.26				0.00		0.00		0.00 	0.00		
189.  R&R Baseboard - 2 1/4"			0.00 LF		2.22				0.00		0.00		0.00 	0.00		
190.  Paint baseboard - one coat			0.00 LF		0.57				0.00		0.00		0.00 	0.00		
																														
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY		UNIT PRICE				TAX		RCV		DEPREC.	ACV		
191.  R&R Vinyl floor covering (sheet goods)			0.00 SF		3.50				0.00		0.00		0.00 	0.00		
192.  R&R Underlayment - 1/4" lauan/mahogany plywood			0.00 SF		1.51				0.00		0.00		0.00 	0.00		
193.  R&R Vanity			3.00 LF		128.12				17.64		402.00		0.00 	402.00		
194.  Sink faucet - Detach & reset			1.00 EA		74.20				0.00		74.20		0.00 	74.20		
195.  P-trap assembly - Detach & reset			1.00 EA		47.28				0.00		47.28		0.00 	47.28		
196.  R&R Angle stop valve			1.00 EA		33.47				0.43		33.90		0.00 	33.90		
197.  Install Claw-foot tub supply lines			1.00 EA		103.13				0.00		103.13		0.00 	103.13		
198.  Toilet - Detach & reset			1.00 EA		151.02				0.27		151.29		0.00 	151.29		
The following line items are to repair water damage to the walls and ceiling in this room.																
199.  R&R Blown-in insulation - 12" depth - R30			10.00 SF		1.89				0.38		19.28		0.00 	19.28		
200.  R&R 5/8" drywall - hung, taped, floated, ready for paint			10.00 SF		2.34				0.34		23.74		0.00 	23.74		
201.  Apply anti-microbial agent to the surface area			10.00 SF		0.20				0.02		2.02		0.00 	2.02		
Application of anti-microbial agent to framing members to inhibit growth.																
202.  Seal the surface area w/latex based stain blocker - one coat			10.00 SF		0.54				0.04		5.44		0.00 	5.44		
203.  Paint  - two coats			0.00 SF		0.88				0.00		0.00		0.00 	0.00		
204.  R&R Acoustic ceiling (popcorn) texture			0.00 SF		1.21				0.00		0.00		0.00 	0.00		
205.  Texture drywall - light hand texture			0.00 SF		0.48				0.00		0.00		0.00 	0.00		
206.  Contents - move out then reset			1.00 EA		50.12				0.00		50.12		0.00 	50.12		
207.  Tree - removal and disposal - per hour including equipment			16.00 HR		70.37				0.00		1,125.92		0.00 	1,125.92		
"This line item is allowance to remove tree from structure so that repairs can be made.
Labor and equipment for 2 person, 8 hours each, to remove tree limbs and debris."																
208.  Crane and operator - 14 ton capacity - 65' extension boom			4.00 HR				171.33		0.00		685.32		0.00 	685.32		
209.  Skid steer loader and operator			4.00 HR				67.58		0.00		270.32		0.00 	270.32		
210.  Boom truck and operator - 20 ton			4.00 HR				106.00		0.00		424.00		0.00 	424.00		
The following line items are to replace the deck on the front, right, back, left side of the house.																
211.  R&R Deck planking - treated lumber (per SF)			0.00 SF				5.72		0.00		0.00		0.00 	0.00		
212.  R&R Deck planking - 5/4" treated lumber, 2 (per SF)			0.00 SF				5.83		0.00		0.00		0.00 	0.00		
213.  R&R Deck planking - Vinyl (per SF)			0.00 SF				9.46		0.00		0.00		0.00 	0.00		
214.  R&R Deck guard rail - treated lumber			10.00 LF				22.78		5.42		233.22		0.00 	233.22		
215.  R&R Deck guard rail - Vinyl			10.00 LF				42.49		15.80		440.70		0.00 	440.70		
216.  Dumpster load - Approx. 20 yards, 4 tons of debris			1.00 EA				420.00		0.00		420.00		0.00 	420.00		
The following line items are to pressure wash and restain the deck on the front, right, back, left side of the house.																
217.  Clean with pressure/chemical spray			1.00 SF				0.21		0.00		0.21		0.00 	0.21		
218.  Stain/finish deck			1.00 SF				0.58		0.01		0.59		0.00 	0.59		
															
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT PRICE						TAX		RCV		DEPREC.	ACV		
219.  Stain/finish deck handrail			1.00 LF                   4.22						0.06		4.28		0.00 	4.28		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
220.  R&R Fascia - metal - 4"			24.00 LF				2.96		1.27		72.31		0.00 	72.31		
221.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
222.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
223.  R&R Fascia - metal - 6"			24.00 LF				3.35		1.71		82.11		0.00 	82.11		
224.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
225.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
226.  R&R Fascia - metal - 8"			24.00 LF				3.65		1.92		89.52		0.00 	89.52		
227.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
228.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the dwelling on the XXXXXXX side of the house.																
229.  R&R Wrap custom fascia with aluminum (PER LF)			24.00 LF				9.92		2.66		240.74		0.00 	240.74		
230.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
231.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to replace the fence on the XXXXXXX side of the house, damaged by XXXXXXXX.																
232.  R&R Wood fence 5'- 6' high - treated			27.00 LF				22.90		15.67		633.97		0.00 	633.97		
233.  R&R Wood gate 5'- 6' high - treated			3.00 LF				30.91		2.71		95.44		0.00 	95.44		
234.  Seal & paint - wood fence/gate			162.00 SF				0.81		3.30		134.52		0.00 	134.52		
235.  R&R Temporary fencing			27.00 LF				5.48		0.00		147.96		0.00 	147.96		
236.  Single axle dump truck - per load - including dump fees			1.00 EA				204.41		0.00		204.41		0.00 	204.41		
The following line items are to pressure wash and restain the fence on the front, right, back, left side of the house.																
237.  Clean with pressure/chemical spray			1.00 SF				0.21		0.00		0.21		0.00 	0.21		
238.  Seal & paint - wood fence/gate			1.00 SF				0.81		0.02		0.83		0.00 	0.83		
"The following line items are to repair wind damage to the gutters and downspouts on the XXXXXXX side of the house.
Depreciation is based on the age and condition of the item.  The gutters are XXXX years old and have a 25 year average useful lifespan.  XX% depreciation withheld."																
239.  R&R Gutter / downspout - aluminum - up to 5"			24.00 LF				4.69		3.31		115.87		0.00 	115.87		
240.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
241.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
GUTTER WIND REPAIR MACROS																
																
																
																
																
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION                                                                   QUANTITY   UNIT PRICE								TAX			RCV        DEPREC.               ACV					
"The following line items are to repair wind damage to the gutters and downspouts on the XXXXXXX side of the house.
Depreciation is based on the age and condition of the item.  The gutters are XXXX years old and have a 25 year average useful lifespan.  XX% depreciation withheld."																
242.  R&R Gutter / downspout - galvanized - up to 5"			12.00 LF				3.91		1.09		48.01		0.00 	48.01		
243.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
244.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
GUTTER WIND REPAIR MACROS																
"The following line items are to repair wind damage to the gutters and downspouts on the XXXXXXX side of the house.
Depreciation is based on the age and condition of the item.  The gutters are XXXX years old and have a 25 year average useful lifespan.  XX% depreciation withheld."																
245.  R&R Gutter / downspout - plastic			12.00 LF				4.18		1.29		51.45		0.00 	51.45		
246.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
247.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to replace the gutters and downspouts on this building.																
"Front:
Gutters - 10LF Downspouts - 10:F"																
"Right:
Gutters - 10LF Downspouts - 10LF"																
"Back:
Gutters - 10LF Downspouts - 10LF"																
"Left:
Gutters - 10LF Downspouts - 10LF"																
248.  R&R Gutter / downspout - aluminum - up to 5"			100.00 LF				4.69		13.80		482.80		0.00 	482.80		
249.  R&R Gutter / downspout - galvanized - up to 5"			100.00 LF				3.91		9.12		400.12		0.00 	400.12		
250.  Prime & paint gutter / downspout			100.00 LF				1.04		1.50		105.50		0.00 	105.50		
251.  R&R Gutter / downspout - plastic			100.00 LF				4.18		10.74		428.74		0.00 	428.74		
252.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the dwelling on the XXXXXXX side of the house.																
253.  R&R Siding - hardboard - sheet			32.00 SF				2.34		2.11		76.99		0.00 	76.99		
254.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
255.  R&R House wrap (air/moisture barrier)			0.00 SF				0.26		0.00		0.00		0.00 	0.00		
256.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
257.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair water damage to the walls and flooring in this room.																
258.  R&R Batt insulation - 4" - R13 - unfaced batt			0.00 SF				0.73		0.00		0.00		0.00 	0.00		
259.  Drywall replacement per LF - up to 2' tall			0.00 LF				6.93		0.00		0.00		0.00 	0.00		
260.  Seal/prime then paint  (2 coats)			0.00 SF				0.58		0.00		0.00		0.00 	0.00		
261.  R&R Wallpaper			0.00 SF				2.26		0.00		0.00		0.00 	0.00		
262.  R&R Baseboard - 2 1/4"			0.00 LF				2.22		0.00		0.00		0.00 	0.00		
263.  Paint baseboard - one coat			0.00 LF				0.57		0.00		0.00		0.00 	0.00		
264.  R&R Vinyl floor covering (sheet goods)			0.00 SF				3.50		0.00		0.00		0.00 	0.00		
265.  R&R Underlayment - 1/4" lauan/mahogany plywood			0.00 SF				1.51		0.00		0.00		0.00 	0.00		
266.  R&R Vanity			3.00 LF				128.12		17.64		402.00		0.00 	402.00		
267.  Sink faucet - Detach & reset			1.00 EA				74.20		0.00		74.20		0.00 	74.20		
268.  Dishwasher - Detach & reset			1.00 EA				168.65		0.00		168.65		0.00 	168.65		
269.  Garbage disposer - Detach & reset			1.00 EA				99.14		0.00		99.14		0.00 	99.14		
270.  Range - gas - Remove & reset			1.00 EA				99.14		0.00		99.14		0.00 	99.14		
271.  Refrigerator - Remove & reset			1.00 EA				27.50		0.00		27.50		0.00 	27.50		
272.  R&R Cabinetry - lower (base) units			5.00 LF				157.12		38.10		823.70		0.00 	823.70		
273.  R&R Cabinetry - upper (wall) units			5.00 LF				114.45		25.30		597.55		0.00 	597.55		
274.  R&R Cabinetry - full height unit			2.00 LF				261.13		26.80		549.06		0.00 	549.06		
275.  R&R Countertop - post formed plastic laminate			15.00 LF				45.05		29.38		705.13		0.00 	705.13		
276.  R&R Countertop - flat laid plastic laminate			15.00 LF				37.63		23.41		587.86		0.00 	587.86		
277.  Add on for undermount sink cutout & polish -			1.00 EA				153.66		0.00		153.66		0.00 	153.66		
double basin																
278.  Add-on for mitered corner (Countertop)				2.00 EA			57.08		0.00		114.16		0.00 	114.16		
279.  Sink - double - Detach & reset				1.00 EA			98.20		0.00		98.20		0.00 	98.20		
The following line items are to repair the roof damaged by wind.																
280.  R&R Modified bitumen roof			1.00 SQ				289.14		5.71		294.85		0.00 	294.85		
281.  R&R Roof vent - turtle type - Metal			1.00 EA				42.27		0.94		43.21		0.00 	43.21		
282.  R&R Roof vent - turtle type - Plastic			1.00 EA				37.51		0.66		38.17		0.00 	38.17		
283.  R&R Roof vent - turbine type			1.00 EA				86.89		3.38		90.27		0.00 	90.27		
284.  R&R Ridge cap - composition shingles			12.00 LF				4.48		0.78		54.54		0.00 	54.54		
285.  R&R Continuous ridge vent - shingle-over style			12.00 LF				5.98		2.05		73.81		0.00 	73.81		
286.  R&R Continuous ridge vent - aluminum			12.00 LF				5.93		2.02		73.18		0.00 	73.18		
287.  R&R Flashing - pipe jack			1.00 EA				25.89		0.34		26.23		0.00 	26.23		
288.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
289.  R&R Exhaust cap - through roof - 6" to 8"			1.00 EA				59.62		1.74		61.36		0.00 	61.36		
290.  R&R Furnace vent - rain cap and storm collar, 5"			1.00 EA				53.16		1.03		54.19		0.00 	54.19		
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
291.  R&R Furnace vent - rain cap and storm collar, 6"			1.00 EA				60.11		1.45		61.56		0.00 	61.56		
292.  R&R Furnace vent - rain cap and storm collar, 8"			1.00 EA				69.40		2.01		71.41		0.00 	71.41		
293.  Flue cap			1.00 EA				96.06		4.82		100.88		0.00 	100.88		
294.  R&R Fireplace - chimney chase cover - sheetmetal			1.00 EA				340.90		11.53		352.43		0.00 	352.43		
295.  Remove Additional charge for high roof (2 stories or greater)			2.00 SQ				3.77		0.00		7.54		0.00 	7.54		
296.  Additional charge for high roof (2 stories or greater)			2.00 SQ				9.35		0.00		18.70		0.00 	18.70		
The following line items are to replace the patio cover on the front, right, back, left sides of the building.																
297.  R&R Patio Cover - Attached - Aluminum - Moderate Load			240.00 SF				11.98		110.45		2,985.65		0.00 	2,985.65		
298.  R&R Patio Cover - Fascia end - Non-guttered			24.00 LF				5.58		3.56		137.48		0.00 	137.48		
299.  R&R Patio Cover - Fascia end - Guttered			20.00 LF				8.18		4.52		168.12		0.00 	168.12		
The following line items are to repaint the deck handrail on the XXXXXXX side of the house.																
300.	Stain/finish deck handrail		24.00 LF				4.22		1.51		102.79		0.00 	102.79		
301.	R&R Metal roofing		100.00 SF				3.61		7.38		368.38		0.00 	368.38		
302.	R&R Ridge cap - metal roofing		10.00 LF				5.23		1.25		53.55		0.00 	53.55		
303.	R&R Power attic vent cover only - metal		1.00 EA				66.83		1.79		68.62		0.00 	68.62		
304.	Flashing - pipe jack		1.00 EA				20.85		0.34		21.19		0.00 	21.19		
305.	Flashing - pipe jack - lead		1.00 EA				49.36		2.05		51.41		0.00 	51.41		
306.	R&R Flashing - pipe jack - split boot		1.00 EA				52.54		1.84		54.38		0.00 	54.38		
307.	Digital satellite system - Detach & reset		1.00 EA				23.78		0.00		23.78		0.00 	23.78		
308.	Ridge / Hip / Rake cap - tile roofing		10.00 LF				9.34		4.15		97.55		0.00 	97.55		
309.	Furnace vent - rain cap and storm collar, 5"		1.00 EA				45.50		1.03		46.53		0.00 	46.53		
310.	Furnace vent - rain cap and storm collar, 8"		1.00 EA				61.74		2.01		63.75		0.00 	63.75		
311.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA				59.62		1.74		61.36		0.00 	61.36		
312.	Additional charge for high roof (2 stories or greater)		10.00 SQ				9.35		0.00		93.50		0.00 	93.50		
313.	Additional charge for steep roof - 7/12 to 9/12 slope		10.00 SQ				21.17		0.00		211.70		0.00 	211.70		
"314.
slope"	Additional charge for steep roof - 10/12 - 12/12		10.00 SQ				33.26		0.00		332.60		0.00 	332.60		
315.	Flashing - rain diverter		1.00 EA				22.94		0.54		23.48		0.00 	23.48		
316.	Valley metal		10.00 LF				3.33		0.98		34.28		0.00 	34.28		
317.	Valley metal - (W) profile		10.00 LF				4.01		1.39		41.49		0.00 	41.49		
318.	Chimney flashing - average (32" x 36")		1.00 EA				201.06		3.21		204.27		0.00 	204.27		
319.	Remove Lightning protection system		1.00 EA				161.48		0.00		161.48		0.00 	161.48		
320.	Install Lightning protection system		1.00 EA				1,483.11		0.00		1,483.11		0.00 	1,483.11		
321.	Remove Tile roofing - Clay - "S" or flat tile		0.00 SQ				140.72		0.00		0.00		0.00 	0.00		
322.	Tile roofing - Clay - "S" or flat tile		0.00 SQ				445.74		0.00		0.00		0.00 	0.00		
323.	Remove Tile roofing - Concrete - "S" or flat tile		0.00 SQ				140.72		0.00		0.00		0.00 	0.00		
324.	Tile roofing - Concrete - "S" or flat tile		0.00 SQ				346.93		0.00		0.00		0.00 	0.00		
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
325.  Ice & water shield			10.00 SF				1.02		0.21		10.41		0.00 	10.41		
326.  Roof vent - turtle type - Metal			1.00 EA				35.84		0.94		36.78		0.00 	36.78		
327.  Roof vent - turtle type - Plastic			1.00 EA				31.08		0.66		31.74		0.00 	31.74		
328.  Roof vent - turbine type			1.00 EA				80.46		3.38		83.84		0.00 	83.84		
329.  R&R Power attic vent cover only - metal			1.00 EA				66.83		1.79		68.62		0.00 	68.62		
330.  Flashing - pipe jack			1.00 EA				20.85		0.34		21.19		0.00 	21.19		
331.  Flashing - pipe jack - lead			1.00 EA				49.36		2.05		51.41		0.00 	51.41		
332.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
Typically used for power mast roof penetration.																
333.	Digital satellite system - Detach & reset		1.00 EA				23.78		0.00		23.78		0.00 	23.78		
334.	Ridge / Hip / Rake cap - tile roofing		10.00 LF				9.34		4.15		97.55		0.00 	97.55		
335.	Furnace vent - rain cap and storm collar, 5"		1.00 EA				45.50		1.03		46.53		0.00 	46.53		
336.	Furnace vent - rain cap and storm collar, 8"		1.00 EA				61.74		2.01		63.75		0.00 	63.75		
337.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA				59.62		1.74		61.36		0.00 	61.36		
338.	Additional charge for high roof (2 stories or greater)		10.00 SQ				9.35		0.00		93.50		0.00 	93.50		
339.	Additional charge for steep roof - 7/12 to 9/12 slope		10.00 SQ				21.17		0.00		211.70		0.00 	211.70		
"340.
slope"	Additional charge for steep roof - 10/12 - 12/12		10.00 SQ				33.26		0.00		332.60		0.00 	332.60		
341.	Flashing - rain diverter		1.00 EA				22.94		0.54		23.48		0.00 	23.48		
342.	Valley metal		10.00 LF				3.33		0.98		34.28		0.00 	34.28		
343.	Valley metal - (W) profile		10.00 LF				4.01		1.39		41.49		0.00 	41.49		
344.	Chimney flashing - average (32" x 36")		1.00 EA				201.06		3.21		204.27		0.00 	204.27		
345.	Remove Lightning protection system		1.00 EA				161.48		0.00		161.48		0.00 	161.48		
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
Detach and reset lightning protection system.																
346.  Install Lightning protection system			1.00 EA				1,483.11		0.00		1,483.11		0.00 	1,483.11		
347.  R&R Cupola - Wood - Small			1.00 EA				560.10		26.06		586.16		0.00 	586.16		
CONTINUED - GROUPINGTREESKETCH																
"DESCRIPTION                                                                   QUANTITY   UNIT PRICE
The following line items are to repair the roof damaged by wind."								TAX			RCV        DEPREC.               ACV					
348.  Remove Roll roofing			1.00 SQ				31.91		0.00		31.91		0.00 	31.91		
349.  Roll roofing			1.00 SQ				77.17		3.42		80.59		0.00 	80.59		
350.  R&R Roof vent - turtle type - Metal			1.00 EA				42.27		0.94		43.21		0.00 	43.21		
351.  R&R Roof vent - turtle type - Plastic			1.00 EA				37.51		0.66		38.17		0.00 	38.17		
352.  R&R Roof vent - turbine type			1.00 EA				86.89		3.38		90.27		0.00 	90.27		
353.  R&R Ridge cap - composition shingles			12.00 LF				4.48		0.78		54.54		0.00 	54.54		
354.  R&R Continuous ridge vent - shingle-over style			12.00 LF				5.98		2.05		73.81		0.00 	73.81		
355.  R&R Continuous ridge vent - aluminum			12.00 LF				5.93		2.02		73.18		0.00 	73.18		
356.  R&R Flashing - pipe jack			1.00 EA				25.89		0.34		26.23		0.00 	26.23		
357.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
358.  R&R Exhaust cap - through roof - 6" to 8"			1.00 EA				59.62		1.74		61.36		0.00 	61.36		
359.  R&R Furnace vent - rain cap and storm collar, 5"			1.00 EA				53.16		1.03		54.19		0.00 	54.19		
360.  R&R Furnace vent - rain cap and storm collar, 6"			1.00 EA				60.11		1.45		61.56		0.00 	61.56		
361.  R&R Furnace vent - rain cap and storm collar, 8"			1.00 EA				69.40		2.01		71.41		0.00 	71.41		
362.  Flue cap			1.00 EA				96.06		4.82		100.88		0.00 	100.88		
363.  R&R Fireplace - chimney chase cover - sheetmetal			1.00 EA				340.90		11.53		352.43		0.00 	352.43		
364.  Remove Additional charge for high roof (2 stories			2.00 SQ				3.77		0.00		7.54		0.00 	7.54		
"or greater)
365.  Additional charge for high roof (2 stories or greater)            2.00 SQ                   9.35                0.00               18.70                (0.00)               18.70
The following line items are to replace the screens on the XXXXXXX side of the house."																
366.  R&R Window screen, 1 - 9 SF			1.00 EA				27.79		1.31		29.10		0.00 	29.10		
367.  R&R Window screen, 10 - 16 SF			1.00 EA				35.19		1.76		36.95		0.00 	36.95		
368.  R&R Window screen, 17 - 25 SF			1.00 EA				44.94		2.34		47.28		0.00 	47.28		
369.  R&R Window screen, 26 - 32 SF			1.00 EA				48.84		2.57		51.41		0.00 	51.41		
370.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
"The following line items are to replace the siding on the front, right, back, and left sides of the house.
No damage found to the front, right, back, left side of the house at time of inspection."																
371.  R&R Siding - steel (29 gauge)			0.00 SF				4.61		0.00		0.00		0.00 	0.00		
373.  R&R Siding - aluminum (.024 thickness)			0.00 SF				4.37		0.00		0.00		0.00 	0.00		
374.  R&R Rigid foam insulation board - 1/2"			0.00 SF				0.88		0.00		0.00		0.00 	0.00		
375.  R&R Builder board - 1/2" (composition or fiberboard sheathing)			0.00 SF				1.37		0.00		0.00		0.00 	0.00		
376.  R&R Light/outlet J-block - Vinyl			1.00 EA				18.75		0.61		19.36		0.00 	19.36		
377.  R&R Metal inside corner post			10.00 LF				3.98		0.70		40.50		0.00 	40.50		
378.  R&R Metal outside corner post			10.00 LF				5.27		1.47		54.17		0.00 	54.17		
379.  R&R Clothes dryer vent - installed			1.00 EA				49.77		1.40		51.17		0.00 	51.17		
380.  Dumpster load - Approx. 20 yards, 4 tons of debris			1.00 EA				420.00		0.00		420.00		0.00 	420.00		
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION                                                                   QUANTITY   UNIT PRICE								TAX			RCV        DEPREC.               ACV					
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
381.  R&R Siding - aluminum (.024 thickness)			32.00 SF				4.37		4.90		144.74		0.00 	144.74		
382.  R&R Metal inside corner post			8.00 LF				3.98		0.56		32.40		0.00 	32.40		
383.  R&R Metal outside corner post			8.00 LF				5.27		1.18		43.34		0.00 	43.34		
384.  R&R Metal J trim			24.00 LF				2.82		0.69		68.37		0.00 	68.37		
385.  Metal or Vinyl siding - Detach & reset			100.00 SF				1.32		0.24		132.24		0.00 	132.24		
386.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
387.  R&R House wrap (air/moisture barrier)			0.00 SF				0.26		0.00		0.00		0.00 	0.00		
388.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
389.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repaint the front, right, back, and left sides of the building.																
390.  Seal & paint wood siding			0.00 SF				0.88		0.00		0.00		0.00 	0.00		
391.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
Ladder jacks required for more than two-story elevations.																
The following line items are to replace the siding on the front, right, back, and left sides of the house.																
No damage found to the front, right, back, left side of the house at time of inspection.																
392.  R&R Siding - vinyl			0.00 SF				2.86		0.00		0.00		0.00 	0.00		
393.  R&R Light/outlet J-block - Vinyl			1.00 EA				18.75		0.61		19.36		0.00 	19.36		
394.  R&R Vinyl inside corner post			10.00 LF				3.96		0.68		40.28		0.00 	40.28		
395.  R&R Vinyl outside corner post			10.00 LF				4.51		1.01		46.11		0.00 	46.11		
396.  R&R Clothes dryer vent - installed			1.00 EA				49.77		1.40		51.17		0.00 	51.17		
397.  Dumpster load - Approx. 20 yards, 4 tons of debris			1.00 EA				420.00		0.00		420.00		0.00 	420.00		
The following line items are to repair the siding on the XXXXXX side of the house.																
398.  R&R Siding - vinyl			0.00 SF				2.86		0.00		0.00		0.00 	0.00		
399.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
400.  R&R Wrap wood window frame & trim with aluminum sheet			1.00 EA				143.24		1.95		145.19		0.00 	145.19		
401.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
402.  R&R Soffit - metal			24.00 SF				3.73		2.30		91.82		0.00 	91.82		
403.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
404.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
405.  R&R Soffit - vinyl			24.00 SF				3.48		1.94		85.46		0.00 	85.46		
406.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
																
																
																
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
407.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
408.  R&R Soffit - wood			24.00 SF				3.91		1.86		95.70		0.00 	95.70		
409.  Prime & paint exterior soffit - wood			96.00 SF				1.38		1.96		134.44		0.00 	134.44		
410.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
411.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to replace the shed.																
412.  R&R Storage shed - Metal - Gable type - 10' x 12'			1.00 EA				1,018.14		36.99		1,055.13		0.00 	1,055.13		
413.  Contents - move out then reset			1.00 EA				50.12		0.00		50.12		0.00 	50.12		
414.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to replace the shed.																
415.  Storage shed - Metal - Gable type - 10' x 12'			1.00 EA				1,018.14		25.05		1,043.19		0.00 	1,043.19		
416.  Exterior Structure Installer - per hour - to remove and replace the shed*			7.00 HR				60.04		0.00		420.28		0.00 	420.28		
417.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
418.  R&R Siding - steel (29 gauge)			32.00 SF				4.61		5.36		152.88		0.00 	152.88		
419.  R&R Metal inside corner post			8.00 LF				3.98		0.56		32.40		0.00 	32.40		
420.  R&R Metal outside corner post			8.00 LF				5.27		1.18		43.34		0.00 	43.34		
421.  R&R Metal J trim			24.00 LF				2.82		0.69		68.37		0.00 	68.37		
422.  Metal or Vinyl siding - Detach & reset			100.00 SF				1.32		0.24		132.24		0.00 	132.24		
423.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
424.  R&R House wrap (air/moisture barrier)			0.00 SF				0.26		0.00		0.00		0.00 	0.00		
425.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
426.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair tree damage to the XXXXX slope of the roof on the house.																
427.  R&R 3 tab - 25 yr. - composition shingle roofing (per SHINGLE)			30.00 EA				11.35		2.86		343.36		0.00 	343.36		
428.  R&R Laminated - comp. shingle rfg (per SHINGLE)			30.00 EA				11.55		3.22		349.72		0.00 	349.72		
429.  R&R Laminated - High grade - comp. shingle rfg. (per SHINGLE)			30.00 EA				12.32		4.00		373.60		0.00 	373.60		
430.  R&R Laminated - Deluxe grd - comp. shingle rfg. (per SHINGLE)			30.00 EA				13.06		4.10		395.90		0.00 	395.90		
431.  R&R Ridge cap - composition shingles			24.00 LF				4.48		1.57		109.09		0.00 	109.09		
432.  R&R Ridge cap - High profile - composition shingles			24.00 LF				5.79		3.57		142.53		0.00 	142.53		
																
																
																
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
433.  Roofing felt - 15 lb.			1.00 SQ				18.00		0.36		18.36		0.00 	18.36		
434.  R&R Sheathing - plywood - 1/2" CDX			32.00 SF				1.76		1.32		57.64		0.00 	57.64		
435.  R&R Rafters - 2x8 - Labor only - (using rafter length)			24.00 LF				2.47		0.04		59.32		0.00 	59.32		
Rafter line items are to repair/sister rafters damaged by fallen tree.																
436.  R&R 2" x 8" lumber (1.33 BF per LF)			24.00 LF				2.76		1.38		67.62		0.00 	67.62		
437.  R&R Drip edge			24.00 LF				1.59		0.85		39.01		0.00 	39.01		
The fo																
TREE DEBRIS REMOVAL																
"This is a line item for hauling off only the tree debris that was removed from the house (chopped and dropped) so that repairs can be made.
438.  Tree - removal and disposal - per hour including                  5.00 HR                70.37                0.00             351.85                (0.00)             351.85
equipment
This line item is allowance to haul away tree debris per policy provisions.
Labor and equipment for 2 persons, 4 hours each to remove tree debris from property subject to coverage limit.
439.  Dumpster load - Approx. 20 yards, 4 tons of debris              1.00 EA              420.00                0.00             420.00                (0.00)             420.00
The following line items are to repair the electrical service damaged by fallen trees."																
440.  R&R Meter mast for overhead power - 2" conduit			1.00 EA				392.75		6.12		398.87		0.00 	398.87		
441.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
442.  R&R Meter base and main disconnect - 200 amp			1.00 EA				383.58		9.60		393.18		0.00 	393.18		
443.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
444.  R&R Siding - vinyl			32.00 SF				2.86		2.42		93.94		0.00 	93.94		
445.  R&R Light/outlet J-block - Vinyl			1.00 EA				18.75		0.61		19.36		0.00 	19.36		
446.  R&R Vinyl J-vent			1.00 EA				20.09		0.69		20.78		0.00 	20.78		
447.  R&R Vinyl J trim			24.00 LF				2.79		0.65		67.61		0.00 	67.61		
448.  R&R Vinyl inside corner post			8.00 LF				3.96		0.55		32.23		0.00 	32.23		
449.  R&R Vinyl outside corner post			8.00 LF				4.51		0.81		36.89		0.00 	36.89		
450.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
451.  R&R House wrap (air/moisture barrier)			0.00 SF				0.26		0.00		0.00		0.00 	0.00		
452.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
453.  Haul debris - per pickup truck load - including			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
"dump fees
The following line items are to repair water damage to the walls and flooring in this room."																
454.  R&R Carpet			0.00 SF				2.99		0.00		0.00		0.00 	0.00		
456.  Carpet pad			0.00 SF				0.59		0.00		0.00		0.00 	0.00		
457.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
																
																
																
																
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION                                                                   QUANTITY   UNIT PRICE								TAX			RCV        DEPREC.               ACV					
"===========================================================================
Water mitigation and remediation"																
===========================================================================																
458.  Air mover (per 24 hour period) - No monitoring			1.00 EA				25.22		0.00		25.22		0.00 	25.22		
X air movers for X days																
459.  Dehumidifier (per 24 hour period) - No monitoring			1.00 EA				55.39		0.00		55.39		0.00 	55.39		
X dehumidifier(s) for X days																
460.  Heat drying - thermal air mover - Electric			0.00 DA				180.00		0.00		0.00		0.00 	0.00		
X heater air movers for X days																
461.  Containment Barrier/Airlock/Decon. Chamber			100.00 SF				0.60		0.54		60.54		0.00 	60.54		
462.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.60		0.00		111.60		0.00 	111.60		
463.  Tear out wet drywall, cleanup, bag for disposal			10.00 SF				0.87		0.11		8.81		0.00 	8.81		
464.  Tear out baseboard			0.00 LF				0.34		0.00		0.00		0.00 	0.00		
465.  Baseboard - Detach & reset			0.00 LF				1.38		0.00		0.00		0.00 	0.00		
466.  Water extraction from carpeted floor			0.00 SF				0.44		0.00		0.00		0.00 	0.00		
467.  Tear out wet non-salvageable carpet, cut & bag for disp.			0.00 SF				0.44		0.00		0.00		0.00 	0.00		
468.  Tear out wet carpet pad and bag for disposal			0.00 SF				0.41		0.00		0.00		0.00 	0.00		
469.  Block and pad furniture in room			1.00 EA				34.59		0.07		34.66		0.00 	34.66		
The following line items are to replace the storm windows and doors on the front, right, back, and left sides of the building.																
470.  R&R Storm window - aluminum, 3-11 sf			1.00 EA				106.59		4.61		111.20		0.00 	111.20		
472.  R&R Storm door assembly			1.00 EA				217.74		8.64		226.38		0.00 	226.38		
The following line items are to repair wind damage to the window glass on the XXXXXXX side of the house.																
474.  Reglaze window, 1 - 9 sf			1.00 EA				64.92		2.37		67.29		0.00 	67.29		
475.  Reglaze window, 10 - 16 sf			1.00 EA				115.42		4.21		119.63		0.00 	119.63		
476.  Reglaze window, 17 - 24 sf			1.00 EA				173.08		6.32		179.40		0.00 	179.40		
477.  R&R Glazing bead - Vinyl			24.00 LF				1.29		0.84		31.80		0.00 	31.80		
478.  R&R Glazing bead - Aluminum			24.00 LF				1.16		0.65		28.49		0.00 	28.49		
479.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to replace the vinyl windows on the front, right, back, and left sides of the building.																
480.  R&R Vinyl window, single hung, 9-12 sf			1.00 EA				204.83		8.40		213.23		0.00 	213.23		
481.  R&R Vinyl window - double hung, 9-12 sf			1.00 EA				251.74		11.21		262.95		0.00 	262.95		
482.  R&R Vinyl window, picture/fixed, 12-23 sf			1.00 EA				221.89		8.98		230.87		0.00 	230.87		
483.  R&R Vinyl window - casement, 6-8 sf			1.00 EA				271.34		12.39		283.73		0.00 	283.73		
484.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to replace the metal clad wood windows on the front, right, back, and left sides of the building.																
485.  R&R Wood window - single hung, 9-12 sf			1.00 EA				399.80		18.15		417.95		0.00 	417.95		
																
																
																
																
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY   UNIT				PRICE		TAX		RCV		DEPREC.	ACV		
486.  R&R Wood window - double hung, 9-12 sf			1.00 EA				457.40		21.61		479.01		0.00 	479.01		
487.  R&R Wood window - picture (fixed), 24-32 sf			1.00 EA				760.19		39.80		799.99		0.00 	799.99		
488.  R&R Wood window - casement, 12-23 sf			1.00 EA				520.44		24.92		545.36		0.00 	545.36		
489.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
The following line items are to repair wind damage to the fascia on the XXXXXXX side of the house.																
490.  R&R Siding - beveled - pine or equal (clapboard)			32.00 SF				4.70		4.72		155.12		0.00 	155.12		
491.  Seal & paint wood siding			0.00 SF				0.88		0.00		0.00		0.00 	0.00		
492.  R&R Fanfold foam insulation board - 1/4"			0.00 SF				0.62		0.00		0.00		0.00 	0.00		
493.  R&R House wrap (air/moisture barrier)			0.00 SF				0.26		0.00		0.00		0.00 	0.00		
494.  Two ladders with jacks and plank (per day)			1.00 DA				104.12		0.00		104.12		0.00 	104.12		
495.  Haul debris - per pickup truck load - including dump fees			1.00 EA				111.18		0.00		111.18		0.00 	111.18		
496.  Wood shakes - medium (1/2") hand split			0.00 SQ				343.65		0.00		0.00		0.00 	0.00		
497.  Remove Tear off, haul and dispose of wood shakes/shingles			0.00 SQ				47.04		0.00		0.00		0.00 	0.00		
498.  Drip edge			10.00 LF				1.35		0.35		13.85		0.00 	13.85		
499.  Drip edge/gutter apron			10.00 LF				1.48		0.43		15.23		0.00 	15.23		
500.  Ice & water shield			10.00 SF				1.02		0.21		10.41		0.00 	10.41		
501.  Roof vent - turtle type - Metal			1.00 EA				35.84		0.94		36.78		0.00 	36.78		
502.  Roof vent - turtle type - Plastic			1.00 EA				31.08		0.66		31.74		0.00 	31.74		
503.  Roof vent - turbine type			1.00 EA				80.46		3.38		83.84		0.00 	83.84		
504.  R&R Power attic vent cover only - metal			1.00 EA				66.83		1.79		68.62		0.00 	68.62		
505.  Flashing - pipe jack			1.00 EA				20.85		0.34		21.19		0.00 	21.19		
506.  Flashing - pipe jack - lead			1.00 EA				49.36		2.05		51.41		0.00 	51.41		
507.  R&R Flashing - pipe jack - split boot			1.00 EA				52.54		1.84		54.38		0.00 	54.38		
Typically used for power mast roof penetration.																
508.	Digital satellite system - Detach & reset		1.00 EA				23.78		0.00		23.78		0.00 	23.78		
509.	Continuous ridge vent - shingle-over style		10.00 LF				5.37		1.71		55.41		0.00 	55.41		
510.	Sheathing - plywood - 1/2" CDX		32.00 SF				1.36		1.32		44.84		0.00 	44.84		
511.	Ridge cap - composition shingles		10.00 LF				3.19		0.65		32.55		0.00 	32.55		
512.	Furnace vent - rain cap and storm collar, 5"		1.00 EA				45.50		1.03		46.53		0.00 	46.53		
513.	Furnace vent - rain cap and storm collar, 8"		1.00 EA				61.74		2.01		63.75		0.00 	63.75		
514.	R&R Exhaust cap - through roof - 6" to 8"		1.00 EA				59.62		1.74		61.36		0.00 	61.36		
515.	Additional charge for high roof (2 stories or greater)		10.00 SQ				9.35		0.00		93.50		0.00 	93.50		
516.	Additional charge for steep roof - 7/12 to 9/12 slope		10.00 SQ				21.17		0.00		211.70		0.00 	211.70		
"517.
slope"	Additional charge for steep roof - 10/12 - 12/12		10.00 SQ				33.26		0.00		332.60		0.00 	332.60		
518.	Flashing - rain diverter		1.00 EA				22.94		0.54		23.48		0.00 	23.48		
																
																
CONTINUED - GROUPINGTREESKETCH																
DESCRIPTION			QUANTITY		UNIT PRICE				TAX		RCV		DEPREC.	ACV		
519.  Valley metal			10.00 LF		3.33				0.98		34.28		0.00 	34.28		
520.  Valley metal - (W) profile			10.00 LF		4.01				1.39		41.49		0.00 	41.49		
521.  Chimney flashing - average (32" x 36")			1.00 EA		201.06				3.21		204.27		0.00 	204.27		
522.  Remove Lightning protection system			1.00 EA		161.48				0.00		161.48		0.00 	161.48		
Detach and reset lightning protection system.																
523.  Install Lightning protection system			1.00 EA		1,483.11				0.00		1,483.11		0.00 	1,483.11		
524.  R&R Cupola - Wood - Small			1.00 EA		560.10				26.06		586.16		0.00 	586.16		
The following line items are to repair wind damage to the door and window wraps on the XXXXXXX side of the house.																
525.  R&R Wrap wood window frame & trim with aluminum sheet			1.00 EA		143.24				1.95		145.19		0.00 	145.19		
526.  R&R Wrap wood window frame & trim with aluminum sheet - Small			1.00 EA		94.54				1.29		95.83		0.00 	95.83		
527.  R&R Wrap wood window frame & trim with aluminum sheet - Large			1.00 EA		191.35				2.38		193.73		0.00 	193.73		
528.  R&R Wrap wood window frame & trim with aluminum sheet - XLarge			1.00 EA		232.45				3.15		235.60		0.00 	235.60		
529.  R&R Custom bent aluminum (PER LF)			12.00 LF		13.30				1.35		160.95		0.00 	160.95		
530.  R&R Wrap wood garage door frame & trim with aluminum (PER LF)			30.00 LF		8.84				3.33		268.53		0.00 	268.53		
531.  R&R Wrap wood post with aluminum (PER LF)			16.00 LF		10.55				1.76		170.56		0.00 	170.56		
532.  R&R Wrap wood door frame & trim with aluminum (PER LF)			16.50 LF		9.74				1.81		162.53		0.00 	162.53		
533.  Haul debris - per pickup truck load - including dump fees			1.00 EA		111.18				0.00		111.18		0.00 	111.18		
Total:  GROUPINGTREESKETCH									1,259.25		65,657.20		0.00	65,657.20		
Labor Minimums Applied																
DESCRIPTION			QUANTITY		UNIT PRICE				TAX		RCV		DEPREC.	ACV		
492.  Awning labor minimum			1.00 EA		6.39				0.00		6.39		0.00 	6.39		
84.  Insulation labor minimum			1.00 EA		84.81				0.00		84.81		0.00 	84.81		
270.  Drywall labor minimum			1.00 EA		243.83				0.00		243.83		0.00 	243.83		
442.  Wallpaper labor minimum			1.00 EA		110.78				0.00		110.78		0.00 	110.78		
268.  Finish carpentry labor minimum			1.00 EA		140.66				0.00		140.66		0.00 	140.66		
438.  Vinyl floor covering labor minimum			1.00 EA		157.18				0.00		157.18		0.00 	157.18		
256.  Framing labor minimum			1.00 EA		30.80				0.00		30.80		0.00 	30.80		
74.  Drywall labor minimum			1.00 EA		288.74				0.00		288.74		0.00 	288.74		
518.  Temporary repair services labor minimum			1.00 EA		46.97				0.00		46.97		0.00 	46.97		
428.  General labor - labor minimum			1.00 EA		17.86				0.00		17.86		0.00 	17.86		
372.  Siding labor minimum			1.00 EA		43.42				0.00		43.42		0.00 	43.42		
455.  Carpet labor minimum			1.00 EA		157.18				0.00		157.18		0.00 	157.18		
																
																
CONTINUED - Labor Minimums Applied																
DESCRIPTION		QUANTITY   UNIT PRICE								TAX	RCV	DEPREC.			ACV	
473.  Door labor minimum		1.00 EA				66.92				0.00	66.92	0.00 			66.92	
Totals:  Labor Minimums Applied										0.00	1,395.54	0.00			1,395.54	
Line Item Totals:  GROUPINGTREESKETCH		1,259.25									67,052.74	0.00        67,052.74				
Coverage		Item Total				%					ACV Total	%				
Dwelling		63,025.80				93.99%					63,025.80	93.99%				
Other Structures		4,026.94				6.01%					4,026.94	6.01%				
Contents		0.00				0.00%					0.00	0.00%				
Total		67,052.74				100.00%					67,052.74	100.00%				
"""

# Optional shared KB appended to all perils (leave empty if you don’t want it)
SHARED_KNOWLEDGE_BASE = r""" """

# ──────────────────────────────────────────────────────────────────────
# 2) Unified schema (items + summary required; rest optional)
# ──────────────────────────────────────────────────────────────────────
ESTIMATE_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "version":      {"type": "string"},
        "generated_at": {"type": "string", "format": "date-time"},
        "currency":     {"type": "string", "pattern": "^[A-Z]{3}$"},
        "peril":        {"type": "string", "enum": ["water", "wind", "fire", "mixed"]},
        "location":     {"type": "string"},
        "items": {
            "type": "array",
            "minItems": 0,
            "items": {"$ref": "#/definitions/LineItem"}
        },
        "summary": {
            "type": "object",
            "properties": {
                "total_project_cost": {"type": "number"},
                "estimate_reasoning": {"type": "string"},
                "future_actions": {"type": "array", "items": {"type": "string"}}
            },
            "required": ["total_project_cost", "estimate_reasoning", "future_actions"],
            "additionalProperties": False
        }
    },
    "required": ["items", "summary"],
    "additionalProperties": False,
    "definitions": {
        "UnitCode": {
            "type": "string",
            "enum": [
                "EA","LF","SF","SQ","SY","HR","FT","YD","GL","GAL","CF","CY","BX",
                "KT","LB","TN","RL","RM","LN","MO","WK","DAY","PH","SET","ROLL","SHT",
                "PC","PR"
            ]
        },
        "LineItem": {
            "type": "object",
            "description": "Choose items from the relevant KB. Decide QUANTITY per industry standard. TOTAL_PRICE = QUANTITY * UNIT_PRICE + TAX.",
            "properties": {
                "id":           {"type": ["integer","string"]},
                "line_items":   {"type": "string", "minLength": 1},
                "QUANTITY":     {"type": "number", "minimum": 0},
                "UNIT_PRICE":   {"type": "number", "minimum": 0},
                "TAX":          {"type": "number", "minimum": 0, "default": 0},
                "TOTAL_PRICE":  {"type": "number", "minimum": 0},
                "Details":      {"type": "string", "default": ""},
                "unit_code":    {"$ref": "#/definitions/UnitCode"},
                "category":     {"type": "string"},
                "tags":         {"type": "array", "items": {"type": "string"}, "uniqueItems": True},
                "source": {
                    "type": "object",
                    "properties": {
                        "catalog_row": {"type": "string"},
                        "file": {"type": "string"},
                        "page": {"type": "integer", "minimum": 1}
                    },
                    "additionalProperties": False
                },
                "metadata": {"type": "object", "additionalProperties": True}
            },
            "required": ["id","line_items","QUANTITY","UNIT_PRICE","TOTAL_PRICE","unit_code","category"],
            "additionalProperties": False
        }
    }
}

STRICT_JSON = (
    "Return ONLY raw JSON that conforms to the schema below. "
    "Do NOT include markdown code fences or any extra text."
)

# ──────────────────────────────────────────────────────────────────────
# 3) Instruction builder (embeds KB + json.dumps(schema, indent=2))
# ──────────────────────────────────────────────────────────────────────
def _kb_for(peril: str, override: Optional[str] = None) -> str:
    """
    No env vars. Priority: explicit override → built-in default.
    Optionally append SHARED_KNOWLEDGE_BASE if you filled it.
    """
    base = (override or "").strip()
    if not base:
        base = {
            "water": WATER_KNOWLEDGE_BASE,
            "fire":  FIRE_KNOWLEDGE_BASE,
            "wind":  WIND_KNOWLEDGE_BASE,
        }.get(peril, "").strip()
    extra = SHARED_KNOWLEDGE_BASE.strip()
    if extra:
        base = (base + "\n\n" + extra) if base else extra
    return base

def make_peril_instructions(peril: str, kb: str) -> str:
    return (
        f"You are a licensed public adjuster specializing in {peril} damage.\n"
        "Use the KNOWLEDGE BASE to select appropriate line items for full estimate.\n"
         "If a floor plan was not provided, Try to guess the measures based on average sizes of objects and from the knowledge base."
        "For each item, compute TOTAL_PRICE = QUANTITY * UNIT_PRICE + TAX.\n"
        "Specialized instruction: in cases where more then 40 percent of a block (ex:roof shingels, tile wall etc.) is damaged you will replace the entire block (wall, roof slope floor etc.)."
        f"{STRICT_JSON}\n\n"
        "KNOWLEDGE BASE:\n"
        f"{kb}\n\n"
        "SCHEMA (copy exactly):\n"
        + json.dumps(ESTIMATE_SCHEMA, indent=2)
    )

# ──────────────────────────────────────────────────────────────────────
# 4) Public builders (what your task imports & uses)
# ──────────────────────────────────────────────────────────────────────
def build_insurance_agents(
    *,
    water_kb: Optional[str] = None,
    fire_kb: Optional[str] = None,
    wind_kb: Optional[str] = None,
    roof_kb: Optional[str] = None,
) -> Tuple[Agent, Agent, Agent, Agent]:
    """
    Returns (triage_agent, wind_agent, fire_agent, water_agent, roof_agent).
    No environment lookups anywhere.
    """
    w_kb = _kb_for("wind",  wind_kb)
    f_kb = _kb_for("fire",  fire_kb)
    wa_kb= _kb_for("water", water_kb)
    ro_kb= _kb_for("roof", roof_kb)

    wind_agent = Agent(
        name="Wind Insurance Agent",
        handoff_description="Specialist for wind-damage policy assessments" 
        "Output _only_ valid JSON matching this schema:\n",
        instructions=make_peril_instructions("wind", w_kb) ,
    )
    fire_agent = Agent(
        name="Fire Insurance Agent",
        handoff_description="Specialist for fire-damage policy assessments"  
        "Output _only_ valid JSON matching this schema:\n",
        instructions=make_peril_instructions("fire", f_kb),
    )
    water_agent = Agent(
        name="Water Insurance Agent",
        handoff_description="Specialist for water-damage policy assessments" 
        "Output _only_ valid JSON matching this schema:\n",
        instructions=make_peril_instructions("water", wa_kb),
    ),
    roof_agent = Agent(
        name="Roofing Insurance Agent",
        handoff_description="Specialist for Roofing-damage policy assessments" 
        "Output _only_ valid JSON matching this schema:\n",
        instructions=make_peril_instructions("Roofing", ro_kb),
    )

    

    triage_agent = Agent(
        name="Insurance Triage Agent",
        instructions=(
            "Analyze the user input (and image, if present) like a senior public adjuster. "
            "Determine the single best peril (water / wind / fire). "
            "HAND OFF to that specialist agent. The specialist must return ONLY raw JSON "
            "that conforms to the unified schema (already embedded in the specialist).\n"
            f"{RECOMMENDED_PROMPT_PREFIX}"
        ),
        handoffs=[wind_agent, fire_agent, water_agent, roof_agent],
 
    )
    return triage_agent, wind_agent, fire_agent, water_agent, roof_agent


def build_run_config(model_name: Optional[str] = None) -> RunConfig:
    """
    No env usage. Pass model_name from your task if you want; otherwise default to a vision-capable model.
    """
    # You can add other knobs here (e.g., temperature=0) if your RunConfig supports them.
    return RunConfig(model=model_name or "gpt-5-mini-2025-08-07")


def build_input_messages(user_text: str, data_uris: Sequence[str]) -> list[dict[str, Any]]:
    """
    Compose the multimodal input expected by your Runner:
    one input_text + one input_image per data URI.
    """
    content: list[dict[str, Any]] = [{"type": "input_text", "text": user_text}]
    for uri in data_uris:
        content.append({"type": "input_image", "image_url": uri})
    return [{"role": "user", "content": content}]
