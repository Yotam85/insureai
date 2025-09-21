"""
Knowledge base for property estimating:

The following is the constant results output sequence you need to follow:
LINE-ITEM | QUANTITY | UNIT | TAX | O&P | RCV | AGE/LIFE | COND. | DEP % | DEPREC. | ACV  /n | note

appendix:
TAX - tax by states
O&P - overhead and profit
RCV - Replacement Cost Value
ACV - Actual Cash Value

1. Single axle dump truck - per load - including dump fees |  1.00 | EA | 203.13 | 0.00 | 40.62 243.75 
debris left from remaining tear out, carpet, repairs and cabinets 
2. Job-site moving/storage container - 20 long - per month* 1.00 | MO | 185.01 | 13.32 | 37.00 | 235.33 | allowance to store contents while repairs are being done to main level 
3. Job-site cargo container - pick up/del. (each way) 16'-40' | 1.00 | EA | 112.00 | 0.00 | 22.40 | 134.40 
4. General Laborer - per hour 2.00 HR 28.10 0.00 11.24 67.44 Additional contents allowance to carefully pack contents into storage container  0/NA 0/NA 0/NA 0/NA  Avg. Avg. Avg. Avg.  NA 0% 0% 0%  (0.00) (0.00) (0.00) (0.00)  243.75 235.33 134.40 67.44  
5. Water heater - Detach 
1.00 EA 91.10 6.56 18.22 115.88 0/NA Avg. 0% (0.00) 115.88 Includes: On site storage and labor. Excludes: Any additional materials or hardware. Note: Labor cost to disconnect, drain, and detach a water heater, then move to an adjacent room or area for storage. The labor type used in this item 
is the Cleaning Remediation Technician. To reinstall see item PLM WHR. No life expectancy data 

6. R&R Water heater - 40 gallon - Electric - 6 yr 
1.00 EA 958.93 31.18 198.04 1,188.15 0/6 yrs Avg. 0% (0.00) 1,188.15 Includes: Electric water heater, in-line ball valve for 3/4" tubing, pressure relief valve, two 3/4" flexible supply lines, and installation labor. Labor cost to remove a water heater and to discard in a job-site waste receptacle. Quality: 40 gallon capacity. Six year warranty. Green: LEED considers water heaters to be green when they contribute to the requirements for residential Efficient Hot Water Distribution System credits. Average life expectancy 6 years 
Average depreciation 16.67% per year Maximum depreciation 100% 

7. R&R Solar water heater system 
1.00 EA 3,977.13 118.80 819.18 4,915.11 0/30 yrs Avg. 0% (0.00) 4,915.11 Includes: Water heater solar panel, supply and return lines, and labor to install. Labor cost to remove a solar water heater system, including a single collector panel, and to discard in a job-site waste receptacle. Quality: Progressive tube open system with single solar collector panel, mounting brackets, and 50 feet of 3/4" coiled copper tubing. Green: LEED considers solar systems to be green if they meet one or more of the following standards: Residential: Renewable Energy, Active Solar-Ready Design. Commercial: Renewable Energy Production, Minimum Energy Performance, Optimize Energy Performance. Note: For additional solar collector panels, see items PLM WHSOP*. For removal of additional panels, see items PLM WHSOP*. Average life expectancy 30 years 
Average depreciation 3.33% per year Maximum depreciation 100% 
QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 

8. Solar water heater panel - Detach & reset 
1.00 EA 701.83 0.00 140.36 842.19 0/NA Avg. 0% (0.00) 842.19 Includes: Water heater solar panel, supply and return lines, and labor to install. Labor cost to remove a solar water heater system, including a single collector panel, and to discard in a job-site waste receptacle. Quality: Progressive tube open system with single solar collector panel, mounting brackets, and 50 feet of 3/4" coiled copper tubing. Green: LEED considers solar systems to be green if they meet one or more of the following standards: Residential: Renewable Energy, Active 
Solar-Ready Design. Commercial: Renewable Energy Production, Minimum Energy Performance, Optimize Energy Performance. Note: For additional solar collector panels, see items PLM WHSOP*. For removal of additional panels, see items PLM WHSOP*. 
Average life expectancy 30 years Average depreciation 3.33% per year Maximum depreciation 100% 

9. Temporary water heater - (Bid Item)  
1.00 EA  0.00  0.00  0.00  0.00  0/NA  Avg.  0%  (0.00)  0.00  

10. Water heater - tankless - Detach & reset  
1.00 EA  423.98  0.00  84.80  508.78  0/NA  Avg.  0%  (0.00)  508.78  
Includes: On site storage, disconnect and drain, and labor. Excludes: Any additional materials or hardware. Note: Labor cost to detach a tankless water heater, move to an adjacent room or area for storage, and reinstall at a later time. No life expectancy data 

11. R&R Water heater - tankless - 20.1kw to 36kw - Electric 
1.00 EA 1,479.91 48.48 305.70 1,834.09 0/20 yrs Avg. 0% (0.00) 1,834.09 Includes: Electric - tankless water heater, in-line ball valve for 3/4" tubing, two 3/4" flexible supply lines, and installation labor. Labor cost to remove a water heater and to discard in a job-site waste receptacle. Quality: 20.1 to 36 KW. Green: LEED considers water heaters to be green when they contribute to the requirements for residential Efficient Hot Water Distribution System credits. Note: Includes plumbing and electrical connections to existing piping, and wiring. Average life expectancy 20 years 
Average depreciation 5% per year Maximum depreciation 100% 

12. R&R Water heater - tankless - 5-5.9 gallon - Gas - Power vent 
1.00 EA 1,974.50 73.58 409.62 2,457.70 0/20 yrs Avg. 0% (0.00) 2,457.70 Includes: Gas - tankless water heater, in-line ball valve for 3/4" tubing, two 3/4" flexible supply lines, and installation labor. Labor cost to remove a water heater and to discard in a job-site waste receptacle. Excludes: Gas flex connection, please see item PLM FT*. Quality: Power and/or direct vent 5 to 5.9 gpm 55 degree rise. Green: LEED considers water heaters to be green when they contribute to the requirements for residential Efficient Hot Water Distribution System credits. Note: Additional line items may be needed to run venting and/or plumbing pipes. Average life expectancy 20 years 
Average depreciation 5% per year Maximum depreciation 100% 

13. R&R Water heater connector line - 3/4" flexible tubing 
1.00 EA 61.81 0.92 12.54 75.27 0/50 yrs Avg. 0% (0.00) 75.27 Includes: Single supply line and installation labor. Labor cost to remove a water heater connector line and to discard in a job-site waste receptacle. Quality: Flexible copper supply line up to 2' long. Average life expectancy 50 years 
Average depreciation 2% per year Maximum depreciation 100% 
2025-08-28-1618 8/31/2025 Page: 3 
QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 

14. R&R Water heater seismic strap kit - 56 to 80 gallon  
1.00 EA  77.34  1.49  15.78  94.61  0/100 yrs  Avg.  0%  (0.00)  94.61  
Includes: Two strap kit and labor to install. Labor cost to remove strap, and to discard in a job-site waste receptacle.  
Quality: Galvanized steel.  
Average life expectancy 100 years  
Average depreciation 1% per year  
Maximum depreciation 100%  

15. R&R Water heater - 50 gallon - Gas - Power vent  
1.00 EA  2,224.42  105.43  465.98  2,795.83  0/11 yrs  Avg.  0%  (0.00)  2,795.83  
Includes: Gas water heater, in-line ball valve for 3/4" tubing, pressure relief valve, two 3/4" flexible supply lines, and installation labor. Labor cost to remove a water heater and to discard in a job-site waste receptacle. Excludes: Gas flex connection, please see item PLM FT*. Quality: Power vent 50 gallon capacity. Green: LEED considers water heaters to be green when they contribute to the requirements for residential Efficient Hot Water Distribution System credits. Note: If PVC venting is needed see item "HVC VENTPVC". Average life expectancy 11 years Average depreciation 9.09% per year Maximum depreciation 100% 

16. R&R Water heater - flood sensor/shutoff - 3/4" 
1.00 EA 233.43 11.10 48.90 293.43 0/70 yrs Avg. 0% (0.00) 293.43 Includes: Water leak sensor system and installation labor. Labor cost to remove a water heater flood sensor and to discard in a job-site waste receptacle. Excludes: Electrical wiring and/or batteries. Quality: 3/4" motorized water shut off valve with sensor and power control unit. Average life expectancy 70 years 
Average depreciation 1.43% per year Maximum depreciation 100% 

17. R&R Water heater - 80 gallon - Electric - Standard grade 
1.00 EA 1,452.94 59.14 302.42 1,814.50 0/11 yrs Avg. 0% (0.00) 1,814.50 
Includes: Electric water heater, in-line ball valve for 3/4" tubing, pressure relief valve, two 3/4" flexible supply lines, and installation labor. Labor cost to remove a water heater and to discard in a job-site waste receptacle. Quality: 80 gallon capacity. Standard grade. Green: LEED considers water heaters to be green when they contribute to the requirements for residential Efficient Hot Water Distribution System credits. Average life expectancy 11 years Average depreciation 9.09% per year Maximum depreciation 100% 

18. R&R Solar water heater panel - over 33 SF 
1.00 EA 1,953.83 69.57 404.70 2,428.10 0/30 yrs Avg. 0% (0.00) 2,428.10 Includes: Solar collector panel and labor to install. Labor cost to remove a water solar panel and to discard in a job-site waste receptacle. Green: LEED considers solar systems to be green if they meet one or more of the following standards: Residential: Renewable Energy, Active Solar-Ready Design. Commercial: Renewable Energy Production, Minimum Energy Performance, Optimize Energy Performance. Average life expectancy 30 years 
Average depreciation 3.33% per year Maximum depreciation 100% 

19. R&R Water heater - enclosure - 30" x 30" 
1.00 EA 407.83 7.02 82.98 497.83 0/20 yrs Avg. 0% (0.00) 497.83 
QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
Includes: Water heater enclosure and labor to install. Labor cost to remove a water heater enclosure and to discard in a job-site waste receptacle. Quality: Galvanized steel, 30" x 30" x 72-1/2". Fits up to 80 gallon water heater. Average life expectancy 20 years Average depreciation 5% per year Maximum depreciation 100% 

20. R&R Water heater - 140 gal - Gas 
1.00 EA 4,338.35 227.88 913.24 5,479.47 0/10 yrs Avg. 0% (0.00) 5,479.47 Includes: Gas water heater, in-line ball valve for 3/4" tubing, pressure relief valve, two 3/4" flexible supply lines, and installation labor. Labor cost to remove a water heater and to discard in a job-site waste receptacle. Excludes: Gas flex connection, please see item PLM FT*. Quality: 140 gallon capacity. Green: LEED considers water heaters to be green when they contribute to the requirements for residential Efficient Hot Water Distribution System credits. Average life expectancy 10 years 
Average depreciation 10% per year Maximum depreciation 100% 

21. R&R Water heater - 100 gal - Residential grade - Gas 
1.00 EA 3,576.71 183.05 751.96 4,511.72 0/10 yrs Avg. 0% (0.00) 4,511.72 Includes: Water heater, in-line ball valve for 3/4" tubing, pressure relief valve, two 3/4" flexible supply lines, and installation labor. Labor cost to remove a water heater and to discard in a job-site waste receptacle. Excludes: Gas flex connection, please see item PLM FT*. Quality: 100 gallon capacity. Average life expectancy 10 years 
Average depreciation 10% per year Maximum depreciation 100% 

22. Water heater - Reset 
1.00 EA 374.85 0.00 74.98 449.83 0/NA Avg. 0% (0.00) 449.83 Includes: On site storage and labor. Excludes: Any additional materials or hardware. 
Note: This item is intended for use as a reset only; detaching of the water heater has previously been performed by another company. No life expectancy data 

23. R&R Water heater - 30 gallon - Gas - 9 yr 
1.00 EA 1,180.41 42.79 244.66 1,467.86 0/9 yrs Avg. 0% (0.00) 1,467.86 Includes: Gas water heater, in-line ball valve for 3/4" tubing, pressure relief valve, two 3/4" flexible supply lines, and installation labor. Labor cost to remove a water heater and to discard in a job-site waste receptacle. Excludes: Gas flex connection, please see item PLM FT*. Quality: 30 gallon capacity. Nine year warranty. Green: LEED considers water heaters to be green when they contribute to the requirements for residential Efficient Hot Water Distribution System credits. Average life expectancy 9 years 
Average depreciation 11.11% per year Maximum depreciation 100% 

24. R&R Water heater platform - wood frame 
1.00 EA 453.21 8.91 92.42 554.54 0/50 yrs Avg. 0% (0.00) 554.54 
Includes: 2" x 4" treated and non-treated lumber, 3/4" CDX plywood, nails, construction adhesive, and labor to install. Labor cost to remove water heater platform and to discard in a job-site waste receptacle. Quality: 18" tall, 3' x 3' platform. Average life expectancy 50 years Average depreciation 2% per year Maximum depreciation 100% 
2025-08-28-1618 8/31/2025 Page: 5 

25. R&R Water heater - 40 gallon - Gas - 6 yr 
1.00 EA 1,128.64 39.69 233.68 1,402.01 0/6 yrs Avg. 0% (0.00) 1,402.01 Includes: Gas water heater, in-line ball valve for 3/4" tubing, pressure relief valve, two 3/4" flexible supply lines, and installation labor. Labor cost to remove a water heater and to discard in a job-site waste receptacle. Excludes: Gas flex connection, please see item PLM FT*. Quality: 40 gallon capacity. Six year warranty. Green: LEED considers water heaters to be green when they contribute to the requirements for residential Efficient Hot Water Distribution System credits. Average life expectancy 6 years 
Average depreciation 16.67% per year Maximum depreciation 100% 

26. R&R Water heater blanket 
1.00 EA 58.21 1.45 11.94 71.60 0/15 yrs Avg. 0% (0.00) 71.60 Includes: Blanket, tape, and labor to install. Labor cost to remove a water heater blanket and to discard in a job-site waste receptacle. Green: LEED considers water heater blankets to be green if they are part of the residential Efficient Hot Water Distribution System credits. Average life expectancy 15 years 
Average depreciation 6.67% per year Maximum depreciation 100% 

27. Clean water heater 
1.00 EA 24.41 1.77 4.88 31.06 0/NA Avg. 0% (0.00) 31.06 Includes: Cleaning chemical and labor. Quality: In-place cleaning of all exposed surfaces. Green: LEED considers cleaners to be green under the following standards, or a local equivalent for projects outside of the U.S.: Green Seal GS-37, GS-40, GS -52/53; Environmental Choice CCD-110, CCD-112, CCD-113, CCD-115, CCD-146, CCD-147, CCD-148; EPA Design for the Environment Program's Standard for Safer Cleaning Products; California Code of Regulations maximum allowable VOC levels for the specific product category. Paper products and trash bags must meet one or more of the following programs or a local equivalent for projects outside the U.S.: EPA comprehensive procurement guidelines, for janitorial paper; Green Seal GS-01; Environmental Choice CCD-082, CCD-086; Janitorial paper products derived from rapidly renewable resources or manufactured from tree-free fibers; FSC certification, for fiber procurement; EPA comprehensive procurement guidelines, for plastic trash can liners (California Code of Regulations Title 14, Chapter 4, Article 5, or SABRC 42290-42297 Recycled Content Plastic Trash Bag Program). 
Note: Generally, light soiling is easily removed with the use of a cleaning agent and one or two passes. No life expectancy data 

28. Water heater - Detach & reset 
1.00 EA 549.78 0.00 109.96 659.74 0/NA Avg. 0% (0.00) 659.74 Includes: On site storage, disconnect and drain, and labor. Excludes: Any additional materials or hardware. 
Note: Labor cost to detach a water heater, move to an adjacent room or area for storage, and reinstall at a later time. No life expectancy data 
Total: Main Level 1,038.81 5,746.94 34,489.30 0.00 34,489.30 
3' 6" 2' 3" 

384.00 SF Walls 144.00 SF Ceiling 
528.00 SF Walls & Ceiling 144.00 SF Floor 
16.00 SY Flooring 48.00 LF Floor Perimeter 
48.00 LF Ceil. Perimeter 
1' 11" 

____________________________________________________________________________________________________________________________________________

# FLOORS 

LINE-ITEM | QUANTITY | UNIT | TAX | O&P | RCV | AGE/LIFE | COND. | DEP % | DEPREC. | ACV  

29. Vapor barrier - 15 felt 30.00 SF 0.27 0.07 
30. Oak flooring - 1 common - no finish 30.00 SF 7.02 7.99 remediation team removing wood floors 
31. Sand & finish wood floor (natural finish) 144.00 SF 3.05 6.31 
32. Add for dustless floor sanding 144.00 SF 1.00 0.00 TRIM 
33. R&R Base shoe - stain grade 38.67 LF 1.47 1.28 
34. Stain & finish base shoe or quarter round 38.67 LF 1.08 0.39 
35. Final cleaning - construction - Residential 144.00 SF 0.19 1.97 
36. Baseboard - 3 1/4" 38.67 LF 4.33 4.94 
37. Seal (1 coat) & paint (1 coat) baseboard 38.67 LF 2.05 0.35 
38. Base shoe 38.67 LF 1.75 1.79 
39. Seal & paint base shoe or quarter round 38.67 LF 1.10 0.32 TRIM 
40. Baseboard - 4 1/4" 38.67 LF 5.32 7.01 TRIM 
41. Baseboard - 5 1/4" 38.67 LF 5.62 7.45 FLOORS 
42. Content Manipulation charge - per hour 1.00 HR 37.25 0.00 
43. Carpet pad - Standard grade 80.00 SF 0.40 1.58 removed by remediation team 2025-08-28-1618  O&P 1.64 43.72 89.10 28.80 11.64 8.44 5.48 34.46 15.94 13.90 8.56 42.54 44.96 7.46 6.72  RCV AGE/LIFE 9.81 13/15 yrs 262.31 13/150 yrs 534.61 13/10 yrs 172.80 13/10 yrs 69.76 13/150 yrs 50.59 13/15 yrs 34.81 13/NA 206.84 0/150 yrs 95.56 0/15 yrs 83.36 0/150 yrs 51.42 0/15 yrs 255.27 0/150 yrs 269.74 0/150 yrs 44.71 0/NA 40.30 0/10 yrs  COND. DEP % DEPREC. Avg. 86.67% (7.08) Avg. 8.67% (18.94) Avg. 100% [M] (445.51) Avg. 100% [M] (144.00) Avg. 8.67% (4.47) Avg. 86.67% (36.53) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) 8/31/2025  ACV 2.73 243.37 89.10 28.80 65.29 14.06 34.81 206.84 95.56 83.36 51.42 255.27 269.74 44.71 40.30 Page: 7  
44. Carpet - Detach & relay | 144.00 SF 0.62 0.17 17.90 
45. Clean and deodorize carpet 144.00 SF 0.47 4.97 13.56 PAINT 
46. Paint the walls - one coat 384.00 SF 0.56 2.53 43.50 no damage in this room--continuous walls from other rooms 
47. Handrail - wall mounted - Detach & reset 10.00 LF 5.31 0.00 10.62 to assist with painting walls DRYWALL 
48. 1/2" drywall - hung, taped, floated, ready for paint 48.00 SF 2.07 1.44 20.16 
49. Batt insulation - 4" - R13 - unfaced batt 10.00 SF 0.59 0.23 1.22 TRIM 
50. Baseboard - 5 1/4" 38.67 LF 4.32 5.29 34.48 
51. Base shoe 38.67 LF 1.19 1.02 9.40 
52. Seal & paint baseboard - two coats* 38.67 LF 1.27 0.23 9.86 
53. Seal & paint base shoe or quarter round 38.67 LF 0.67 0.21 5.22 
54. Interior door unit - Standard grade 1.00 EA 242.97 11.21 50.84 55. Seal & paint door or window opening (per side) 1.00 EA 30.68 0.29 6.20 56. Paint door slab only - 2 coats (per side) 2.00 EA 36.43 0.93 14.76 57. Door knob/lockset - Detach & reset 1.00 EA 20.35 0.00 4.08 58. Seal the floor perimeter w/PVA primer - one coat 48.00 SF 0.58 0.17 5.60 59. Paint the walls - one coat 384.00 SF 0.44 2.53 34.30 60. Detach & Reset Window blind - PVC - 2" - 14.1 to 20 SF 2.00 EA 30.48 0.00 12.20 FLOORS 2025-08-28-1618  RCV AGE/LIFE 107.35 0/NA 86.21 0/NA 261.07 3/15 yrs 63.72 0/NA 120.96 16/150 yrs 7.35 16/150 yrs 206.82 16/150 yrs 56.44 16/150 yrs 59.20 16/15 yrs 31.34 16/15 yrs 305.02 0/100 yrs 37.17 16/15 yrs 88.55 0/15 yrs 24.43 0/NA 33.61 16/15 yrs 205.79 16/15 yrs 73.16 16/5 yrs  COND. DEP % DEPREC. Avg. 0% (0.00) Avg. 0% (0.00) Avg. 20% (43.52) Avg. 0% (0.00) Avg. 10.67% (10.75) Avg. 10.67% (0.65) Avg. 10.67% (18.38) Avg. 10.67% (5.02) Avg. 100% [M] (49.34) Avg. 100% [M] (26.12) Avg. 0% (0.00) Avg. 100% [M] (30.97) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 100% [M] (28.01) Avg. 100% [M] (171.49) Avg. 100% [M] (0.00) 8/31/2025  ACV 107.35 86.21 217.55 63.72 110.21 6.70 188.44 51.42 9.86 5.22 305.02 6.20 88.55 24.43 5.60 34.30 73.16 Page: 8  
61. Vinyl plank flooring - Standard grade - 144.00 SF  3.90  14.00  115.12  690.72  0/50 yrs  Avg.  0%  (0.00)  690.72  
62. Final cleaning - construction - Residential | 144.00 SF  0.19  1.97  5.48  34.81  16/NA  Avg.  0%  (0.00)  34.81  
63. Content Manipulation charge - per hour | 0.50 HR  37.25  0.00  3.72  22.35  0/NA  Avg.  0%  (0.00)  22.35  
64. R&R Engineered wood flooring - Standard grade | 144.00 SF  8.43  31.02  248.98  1,493.92  0/50 yrs  Avg.  0%  (0.00)  1,493.92 continuous flooring from damaged area  
65. R&R Base shoe | 38.67 LF  1.52  1.14  11.98  71.90  0/150 yrs  Avg.  0%  (0.00)  71.90  
66. Seal & paint base shoe or quarter round | 38.67 LF  0.78  0.23  6.08  36.47  0/15 yrs  Avg.  0%  (0.00)  36.47  
67. Paint baseboard - one coat | 38.67 LF  0.91  0.19  7.08  42.46  0/15 yrs  Avg.  0%  (0.00)  42.46  
68. Interior door - Detach & reset - slab only | 1.00 EA  21.06  0.00  4.22  25.28  0/NA  Avg.  0%  (0.00)  25.28  
69. Content Manipulation charge - per hour | 0.50 HR  37.25  0.00  3.72  22.35  0/NA  Avg.  0%  (0.00)  22.35  
70. R&R Engineered wood flooring - Standard grade | 144.00 SF  8.43  31.02  248.98  1,493.92  0/50 yrs  Avg.  0%  (0.00)  1,493.92  

- Water damaged -  

71. R&R Quarter round - for wood flooring | 38.67 LF  3.76  6.98  30.48  182.86  0/25 yrs  Avg.  0%  (0.00)  182.86  
72. Seal & paint base shoe or quarter round  | 38.67 LF  0.78  0.23  6.08  36.47  0/15 yrs  Avg.  0%  (0.00)  36.47  
73. Paint baseboard - one coat - 38.67 LF  0.91  0.19  7.08  42.46  0/15 yrs  Avg.  0%  (0.00)  42.46  
74. Interior door - Detach & reset - slab only - 1.00 EA  21.06  0.00  4.22  25.28  0/NA  Avg.  0%  (0.00)  25.28  

- FOUNDATION REPAIR -

75. Plaster (parget) foundation | 16.00 SF  1.24  0.32  4.02  24.18  1/100 yrs  Avg.  1%  (0.20)  23.98  for damaged foundation styrofoam  
76. Stucco Plasterer - per hour | 4.00 HR  55.71  0.00  44.56  267.40  0/100 yrs  Avg.  0%  (0.00)  267.40  Additional labor hours added due the small nature of the repair 

FLOORS 

77. Remove Ceramic tile - Standard grade 144.00 SF 1.82 0.00 52.42 314.50 0/150 yrs continuous from the damaged area 
78. Ceramic tile - Standard grade 144.00 SF 11.50 24.71 336.14 2,016.85 0/150 yrs 
79. Remove 1/4" Cement board 144.00 SF 0.84 0.00 24.20 145.16 0/150 yrs 
80. 1/4" Cement board 144.00 SF 4.47 11.06 130.96 785.70 0/150 yrs 
81. Remove Ceramic/porcelain tile 84.00 SF 1.81 0.00 30.40 182.44 0/150 yrs 
82. Ceramic/porcelain tile 144.00 SF 11.65 35.16 342.56 2,055.32 0/150 yrs 
83. Remove Mortar bed for tile 84.00 SF 1.46 0.00 24.52 147.16 0/150 yrs 60 sq ft already removed 
84. Carpet - metal transition strip 2.00 LF 2.34 0.13 0.96 5.77 0/10 yrs 
85. Remove Tear out vinyl & underlayment 144.00 SF 1.20 0.00 34.56 207.36 2/150 yrs 
86. Underlayment - 1/4" lauan/mahogany plywood 144.00 SF 1.23 4.23 36.26 217.61 0/150 yrs ****************ADD VINYL DROP and FILL HERE*********************** ---------estimated via Sketch using the drop & fill method. 
87. R&R Vinyl - metal transition strip 2.67 LF 3.10 0.17 1.70 10.15 0/50 yrs 
88. Toilet - Detach & reset 1.00 EA 200.90 0.38 40.26 241.54 2/NA 
89. Plumber - per hour 1.00 HR 100.03 0.00 20.00 120.03 2/NA Additional labor hours added due the small nature of the repair 
90. Remove Base shoe 36.67 LF 0.17 0.00 1.24 7.47 10/150 yrs less 2' removed 
91. Paint door/window trim & jamb - 1 coat (per side) 5.00 EA 22.55 1.11 22.78 136.64 10/15 yrs TRIM 
92. Add for glued down application over concrete substrate* 144.00 SF 2.57 7.52 75.50 453.10 0/150 yrs 
93. Paint baseboard, oversized - one coat 38.67 LF 0.71 0.23 5.54 33.23 0/15 yrs 
94. Tear off, haul and dispose rubber roofing - per adhered 0.00 SQ 70.57 0.00 0.00 
95. Rubber roofing - Perimeter adhered system - 45 mil 0.00 SQ 455.36 0.00 0.00 
96. Exhaust cap - through flat roof 3.00 EA 121.45 13.89 75.66 
97. Sand, stain, and finish wood floor 144.00 SF 3.72 7.78 108.70 continuous floor from other rooms 
98. R&R Carpet pad 144.00 SF 0.82 4.67 24.56 1,198. Remove Carpet 144.00 SF 0.33 0.00 9.50 
99. Carpet 165.60 SF 3.91 29.51 135.40 15 % waste added for Carpet. 
100. Additional labor cost for Berber or patterned carpets 144.00 SF 0.27 0.00 7.78 
101. Apply anti-microbial agent to the floor 144.00 SF 0.36 4.29 10.46 
102. R&R Batt insulation - 6" - R19 - paper / foil faced 384.00 SF 1.21 14.28 95.80 
103. R&R Vapor barrier - visqueen - 6mil 144.00 SF 0.37 0.52 10.76 
104. Seal floor or ceiling joist system 144.00 SF 1.19 1.99 34.68 
105. Clean floor or roof joist system 144.00 SF 0.96 10.13 27.68 FLOORS 
106. Content Manipulation charge - per hour 1.00 HR 37.25 0.00 7.46 
107. Carpet pad - Standard grade 12.00 SF 0.40 0.24 1.00 
108. Carpet - Detach & relay 144.00 SF 0.62 0.17 17.90 
109. Clean and deodorize carpet 144.00 SF 0.47 4.97 13.56 
110. R&R Snaplock Laminate - simulated wood flooring 144.00 SF 7.96 29.20 235.10 
111. Dust control barrier per square foot 62.22 SF 0.89 0.67 11.22 
112. Contents - move out then reset 1.00 EA 75.63 0.00 15.12 
113. Water extraction from carpeted floor 144.00 SF 0.58 6.01 16.70 
114. Tear out wet drywall, cleanup, bag for disposal 192.00 SF 1.22 1.61 47.16 
115. Tear out wet carpet pad and bag for disposal 144.00 SF 0.71 0.43 20.52 
116. Lift carpet for drying 144.00 SF 0.50 5.18 14.40 
117. Air mover (per 24 hour period) - No monitoring 3.00 EA 27.00 5.83 16.20 
118. Dehumidifier (per 24 hr period)- up to 69 ppd- No monitor. 3.00 EA 54.04 11.68 32.42 
119. Seal/prime (1 coat) then paint (1 coat) the walls - 2 colors 384.00 SF 1.54 5.07 119.30 
120. Lay existing carpet - Labor only 144.00 SF 0.77 0.26 22.24 
121. Paint baseboard - two coats 48.00 LF 1.98 0.49 19.10 
122. Baseboard - 2 1/4" 48.00 LF 3.68 4.49 36.22 
123. Paint the walls - two coats 384.00 SF 1.30 6.68 101.18 
124. Block and pad furniture in room 0.00 EA 63.27 0.00 0.00 
125. Baseboard - Detach 48.00 LF 1.58 5.46 15.16 
126. Water extraction from carpeted floor - Heavy 144.00 SF 0.70 7.26 20.16 
127. Tear out wet non-salvageable carpet, cut & bag for disp. 144.00 SF 0.77 0.43 22.26 
128. R&R Stair tread - hardwood - up to 4' - High grade 1.00 EA 130.23 5.35 27.12 
129. Stain & finish stair tread - per side - per LF 1.00 LF 8.53 0.06 1.72 
130. R&R Stair riser - hardwood - up to 4' 1.00 EA 59.71 2.22 12.40 131. Stain & finish stair riser - per side - per LF 1.00 LF 5.68 0.04 1.14  RCV AGE/LIFE 90.75 0/NA 106.23 0/NA 283.01 0/NA 123.19 0/NA 91.58 0/NA 103.03 0/NA 206.22 0/NA 715.73 0/15 yrs 133.38 0/10 yrs 114.63 0/15 yrs 217.35 0/150 yrs 607.06 0/15 yrs 0.00 0/NA 96.46 0/NA 128.22 0/NA 133.57 0/NA 162.70 0/100 yrs 10.31 0/15 yrs 74.33 0/50 yrs 6.86 0/15 yrs  COND. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg.  DEP % DEPREC. 0% (0.00) 0% (0.00) NA (0.00) NA (0.00) 0% <0.00> 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) NA (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00)  ACV 90.75 106.23 283.01 123.19 91.58 103.03 206.22 715.73 133.38 114.63 217.35 607.06 0.00 96.46 128.22 133.57 162.70 10.31 74.33 6.86  QUANTITY UNIT TAX O&P RCV AGE/LIFE 132. R&R Trim board - 1" x 12" - installed (hardwood - oak or =) 1.00 LF 18.85 0.94 3.96 23.75 0/150 yrs 133. Stain & finish trim 1.00 LF 2.17 0.02 0.44 2.63 0/15 yrs 134. R&R Balustrade - wood handrail w/iron balusters - High grade 1.00 LF 264.33 6.69 54.22 325.24 0/150 yrs 135. Baluster - High grade - material only 1.00 EA 24.97 1.50 5.30 31.77 0/150 yrs 136. R&R Handrail - detailed profile - hardwood - wall mounted 1.00 LF 21.09 0.71 4.36 26.16 0/150 yrs 137. Balustrade top rail - High grade - material only 1.00 LF 25.94 1.56 5.50 33.00 0/150 yrs 138. R&R Balustrade - Labor only 1.00 LF 134.55 0.01 26.92 161.48 0/150 yrs 139. Stain & finish balustrade 1.00 LF 40.19 0.33 8.10 48.62 0/15 yrs 140. Stain & finish handrail - wall mounted 1.00 LF 2.92 0.03 0.58 3.53 0/15 yrs 141. Additional labor to remove stone from concrete slab 144.00 SF 2.50 0.00 72.00 432.00 0/150 yrs 142. R&R Stone floor covering - High grade 144.00 SF 28.53 88.30 839.34 5,035.96 0/150 yrs 143. R&R Marble or Granite floor tile 144.00 SF 26.08 78.97 766.92 4,601.41 0/150 yrs 144. R&R Slate floor covering - High grade 144.00 SF 28.34 83.38 832.88 4,997.22 0/150 yrs 145. Tile/stone sealer 144.00 SF 1.08 3.11 31.72 190.35 0/2 yrs 146. Regrout stone floor 144.00 SF 4.39 0.86 126.62 759.64 0/10 yrs 147. Remove Tile floor covering 144.00 SF 3.04 0.00 87.56 525.32 0/100 yrs 148. Additional labor to remove tile from concrete slab 144.00 SF 2.09 0.00 60.20 361.16 0/100 yrs 149. Floor leveling cement - Light 144.00 SF 2.15 8.21 63.56 381.37 0/50 yrs 150. R&R Mortar bed for tile floors 144.00 SF 7.04 19.70 206.68 1,240.14 0/100 yrs 151. R&R 1/4" Cement board 144.00 SF 6.00 13.82 175.56 1,053.38 0/100 yrs  COND. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg.  DEP % DEPREC. 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) NA (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) 0% (0.00) NA (0.00) NA (0.00) 0% (0.00) 0% (0.00) 0% (0.00)  ACV 23.75 2.63 325.24 31.77 26.16 33.00 161.48 48.62 3.53 432.00 5,035.96 4,601.41 4,997.22 190.35 759.64 525.32 361.16 381.37 1,240.14 1,053.38  


QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 

152. Tile floor covering - 144.00 SF 13.05 47.87 385.42 2,312.49 0/100 yrs Avg. 0% (0.00) 2,312.49 
153. Add-on for diagonal tile installation - 144.00 SF 1.71 0.00 49.24 295.48 0/100 yrs Avg. 0% (0.00) 295.48 
154. Regrout tile floor - 144.00 SF 4.64 4.75 134.60 807.51 0/10 yrs Avg. 0% (0.00) 807.51 
155. Grout sealer - 144.00 SF 1.62 1.64 46.98 281.90 0/2 yrs Avg. 0% (0.00) 281.90 
156. R&R Oak flooring - clear grade - no finish - 144.00 SF 16.46 84.41 490.92 2,945.57 0/150 yrs Avg. 0% (0.00) 2,945.57 
157. Add for glued down wood flooring appl. over wood substrate - 144.00 SF 5.04 10.11 147.18 883.05 0/150 yrs Avg. 0% (0.00) 883.05 
158. Add for diagonal installation - 144.00 SF 1.27 0.00 36.58 219.46 0/NA Avg. 0% (0.00) 219.46 
159. Additional coats of finish (per coat) - 144.00 SF 1.16 2.51 33.90 203.45 0/10 yrs Avg. 0% (0.00) 203.45 
160. Wood floor border inlay - 0.00 LF 16.54 0.00 0.00 0.00 0/150 yrs Avg. 0% (0.00) 0.00 

______________________________________________________________________________________________________________________________________
# Kitchen  

328.00 SF Walls 102.00 SF Ceiling 
430.00 SF Walls & Ceiling 102.00 SF Floor 
11.33 SY Flooring 41.00 LF Floor Perimeter 
41.00 LF Ceil. Perimeter 


LINE-ITEM QUANTITY  UNIT  TAX  O&P  RCV  AGE/LIFE  COND.  DEP %  DEPREC.  ACV  

161. Refrigerator - Remove & reset 1.00 EA 41.00 162. Range - gas - Remove & reset 1.00 EA 143.28 163. Dishwasher - Detach & reset 1.00 EA 209.01 CABINETS  TAX 0.00 0.00 0.00  O&P 8.20 28.66 41.80  RCV 49.20 171.94 250.81  AGE/LIFE 0/NA 0/NA 0/NA  COND. Avg. Avg. Avg.  DEP % 0% 0% 0%  DEPREC. (0.00) (0.00) (0.00)  ACV 49.20 171.94 250.81  
164. R&R Cabinet panels - side, end, or back 6.00 SF 17.74 2.76 21.86 bottom of cabinet under sink 
165. Interior door - Detach & reset - slab only 1.00 EA 21.08 0.00 4.22 
166. Paint casing - one coat 51.00 LF 0.94 0.31 9.64 167. P-trap assembly - Detach & reset 1.00 EA 53.45 0.00 10.70 
168. Garbage disposer - Detach & reset* 1.00 EA 143.30 0.00 28.66 
169. R&R Plumbing fixture supply line 2.00 EA 23.79 0.72 9.66 CABINET 
170. R&R Cabinetry - lower (base) units 4.00 LF 213.89 40.19 179.16 both sides damaged by water 
171. Detach & Reset Countertop - flat laid plastic laminate 8.67 LF 18.10 0.00 31.38 
172. Sink - double - Detach & reset* 1.00 EA 143.44 0.03 28.68 
173. R&R Angle stop valve 2.00 EA 34.41 0.86 13.94 
174. P-trap assembly - ABS (plastic) 1.00 EA 55.47 0.41 11.18 CABINETS 
175. R&R Cabinetry - lower (base) units - Standard grade 13.00 LF 139.76 76.40 378.66 
176. Countertop - solid surface/granite - Detach & reset 26.00 SF 21.78 0.00 113.26 
177. P-trap assembly - Detach & reset 1.00 EA 48.94 0.00 9.78 
178. R&R Angle stop valve 2.00 EA 34.46 0.86 13.98 
179. Sink - undermount - Detach & reset 1.00 EA 203.53 0.08 40.72 
180. Countertop - flat laid plastic laminate - Detach & reset 8.67 LF 16.19 0.00 28.08 
181. Cabinet knobs or pulls - Detach & reset 1.00 EA 2.16 0.00 0.44 2025-08-28-1618  RCV AGE/LIFE 131.06 6/50 yrs 25.30 6/NA 57.89 6/15 yrs 64.15 0/NA 171.96 0/NA 57.96 6/20 yrs 1,074.91 0/50 yrs 188.31 0/15 yrs 172.15 0/NA 83.62 4/100 yrs 67.06 4/25 yrs 2,271.94 3/50 yrs 679.54 3/NA 58.72 3/NA 83.76 3/100 yrs 244.33 0/NA 168.45 0/NA 2.60 0/NA  COND. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg. Avg.  DEP % DEPREC. 12% (11.51) 0% (0.00) 40% (19.30) 0% (0.00) 0% (0.00) 30% (11.10) 0% (0.00) 0% (0.00) 0% (0.00) 4% (2.38) 16% (8.95) 6% (107.70) 0% (0.00) 0% (0.00) 3% (1.80) 0% (0.00) 0% (0.00) 0% (0.00) 8/31/2025  ACV 119.55 25.30 38.59 64.15 171.96 46.86 1,074.91 188.31 172.15 81.24 58.11 2,164.24 679.54 58.72 81.96 244.33 168.45 2.60 Page: 15  

182. Cabinetry (Bid Item) - 1.00 EA 0.00 0.00 0.00 0.00 2/NA  Avg.  10% [%] (0.00)  0.00  Renovar Bid Estimate  
183. Detach & Reset P-trap assembly - ABS (plastic) - 1.00 EA 48.91 0.00 9.78 58.69 4/25 yrs  Avg.  16% (0.00)  58.69  
184. Detach & Reset Garbage disposer* - 1.00 EA 148.87 0.00 29.78 178.65 0/12 yrs  Avg.  0% (0.00)  178.65  

185. R&R 110 volt copper wiring run and box - rough-in only  
1.00 EA 72.47 1.14 14.72 88.33 0/100 yrs  Avg.  0% (0.00)  88.33  
186. R&R Fluorescent light fixture - Premium grade  
1.00 EA 217.92 8.80 45.34 272.06 0/20 yrs  Avg.  0% (0.00)  272.06  
187. R&R 110 volt copper wiring run, box and switch  
1.00 EA 90.81 1.33 18.42 110.56 0/100 yrs  Avg.  0% (0.00)  110.56  
188. R&R 110 volt copper wiring run, box and outlet  
1.00 EA 90.11 1.28 18.28 109.67 0/100 yrs  Avg.  0% (0.00)  109.67  
189. R&R 220 volt copper wiring run, box and receptacle  
1.00 EA 222.93 7.79 46.14 276.86 0/100 yrs  Avg.  0% (0.00)  276.86  
190. R&R Ground fault interrupter (GFI) outlet  
1.00 EA 42.22 1.19 8.68 52.09 0/10 yrs  Avg.  0% (0.00)  52.09  
191. R&R Fluorescent light fixture  
1.00 EA 123.52 3.14 25.32 151.98 0/20 yrs  Avg.  0% (0.00)  151.98  
192. R&R Custom cabinets - full height units - Premium grade  
0.00 LF 936.57 0.00 0.00 0.00 0/50 yrs  Avg.  0% (0.00)  0.00  
193. R&R Custom cabinets - base units - Premium grade  
0.00 LF 741.16 0.00 0.00 0.00 0/50 yrs  Avg.  0% (0.00)  0.00  
194. R&R Custom cabinets - wall units - up to 24" tall - Prem grade  
0.00 LF 436.52 0.00 0.00 0.00 0/50 yrs  Avg.  0% (0.00)  0.00  
195. R&R Custom cabinets - wall units - 30" tall - Premium grade  
0.00 LF 466.87 0.00 0.00 0.00 0/50 yrs  Avg.  0% (0.00)  0.00  
196. R&R Custom cabinets - wall units - 36" tall - Premium grade  
0.00 LF 488.66 0.00 0.00 0.00 0/50 yrs  Avg.  0% (0.00)  0.00  
197. R&R Custom cabinets - wall units - 42" tall - Premium grade  
0.00 LF 525.54 0.00 0.00 0.00 0/50 yrs  Avg.  0% (0.00)  0.00  
198. R&R Cabinet valance  
0.00 LF 47.46 0.00 0.00 0.00 0/50 yrs  Avg.  0% (0.00)  0.00  
199. R&R Appliance panel - 1/4" finished veneer  
0.00 SF 24.89 0.00 0.00 0.00 0/50 yrs  Avg.  0% (0.00)  0.00  
200. R&R Wood appliance panel - Premium grade  
0.00 SF 57.32 0.00 0.00 0.00 0/50 yrs  Avg.  0% (0.00)  0.00  
201. Add for prefinished crown molding per LF  
0.00 LF 10.88 0.00 0.00 0.00 0/150 yrs  Avg.  0% (0.00)  0.00  
2025-08-28-1618  8/31/2025  Page: 16  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
202. Carpenter - Finish, Trim / Cabinet - per hour 
0.00 HR 83.34 0.00 0.00 0.00 0/NA Avg. 0% (0.00) 0.00 
203. R&R Cabinet knob or pull - Premium grade 

0.00 EA 19.18 0.00 0.00 0.00 0/20 yrs Avg. 0% (0.00) 0.00 
204. Add for frosted/etched or beveled glass, per cabinet door 

0.00 EA 45.09 0.00 0.00 0.00 0/50 yrs Avg. 0% (0.00) 0.00 
205. Add for leaded glass (standard design), per cabinet door 

0.00 EA 64.86 0.00 0.00 0.00 0/50 yrs Avg. 0% (0.00) 0.00 
206. R&R Countertop - (terrazzo) 

0.00 SF 312.61 0.00 0.00 0.00 0/40 yrs Avg. 0% (0.00) 0.00 
207. R&R Countertop - Granite or Marble - High grade 

0.00 SF 93.29 0.00 0.00 0.00 0/150 yrs Avg. 0% (0.00) 0.00 
208. R&R Island hood, 48" - tapered canopy - Premium grade 

0.00 EA 5,321.00 0.00 0.00 0.00 0/20 yrs Avg. 0% (0.00) 0.00 
209. Dishwasher connection 
1.00 EA 131.83 2.01 26.76 160.60 0/100 yrs Avg. 0% (0.00) 160.60 
210. R&R Sink - double basin 

1.00 EA 425.35 17.89 88.66 531.90 0/50 yrs Avg. 0% (0.00) 531.90 
211. Rough-in plumbing - per fixture 

1.00 EA 626.16 9.88 127.22 763.26 0/80 yrs Avg. 0% (0.00) 763.26 
212. R&R Sink faucet - Kitchen 

1.00 EA 301.97 11.67 62.74 376.38 0/15 yrs Avg. 0% (0.00) 376.38 
213. R&R Garbage disposal / disposer 

1.00 EA 279.30 9.00 57.66 345.96 0/12 yrs Avg. 0% (0.00) 345.96 
214. R&R Appliance water line - 1/4" 

1.00 EA 93.78 2.35 19.24 115.37 0/50 yrs Avg. 0% (0.00) 115.37 


Totals: Kitchen 200.09 1,611.40 9,668.02 162.74 9,505.28 

___________________________________________________________________________________________________________________________________________
    
# BATHROOM | 
The following line items were calculated by these measures:
278.67 SF Walls 62.08 SF Ceiling 
340.75 SF Walls & Ceiling 62.08 SF Floor 
6.90 SY Flooring 34.83 LF Floor Perimeter 
34.83 LF Ceil. Perimeter

LINE-ITEM QUANTITY  UNIT  TAX  O&P  RCV  AGE/LIFE  COND.  DEP %  DEPREC.  ACV  

215. R&R Vanity - Standard grade 4.17 LF 132.81 22.77 115.32 691.91 4/50 yrs damaged by water 
216. Vanity top - Detach & reset 4.17 LF 44.35 0.00 36.98 221.92 4/NA 
217. R&R Angle stop valve 2.00 EA 34.41 0.86 13.94 83.62 4/100 yrs 
218. R&R P-trap assembly - ABS (plastic) 1.00 EA 58.07 0.36 11.70 70.13 4/25 yrs 
219. Mirror - plate glass - Detach & reset 12.00 SF 5.03 0.00 12.08 72.44 0/NA to assist with cabinet replace SHOWER 
220. R&R Ceramic tile - Standard grade 81.42 SF 13.09 12.99 215.76 1,294.54 14/150 yrs removed & replaced to access the shower pan damage below the shower shower pan replace not included per the desk adjuster 
221. R&R Tile framed shower curb - per LF 0.00 LF 111.17 0.00 0.00 0.00 0/150 yrs 
222. R&R Mortar bed for tile 18.24 SF 9.11 1.83 33.58 201.58 14/150 yrs floor of shower only 
223. R&R 1/2" Cement board 81.42 SF 5.23 5.91 86.34 518.07 14/150 yrs wall board will be damage when the tile is removed 
224. Additional charge to tile a bench seat 1.00 EA 165.76 2.24 33.60 201.60 14/150 yrs 
225. Add-on for diagonal tile installation 81.42 SF 1.60 0.00 26.06 156.33 14/150 yrs 
226. Add-on for tile feature strip - High grade 18.33 LF 11.49 5.57 43.24 259.42 14/150 yrs 
227. Detach & Reset Shower faucet - High grade 1.00 EA 64.01 0.00 12.80 76.81 0/20 yrs 
228. Plumber - per hour 3.00 HR 100.03 0.00 60.02 360.11 14/NA Additional labor hours added due the small nature of the repair 
229. R&R Wall - soap dish - cultured marble 1.00 EA 64.88 1.86 13.36 80.10 14/150 yrs 
230. R&R Custom shower door & partition - 1/4" glass w/frame  48.53 SF 21.95 45.86 222.22 1,333.32 14/25 yrs cannot be detached and reset based on the condition FLOORS 
231. R&R Tile floor covering - Standard grade 62.08 SF 11.97 9.16 150.46 902.72 14/100 yrs 
232. Add-on for diagonal tile installation 62.08 SF 1.60 0.00 19.86 119.19 14/100 yrs 
233. R&R 1/4" Cement board 62.08 SF 5.30 4.77 66.78 400.58 14/100 yrs 
234. R&R Threshold - natural marble 0.00 LF 68.65 0.00 0.00 0.00 14/150 yrs 
235. Interior door - Detach & reset - slab only 2.00 EA 18.80 0.00 7.52 45.12 14/NA FRAMING 
236. R&R Sheathing - OSB - 3/4"- T&G - High grade eng. wtr resist. 64.00 SF 3.73 4.19 48.60 291.51 14/150 yrs 
237. 2" x 4" x 12' #2 treated pine (material only) 1.00 EA 7.21 0.43 1.52 9.16 14/150 yrs bottom plate next to shower that will be damaged 
238. R&R 2" x 10" lumber (1.67 BF per LF) 20.00 LF 4.23 1.52 17.22 103.34 14/150 yrs 2, 10' joists that were damaged by water 
239. Carpenter - General Framer - per hour 3.00 HR 76.03 0.00 45.62 273.71 14/NA Additional labor hours added due the small nature of the repair SHOWER 
240. R&R Ceramic tile - Standard grade 81.42 SF 13.09 12.99 215.76 1,294.54 14/150 yrs removed & replaced to access the shower pan damage below the shower shower pan replace not included per the desk adjuster 
241. R&R Tile framed shower curb - per LF 0.00 LF 111.17 0.00 0.00 0.00 0/150 yrs 
242. R&R Mortar bed for tile 18.24 SF 9.11 1.83 33.58 201.58 14/150 yrs floor of shower only 
243. R&R 1/2" Cement board 81.42 SF 5.23 5.91 86.34 518.07 14/150 yrs wall board will be damage when the tile is removed 
244. Additional charge to tile a bench seat 1.00 EA 165.76 2.24 33.60 201.60 14/150 yrs 
245. Add-on for diagonal tile installation 81.42 SF 1.60 0.00 26.06 156.33 14/150 yrs 
246. Add-on for tile feature strip - High grade 18.33 LF 11.49 5.57 43.24 259.42 14/150 yrs 2025-08-28-1618  COND. DEP % DEPREC. Avg. 14% (83.59) Avg. 14% (13.91) Avg. 14% (39.43) Avg. 9.33% (0.00) Avg. 0% (0.00) Avg. 9.33% (14.67) Avg. 9.33% (0.71) Avg. 9.33% (6.28) Avg. 0% (0.00) Avg. 9.33% (86.93) Avg. 0% (0.00) Avg. 9.33% (13.19) Avg. 9.33% (33.91) Avg. 9.33% (15.68) Avg. 9.33% (12.16) Avg. 9.33% (20.18) 8/31/2025  ACV 819.13 105.28 361.15 0.00 45.12 276.84 8.45 97.06 273.711,207.61 0.00 188.39 484.16 185.92 144.17 239.24 Page: 19  
247. Detach & Reset Shower faucet - High grade 1.00 EA 64.01 0.00 12.80 76.81 0/20 yrs 248. Plumber - per hour 3.00 HR 100.03 0.00 60.02 360.11 14/NA Additional labor hours added due the small nature of the repair 249. R&R Wall - soap dish - cultured marble 1.00 EA 64.88 1.86 13.36 80.10 14/150 yrs 250. R&R Custom shower door & partition - 1/4" glass w/frame 48.53 SF 21.95 45.86 222.22 1,333.32 14/25 yrs cannot be detached and reset based on the condition FLOORS 251. R&R Tile floor covering - Standard grade 62.08 SF 11.97 9.16 150.46 902.72 14/100 yrs 252. Add-on for diagonal tile installation 62.08 SF 1.60 0.00 19.86 119.19 14/100 yrs 253. R&R 1/4" Cement board 62.08 SF 5.30 4.77 66.78 400.58 14/100 yrs 254. R&R Threshold - natural marble 0.00 LF 68.65 0.00 0.00 0.00 14/150 yrs 255. Interior door - Detach & reset - slab only 2.00 EA 18.80 0.00 7.52 45.12 14/NA FRAMING 256. R&R Sheathing - OSB - 3/4"- T&G - High grade eng. wtr resist. 64.00 SF 3.73 4.19 48.60 291.51 14/150 yrs 257. 2" x 4" x 12' #2 treated pine (material only) 1.00 EA 7.21 0.43 1.52 9.16 14/150 yrs bottom plate next to shower that will be damaged 258. R&R 2" x 10" lumber (1.67 BF per LF) 20.00 LF 4.23 1.52 17.22 103.34 14/150 yrs 2, 10' joists that were damaged by water 259. Carpenter - General Framer - per hour 3.00 HR 76.03 0.00 45.62 273.71 14/NA Additional labor hours added due the small nature of the repair 260. Toilet - Reset 0.00 EA 133.97 0.00 0.00 0.00 0/NA 261. 1/4" Cement board 62.08 SF 5.84 5.96 73.72 442.23 0/150 yrs SHOWER 262. Remove Tile tub surround - 60 to 75 SF 1.00 EA 149.68 0.00 29.94 179.62 0/150 yrs remove remaining tile in shower 2025-08-28-1618  COND. DEP % DEPREC. Avg. 0% (0.00) Avg. 0% (0.00) Avg. 9.33% (5.64) Avg. 56% (571.12) Avg. 14% (83.59) Avg. 14% (13.91) Avg. 14% (39.43) Avg. 9.33% (0.00) Avg. 0% (0.00) Avg. 9.33% (14.67) Avg. 9.33% (0.71) Avg. 9.33% (6.28) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. NA (0.00) 8/31/2025  ACV 76.81 360.1174.46 762.20 819.13 105.28 361.15 0.00 45.12 276.84 8.45 97.06 273.710.00 442.23 179.62 Page: 20  
    
263. Tile shower - 61 to 100 SF 1.00 EA 1,741.37 30.68 354.42 264. Detach & Reset Tub/shower faucet - Standard grade 1.00 EA 73.81 0.00 14.76 265. R&R Shower drain - for use with waterproof membrane 1.00 EA 207.76 8.74 43.30 266. R&R Soap holder - recessed 1.00 EA 35.18 1.02 7.24 267. R&R Mosaic - ceramic/porcelain tile - Standard grade 8.00 SF 15.13 2.41 24.70 CABINET 268. Backsplash - solid surface - Unattached - Reset 4.50 LF 2.16 0.02 1.94 CABINET 269. R&R Vanity - Standard grade 4.17 LF 132.81 22.77 115.32 damaged by water 270. Vanity top - Detach & reset 4.17 LF 44.35 0.00 36.98 271. R&R Angle stop valve 2.00 EA 34.41 0.86 13.94 272. R&R P-trap assembly - ABS (plastic) 1.00 EA 58.07 0.36 11.70 273. Mirror - plate glass - Detach & reset 15.00 SF 5.03 0.00 15.10 to assist with cabinet replace WALLS 274. Mask per square foot for drywall work 62.08 SF 0.21 0.19 2.64 275. Drywall patch / small repair, ready for paint 1.00 EA 90.52 0.16 18.14 276. Seal the surface area w/PVA primer - one coat 4.00 SF 0.50 0.01 0.40 277. Paint the walls - one coat 278.67 SF 0.44 1.84 24.88 278. R&R Wallpaper border 34.83 LF 3.22 2.53 22.92 279. Final cleaning - construction - Residential 62.08 SF 0.23 1.03 2.86 FLOORS 2025-08-28-1618  RCV AGE/LIFE 2,126.47 0/150 yrs 88.57 0/20 yrs 259.80 0/100 yrs 43.44 0/50 yrs 148.15 0/150 yrs 11.68 0/NA 691.91 4/50 yrs 221.92 4/NA 83.62 4/100 yrs 70.13 4/25 yrs 90.55 0/NA 15.87 0/150 yrs 108.82 0/150 yrs 2.41 10/15 yrs 149.33 10/15 yrs 137.60 0/7 yrs 18.17 10/NA  COND. DEP % DEPREC. Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 8% (43.60) Avg. 0% (0.00) Avg. 4% (2.38) Avg. 16% (8.14) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 66.67% (1.34) Avg. 66.67% (82.97) Avg. 0% (0.00) Avg. 0% (0.00) 8/31/2025  ACV 2,126.47 88.57 259.80 43.44 148.15 11.68 648.31 221.92 81.24 61.99 90.55 15.87 108.82 1.07 66.36 137.60 18.17 Page: 21  

280. Remove Tear out vinyl & underlayment 62.08 SF 1.20 0.00 14.90 
281. Floor preparation for resilient flooring 62.08 SF 0.43 0.37 5.42 
282. Install Toilet - Detach & reset 1.00 EA 194.94 0.00 38.98 *********drop FCV AV- into sketch 
283. Vinyl - metal transition strip 2.00 LF 2.34 0.13 0.96 
284. Baseboard - 3 1/4" 29.83 LF 2.84 2.08 17.36 
285. Seal & paint baseboard - two coats* 29.83 LF 1.43 0.20 8.58 
286. Base shoe 29.83 LF 1.19 0.79 7.26 
287. Seal & paint base shoe or quarter round 29.83 LF 0.70 0.18 4.22 
288. Interior door - Detach & reset - slab only 1.00 EA 18.80 0.00 3.76 to assist with floor covering remove and replace ******************underlayment needs to be added 
289. R&R Cabinetry - lower (base) units - Standard grade 3.00 LF 139.76 17.63 87.38 290. Countertop - solid surface/granite - Detach & reset 24.00 SF 21.78 0.00 104.54 291. P-trap assembly - Detach & reset 1.00 EA 48.94 0.00 9.78 292. Detach & Reset Garbage disposer* 1.00 EA 143.28 0.00 28.66 293. Sink - undermount - Detach & reset 1.00 EA 203.53 0.08 40.72 294. Detach & Reset P-trap assembly - ABS (plastic) 1.00 EA 48.91 0.00 9.78 295. Detach & Reset Shower faucet 1.00 EA 72.42 0.00 14.48 FRAMING 296. R&R 110 volt copper wiring run and box - rough-in only 1.00 EA 72.47 1.14 14.72 297. R&R Light bar - 4 lights - High grade 1.00 EA 233.65 9.30 48.60 2025-08-28-1618  RCV AGE/LIFE 89.40 2/150 yrs 32.48 0/50 yrs 233.92 2/NA 5.77 0/50 yrs 104.16 0/150 yrs 51.44 0/15 yrs 43.55 2/150 yrs 25.28 2/15 yrs 22.56 0/NA 524.29 3/50 yrs 627.26 3/NA 58.72 3/NA 171.94 0/12 yrs 244.33 0/NA 58.69 4/25 yrs 86.90 0/20 yrs 88.33 0/100 yrs 291.55 0/20 yrs  COND. DEP % DEPREC. Avg. NA (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 1.33% (0.48) Avg. 13.33% (2.80) Avg. 0% (0.00) Avg. 6% (24.86) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 16% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) Avg. 0% (0.00) 8/31/2025  ACV 89.40 32.48 233.92 5.77 104.16 51.44 43.07 22.48 22.56 499.43 627.26 58.72 171.94 244.33 58.69 86.90 88.33 291.55 Page: 22  


298. R&R Exhaust fan - 1.00 EA  291.79  6.68  59.70  358.17  0/14 yrs  Avg.  0%  (0.00)  358.17  
299. R&R 110 volt copper wiring run, box and switch - 1.00 EA  90.81  1.33  18.42  110.56  0/100 yrs  Avg.  0%  (0.00)  110.56  
300. R&R Ground fault interrupter (GFI) outlet - 1.00 EA  42.22  1.19  8.68  52.09  0/10 yrs  Avg.  0%  (0.00)  52.09  
301. R&R 110 volt copper wiring run, box and outlet - 1.00 EA  90.11  1.28  18.28  109.67  0/100 yrs  Avg.  0%  (0.00)  109.67  
302. R&R Toilet - 1.00 EA  541.53  19.65  112.26  673.44  0/150 yrs  Avg.  0%  (0.00)  673.44  
303. R&R Toilet seat  
1.00 EA  60.94  1.89  12.58  75.41  0/9 yrs  Avg.  0%  (0.00)  75.41  
304. R&R Fiberglass tub & shower combination  
1.00 EA  1,381.56  49.91  286.30  1,717.77  0/50 yrs  Avg.  0%  (0.00)  1,717.77  
305. Rough-in plumbing - per fixture  
3.00 EA  626.16  29.63  381.62  2,289.73  0/80 yrs  Avg.  0%  (0.00)  2,289.73  
306. R&R Tub/shower faucet  
1.00 EA  321.90  8.79  66.14  396.83  0/20 yrs  Avg.  0%  (0.00)  396.83  
307. R&R Sink - single  
1.00 EA  283.20  9.87  58.62  351.69  0/50 yrs  Avg.  0%  (0.00)  351.69  
308. R&R Sink faucet - Bathroom  
1.00 EA  255.97  8.91  52.98  317.86  0/20 yrs  Avg.  0%  (0.00)  317.86  
309. R&R Shower door - High grade  
1.00 EA  939.96  41.97  196.40  1,178.33  0/25 yrs  Avg.  0%  (0.00)  1,178.33  
Includes: Shower door, side light, and installation labor. Labor cost to remove a shower door and to discard in a job-site waste receptacle.  
Quality: Brass frame, clear or striped glass, 30" wide door.  
 
310. Shower curtain rod - Detach & reset  
1.00 EA  20.08  0.00  4.02  24.10  0/NA  Avg.  0%  (0.00)  24.10  

311. Clean shower curtain - Full service  
1.00 EA  24.23  0.00  4.84  29.07  0/NA  Avg.  0%  (0.00)  29.07  

312. Clean shower curtain - Drop off  
1.00 EA  20.11  0.00  4.02  24.13  0/NA  Avg.  0%  (0.00)  24.13  

313. Corrosion mitigation of shower  
1.00 EA  42.87  3.09  8.58  54.54  0/NA  Avg.  0%  (0.00)  54.54  

314. R&R Shower light - waterproof fixture  
1.00 EA  206.06  5.83  42.36  254.25  0/20 yrs  Avg.  0%  (0.00)  254.25  

315. R&R Custom shower door & partition - 1/2" glass - frameless  
1.00 SF  97.44  3.38  20.18  121.00  0/25 yrs  Avg.  0%  (0.00)  121.00  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
316. Corrosion mitigation of tub / shower faucet 
1.00 EA 12.39 0.89 2.48 15.76 0/NA Avg. 0% (0.00) 15.76 
317. R&R Concrete shower curb - cultured marble - per LF 
34.83 LF 208.37 52.27 1,461.98 8,771.78 0/20 yrs Avg. 0% (0.00) 8,771.78 
318. Mirror & Shower Door Installer - per hour 

1.00 HR 72.14 0.00 14.42 86.56 0/NA Avg. 0% (0.00) 86.56 
319. R&R Polystyrene shower curb - per LF 
34.83 LF 41.16 39.58 294.64 1,767.82 0/150 yrs Avg. 0% (0.00) 1,767.82 
320. Fiberglass tub & shower combination - Detach & reset 
1.00 EA 558.14 0.00 111.62 669.76 0/NA Avg. 0% (0.00) 669.76 Includes: On-site storage and labor. Excludes: Repairing of adjacent surfaces, manipulation of the tub/shower faucet (see PLM TSFAURS), sliding glass doors (see MSD TUBDR), or 
any additional materials or hardware. Note: Labor cost to disconnect and detach a fiberglass tub/shower unit, move to an adjacent room for storage, and reinstall at a later time. 
321. R&R Claw-foot shower curtain surround 
1.00 EA 258.12 10.44 53.70 322.26 0/15 yrs Avg. 0% (0.00) 322.26 Includes: Claw-foot shower curtain surround and installation labor. Labor cost to remove a shower curtain surround and to discard in a job-site waste receptacle. Quality: Oval or d-ring shower curtain surround. Note: Due to the custom features of claw-foot tubs and accessories, size, finish, and/or style may not be the only factor in the price of materials. 
Average life expectancy 15 years Average depreciation 6.67% per year 
322. R&R Shower drain - for use with waterproof membrane 
1.00 EA 221.08 8.74 45.96 275.78 0/100 yrs Avg. 0% (0.00) 275.78 Includes: Drain and installation labor. Labor cost to remove a shower drain and to discard in a job-site waste receptacle Excludes: Mortar bed or polystyrene base. Quality: Drain with grate. Note: For use in waterproof membrane shower/floor systems. 
Average life expectancy 100 years Average depreciation 1% per year 
323. Shower seat add on - hot mop - built in 

1.00 EA 60.77 0.19 12.20 73.16 0/100 yrs Avg. 0% (0.00) 73.16 
Includes: Felt paper, tar, and installation labor. Note: Addional cost to mop a built in shower seat. Average life expectancy 100 years Average depreciation 1% per year 
324. R&R Claw-foot tub faucet with shower 

1.00 EA 873.81 35.70 181.90 1,091.41 0/20 yrs Avg. 0% (0.00) 1,091.41 
QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
Includes: Claw-foot tub faucet, exposed shower plumbing and shower head, shower curtain attachment, and installation labor. Labor cost to remove a claw-foot tub faucet with a shower/curtain attachment and to discard in a job-site waste receptacle Excludes: Supply lines. Quality: Solid brass, deck mounted design with a polished finish. Green: LEED considers shower heads to be green when they are Water Sense labeled and meet the following conditions: Residential: flow rate not to exceed 1.5 gallons per minute (5.6 liters per minute) for 2 points or 1.75 gallons per minute (6.6 liters per minute) for 1 point. Water pressure must not exceed 60 psi (414 kPa). Commercial: flow rate not to exceed 2.5 gpm (9.5 lpm) at 80 psi (550 kPa). Note: Due to the custom features of claw-foot tubs and accessories, size, finish, and/or style may not be the only factor in the price of materials. Average life expectancy 20 years Average depreciation 5% per year 
325. R&R Custom shower door & partition - 1/4" glass w/frame 
1.00 SF 36.61 1.27 7.58 45.46 0/25 yrs Avg. 0% (0.00) 45.46 Includes: Shower door/partition material and installation labor. Labor cost to remove a shower door/partition and to discard in a job-site waste receptacle. Quality: 1/4" tempered glass with aluminum frame. 
Average life expectancy 25 years Average depreciation 4% per year 
326. Mirror/Shower Door - Labor Minimum 
1.00 EA 180.36 0.00 36.08 216.44 0/NA Avg. 0% (0.00) 216.44 Includes: 2 1/2 hours labor. 
Note: Minimum charge for mirror and shower door repair. If additional time is needed to match or purchase materials, it may be necessary to add supplemental labor hours; see item MSD LAB. 
327. R&R Polystyrene shower floor base 
0.00 SF 19.21 0.00 0.00 0.00 0/150 yrs Avg. 0% (0.00) 0.00 Includes: Polystyrene shower base, thinset, and installation labor. Labor cost to remove polystyrene shower floor base and to discard in a job-site waste receptacle. Excludes: Shower pan/membrane. Quality: Pre-formed high density polystyrene sloped floor base or equal. Note: This item is for the construction of a polystyrene shower floor base, to be used in place of mortar bed. 
Average life expectancy 150 years Average depreciation 0.67% per year 
328. Bathtub or shower faucet (finish trim) - Detach & reset 
1.00 EA 68.87 0.00 13.78 82.65 0/NA Avg. 0% (0.00) 82.65 Includes: On-site storage and labor. Excludes: Removing of components behind wall finish such as rough plumbing or valve body. Any additional materials or hardware. 
Note: Labor cost to disconnect and detach a tub spout & handle or shower head & handle, move to an adjacent room for storage, and reinstall at a later time. 
329. Shower door system - corner unit - Detach & reset 
1.00 EA 375.92 0.00 75.18 451.10 0/NA Avg. 0% (0.00) 451.10 Includes: On site storage and labor to detach and reset doors, glass panels, styles, rails, and supports. Excludes: Any additional materials or hardware. Note: Labor cost to detach a corner shower door system, move to an adjacent room for storage, and reinstall at a later time. Pricing could vary 
based on factors such as shower material, frame design, degree of difficulty, etc.; users may want to compare this item with their specific costs and make adjustments if necessary. 
330. Tile shower - regrout 

1.00 EA 225.54 1.32 45.36 272.22 0/10 yrs Avg. 0% (0.00) 272.22 
QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
Includes: Grout and labor. Green: LEED considers tile setting adhesive and grout to be green if: all adhesives and sealants wet-applied on site meet the applicable chemical content requirements of SCAQMD Rule 1168, July 1, 2005, Adhesive and Sealant Applications, as analyzed by the methods specified in Rule 1168.
 The provisions of SCAQMD Rule 1168 do not apply to adhesives and sealants subject to state or federal consumer product VOC regulations. Average life expectancy 10 years Average depreciation 10% per year 
331. R&R Bathtub faucet (no shower) - High grade 
1.00 
EA 305.77 8.52 62.84 377.13 0/15 yrs Avg. 0% (0.00) 377.13 Includes: Bathtub faucet and installation labor. Labor cost to remove a bathtub faucet and to discard in a job-site waste receptacle. Quality: Chrome or brass washerless faucet with double or single handle design. Green: LEED considers bathroom faucets to be green when they are Water Sense labeled and meet the following conditions: Residential: Flow rate 

not to exceed 1.0 gallons per minute (5.6 liters per minute) for 2 points or 1.5 gallons per minute (6.6 liters per minute) for 1 point. Water pressure must not exceed 60 psi (414 kPa). Commercial: Public lavatory (restroom) faucets 0.5 gpm (1.9 lpm) at 60 psi (415 kPa); private lavatory faucets 

2.2
 gpm at 60 psi (8.3 lpm at 415 kPa). Average life expectancy 15 years Average depreciation 6.67% per year 


332. R&R Fiberglass tub & shower combination 
1.00 EA 1,381.56 49.91 286.30 1,717.77 0/50 yrs Avg. 0% (0.00) 1,717.77 Includes: Tub and shower combination, drain set, and installation labor. Labor cost to remove a tub and shower combination unit and to discard in a job-site waste receptacle. Quality: Fiberglass and/or acrylic with one or two shelves. All standard colors. Green: LEED considers fiberglass to be green if it contributes to one or more of the following credits: Residential: Environmentally Preferable Products, and/or Low-emitting Products. Commercial: Building Life-Cycle Reduction and/or Building Product Disclosure and Optimization; Environmental Product Declaration. 
Average life expectancy 50 years Average depreciation 2% per year 
333. Tub/shower faucet - Detach & reset 
1.00 EA 183.65 0.00 36.74 220.39 0/NA Avg. 0% (0.00) 220.39 Includes: On-site storage and labor. Excludes: Any additional materials or hardware. 
Note: Labor cost to disconnect and detach a complete tub/shower faucet, including valve and shower head assembly behind the wall, move to an adjacent room for storage, and reinstall at a later time. 
334. Fiberglass shower unit - Detach & reset 
1.00 EA 443.08 0.00 88.62 531.70 0/NA Avg. 0% (0.00) 531.70 Includes: On-site storage and labor. Excludes: Repairing of adjacent surfaces, manipulation of the shower faucet (see PLM TSFAURS), shower door (see MSD SDORRS), or any 
additional materials or hardware. Note: Labor cost to disconnect and detach a fiberglass shower unit, move to an adjacent room for storage, and reinstall at a later time. 
335. Shower door system - Detach & reset 
1.00 EA 265.53 0.00 53.10 318.63 0/NA Avg. 0% (0.00) 318.63 Includes: On site storage and labor to detach and reset styles, rails, and supports. Excludes: Any additional materials or hardware. Note: Labor cost to detach a shower door system, move to an adjacent room for storage, and reinstall at a later time. Pricing could vary based on 
factors such as shower material, frame design, degree of difficulty, etc.; users may want to compare this item with their specific costs and make adjustments if necessary. 
336. R&R Shower door - corner unit - High grade 

1.00 EA 1,566.38 77.10 328.70 1,972.18 0/25 yrs Avg. 0% (0.00) 1,972.18 
QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
Includes: Neo-angle unit with a single pivot door on the diagonal wall. Labor cost to remove a shower door and to discard in a job-site waste receptacle. Quality: 38" unit with chrome or brass color trim and clear glass. Average life expectancy 25 years Average depreciation 4% per year Maximum depreciation 100% 
337. R&R Tile framed shower curb - per LF 
34.83 LF 122.75 49.78 865.04 5,190.20 0/150 yrs Avg. 0% (0.00) 5,190.20 Includes: Three rows of 2"x 4" material for shower curb, metal lath, mortar, thinset, ceramic tile, grout, trim pieces, the use of a mortar mixer and ceramic tile saw, and labor for construction of framed shower curb and for tile installation. Labor cost to remove framed shower curb with ceramic tile and to discard in a job-site waste receptacle. Excludes: Shower pan. Green: LEED considers tiles to be green when they are recycled or made from pre-consumer recycled materials. All adhesives and sealants wet-applied on site must meet the applicable chemical content requirements of SCAQMD Rule 1168, July 1, 2005, Adhesive and Sealant Applications, as analyzed by the methods specified in Rule 1168. The provisions of SCAQMD Rule 1168 do not apply to adhesives and sealants subject to state or federal consumer product VOC regulations. Note: This item is for the construction of a framed shower curb with ceramic tile installed over it. 
Average life expectancy 150 years Average depreciation 0.67% per year 
338. Clean shower curtain rod - Heavy 
1.00 EA 12.06 0.86 2.42 15.34 0/NA Avg. 0% (0.00) 15.34 Includes: Three rows of 2"x 4" material for shower curb, metal lath, mortar, thinset, ceramic tile, grout, trim pieces, the use of a mortar mixer and ceramic tile saw, and labor for construction of framed shower curb and for tile installation. Labor cost to remove framed shower curb with ceramic tile and to discard in a job-site waste receptacle. Excludes: Shower pan. Green: LEED considers tiles to be green when they are recycled or made from pre-consumer recycled materials. All adhesives and sealants wet-applied on site must meet the applicable chemical content requirements of SCAQMD Rule 1168, July 1, 2005, Adhesive and Sealant Applications, as analyzed by the methods specified in Rule 1168. The provisions of SCAQMD Rule 1168 do not apply to adhesives and sealants subject to state or federal consumer product VOC regulations. Note: This item is for the construction of a framed shower curb with ceramic tile installed over it. 
Average life expectancy 150 years Average depreciation 0.67% per year 
339. R&R Floor drain - tub/shower - metal/plastic 
1.00 EA 47.70 0.59 9.66 57.95 0/65 yrs Avg. 0% (0.00) 57.95 Includes: Drain and labor to install. Labor cost to remove a metal/plastic tub or shower drain and to discard in a job-site waste receptacle. Excludes: Plumbing pipe, fittings, p-trap. Quality: Metal/plastic tub or shower drain. 
Average life expectancy 65 years Average depreciation 1.54% per year 
340. R&R Tile shower - 121 to 150 SF - High grade 

1.00 EA 4,706.32 103.16 961.92 5,771.40 0/150 yrs Avg. 0% (0.00) 5,771.40 
341. Shower pan - hot mop - 31 to 40 SF 

1.00 EA 461.93 2.30 92.84 557.07 0/100 yrs Avg. 0% (0.00) 557.07 
342. Clean shower door - Heavy 

1.00 EA 30.55 2.21 6.12 38.88 0/NA Avg. 0% (0.00) 38.88 
QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
Includes: Cleaning chemical and labor. Quality: Clean glass, frame, threshold, and hardware - both sides. Green: LEED considers cleaners to be green under the following standards, or a local equivalent for projects outside of the U.S.: Green Seal GS-37, GS-40, GS -52/53; Environmental Choice CCD-110, CCD-112, CCD-113, CCD-115, CCD-146, CCD-147, CCD-148; EPA Design for the Environment Program's Standard for Safer Cleaning Products; California Code of Regulations maximum allowable VOC levels for the specific product category. Paper products and trash bags must meet one or more of the following programs or a local equivalent for projects outside the U.S.: EPA comprehensive procurement guidelines, for janitorial paper; Green Seal GS-01; Environmental Choice CCD-082, CCD-086; Janitorial paper products derived from rapidly renewable resources or manufactured from tree-free fibers; FSC certification, for fiber procurement; EPA comprehensive procurement guidelines, for plastic trash can liners (California Code of Regulations Title 14, Chapter 4, Article 5, or SABRC 42290-42297 Recycled Content Plastic Trash Bag Program). Note: Generally, heavy soiling requires specialized cleaning agents, heavy scrubbing/agitation, and extensive rinsing. 
343. Shower pan - hot mop - 17 to 30 SF  
1.00 EA  386.96  1.62  77.72  466.30  0/100 yrs  Avg.  0%  (0.00)  466.30  
Includes: Felt paper, tar, and installation labor.  
Quality: 17 to 30 square feet.  
Average life expectancy 100 years  
Average depreciation 1% per year  
Maximum depreciation 100%  
344. R&R Fiberglass shower unit - High grade  
1.00 EA  1,281.72  52.66  266.90  1,601.28  0/50 yrs  Avg.  0%  (0.00)  1,601.28  

Includes: Fiberglass shower unit, drain, and installation labor. Labor cost to remove a fiberglass or acrylic shower unit and to discard in a job-site waste receptacle. Excludes: Shower doors (see items MSD SDORC, MSD SDORC+, or MSD SDORC++ for shower door corner units, if needed). Quality: 38" corner unit in all colors. May have 2 to 3 shelves with acrylic towel/washcloth bars. Green: LEED considers fiberglass to be green if it contributes to one or more of the following credits: Residential: Environmentally Preferable Products, and/or Low-emitting Products. Commercial: Building Life-Cycle Reduction and/or Building Product Disclosure and Optimization; Environmental Product Declaration. Average life expectancy 50 years Average depreciation 2% per year 
345. R&R Tile shower - 121 to 150 SF 
1.00 EA 3,964.31 69.61 806.80 4,840.72 0/150 yrs Avg. 0% (0.00) 4,840.72 Includes: Ceramic tile, grout, thinset, radius trim piece/bullnose, tile soap dish, the use of a ceramic tile saw, and installation labor. Labor cost to remove ceramic tile and to discard in a job-site waste receptacle. Excludes: Shower pan or mortar bed for the tile. Green: LEED considers tiles to be green when they are recycled or made from pre-consumer recycled materials. All adhesives and sealants wet-applied on site must meet the applicable chemical content requirements of SCAQMD Rule 1168, July 1, 2005, Adhesive and Sealant Applications, as analyzed by the methods specified in Rule 1168. The provisions of SCAQMD Rule 1168 do not apply to adhesives and sealants subject to state or federal consumer product VOC regulations. Note: If a mortar bed is used see item TILBMUD. If a cement backer board is used see TILBCEM1/2. Average life expectancy 150 years 
Average depreciation 0.67% per year Maximum depreciation 100% 
346. Clean shower - Heavy 

1.00 EA 76.18 5.49 15.24 96.91 0/NA Avg. 0% (0.00) 96.91 
QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
Includes: Cleaning chemical and labor. Excludes: Faucets, grab bars, and accessories. Quality: Marlite or pre-formed acrylic shower walls, floor, and trim. Green: LEED considers cleaners to be green under the following standards, or a local equivalent for projects outside of the U.S.: Green Seal GS-37, GS-40, GS -52/53; Environmental Choice CCD-110, CCD-112, CCD-113, CCD-115, CCD-146, CCD-147, CCD-148; EPA Design for the Environment Program's Standard for Safer Cleaning Products; California Code of Regulations maximum allowable VOC levels for the specific product category. Paper products and trash bags must meet one or more of the following programs or a local equivalent for projects outside the U.S.: EPA comprehensive procurement guidelines, for janitorial paper; Green Seal GS-01; Environmental Choice CCD-082, CCD-086; Janitorial paper products derived from rapidly renewable resources or manufactured from tree-free fibers; FSC certification, for fiber procurement; EPA comprehensive procurement guidelines, for plastic trash can liners (California Code of Regulations Title 14, Chapter 4, Article 5, or SABRC 42290-42297 Recycled Content Plastic Trash Bag Program). Note: Generally, heavy soiling requires specialized cleaning agents, heavy scrubbing/agitation, and extensive rinsing. 
347. R&R Shower bench 
1.00 EA 538.16 22.56 112.16 672.88 0/150 yrs Avg. 0% (0.00) 672.88 Includes: Shower bench and installation labor. Labor cost to remove a shower bench and to discard in a job-site waste receptacle. Quality: Phenolic folding bench. Average life expectancy 150 years 
Average depreciation 0.67% per year Maximum depreciation 100% 
348. R&R Tub/shower faucet - High grade 
1.00 EA 400.35 13.50 82.78 496.63 0/20 yrs Avg. 0% (0.00) 496.63 Includes: Combination tub/shower faucet, shower head, shower valve, and installation labor. Labor cost to remove a tub and shower faucet and to discard in a job-site waste receptacle. Quality: Bronze or gold finish, washerless design with chrome plated plastic handles. Green: LEED considers shower faucets to be green when they are Water Sense labeled and meet the following conditions: Residential: flow rate not to exceed 1.5 gallons per minute (5.6 liters per minute) for 2 points or 1.75 gallons per minute (6.6 liters per minute) for 1 point. Water pressure must not exceed 60 psi (414 kPa). Commercial: flow rate not to exceed 2.5 gpm (9.5 lpm) at 80 psi (550 kPa). Average life expectancy 20 years 
Average depreciation 5% per year Maximum depreciation 100% 
349. R&R Shower curtain rod 
1.00 EA 44.70 1.22 9.18 55.10 0/50 yrs Avg. 0% (0.00) 55.10 Includes: Shower curtain rod and installation labor. Labor cost to remove a shower curtain rod and to discard in a job-site waste receptacle. Quality: Up to 72" fixed or adjustable rod, straight or curved. Chrome, brushed nickel, or other common finishes. Average life expectancy 50 years 
Average depreciation 2% per year Maximum depreciation 100% 
350. R&R Shower head only - High grade 
1.00 EA 113.27 4.75 23.62 141.64 0/20 yrs Avg. 0% (0.00) 141.64 Includes: Shower head and installation labor. Labor cost to remove a shower head and to discard in a job-site waste receptacle. Excludes: Shower faucet, shower valve. Quality: Bronze, gold, nickel, or equal finish. May have adjustable spray and/or detachable shower head. Green: LEED considers shower heads to be green when they are Water Sense labeled and meet the following conditions: Residential: flow rate not to exceed 1.5 gallons per minute (5.6 liters per minute) for 2 points or 1.75 gallons per minute (6.6 liters per minute) for 1 point. Water pressure must not exceed 60 psi (414 kPa). Commercial: flow rate not to exceed 2.5 gpm (9.5 lpm) at 80 psi (550 kPa). Note: This line item is for replacement of shower head only. Average life expectancy 20 years 
Average depreciation 5% per year Maximum depreciation 100% 
QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
351. Shower pan  
1.00 EA  150.04  2.97  30.60  183.61  0/20 yrs  Avg.  0%  (0.00)  183.61  
Includes: Rubber or plastic sheet material, pre-molded corners, adhesive, shower drain, and installation labor.  
Note: Material and labor to fabricate and install an average size (36" x 36") shower pan from rubber or plastic sheet material.  
Average life expectancy 20 years  
Average depreciation 5% per year  
Maximum depreciation 100%  
352. R&R Shower faucet - High grade  
1.00 EA  319.59  12.30  66.38  398.27  0/20 yrs  Avg.  0%  (0.00)  398.27  

Includes: Shower faucet, shower head, shower valve, hardware, and installation labor. Labor cost to remove a shower faucet and to discard in a job-site waste receptacle. Quality: Bronze, gold, nickel, or equal finish, washerless design with chrome plated plastic handles. May have adjustable spray and/or detachable shower head. Green: LEED considers shower faucets to be green when they are Water Sense labeled and meet the following conditions: Residential: flow rate not to exceed 1.5 gallons per minute (5.6 liters per minute) for 2 points or 1.75 gallons per minute (6.6 liters per minute) for 1 point. Water pressure must not exceed 60 psi (414 kPa). Commercial: flow rate not to exceed 2.5 gpm (9.5 lpm) at 80 psi (550 kPa). Average life expectancy 20 years Average depreciation 5% per year Maximum depreciation 100% 
353. R&R Shower base (cultured marble) 
1.00 EA 842.86 29.65 174.52 1,047.03 0/20 yrs Avg. 0% (0.00) 1,047.03 Includes: Shower base, drain, dry mix concrete, and installation labor. Labor cost to remove a shower base and to discard in a job-site waste receptacle. Quality: 36" x 36" cultured marble, standard colors. Note: Use PLM SLABOC when installed over concrete. Average life expectancy 20 years 
Average depreciation 5% per year Maximum depreciation 100% 
354. R&R Shower base 

1.00 EA 564.38 19.36 116.74 700.48 0/50 yrs Avg. 0% (0.00) 700.48 
Includes: Shower base, drain, and installation labor. Labor cost to remove a shower base and to discard in a job-site waste receptacle. Quality: 36" x 36" fiberglass or acrylic, standard colors. Green: LEED considers fiberglass to be green if it contributes to one or more of the following credits: Residential: Environmentally Preferable Products, and/or Low-emitting Products. Commercial: Building Life-Cycle Reduction and/or Building Product Disclosure and Optimization; Environmental Product Declaration. Note: Use PLM SLABOC when installed over concrete. Average life expectancy 50 years Average depreciation 2% per year Maximum depreciation 100% 
355. R&R Shower door - corner unit - oversized - High grade 
1.00 EA 1,781.51 85.64 373.44 2,240.59 0/25 yrs Avg. 0% (0.00) 2,240.59 Includes: Neo-angle unit with a single pivot door on the diagonal wall. Labor cost to remove a shower door and to discard in a job-site waste receptacle. Quality: Up to 60" unit with chrome or brass color trim and clear glass. Average life expectancy 25 years 
Average depreciation 4% per year Maximum depreciation 100% 



633.33 SF Walls 331.00 SF Ceiling 
964.33 SF Walls & Ceiling 331.00 SF Floor 
36.78 SY Flooring 79.17 LF Floor Perimeter 
79.17 LF Ceil. Perimeter 

# Ceiling
    
QUANTITY UNIT TAX O&P RCV AGE/LIFE WALLS 
356. Mask and prep for paint - plastic, paper, tape (per LF) 79.17 LF 0.92 1.05 14.78 88.67 11/15 yrs 
357. Remove 1/2" drywall - hung, taped, floated, ready for paint 8.00 SF 0.32 0.00 0.52 3.08 11/150 yrs 
358. 1/2" drywall - hung, taped, floated, ready for paint 8.00 SF 1.58 0.22 2.56 15.42 11/150 yrs 
359. R&R Batt insulation - 4" - R13 - paper faced* 8.00 SF 0.75 0.20 1.24 7.44 11/150 yrs 
360. Seal the surface area w/latex based stain blocker - one coat 8.00 SF 0.38 0.03 0.60 3.67 11/15 yrs 
361. Paint the walls - one coat 633.33 SF 0.44 4.18 56.58 339.43 11/15 yrs 
362. Painter - per hour 2.00 HR 52.02 0.00 20.80 124.84 0/15 yrs Additional labor hours added due the small nature of the repair 
363. Final cleaning - construction - Residential 331.00 SF 0.19 4.52 12.58 79.99 0/NA TRIM 
364. R&R Baseboard - 6" 7.00 LF 5.11 1.13 7.38 44.28 14/150 yrs 
365. Seal & paint baseboard, oversized - two coats* 7.00 LF 1.35 0.06 1.92 11.43 14/15 yrs 
366. Paint baseboard, oversized - one coat 71.83 LF 0.89 0.43 12.86 77.22 14/15 yrs remaining base 
367. R&R Base shoe 71.83 LF 1.34 1.81 19.60 117.66 14/150 yrs 
368. Finish Carpenter - per hour 2.00 HR 70.22 0.00 28.08 168.52 14/NA Additional labor hours added due the small nature of the repair 
369. Seal & paint base shoe or quarter round 71.83 LF 0.67 0.39 9.70 58.22 14/15 yrs 
370. Paint casing - one coat 0.00 LF 0.81 0.00 0.00 0.00 14/15 yrs for door trim where base is being replaced 
371. Painter - per hour 1.00 HR 63.11 0.00 12.62 75.73 14/15 
    

QUANTITY UNIT TAX O&P 
    
Additional labor hours added due the small nature of the repair TRIM 372. 
    
Baseboard - 3 1/4" 20.00 LF 2.84 1.39 11.64 
    
373. Seal & paint baseboard - two coats* 20.00 LF 1.43 0.13 5.74 
374. Paint baseboard - one coat 51.83 LF 0.91 0.25 9.50 paint remaining base TRIM 
375. Baseboard - 4 1/4" 20.00 LF 3.56 2.16 14.68 
376. Seal & paint baseboard - two coats* 20.00 LF 1.43 0.13 5.74 
377. Paint baseboard - one coat 51.83 LF 0.91 0.25 9.50 paint remaining base WALLS 
378. Paint the walls - one coat 633.33 SF 0.70 5.32 89.72 
379. Paint door/window trim & jamb - 1 coat (per side) 3.00 EA 22.40 0.66 13.58 
380. Paint baseboard - one coat 71.83 LF 1.00 0.39 14.44 CEILING & WALLS 
381. Content Manipulation charge - per hour 1.00 HR 34.22 0.00 6.84 
382. Mask and cover light fixture 1.00 EA 12.20 0.04 2.44 
383. Paint the walls and ceiling - one coat 964.33 SF 0.56 6.36 109.28 smoke sealant 
384. Paint crown molding - one coat 139.17 LF 0.93 1.00 26.08 tray ceiling as well 
385. Paint door or window opening - 2 coats (per side) 5.00 EA 29.18 1.51 29.48 for windows 
386. Paint door slab only - 1 coat (per side) 3.00 EA 23.29 0.99 14.18 
387. Paint door/window trim & jamb - 1 coat (per side) 3.00 EA 19.75 0.66 12.00 71.91 21/15 yrs     
388. Paint baseboard - one coat 71.83 LF 0.88 0.39 12.72 76.32 21/15 yrs 
389. Install Window blind - PVC - 2" - 7.1 to 14 SF 4.00 EA 37.66 0.00 30.12 180.76 21/5 yrs cleaned by remediation team FLOORS 
390. Clean and deodorize carpet 331.00 SF 0.49 11.89 32.48 206.56 21/NA 
391. R&R Chair rail - 2 1/2" 79.17 LF 4.26 8.79 69.22 415.28 0/150 yrs 
392. Seal (1 coat) & paint (1 coat) chair rail 79.17 LF 1.98 0.81 31.52 189.09 0/15 yrs 
393. R&R Crown molding - 3 1/4" 79.17 LF 5.88 10.02 95.10 570.64 0/150 yrs 
394. Paint crown molding - two coats 79.17 LF 2.08 0.95 33.14 198.76 0/15 yrs 
395. R&R 5/8" drywall - type C - hung, taped, light texture 633.33 SF 3.38 33.82 434.88 2,609.35 0/150 yrs The above item represents one layer for a 1 HR rated fire wall.
396. R&R 5/8" drywall - type C - hung, taped, light texture 1,266.67 SF 3.38 67.64 869.80 5,218.79 0/150 yrs The above item represents two layers for a 2 HR rated fire wall. 
397. R&R 5/8" drywall - hung & fire taped only 964.33 SF 2.77 45.71 543.38 3,260.28 0/150 yrs 
398. R&R 5/8" drywall - lead lined - 4# 964.33 SF 17.31 517.85 3,442.10 20,652.50 0/150 yrs 
399. Seal/prime (1 coat) then paint (2 coats) the walls and ceiling 964.33 SF 1.74 20.25 339.64 2,037.82 0/15 yrs 
400. R&R Cove base molding - rubber or vinyl, 4" high 79.17 LF 3.03 8.12 49.60 297.60 0/50 yrs 
401. R&R 1/2" water rock (greenboard) hung, taped ready for texture 633.33 SF 3.19 33.44 410.74 2,464.50 0/150 yrs 
402. Add for bullnose (rounded) corners 964.33 SF 0.21 1.16 40.74 244.41 0/150 yrs 
403. R&R 5/8" drywall - hung, taped, floated, ready for paint 331.00 SF 3.35 17.28 225.22 1,351.35 0/150 yrs 
404. Acoustic ceiling (popcorn) texture 331.00 SF 1.10 1.59 73.14 438.83 0/150 yrs 2
406. Additional cost for high wall or ceiling - over 14' to 20' 964.33 SF 0.74 0.00 142.72 CEILING 
407. Mask wall - plastic, paper, tape (per LF) 79.17 LF 1.10 1.05 17.64 
408. Remove 1/2" drywall - hung, taped, ready for texture 32.00 SF 0.37 0.00 2.36 
409. 1/2" drywall - hung, taped, ready for texture 32.00 SF 1.65 0.79 10.72 
410. Texture drywall - light hand texture 48.00 SF 0.51 0.12 4.92 
411. Batt insulation - 10" - R30 - unfaced batt 32.00 SF 1.01 1.46 6.76 
412. Seal/prime then paint the surface area (2 coats)* 48.00 SF 0.64 0.43 6.22 
413. Paint part of the ceiling - one coat 283.00 SF 0.53 1.87 30.38 
414. R&R Crown molding - 4 1/4" 14.00 LF 4.74 1.52 13.58 
415. Paint crown molding, oversized - two coats 14.00 LF 1.00 0.11 2.82 WALLS 
416. Contents - move out then reset 1.00 EA 41.49 0.00 8.30 
417. Remove 1/2" drywall - hung, taped, ready for texture 32.00 SF 0.37 0.00 2.36 
418. 1/2" drywall - hung, taped, ready for texture 32.00 SF 1.65 0.79 10.72 
419. Texture drywall - light hand texture 48.00 SF 0.51 0.12 4.92 
420. R&R Batt insulation - 6" - R19 - unfaced batt 32.00 SF 0.93 1.02 6.16 
421. Seal/prime then paint the surface area (2 coats)* 33.00 SF 0.64 0.30 4.28 
422. Paint part of the walls - one coat 570.33 SF 0.53 3.76 61.22 
423. Final cleaning - construction - Residential 331.00 SF 0.23 5.48 15.22 TRIM 
424. R&R Judges paneling - raised panel - hardwood 24.00 SF 31.37 14.73 
425. Finish Carpenter - per hour 8.00 HR 71.01 0.00 
426. R&R Baseboard - 8" paint grade - 2 piece 15.00 LF 6.10 2.08 
427. Paint - judges paneling - two coats 15.00 SF 2.84 0.22 
428. Paint baseboard, oversized - two coats 15.00 LF 1.01 0.14 FLOORS 
429. Carpet - Detach & relay 64.00 SF 0.64 0.08 
430. R&R Carpet pad 64.00 SF 0.63 1.73 
431. Floor protection - self-adhesive plastic film 1.00 SF 0.83 0.01 
432. Scrape the walls & prep for paint 633.33 SF 0.88 0.38                     
433. Texture drywall - machine 633.33 SF 0.70 2.66 
434. Cleaning Technician - per hour 1.00 HR 54.18 3.90 CABINET 
435. R&R Vanity - Standard grade 3.42 LF 132.81 18.67 damaged by water 
436. Vanity top - Detach & reset 3.42 LF 44.35 0.00 
437. R&R Angle stop valve 2.00 EA 34.41 0.86 
438. R&R P-trap assembly - ABS (plastic) 1.00 EA 58.07 0.36 
439. Mirror - plate glass - Detach & reset 12.00 SF 5.03 0.00 to assist with cabinet replace CABINET 
440. Detach & Reset Vanity - Standard grade 3.00 LF 49.66 0.00 tile is under the cabinet
441. Vanity top - Detach & reset 
3.00 LF 44.35 0.00 26.62 159.67 4/NA Avg. 0% (0.00) 159.67 
442. R&R Angle stop valve 
2.00 EA 34.41 0.86 13.94 83.62 4/100 yrs Avg. 4% (2.38) 81.24 
no option to detach and reset 
443. Detach & Reset P-trap assembly - ABS (plastic) 
1.00 EA 48.91 0.00 9.78 58.69 4/25 yrs Avg. 16% (0.00) 58.69 

FENCE 
444. Install Vinyl (PVC) fence post with cap - 5" x 5"* 
1.00 EA 17.79 0.00 3.56 21.35 0/150 yrs Avg. 0% (0.00) 21.35 fence post not damaged--install only 

445. R&R Vinyl (PVC) fence post cap only - 5" x 5" 
1.00 EA 9.04 0.23 1.84 11.11 0/150 yrs Avg. 0% (0.00) 11.11 

446. Remove Wallpaper 
633.33 SF 1.33 0.00 168.46 1,010.79 0/7 yrs Avg. NA (0.00) 1,010.79 
447. Additional charge to remove non-strippable wallpaper 
633.33 SF 0.56 0.76 71.10 426.52 0/7 yrs Avg. NA (0.00) 426.52 

448. Prep wall for wallpaper 
633.33 SF 0.88 0.00 111.46 668.79 0/NA Avg. 0% (0.00) 668.79 

449. Wallpaper 
633.33 SF 3.04 42.18 393.50 2,361.00 0/7 yrs Avg. 0% (0.00) 2,361.00 
450. R&R Wallpaper border 
79.17 LF 4.66 7.08 75.22 451.23 0/7 yrs Avg. 0% (0.00) 451.23 

Totals: walls 930.72 9,361.38 56,193.18 2,400.62 53,792.56 

              ___________________________________________________________________________________________________________________-
              
# Celling 
              
Height: 8' 

446.67 SF Walls 192.46 SF Ceiling 
639.13 SF Walls & Ceiling 192.46 SF Floor 
21.38 SY Flooring 55.83 LF Floor Perimeter 
55.83 LF Ceil. Perimeter 
    
QUANTITY UNIT TAX CEILING 451. Content Manipulation charge - per hour 1.00 HR 32.54 0.00  O&P 6.50  RCV 39.04  AGE/LIFE 11/NA  COND. Avg.  DEP % 0%  DEPREC. (0.00)  ACV 39.04  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
452. Mask per square foot for drywall work  
192.46 SF  0.16  0.58  6.28  37.65  11/150 yrs  Avg.  7.33%  (2.30)  35.35  
453. Remove 5/8" drywall - hung, taped, ready for texture  
6.00 SF  0.33  0.00  0.40  2.38  11/150 yrs  Avg.  NA  (0.00)  2.38  
454. 5/8" drywall - hung, taped, ready for texture  
6.00 SF  1.47  0.18  1.80  10.80  11/150 yrs  Avg.  7.33%  (0.66)  10.14  
455. R&R Batt insulation - 6" - R19 - unfaced batt  
6.00 SF  1.01  0.19  1.26  7.51  0/150 yrs  Avg.  0%  (0.00)  7.51  
456. Drywall Installer / Finisher - per hour  
2.00 HR  54.72  0.00  21.88  131.32  0/150 yrs  Avg.  0%  (0.00)  131.32  
Additional labor hours added due the small nature of the repair  
457. Seal the surface area w/latex based stain blocker - one coat  
6.00 SF  0.39  0.02  0.46  2.82  11/15 yrs  Avg. 73.33%  (1.73)  1.09  
458. Paint the ceiling - one coat  
192.46 SF  0.44  1.27  17.20  103.15  11/15 yrs  Avg. 73.33%  (63.03)  40.12  
CEILING  
459. Content Manipulation charge - per hour  
1.00 HR  32.50  0.00  6.50  39.00  10/NA  Avg.  0%  (0.00)  39.00  
460. Mask per square foot for drywall work  
192.46 SF  0.21  0.58  8.20  49.20  0/150 yrs  Avg.  0%  (0.00)  49.20  
461. Remove 5/8" drywall - hung, taped, floated, ready for paint  
48.00 SF  0.43  0.00  4.12  24.76  10/150 yrs  Avg.  NA  (0.00)  24.76  
462. 5/8" drywall - hung, taped, floated, ready for paint  
48.00 SF  1.73  1.56  16.92  101.52  10/150 yrs  Avg.  6.67%  (5.64)  95.88  
463. Seal the surface area w/PVA primer - one coat  
48.00 SF  0.50  0.14  4.82  28.96  10/15 yrs  Avg. 66.67%  (16.09)  12.87  
464. Paint the ceiling - one coat  
192.46 SF  0.44  1.27  17.20  103.15  10/15 yrs  Avg. 66.67%  (57.30)  45.85  
WALLS  
465. Remove 1/2" drywall - hung, taped, floated, ready for paint  
64.00 SF  0.32  0.00  4.10  24.58  10/150 yrs  Avg.  NA  (0.00)  24.58  
466. 1/2" drywall - hung, taped, floated, ready for paint  
64.00 SF  1.58  1.73  20.56  123.41  10/150 yrs  Avg.  6.67%  (6.86)  116.55  
467. Drywall Installer / Finisher - per hour  
2.00 HR  60.00  0.00  24.00  144.00  10/150 yrs  Avg.  6.67%  (8.00)  136.00  
Labor hours added for trip charge and mobilization to make the needed repair.  
468. R&R Batt insulation - 4" - R13 - paper faced*  
64.00 SF  0.75  1.57  9.92  59.49  10/150 yrs  Avg.  6.67%  (2.45)  57.04  
469. Seal the surface area w/PVA primer - one coat  
64.00 SF  0.50  0.19  6.44  38.63  10/15 yrs  Avg. 66.67%  (21.46)  17.17  
2025-08-28-1618  8/31/2025  Page: 37  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
470. Paint the walls - one coat  
446.67 SF  0.44  2.95  39.90  239.38  10/15 yrs  Avg. 66.67%  (132.99)  106.39  
471. Paint baseboard - one coat  
50.83 LF  0.63  0.21  6.44  38.67  10/15 yrs  Avg. 66.67%  (21.49)  17.18  
472. Final cleaning - construction - Residential  
192.46 SF  0.23  3.19  8.86  56.32  10/NA  Avg.  0%  (0.00)  56.32  
CEILING  
473. Mask and cover light fixture  
1.00 EA  12.20  0.04  2.44  14.68  0/15 yrs  Avg.  0%  (0.00)  14.68  
474. Paint the ceiling - one coat  
192.46 SF  0.56  1.27  21.82  130.87  3/15 yrs  Avg.  20%  (21.81)  109.06  
no damage in this room--continuous ceiling from other rooms  
CEILING  
475. Content Manipulation charge - per hour  
1.00 HR  32.50  0.00  6.50  39.00  0/NA  Avg.  0%  (0.00)  39.00  
476. Mask per square foot for drywall work  
192.46 SF  0.21  0.58  8.20  49.20  0/150 yrs  Avg.  0%  (0.00)  49.20  
477. Drywall patch / small repair, ready for paint  
1.00 EA  90.52  0.16  18.14  108.82  0/150 yrs  Avg.  0%  (0.00)  108.82  
478. Drywall Installer / Finisher - per hour  
1.50 HR  80.21  0.00  24.06  144.38  0/150 yrs  Avg.  0%  (0.00)  144.38  
Additional labor hours added due the small nature of the repair  
479. Mask and cover light fixture  
2.00 EA  12.20  0.07  4.90  29.37  0/15 yrs  Avg.  0%  (0.00)  29.37  
480. Mask and prep for paint - plastic, paper, tape (per LF)  
16.00 LF  1.36  0.25  4.42  26.43  0/15 yrs  Avg.  0%  (0.00)  26.43  
cabinet protection  
481. Seal the surface area w/PVA primer - one coat  
4.00 SF  0.50  0.01  0.40  2.41  0/15 yrs  Avg.  0%  (0.00)  2.41  
482. Paint the ceiling - one coat  
192.46 SF  0.56  1.27  21.82  130.87  10/15 yrs  Avg. 66.67%  (72.70)  58.17  
483. Final cleaning - construction - Residential  
192.46 SF  0.22  3.05  8.46  53.85  0/NA  Avg.  0%  (0.00)  53.85  
CEILING  
484. Content Manipulation charge - per hour  
1.00 HR  32.50  0.00  6.50  39.00  6/NA  Avg.  0%  (0.00)  39.00  
485. Mask per square foot for drywall work  
192.46 SF  0.21  0.58  8.20  49.20  0/150 yrs  Avg.  0%  (0.00)  49.20  
486. Blown-in insulation - 8" depth - R19  
120.00 SF  0.61  2.81  15.20  91.21  0/150 yrs  Avg.  0%  (0.00)  91.21  
2025-08-28-1618  8/31/2025  Page: 38  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
487. Remove 5/8" drywall - hung, taped, floated, ready for paint  
120.00 SF  0.43  0.00  10.32  61.92  6/150 yrs  Avg.  NA  (0.00)  61.92  
488. 5/8" drywall - hung, taped, floated, ready for paint  
120.00 SF  1.73  3.89  42.30  253.79  0/150 yrs  Avg.  0%  (0.00)  253.79  
489. Mask and cover large light fixture  
1.00 EA  16.88  0.04  3.38  20.30  0/15 yrs  Avg.  0%  (0.00)  20.30  
490. Seal the surface area w/PVA primer - one coat  
120.00 SF  0.50  0.36  12.08  72.44  0/15 yrs  Avg.  0%  (0.00)  72.44  
491. Paint the ceiling - one coat  
192.46 SF  0.44  1.27  17.20  103.15  6/15 yrs  Avg.  40%  (34.38)  68.77  
CEILING  
492. Mask and cover light fixture  
3.00 EA  12.20  0.11  7.34  44.05  0/15 yrs  Avg.  0%  (0.00)  44.05  
493. Mask and prep for paint - plastic, paper, tape (per LF)  
20.00 LF  1.35  0.31  5.46  32.77  0/15 yrs  Avg.  0%  (0.00)  32.77  
cabinet protection  
494. Paint the ceiling - one coat  
192.46 SF  0.56  1.27  21.82  130.87  3/15 yrs  Avg.  20%  (21.81)  109.06  
no damage in this room--continuous ceiling from other rooms  
CEILING  
495. Content Manipulation charge - per hour  
1.00 HR  32.54  0.00  6.50  39.04  11/NA  Avg.  0%  (0.00)  39.04  
496. Mask per square foot for drywall work  
192.46 SF  0.16  0.58  6.28  37.65  11/150 yrs  Avg.  7.33%  (2.30)  35.35  
497. Remove 5/8" drywall - hung, taped, ready for texture  
96.00 SF  0.33  0.00  6.34  38.02  11/150 yrs  Avg.  NA  (0.00)  38.02  
498. 5/8" drywall - hung, taped, ready for texture  
96.00 SF  1.47  2.82  28.78  172.72  11/150 yrs  Avg.  7.33%  (10.56)  162.16  
499. Drywall Installer / Finisher - per hour  
2.00 HR  54.72  0.00  21.88  131.32  0/150 yrs  Avg.  0%  (0.00)  131.32  
additional labor for drywall  
500. Seal the surface area w/latex based stain blocker - one coat  
96.00 SF  0.39  0.35  7.56  45.35  11/15 yrs  Avg. 73.33%  (27.72)  17.63  
501. Paint the ceiling - one coat  
192.46 SF  0.44  1.27  17.20  103.15  11/15 yrs  Avg. 73.33%  (63.03)  40.12  
CEILING & WALLS  
CEILING  
502. Content Manipulation charge - per hour  
1.00 HR  32.50  0.00  6.50  39.00  0/NA  Avg.  0%  (0.00)  39.00  
503. Mask per square foot for drywall work  
192.46 SF  0.16  0.58  6.28  37.65  0/150 yrs  Avg.  0%  (0.00)  37.65  
2025-08-28-1618  8/31/2025  Page: 39  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
                
to protect when applying texture  
504. R&R 5/8" drywall - hung, taped, floated, ready for paint  
12.00 SF  1.86  0.40  4.54  27.26  0/150 yrs  Avg.  0%  (0.00)  27.26  
505. Remove Acoustic ceiling (popcorn) texture  
180.46 SF  0.38  0.00  13.72  82.29  10/150 yrs  Avg.  NA  (0.00)  82.29  
506. Acoustic ceiling (popcorn) texture  
192.46 SF  0.89  0.81  34.42  206.52  10/150 yrs  Avg.  6.67%  (11.47)  195.05  
507. Mask and prep for paint - plastic, paper, tape (per LF)  
55.83 LF  1.22  0.87  13.80  82.78  0/15 yrs  Avg.  0%  (0.00)  82.78  
for texture protection  
508. Seal the ceiling w/PVA primer - one coat  
192.46 SF  0.50  0.58  19.36  116.17  0/15 yrs  Avg.  0%  (0.00)  116.17  
509. Contents - move out then reset  
1.00 EA  41.49  0.00  8.30  49.79  39/NA  Avg.  0%  (0.00)  49.79  
510. Mask wall - plastic, paper, tape (per LF)  
55.83 LF  1.10  0.74  12.42  74.57  39/150 yrs  Avg.  26%  (16.16)  58.41  
511. Texture drywall - machine - knockdown  
25.00 SF  0.35  0.05  1.78  10.58  39/150 yrs  Avg.  26%  (2.29)  8.29  
512. Blown-in insulation - 12" depth - R30  
25.00 SF  0.79  0.90  4.14  24.79  0/150 yrs  Avg.  0%  (0.00)  24.79  

# WALLS
             
513. Contents - move out then reset  
1.00 EA  41.49  0.00  8.30  49.79  39/NA  Avg.  0%  (0.00)  49.79  
514. Texture drywall - machine - knockdown  
25.00 SF  0.35  0.05  1.78  10.58  39/150 yrs  Avg.  26%  (2.29)  8.29  
515. Seal/prime then paint the surface area (2 coats)*  
25.00 SF  0.64  0.23  3.24  19.47  1/15 yrs  Avg.  6.67%  (1.09)  18.38  
516. Material Only Texture drywall - light hand texture  
4.00 SF  0.08  0.02  0.06  0.40  10/150 yrs  Avg.  6.67%  (0.02)  0.38  
517. Painter - per hour  
2.00 HR  64.02  0.00  25.60  153.64  0/15 yrs  Avg.  0%  (0.00)  153.64 
 Additional labor hours added due the small nature of the repair  
518. Mask the floor per square foot - plastic and tape - 4 mil  
192.46 SF  0.22  0.58  8.58  51.50  0/15 yrs  Avg.  0%  (0.00)  51.50  
519. 5/8" acoustic drywall - hung, taped, ready for texture  
8.00 SF  4.42  1.12  7.30  43.78  14/150 yrs  Avg.  9.33%  (3.40)  40.38  
520. R&R Suspended ceiling system - 2' x 2'  
192.46 SF  5.13  28.87  203.24  1,219.43  0/150 yrs  Avg.  0%  (0.00)  1,219.43  
521. R&R Suspended ceiling system - 2' x 4'  
192.46 SF  4.47  23.10  176.68  1,060.08  0/150 yrs  Avg.  0%  (0.00)  1,060.08  
2025-08-28-1618  8/31/2025  Page: 40  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
522. Suspended ceiling tile - Detach & reset 
192.46 SF 0.74 0.00 28.48 170.90 0/NA Avg. 0% (0.00) 170.90 
523. Acoustical Treatments Installer - per hour 
0.00 HR 89.51 0.00 0.00 0.00 0/NA Avg. 0% (0.00) 0.00 
The above line item is an additional labor allowance to 
524. R&R Fluorescent - acoustic grid fixture, 2' x 2' 
1.00 EA 204.58 4.74 41.86 251.18 0/20 yrs Avg. 0% (0.00) 251.18 
525. R&R Fluorescent - acoustic grid fixture - four tube, 2'x 4' 
1.00 EA 273.98 5.64 55.92 335.54 0/20 yrs Avg. 0% (0.00) 335.54 
526. Floor protection - self-adhesive plastic film 
1.00 SF 0.83 0.01 0.16 1.00 0/15 yrs Avg. 0% (0.00) 1.00 
527. R&R 1/2" drywall - hung, taped, ready for texture 
48.11 SF 2.87 2.16 28.04 168.28 0/150 yrs Avg. 0% (0.00) 168.28 Note: Includes: texture compound, texture machine, and installation labor. Quality: includes orange peel or similar machine applied texture. 
528. Scrape the ceiling & prep for paint 

192.46 SF 0.88 0.12 33.90 203.38 0/15 yrs Avg. 0% (0.00) 203.38 
529. Texture drywall - heavy hand texture 
192.46 SF 1.40 3.00 54.48 326.92 0/150 yrs Avg. 0% (0.00) 326.92 
530. Cleaning Technician - per hour 
1.00 HR 54.18 3.90 10.84 68.92 0/NA Avg. 0% (0.00) 68.92 
ELECTRICAL 
531. R&R Smoke detector - Standard grade 

1.00 EA 51.76 1.07 10.56 63.39 0/10 yrs Avg. 0% (0.00) 63.39 
item was damaged 
532. Seal stud wall for odor control 
446.67 SF 0.75 4.56 67.92 407.48 0/15 yrs Avg. 0% (0.00) 407.48 
533. Seal floor or ceiling joist system 


192.46 SF 1.07 2.54 41.68 250.15 0/15 yrs Avg. 0% (0.00) 250.15 
Totals: celling 124.63 1,533.14 9,208.78 631.03 8,577.75 

# Doors 

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
BACK SHED DOOR 
534. R&R Exterior door slab - metal - insulated - flush or panel 
1.00 EA 219.19 6.90 45.22 271.31 0/100 yrs Avg. 0% (0.00) 271.31 
rear door was damaged 
535. Detach & Reset Door lockset - exterior - Standard grade 

1.00 EA 18.43 0.00 3.68 22.11 0/20 yrs Avg. 0% (0.00) 22.11 
536. Paint door slab only - 2 coats (per side) 
2.00 EA 30.58 0.79 12.40 74.35 0/15 yrs Avg. 0% (0.00) 74.35 
537. R&R Interior door - birch - pre-hung unit 

2.00 EA 378.00 34.73 158.14 948.87 0/100 yrs Avg. 0% (0.00) 948.87 
538. Door knob/lockset - Detach & reset 
2.00 EA 28.68 0.00 11.48 68.84 0/NA Avg. 0% (0.00) 68.84 
539. Paint door/window trim & jamb - 2 coats (per side) 
1.00 EA 42.84 0.37 8.64 51.85 0/15 yrs Avg. 0% (0.00) 51.85 
540. Stain & finish door slab only (per side) 
2.00 EA 79.91 1.40 32.24 193.46 0/15 yrs Avg. 0% (0.00) 193.46 
541. R&R Interior door - birch - slab only 
1.00 EA 106.36 2.59 21.80 130.75 24/100 yrs Avg. 24% (24.60) 106.15 
542. Paint door slab only - 2 coats (per side) 
1.00 EA 24.75 0.38 5.04 30.17 10/15 yrs Avg. 66.67% (16.75) 13.42 
543. Door lockset - Detach & reset* 
1.00 EA 19.68 0.00 3.94 23.62 0/NA Avg. 0% (0.00) 23.62 
544. R&R Storm door assembly - Standard grade 
1.00 EA 216.80 6.90 44.74 268.44 0/40 yrs Avg. 0% (0.00) 268.44 Includes: Screen door, frame, lockset, threshold and installation labor. Labor cost to remove a storm door unit and to discard in a job-site waste 
receptacle. Quality: 1" aluminum screen door, self storing, mill finish or white, reversible universal hinge. 
545. R&R Steel door frame - 3' opening 
1.00 EA 437.17 21.00 91.64 549.81 0/100 yrs Avg. 0% (0.00) 549.81 
546. R&R Steel door, 3' x 7' 
1.00 EA 561.85 28.67 118.10 708.62 0/100 yrs Avg. 0% (0.00) 708.62 
547. R&R Wood door - oak face, solid core 
1.00 EA 308.37 13.45 64.38 386.20 0/100 yrs Avg. 0% (0.00) 386.20 
548. Door Installer/Finish Carpenter - per hour 
1.00 HR 83.34 0.00 16.66 100.00 0/NA Avg. 0% (0.00) 100.00 
The above line item represents an allowance for additional labor required to mortise the door for hinges and cut the holes for the lockset and deadbolt. 
549. R&R Door hinges (set of 3) 
1.00 EA 69.17 0.80 14.00 83.97 0/20 yrs Avg. 0% (0.00) 83.97 
550. R&R Lockset - passage - Medium duty - Commercial grade 
1.00 EA 113.40 4.39 23.56 141.35 0/20 yrs Avg. 0% (0.00) 141.35 
551. R&R Lockset - keyed - Medium duty - Commercial grade 
1.00 EA 162.06 7.31 33.88 203.25 0/20 yrs Avg. 0% (0.00) 203.25 
552. R&R Door closer - Heavy duty - Commercial grade 


1.00 EA 368.93 19.19 77.62 465.74 0/20 yrs Avg. 0% (0.00) 465.74 
QUANTITY  UNIT  TAX  O&P  RCV  AGE/LIFE  COND.  DEP %  DEPREC.  ACV  
553. R&R Deadbolt - Commercial grade  
1.00 EA  116.73  4.81  24.30  145.84  0/20 yrs  Avg.  0%  (0.00)  145.84  
DOOR  
554. R&R Exterior door - metal - insulated - Standard grade  
1.00 EA  294.57  11.18  61.16  366.91  0/100 yrs  Avg.  0%  (0.00)  366.91  
555. Prime & paint door slab only - exterior (per side)  
2.00 EA  43.83  1.59  17.86  107.11  0/15 yrs  Avg.  0%  (0.00)  107.11  
556. Door lockset & deadbolt - exterior - Detach & reset  
1.00 EA  28.47  0.00  5.70  34.17  0/NA  Avg.  0%  (0.00)  34.17  
557. R&R Exterior door - metal - insulated / wood - High grade  
1.00 EA  673.50  32.92  141.28  847.70  0/100 yrs  Avg.  0%  (0.00)  847.70  
558. R&R Casing - 2 1/4"  
18.00 LF  3.35  1.70  12.40  74.40  0/150 yrs  Avg.  0%  (0.00)  74.40  
The above line item is allowance for the casing on the interior of the door unit which is not included in the original door line item.  
559. R&R Door lockset & deadbolt - exterior - High grade  
1.00 EA  159.67  6.48  33.24  199.39  0/20 yrs  Avg.  0%  (0.00)  199.39  
560. R&R Interior door unit  
1.00 EA  359.74  16.27  75.22  451.23  0/100 yrs  Avg.  0%  (0.00)  451.23  
561. Door knob - interior  
1.00 EA  47.81  1.36  9.84  59.01  0/20 yrs  Avg.  0%  (0.00)  59.01  
562. R&R Interior door unit - mobile home - Standard grade  
1.00 EA  214.23  7.54  44.36  266.13  0/100 yrs  Avg.  0%  (0.00)  266.13  
563. R&R Door knob - interior - Standard grade  
1.00 EA  55.76  0.93  11.34  68.03  0/20 yrs  Avg.  0%  (0.00)  68.03  
564. R&R Screen door - metal - 30" - 36" full scrn - Standard grade  
1.00 EA  113.90  3.37  23.46  140.73  0/40 yrs  Avg.  0%  (0.00)  140.73  
SHUTTERS  
565. Shutters - Detach & reset  
1.00 EA  24.16  0.00  4.84  29.00  0/NA  Avg.  0%  (0.00)  29.00  
566. R&R Security shutter - accordion or folding type  
0.00 SF  44.47  0.00  0.00  0.00  0/40 yrs  Avg.  0%  (0.00)  0.00  
567. Motorization for security shutters  
0.00 SF  9.66  0.00  0.00  0.00  0/40 yrs  Avg.  0%  (0.00)  0.00  
568. R&R Security/storm shutter - roll-up type  
0.00 SF  58.97  0.00  0.00  0.00  0/40 yrs  Avg.  0%  (0.00)  0.00  
Totals: Doors  237.02  1,252.16  7,512.36  41.35  7,471.01  

384.00 SF Walls 144.00 SF Ceiling 
528.00 SF Walls & Ceiling 144.00 SF Floor

water - house 
                                
12' 
16.00 SY Flooring 48.00 LF Floor Perimeter 
48.00 LF Ceil. Perimeter 

QUANTITY  UNIT  TAX  O&P  RCV  AGE/LIFE  COND.  DEP %  DEPREC.  ACV  
569. Structural Dry-Out per Method #1 of FEMA memo W-13025a* 144.00 SF 0.85 7.34 0.00  129.74  0/NA  Avg.  0%  (0.00)  129.74  
Totals: water - house  7.34  0.00  129.74  0.00  129.74  

384.00 SF Walls 144.00 SF Ceiling 
6'5' 8" 5' 4" 12' 8"
528.00 SF Walls & Ceiling 144.00 SF Floor
                                
                                
                                
# Windows 
 

16.00 SY Flooring 48.00 LF Floor Perimeter 
48.00 LF Ceil. Perimeter 
2' 8"  6' 11"  
QUANTITY  UNIT  TAX  O&P  RCV  AGE/LIFE  COND.  DEP %  DEPREC.  ACV  
WINDOWS  
570. R&R Wrap wood window frame & trim with aluminum sheet - Small  
1.00 EA  116.27  1.60  23.58  141.45  0/50 yrs  Avg.  0%  (0.00)  141.45  
WINDOWS  
571. R&R Block - glass - 4"x 8"x 8"  
16.00 SF  30.54  14.51  100.62  603.77  0/100 yrs  Avg.  0%  (0.00)  603.77  
glass block window damaged  
SCREENS  
572. R&R Window screen, 1 - 9 SF  
2.00 EA  44.20  4.47  18.58  111.45  0/30 yrs  Avg.  0%  (0.00)  111.45  
WINDOW TRIM  
573. R&R Wrap wood window frame & trim with aluminum sheet  
7.00 EA  174.23  16.74  247.26  1,483.61  0/50 yrs  Avg.  0%  (0.00)  1,483.61  
damaged by hail  
WINDOW TRIM  
574. Content Manipulation charge - per hour  
1.00 HR  32.50  0.00  6.50  39.00  0/NA  Avg.  0%  (0.00)  39.00  
575. Mask per square foot for drywall work  
528.00 SF  0.16  1.58  17.22  103.28  0/150 yrs  Avg.  0%  (0.00)  103.28  
to protect when applying texture  
576. R&R 5/8" drywall - hung, taped, floated, ready for paint  
4.00 SF  1.86  0.13  1.50  9.07  0/150 yrs  Avg.  0%  (0.00)  9.07  
2025-08-28-1618  8/31/2025  Page: 44  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
577. Batt insulation - 6" - R19 - unfaced batt 
4.00 SF 0.76 0.13 0.62 3.79 10/150 yrs Avg. 6.67% (0.21) 3.58 
578. Remove Acoustic ceiling (popcorn) texture 
140.00 SF 0.38 0.00 10.64 63.84 0/150 yrs Avg. NA (0.00) 63.84 
579. Seal the ceiling w/latex based stain blocker - one coat 
144.00 SF 0.52 0.60 15.10 90.58 10/15 yrs Avg. 66.67% (50.32) 40.26 
580. Acoustic ceiling (popcorn) texture 
144.00 SF 0.64 0.60 18.56 111.32 0/150 yrs Avg. 0% (0.00) 111.32 
581. Mask and cover light fixture 
1.00 EA 11.59 0.04 2.32 13.95 0/15 yrs Avg. 0% (0.00) 13.95 
582. Final cleaning - construction - Residential 
144.00 SF 0.22 2.28 6.34 40.30 0/NA Avg. 0% (0.00) 40.30 
583. Drywall Installer / Finisher - per hour 
0.00 HR 80.00 0.00 0.00 0.00 0/150 yrs Avg. 0% (0.00) 0.00 
Additional labor hours added due the small nature of the repair 
584. Painter - per hour 
0.00 HR 63.50 0.00 0.00 0.00 0/15 yrs Avg. 0% (0.00) 0.00 
Labor hours added for trip charge and mobilization to make the needed repair. 
585. Insulation Installer - per hour 
0.00 HR 42.50 0.00 0.00 0.00 0/NA Avg. 0% (0.00) 0.00 
Additional labor hours added due the small nature of the repair 
586. Reglaze window, 1 - 9 sf 
1.00 EA 68.31 2.37 14.14 84.82 0/18 yrs Avg. 0% (0.00) 84.82 
587. Add on for grid (double or triple glazed windows) 
9.00 SF 2.35 1.27 4.50 26.92 13/30 yrs Avg. 43.33% (9.72) 17.20 
588. Add on for "Low E" glass 
9.00 SF 1.71 0.92 3.26 19.57 13/20 yrs Avg. 65% (10.60) 8.97 
589. R&R Roof window step flashing kit 
1.00 EA 134.81 6.11 28.18 169.10 0/18 yrs Avg. 0% (0.00) 169.10 
590. R&R Roof window step flashing kit - Large 
1.00 EA 159.21 7.14 33.26 199.61 0/18 yrs Avg. 0% (0.00) 199.61 
591. R&R Skylight flashing kit - dome 
1.00 EA 111.58 5.23 23.36 140.17 0/15 yrs Avg. 0% (0.00) 140.17 
592. R&R Vinyl window - double hung, 13-19 sf - High grade 
1.00 EA 713.06 35.41 149.68 898.15 0/30 yrs Avg. 0% (0.00) 898.15 
Note: Includes: vinyl frame, double hung window, screen and installation labor. Quality: 13 to 19 SF vertical sliding window with heavy duty (reinforced) frame and sash, high grade hardware, (pivots, latches) and double glazing. Width of glazing unit is 13/16" to 1". 
593. R&R Casing - 2 1/4" 
16.00 LF 3.35 1.51 11.02 66.13 0/150 yrs Avg. 0% (0.00) 66.13 
594. Paint casing - two coats 
20.00 LF 2.01 0.24 8.08 48.52 0/15 yrs Avg. 0% (0.00) 48.52 
2025-08-28-1618 8/31/2025 Page: 45 
QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
WINDOW 
595. R&R Vinyl window, single hung, 9-12 sf 
2.00 EA 208.11 15.67 86.38 518.27 16/30 yrs Avg. 53.33% (206.25) 312.02 
596. Add on for "Low E" glass 
25.00 SF 1.71 2.57 9.08 54.40 16/20 yrs Avg. 80% (36.26) 18.14 
597. Flashing - Sill flashing - moldable tape 
25.00 LF 6.69 4.11 34.28 205.64 16/30 yrs Avg. 53.33% (91.39) 114.25 
598. Additional charge for a retrofit window, 3-11 sf 
2.00 EA 69.63 1.23 28.10 168.59 16/18 yrs Avg. 88.89% (124.88) 43.71 
599. Add on for grid (double or triple glazed windows) 
25.00 SF 2.35 3.53 12.46 74.74 16/30 yrs Avg. 53.33% (33.21) 41.53 
600. R&R Aluminum window, single hung 20-28 sf (2 pane w/thermal) 
1.00 EA 593.54 27.33 124.16 745.03 0/18 yrs Avg. 0% (0.00) 745.03 
601. R&R Window stool & apron 
4.00 LF 9.87 1.04 8.10 48.62 0/150 yrs Avg. 0% (0.00) 48.62 

602. Seal & paint window sill 
4.00 LF 3.50 0.07 2.82 16.89 0/15 yrs Avg. 0% (0.00) 16.89 
Totals: Windows 158.43 1,049.70 6,300.58 562.84 5,737.74 garden Height: 8' 
388.00 SF Walls 147.00 SF Ceiling 
535.00 SF Walls & Ceiling 147.00 SF Floor 
16.33 SY Flooring 48.50 LF Floor Perimeter 
48.50 LF Ceil. Perimeter 

QUANTITY UNIT TAX O&P TREE 603. Tree - removal and disposal - per hour including equipment 4.00 HR 85.70 0.00 68.56 2 men 2 hours to remove the branches from the roof and building 604. Tree - removal and disposal - per hour including equipment 4.00 HR 85.70 0.00 68.56 for tree branch removal off the premises--2 men 2 hours DECKING 605. 2" x 4" x 12' #2 treated pine (material only) 1.00 EA 7.71 0.46 1.64  RCV 411.36 411.36 9.81  AGE/LIFE 0/NA 0/NA 0/150 yrs  COND. Avg. Avg. Avg.  DEP % NA NA 0%  DEPREC. (0.00) (0.00) (0.00)  ACV 411.36 411.36 9.81  
2025-08-28-1618  8/31/2025  Page: 46  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
railing damaged by hail  

606. R&R Deck hand rail/guard rail - Labor only  
12.00 LF  21.62  0.17  51.92  311.53  0/20 yrs  Avg.  0%  (0.00)  311.53  
FASCIA  

607. R&R Fascia - metal - 8"  
12.00 LF  5.07  1.47  12.48  74.79  15/50 yrs  Avg.  30%  (17.50)  57.29  
Front gable metal  
FASCIA  

608. R&R Fascia - metal - 8"  
6.00 LF  4.81  0.73  5.90  35.49  0/50 yrs  Avg.  0%  (0.00)  35.49  
fascia damaged  
FASCIA  

609. R&R Fascia - metal - 8"  
12.00 LF  5.07  1.47  12.48  74.79  15/50 yrs  Avg.  30%  (17.50)  57.29 
 Rear gable metal  

610. Soffit & Fascia Installer - per hour  
3.00 HR  74.95  0.00  44.98  269.83  15/NA  Avg.  0%  (0.00)  269.83  
Labor hours added for trip charge and mobilization to make the needed repair.  
FASCIA  

611. R&R Fascia - metal - 8"  
12.00 LF  5.07  1.47  12.48  74.79  15/50 yrs  Avg.  30%  (17.50)  57.29  
Right gable metal  
612. R&R Post - wood - 4" x 4" treated lumber  
6.00 EA  66.29  8.04  81.16  486.94  0/12 yrs  Avg.  0%  (0.00)  486.94  
613. Wood fence 5' - 6' high - Detach & reset - per 8' section  
6.00 EA  72.43  0.80  87.08  522.46  0/NA  Avg.  0%  (0.00)  522.46  
614. Detach & Reset Exterior light fixture - Standard grade  
2.00 EA  69.57  0.00  27.82  166.96  0/20 yrs  Avg.  0%  (0.00)  166.96  
remove and reset to assist with siding install  

# MAILBOX  
615. R&R Rural mailbox  
1.00 EA  53.70  1.77  11.10  66.57  20/20 yrs  Avg.  100%  [M]  <47.97>  18.60  
damaged by hail  
616. Asphalt cutting - driveway (per LF per inch of saw depth)  
48.50 LF  5.55  0.00  53.84  323.02  0/18 yrs  Avg.  0%  (0.00)  323.02  
617. R&R Concrete slab on grade - 4" - finished in place  
147.00 SF  11.14  22.93  332.10  1,992.61  0/50 yrs  Avg.  0%  (0.00)  1,992.61  
Includes: Concrete, forms, and installation labor.  

# FENCE  
618. R&R Wood fence slat 3' - 4' high - treated  
10.00 EA  4.42  1.06  9.06  54.32  0/12 yrs  Avg.  0%  (0.00)  54.32  
10 pieces damaged  
2025-08-28-1618  8/31/2025  Page: 47  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
619. R&R Wood gate 5'- 6' high - treated  
0.00 LF  38.73  0.00  0.00  0.00  0/12 yrs  Avg.  0%  (0.00)  0.00  
620. R&R Wood fence 5'- 6' high - treated  
0.00 LF  24.19  0.00  0.00  0.00  0/12 yrs  Avg.  0%  (0.00)  0.00  
621. R&R Basket weave fence - 4' to 6' high  
0.00 LF  56.20  0.00  0.00  0.00  0/12 yrs  Avg.  0%  (0.00)  0.00  
622. R&R Basket weave fence gate - 4' to 6' high  
0.00 LF  80.57  0.00  0.00  0.00  0/12 yrs  Avg.  0%  (0.00)  0.00  
623. R&R Wood fence - B on B - 5'- 6' high - treated - High grade  
0.00 LF  45.59  0.00  0.00  0.00  0/12 yrs  Avg.  0%  (0.00)  0.00  
624. R&R Wood fence 5'- 6' high - cedar or equal  
0.00 LF  48.73  0.00  0.00  0.00  0/12 yrs  Avg.  0%  (0.00)  0.00  
625. R&R Wood gate 5'- 6' high - cedar or equal  
0.00 LF  69.77  0.00  0.00  0.00  0/12 yrs  Avg.  0%  (0.00)  0.00  
626. R&R Post - wood - 4" x 4" fence grade cedar or equal  
1.00 EA  96.03  3.12  19.82  118.97  0/12 yrs  Avg.  0%  (0.00)  118.97  
Additional post for gate opening.  
627. R&R Post & rail fence - Dowelled cedar - 3 rail  
0.00 LF  25.22  0.00  0.00  0.00  0/12 yrs  Avg.  0%  (0.00)  0.00  
628. R&R Cedar post - Dowelled - corner/end/line - 3 hole  
1.00 EA  82.30  2.30  16.92  101.52  0/12 yrs  Avg.  0%  (0.00)  101.52  
629. R&R Wood fence rail - Dowelled cedar  
1.00 EA  38.25  1.51  7.96  47.72  0/12 yrs  Avg.  0%  (0.00)  47.72  
630. R&R Chain link fence w/posts & top rail - 4' high - 11 gauge  
0.00 LF  21.31  0.00  0.00  0.00  0/30 yrs  Avg.  0%  (0.00)  0.00  
631. R&R Chain link fence gate - 4' high - swinging  
0.00 LF  54.14  0.00  0.00  0.00  0/30 yrs  Avg.  0%  (0.00)  0.00  
632. R&R Chain link fence gate - 4' high - rolling  
0.00 LF  118.52  0.00  0.00  0.00  0/30 yrs  Avg.  0%  (0.00)  0.00  
633. Chain link fence fabric - Detach & reset  
0.00 SF  0.86  0.00  0.00  0.00  0/NA  Avg.  0%  (0.00)  0.00  
634. Chain link fence gate - rolling - Detach & reset  
0.00 LF  16.61  0.00  0.00  0.00  0/NA  Avg.  0%  (0.00)  0.00  
635. Chain link fence gate - swinging - Detach & reset  
0.00 LF  18.17  0.00  0.00  0.00  0/NA  Avg.  0%  (0.00)  0.00  
636. R&R Chain-link fence - top rail  
0.00 LF  4.85  0.00  0.00  0.00  0/30 yrs  Avg.  0%  (0.00)  0.00  
637. R&R Post - 2 3/8" diameter metal - 4' high fence  
1.00 EA  85.79  2.51  17.66  105.96  0/30 yrs  Avg.  0%  (0.00)  105.96  
638. R&R Picket fence, 3' to 4' high  
0.00 LF  34.18  0.00  0.00  0.00  0/12 yrs  Avg.  0%  (0.00)  0.00  
2025-08-28-1618  8/31/2025  Page: 48  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
639. R&R Picket fence gate - 3' to 4' high 
0.00 LF 61.01 0.00 0.00 0.00 0/12 yrs Avg. 0% (0.00) 0.00 
FENCE POST CAPS 
640. R&R Fence/deck post cap - 6" x 6" - copper 
1.00 EA 33.12 1.37 6.92 41.41 0/150 yrs Avg. 0% (0.00) 41.41 

# FENCE 
641. R&R Vinyl (PVC) fence, 5'- 6' high - full slat 
24.00 LF 41.32 35.83 205.48 1,232.99 0/150 yrs Avg. 0% (0.00) 1,232.99 
4 sections @ 6 feet 
642. R&R Vinyl (PVC) fence post cap only - 5" x 5" 
3.00 EA 9.04 0.70 5.56 33.38 0/150 yrs Avg. 0% (0.00) 33.38 
643. R&R Vinyl (PVC) fence, 5'- 6' high - w/lattice 
0.00 LF 64.60 0.00 0.00 0.00 0/150 yrs Avg. 0% (0.00) 0.00 
644. R&R Vinyl (PVC) fence gate, 5'- 6' high - w/lattice 
0.00 LF 180.94 0.00 0.00 0.00 0/150 yrs Avg. 0% (0.00) 0.00 
645. R&R Post - 2 3/8" diameter metal - terminal 
1.00 EA 98.02 3.24 20.24 121.50 0/30 yrs Avg. 0% (0.00) 121.50 
646. R&R Wood fence rail - 2" x 4" x 8' - treated 
1.00 EA 20.79 0.47 4.26 25.52 0/12 yrs Avg. 0% (0.00) 25.52 
647. R&R Wood fence slat 5' - 6' high - treated 
1.00 EA 7.32 0.23 1.52 9.07 0/12 yrs Avg. 0% (0.00) 9.07 
648. Wood fence slat - Detach & reset 
1.00 EA 3.40 0.00 0.68 4.08 0/NA Avg. 0% (0.00) 4.08 
649. Wood or vinyl gate - Detach & reset 



0.00 LF 20.60 0.00 0.00 0.00 0/NA Avg. 0% (0.00) 0.00 
650. Tree - removal and disposal - per hour including equipment 
13.00 HR 72.82 0.00 189.34 1,136.00 0/NA Avg. NA (0.00) 1,136.00 multiple trees 

Totals: garden 91.65 1,377.52 8,264.75 100.47 8,164.28 

___________________________________________________________________________________________________________________________________
                      
# Deck 

Height: 3' 
40.00 LF Floor Perimeter 

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
651. R&R Concrete slab on grade - 4" - finished in place 
0.00 SF 6.73 0.00 0.00 0.00 0/50 yrs Avg. 0% (0.00) 0.00 
652. 2" x 10" x 8' #2 treated pine (material only) 
1.00 EA 15.26 0.92 3.24 19.42 0/150 yrs Avg. 0% (0.00) 19.42 
653. 2" x 2" x 8' #2 treated pine (material only) 
4.00 EA 4.63 1.11 3.92 23.55 0/150 yrs Avg. 0% (0.00) 23.55 
654. 4" x 4" x 8' - treated lumber post - material only 
2.00 EA 13.42 1.61 5.68 34.13 0/150 yrs Avg. 0% (0.00) 34.13 
655. 2" x 4" x 8' #2 treated pine (material only) 

2.00 EA 6.29 0.75 2.68 16.01 0/150 yrs Avg. 0% (0.00) 16.01 
656. R&R Stair stringer - Labor only 
8.00 LF 6.75 0.00 10.80 64.80 0/150 yrs Avg. 0% (0.00) 64.80 
657. 5/4" x 6" x 8' #1 treated pine (material only) 
5.00 EA 9.98 2.99 10.58 63.47 0/25 yrs Avg. 0% (0.00) 63.47 
658. Stain/finish deck 
23.05 SF 1.27 0.43 5.94 35.64 0/15 yrs Avg. 0% (0.00) 35.64 
659. Stain/finish deck handrail 
7.33 LF 9.52 0.83 14.12 84.73 0/15 yrs Avg. 0% (0.00) 84.73 
660. R&R Deck hand rail/guard rail - Labor only 
8.00 LF 26.59 0.15 42.60 255.47 0/20 yrs Avg. 0% (0.00) 255.47 

Totals: Deck1 8.79 99.56 597.22 0.00 597.22 

# General Jobs 

384.00 SF Walls 144.00 SF Ceiling 
528.00 SF Walls & Ceiling 144.00 SF Floor 
16.00 SY Flooring 48.00 LF Floor Perimeter 
48.00 LF Ceil. Perimeter 
QUANTITY UNIT TAX O&P RCV AGE/LIFE 
                                                                                             
661. Single axle dump truck - per load - including dump fees 1.00 EA 203.13 0.00 40.62 243.75 0/NA debris left from remaining tear out, carpet, repairs and cabinets 662. Job-site moving/storage container - 20' long - per month* 1.00 MO 185.01 13.32 37.00 235.33 0/NA allowance to store contents while repairs are being done to main level 663. Job-site cargo container - pick up/del. (each way) 16'-40' 1.00 EA 112.00 0.00 22.40 134.40 0/NA 664. General Laborer - per hour 2.00 HR 28.10 0.00 11.24 67.44 0/NA Additional contents allowance to carefully pack contents into storage container  COND. Avg. Avg. Avg. Avg.  DEP % DEPREC. NA (0.00) 0% (0.00) 0% (0.00) 0% (0.00)  ACV 243.75 235.33 134.40 67.44  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
665. Temporary toilet (per month)  
2.00 MO  102.19  0.00  40.88  245.26  0/NA  Avg.  0%  (0.00)  245.26  
666. Haul debris - per pickup truck load - including dump fees  
1.00 EA  113.37  0.00  22.68  136.05  0/NA  Avg.  NA  (0.00)  136.05  
667. General clean - up  
16.00 HR  10.90  10.47  0.00  184.87  0/NA  Avg.  0%  (0.00)  184.87  Remove tree debris off of roof and well head  
668. R&R Patio/pool Enclosure - Rescreen  
40.00 SF  1.47  0.98  11.96  71.74  0/40 yrs  Avg.  0%  (0.00)  71.74  to repair screens that were damaged  
669. Awning & Patio Cover Installer - per hour  
2.00 HR  67.74  0.00  27.10  162.58  0/NA  Avg.  0%  (0.00)  162.58  Additional labor hours added due the small nature of the repair  
670. Contents - move out then reset  
1.00 EA  75.63  0.00  15.12  90.75  0/NA  Avg.  0%  (0.00)  90.75  
671. R&R Heat/AC register - Mechanically attached  
1.00 EA  30.67  0.79  6.28  37.74  0/25 yrs  Avg.  0%  (0.00)  37.74  
672. R&R 110 volt copper wiring run, box and outlet  
1.00 EA  90.11  1.28  18.28  109.67  0/100 yrs  Avg.  0%  (0.00)  109.67  
673. R&R 110 volt copper wiring run, box and switch  
1.00 EA  90.81  1.33  18.42  110.56  0/100 yrs  Avg.  0%  (0.00)  110.56  
674. R&R 110 volt copper wiring run and box - rough-in only  
1.00 EA  72.47  1.14  14.72  88.33  0/100 yrs  Avg.  0%  (0.00)  88.33  
675. R&R Ceiling fan & light  
1.00 EA  391.32  9.07  80.08  480.47  0/20 yrs  Avg.  0%  (0.00)  480.47  
676. Apply anti-microbial agent to the walls and ceiling  
528.00 SF  0.36  15.72  38.40  244.20  0/NA  Avg.  0%  (0.00)  244.20  
677. R&R Batt insulation - 6" - R19 - unfaced batt  
144.00 SF  1.98  8.38  58.70  352.20  0/150 yrs  Avg.  0%  (0.00)  352.20  
678. R&R 5/8" drywall - hung, taped, floated, ready for paint  
144.00 SF  3.35  7.52  97.98  587.90  0/150 yrs  Avg.  0%  (0.00)  587.90  
679. R&R Batt insulation - 4" - R11- unfaced batt  
384.00 SF  1.27  10.83  99.70  598.21  0/150 yrs  Avg.  0%  (0.00)  598.21  
680. R&R 1/2" drywall - hung, taped, floated, ready for paint  
384.00 SF  3.21  17.51  250.02  1,500.17  0/150 yrs  Avg.  0%  (0.00)  1,500.17  
681. R&R Interior door - Colonist - pre-hung unit  
1.00 EA  359.74  16.27  75.22  451.23  0/100 yrs  Avg.  0%  (0.00)  451.23  
682. Paint door slab only - 2 coats (per side)  
1.00 EA  50.67  0.59  10.26  61.52  0/15 yrs  Avg.  0%  (0.00)  61.52  
683. Paint door/window trim & jamb - 1 coat (per side)  
1.00 EA  28.98  0.27  5.86  35.11  0/15 yrs  Avg.  0%  (0.00)  35.11  
2025-08-28-1618  8/31/2025  Page: 51  

QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
684. R&R Door knob - interior  
1.00 EA  62.99  1.36  12.88  77.23  0/20 yrs  Avg.  0%  (0.00)  77.23  
685. R&R Baseboard - 3 1/4"  
48.00 LF  4.88  6.13  48.06  288.43  0/150 yrs  Avg.  0%  (0.00)  288.43  
686. R&R Crown molding - 4 1/4"  
48.00 LF  6.92  8.70  68.18  409.04  0/150 yrs  Avg.  0%  (0.00)  409.04  
687. R&R Chair rail - 2 1/2"  
48.00 LF  4.26  5.33  41.96  251.77  0/150 yrs  Avg.  0%  (0.00)  251.77  
688. R&R Window stool & apron  
3.50 LF  9.87  0.91  7.08  42.54  0/150 yrs  Avg.  0%  (0.00)  42.54  
689. Seal/prime (1 coat) then paint (2 coats) the walls and ceiling  
528.00 SF  1.74  11.09  185.96  1,115.77  0/15 yrs  Avg.  0%  (0.00)  1,115.77  
690. Seal (1 coat) & paint (1 coat) baseboard  
48.00 LF  2.05  0.43  19.76  118.59  0/15 yrs  Avg.  0%  (0.00)  118.59  
691. Seal (1 coat) & paint (1 coat) crown molding  
48.00 LF  2.06  0.52  19.88  119.28  0/15 yrs  Avg.  0%  (0.00)  119.28  
692. Seal (1 coat) & paint (1 coat) chair rail  
48.00 LF  1.98  0.49  19.10  114.63  0/15 yrs  Avg.  0%  (0.00)  114.63  
693. Seal & paint window sill  
3.50 LF  3.50  0.07  2.48  14.80  0/15 yrs  Avg.  0%  (0.00)  14.80  
694. R&R Carpet pad - High grade  
144.00 SF  1.02  6.39  30.66  183.93  0/10 yrs  Avg.  0%  (0.00)  183.93  
1,199. Remove Carpet - High grade  
144.00 SF  0.33  0.00  9.50  57.02  0/10 yrs  Avg.  NA  (0.00)  57.02  
695. Carpet - High grade  
165.60 SF  5.85  48.79  203.52  1,221.07  0/10 yrs  Avg.  0%  (0.00)  1,221.07  
15 % waste added for Carpet - High grade.  
Totals: general jobs  205.68  1,671.94  10,243.58  0.00  10,243.58  

                    _________________________________________________________________________________________
                    
# Garage 
                    
12' 
384.00 SF Walls 144.00 SF Ceiling 
528.00 SF Walls & Ceiling 144.00 SF Floor
Garage 
16.00 SY Flooring 48.00 LF Floor Perimeter 

48.00 LF Ceil. Perimeter 
3' 3" 
8' 
9" 3' 7" 

# GARAGE DOOR 
QUANTITY UNIT TAX O&P RCV AGE/LIFE COND. DEP % DEPREC. ACV 
                    
696. R&R Overhead door & hardware - 8' x 7' - Standard grade  
1.00 EA  763.38  23.52  157.38  944.28  1/35 yrs  Avg.  NA  (0.00)  944.28  
697. Overhead door weather stop  
22.00 LF  3.88  1.56  17.40  104.32  0/35 yrs  Avg.  NA  (0.00)  104.32  
698. Clean door / window opening (per side)  
1.00 EA  11.03  0.79  2.20  14.02  0/NA  Avg.  NA  (0.00)  14.02  
699. Seal & paint single garage door opening & trim  
1.00 EA  85.61  0.42  17.20  103.23  0/15 yrs  Avg.  0%  (0.00)  103.23  
700. Paint overhead door - 2 coats (per side)  
1.00 EA  101.45  2.15  20.74  124.34  0/15 yrs  Avg.  NA  (0.00)  124.34  

GARAGE  
701. R&R Wrap wood garage door frame & trim with aluminum (PER LF)  
32.00 LF  10.68  4.22  69.20  415.18  0/50 yrs  Avg.  0%  (0.00)  415.18  
damaged by hail  

GARAGE DOOR  
702. R&R Overhead door & hardware - 18' x 7' - Standard grade  
1.00 EA  1,557.39  65.10  324.50  1,946.99  1/35 yrs  Avg.  NA  (0.00)  1,946.99  
703. Overhead door weather stop  
32.00 LF  3.88  2.27  25.30  151.73  0/35 yrs  Avg.  NA  (0.00)  151.73  
704. Clean door / window opening (per side)  
1.00 EA  11.03  0.79  2.20  14.02  0/NA  Avg.  NA  (0.00)  14.02  
705. Seal & paint single garage door opening & trim  
1.00 EA  85.61  0.42  17.20  103.23  0/15 yrs  Avg.  0%  (0.00)  103.23  
706. Paint overhead door - 2 coats (per side)  
1.00 EA  101.45  2.15  20.74  124.34  0/15 yrs  Avg.  NA  (0.00)  124.34  

GARAGE DOOR OPENER  
707. R&R Overhead (garage) door opener - Standard grade  
1.00 EA  395.41  8.58  80.82  484.81  3/10 yrs  Avg.  0%  (0.00)  484.81  

7' 10" 

Attic Height: 8'
7' 2" 

306.67 SF Walls 86.00 SF Ceiling 
392.67 SF Walls & Ceiling 86.00 SF Floor 

Attic 

9.56 SY Flooring 38.33 LF Floor Perimeter 
38.33 LF Ceil. Perimeter 
12'12' 8" 

QUANTITY  UNIT  TAX  O&P  RCV  AGE/LIFE  COND.  DEP %  DEPREC.  ACV 

708. R&R Blown-in insulation - 14" depth - R38  
86.00 SF  2.28  4.08  40.02  240.18  0/150 yrs  Avg.  0%  (0.00)  240.18  
709. Seal floor or ceiling joist system (shellac)  
86.00 SF  1.30  1.50  22.66  135.96  0/15 yrs  Avg.  0%  (0.00)  135.96  
710. Clean floor or roof joist system  
86.00 SF  0.96  6.05  16.54  105.15  0/NA  Avg.  0%  (0.00)  105.15  

# INSULATION  

711. R&R Blown-in insulation - 10" depth - R26  
86.00 SF  1.60  2.63  28.04  168.27  16/150 yrs  Avg. 10.67%  (6.98)  161.29  
712. R&R Ductwork - flexible - insulated - 12" round  
2.00 LF  11.44  0.71  4.72  28.31  16/30 yrs  Avg. 53.33%  (11.78)  16.53  
713. Seal attic framing for odor control - 6 to 8/12  
86.00 SF  1.09  1.03  18.94  113.71  16/15 yrs  Avg.  100%  [M]  (94.77)  18.94  
714. R&R Ductwork - Mechanical room - Plenum & Return air  
1.00 EA  945.05  10.25  191.06  1,146.36  16/30 yrs  Avg. 53.33%  (489.49)  656.87  
715. Furnace - check, heavy clean, replace filters and service*  
1.00 EA  209.44  0.75  42.04  252.23  16/NA  Avg.  0%  (0.00)  252.23 


________________________________________________________________________________________________________________________
           
|   # | DESCRIPTION                                               |    QTY | UNIT |    TAX |  O\&P |      RCV | AGE/LIFE | COND. | DEP% | DEPREC. |      ACV | NOTES                        |
| --: | --------------------------------------------------------- | -----: | :--: | -----: | ----: | -------: | :------: | :---: | ---: | ------: | -------: | ---------------------------- |
| 716 | Remove tear off, haul & dispose of comp. shingles – 3-tab |  16.77 |  SQ  |  42.57 |  0.00 |   856.68 | 0/25 yrs |  Avg. |   NA |  (0.00) |   856.68 | —                            |
| 717 | 3-tab 25-yr comp. shingle roofing – w/out felt            |  20.00 |  SQ  | 189.04 | 89.72 | 4,644.62 | 0/25 yrs |  Avg. |   0% |  (0.00) | 4,644.62 | Starter & ridge in 10% waste |
| 718 | Roofing felt – 30 lb                                      |  16.77 |  SQ  |  38.68 | 14.28 |   795.54 | 0/20 yrs |  Avg. |   0% |  (0.00) |   795.54 | —                            |
| 719 | Drip edge                                                 | 171.80 |  LF  |   2.21 |  6.91 |   463.91 | 0/35 yrs |  Avg. |   0% |  (0.00) |   463.91 | —                            |
| 720 | Flashing – pipe jack                                      |   0.00 |  EA  |  40.16 |  0.00 |     0.00 | 0/35 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 721 | Flashing – pipe jack – 6"                                 |   0.00 |  EA  |  44.18 |  0.00 |     0.00 | 0/35 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 722 | Flashing – pipe jack – 8"                                 |   0.00 |  EA  |  53.82 |  0.00 |     0.00 | 0/35 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 723 | Flashing – pipe jack – split boot                         |   0.00 |  EA  |  59.02 |  0.00 |     0.00 | 0/35 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 724 | R\&R Flat roof exhaust vent/cap – gooseneck 8"            |   0.00 |  EA  |  83.24 |  0.00 |     0.00 | 0/35 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 725 | R\&R Roof vent – turbine – Std grade                      |   0.00 |  EA  |  83.33 |  0.00 |     0.00 | 0/35 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 726 | R\&R Continuous ridge vent – shingle-over                 |  30.00 |  LF  |   7.12 |  5.42 |   262.82 | 0/35 yrs |  Avg. |   0% |  (0.00) |   262.82 | —                            |
| 727 | R\&R Roof vent – turtle – metal                           |   0.00 |  EA  |  50.37 |  0.00 |     0.00 | 0/35 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 728 | Apply mastic around vent pipes                            |   0.00 |  EA  |  16.40 |  0.00 |     0.00 | 0/17 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 729 | R\&R Power attic vent cover – metal                       |   0.00 |  EA  |  79.14 |  0.00 |     0.00 |  0/7 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 730 | Flashing – L flashing – galvanized                        |   0.00 |  LF  |   2.88 |  0.00 |     0.00 | 0/35 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 731 | Step flashing                                             |   0.00 |  LF  |   6.93 |  0.00 |     0.00 | 0/35 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 732 | R\&R Flashing – rain diverter                             |   0.00 |  EA  |  36.49 |  0.00 |     0.00 | 0/35 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 733 | Digital satellite system – Detach & reset                 |   0.00 |  EA  |  25.95 |  0.00 |     0.00 |   0/NA   |  Avg. |   0% |  (0.00) |     0.00 | —                            |
| 734 | **Remove** steep roof add – 7/12 to 9/12                  |  16.77 |  SQ  |  13.40 |  0.00 |   269.66 |   0/NA   |  Avg. |   NA |  (0.00) |   269.66 | —                            |
| 735 | Steep roof add – 7/12 to 9/12                             |  16.77 |  SQ  |  27.75 |  0.00 |   558.45 |   0/NA   |  Avg. |   0% |  (0.00) |   558.45 | —                            |
| 736 | **Remove** steep roof add – 10/12–12/12                   |  16.77 |  SQ  |  21.06 |  0.00 |   423.82 |   0/NA   |  Avg. |   NA |  (0.00) |   423.82 | —                            |
| 737 | Steep roof add – 10/12–12/12                              |  16.77 |  SQ  |  43.61 |  0.00 |   877.60 |   0/NA   |  Avg. |   0% |  (0.00) |   877.60 | —                            |
| 738 | **Remove** high roof add (2-story+)                       |  16.77 |  SQ  |   5.06 |  0.00 |   101.84 |   0/NA   |  Avg. |   NA |  (0.00) |   101.84 | —                            |

|       # | DESCRIPTION                                      |   QTY | UNIT |    TAX |  O\&P |      RCV |  AGE/LIFE |    COND.   |      DEP% |    DEPREC. |      ACV | NOTES                            |
| ------: | ------------------------------------------------ | ----: | :--: | -----: | ----: | -------: | :-------: | :--------: | --------: | ---------: | -------: | -------------------------------- |
|     739 | High roof add (2-story+)                         | 16.77 |  SQ  |  12.25 |  0.00 |   246.51 |    0/NA   |    Avg.    |        0% |     (0.00) |   246.51 | —                                |
|     740 | R\&R Gutter/downspout – alum. – up to 5"         | 60.00 |  LF  |   5.49 |  8.93 |   405.99 |  5/25 yrs |    Avg.    |        0% |     (0.00) |   405.99 | Hail damage                      |
|     741 | R\&R Gable cornice return – laminated            |  2.00 |  EA  |  70.03 |  0.67 |   168.87 | 18/30 yrs |    Avg.    |        0% |     (0.00) |   168.87 | —                                |
|     742 | R\&R Gable cornice return – laminated – 2-story+ |  2.00 |  EA  |  84.14 |  0.67 |   202.75 | 18/30 yrs |    Avg.    |        0% |     (0.00) |   202.75 | —                                |
|     743 | R\&R Gable cornice strip – laminated – 2-story+  |  8.00 |  LF  |  12.05 |  1.47 |   117.45 | 18/30 yrs |    Avg.    |        0% |     (0.00) |   117.45 | —                                |
|     744 | Roofer – per hour                                |  3.00 |  HR  |  85.00 |  0.00 |   306.00 |   15/NA   |    Avg.    |        0% |     (0.00) |   306.00 | Trip/mobilization                |
| 745–757 | Vents/flashings (0 qty)                          |     — |   —  |      — |     — |     0.00 |     —     |    Avg.    |         — |     (0.00) |     0.00 | Listed items have 0.00 qty       |
|     758 | R\&R Gable cornice return – 3-tab                |  0.00 |  EA  |  77.34 |  0.00 |     0.00 |  0/25 yrs |    Avg.    |        0% |     (0.00) |     0.00 | —                                |
|     759 | R\&R Gable cornice return – 3-tab – 2-story+     |  0.00 |  EA  |  93.39 |  0.00 |     0.00 |  0/25 yrs |    Avg.    |        0% |     (0.00) |     0.00 | —                                |
|     760 | R\&R Gable cornice strip – 3-tab                 |  0.00 |  LF  |  10.67 |  0.00 |     0.00 |  0/25 yrs |    Avg.    |        0% |     (0.00) |     0.00 | —                                |
|     761 | R\&R Gable cornice strip – 3-tab – 2-story+\*    |  0.00 |  LF  |  12.52 |  0.00 |     0.00 |  0/25 yrs |    Avg.    |        0% |     (0.00) |     0.00 | —                                |
|     762 | Apply mastic around vent pipes (dep note)        |  0.00 |  EA  |  16.40 |  0.00 |     0.00 | 15/17 yrs |    Avg.    |    88.24% |     (0.00) |     0.00 | —                                |
|     763 | **Remove** tear off comp. shingles – 3-tab       | 16.77 |  SQ  |  50.56 |  0.00 | 1,017.47 | 20/25 yrs | Below Avg. |   NA \[M] |     (0.00) | 1,017.47 | —                                |
|     764 | Roofing felt – 30 lb.                            | 16.77 |  SQ  |  25.55 |  9.39 |   525.44 | 20/20 yrs | Below Avg. | 100% \[M] |   (437.86) |    87.58 | —                                |
|     765 | Laminated comp. shingles – w/out felt            | 18.67 |  SQ  | 167.65 | 96.98 | 3,872.41 | 20/30 yrs | Below Avg. |    93.33% | (3,011.87) |   860.54 | 10% waste                        |
|     766 | R\&R Continuous ridge vent – shingle-over        | 18.00 |  LF  |   7.21 |  3.25 |   159.65 | 20/35 yrs | Below Avg. |       80% |    (94.33) |    65.32 | —                                |
|     767 | R\&R Flashing – pipe jack                        |  3.00 |  EA  |  34.96 |  1.40 |   127.54 | 20/35 yrs | Below Avg. |       80% |    (68.13) |    59.41 | —                                |
|     768 | R\&R Furnace vent rain cap & storm collar – 5"   |  2.00 |  EA  |  61.40 |  2.40 |   150.24 | 10/25 yrs |    Avg.    |       40% |    (41.50) |   108.74 | —                                |
|     769 | R\&R Roof vent – turtle – metal                  |  3.00 |  EA  |  50.36 |  2.76 |   184.62 | 20/35 yrs |    Avg.    |    57.14% |    (73.13) |   111.49 | —                                |
|     770 | Step flashing                                    |  6.17 |  LF  |   6.93 |  0.61 |    52.05 | 20/35 yrs | Below Avg. |       80% |    (34.70) |    17.35 | Front shed roof                  |
|     771 | R\&R Flashing – L flashing – color finish        | 28.00 |  LF  |   3.83 |  2.82 |   132.08 | 20/35 yrs | Below Avg. |       80% |    (75.51) |    56.57 | Top of front elevation shed roof |


Roof (WOOD SHAKE ROOF 772–792)

|       # | DESCRIPTION                                      |      QTY | UNIT |    TAX |   O\&P |       RCV |  AGE/LIFE  | COND. |      DEP% |    DEPREC. |      ACV | NOTES                                    |
| ------: | ------------------------------------------------ | -------: | :--: | -----: | -----: | --------: | :--------: | :---: | --------: | ---------: | -------: | ---------------------------------------- |
|     772 | Tear off, haul & dispose of wood shakes/shingles |    16.77 |  SQ  |  60.18 |   0.00 |  1,211.06 |  23/40 yrs |  Avg. |        NA |     (0.00) | 1,211.06 | —                                        |
|     773 | Roofing felt – 15 lb.                            |    16.77 |  SQ  |  26.61 |   5.32 |    541.89 |  23/20 yrs |  Avg. | 100% \[M] |   (451.57) |    90.32 | —                                        |
|     774 | Wood shakes – medium (1/2") hand split           |    18.45 |  SQ  | 606.14 | 395.69 | 13,894.77 |  23/40 yrs |  Avg. |     57.5% | (6,657.91) | 7,236.86 | 10% waste added                          |
|     775 | R\&R Copper ridge or hip                         |    30.00 |  LF  |  15.76 |  19.60 |    590.88 | 23/150 yrs |  Avg. |    15.33% |    (72.75) |   518.13 | —                                        |
|     776 | R\&R Drip edge – copper                          |   171.80 |  LF  |   8.90 |  74.53 |  1,924.25 | 23/150 yrs |  Avg. |    15.33% |   (237.19) | 1,687.06 | —                                        |
|     777 | Re-nailing of roof sheathing – complete re-nail  | 1,677.05 |  SF  |   0.23 |   1.01 |    464.07 |  0/150 yrs |  Avg. |        0% |     (0.00) |   464.07 | Code 708.7 note                          |
|     778 | Roof vent – off ridge type – 6'                  |     3.00 |  EA  | 154.14 |   8.56 |    565.18 |  0/35 yrs  |  Avg. |        0% |     (0.00) |   565.18 | —                                        |
|     779 | **Remove** tear off comp. shingles – laminated   |    16.77 |  SQ  |  43.97 |   0.00 |    884.86 |  0/30 yrs  |  Avg. |        NA |     (0.00) |   884.86 | —                                        |
|     780 | Ridge cap – composition shingles\*               |    30.00 |  LF  |   3.85 |   1.62 |    140.54 |  0/25 yrs  |  Avg. |        0% |     (0.00) |   140.54 | —                                        |
|     781 | Exhaust cap – through roof – 6" to 8"            |     1.00 |  EA  |  80.27 |   1.86 |     98.57 |  0/35 yrs  |  Avg. |        0% |     (0.00) |    98.57 | —                                        |
|     782 | R\&R Roof vent – off ridge type – 8'             |     3.00 |  EA  | 223.34 |  13.40 |    820.10 |  0/35 yrs  |  Avg. |        0% |     (0.00) |   820.10 | —                                        |
| 783–791 | Gutters/vents/priming (0 qty)                    |        — |   —  |      — |      — |      0.00 |      —     |  Avg. |         — |     (0.00) |     0.00 | Gutters attached through drip edge (784) |
|     785 | Asphalt starter – universal starter course       |   171.80 |  LF  |   1.98 |   6.80 |    416.36 |  0/20 yrs  |  Avg. |        0% |     (0.00) |   416.36 | —                                        |
|     792 | R\&R Flashing – kick-out diverter                |     1.00 |  EA  |  28.80 |   0.72 |     35.42 |  0/35 yrs  |  Avg. |        0% |     (0.00) |    35.42 | —                                        |

Roof (Repairs, Solar, Labor Min 793–801)
|   # | DESCRIPTION                                      |   QTY | UNIT |    TAX | O\&P |      RCV | AGE/LIFE | COND. | DEP% | DEPREC. |      ACV | NOTES                               |
| --: | ------------------------------------------------ | ----: | :--: | -----: | ---: | -------: | :------: | :---: | ---: | ------: | -------: | ----------------------------------- |
| 793 | Remove 3-tab comp shingles (per shingle)         | 24.00 |  EA  |   5.30 | 0.00 |   152.64 | 0/25 yrs |  Avg. |   NA |  (0.00) |   152.64 | —                                   |
| 794 | 3-tab comp shingles (per shingle)                | 24.00 |  EA  |  12.29 | 2.55 |   357.03 | 0/25 yrs |  Avg. |   0% |  (0.00) |   357.03 | Repair factor ×2 applied            |
| 795 | Solar electric panel – Detach & reset            | 25.00 |  EA  | 125.00 | 0.00 | 3,750.00 |   0/NA   |  Avg. |   0% |  (0.00) | 3,750.00 | —                                   |
| 796 | Solar panel mounting hardware – Detach & reset\* | 25.00 |  EA  |  20.37 | 0.00 |   611.11 |   0/NA   |  Avg. |   0% |  (0.00) |   611.11 | —                                   |
| 797 | Skylight – reflective tube – flash/dome – D\&R   |  1.00 |  EA  |  32.96 | 0.00 |    39.56 |   15/NA  |  Avg. |   0% |  (0.00) |    39.56 | —                                   |
| 798 | Tear off comp shingles (no haul off)\*           | 16.77 |  SQ  |  37.50 | 0.00 |   754.66 |   3/NA   |  Avg. |   NA |  (0.00) |   754.66 | —                                   |
| 799 | R\&R Gutter guard/screen                         |  0.00 |  LF  |   3.13 | 0.00 |     0.00 | 0/20 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                                   |
| 800 | **Material Only** 3-tab 25-yr – w/out felt       |  0.33 |  SQ  |  78.51 | 1.55 |    32.96 | 0/25 yrs |  Avg. |   0% |  (0.00) |    32.96 | All slopes: 0 wind-damaged shingles |
| 801 | Roofing – Labor Minimum                          |  1.00 |  EA  | 448.40 | 0.00 |   538.08 |   10/NA  |  Avg. |   0% |  (0.00) |   538.08 | Allowance; trip/mobilization        |

Roof (Additional systems 802–819) -
|       # | DESCRIPTION                                                |    QTY | UNIT |    TAX |   O\&P |       RCV |  AGE/LIFE | COND. | DEP% | DEPREC. |       ACV | NOTES           |
| ------: | ---------------------------------------------------------- | -----: | :--: | -----: | -----: | --------: | :-------: | :---: | ---: | ------: | --------: | --------------- |
|     802 | Add’l layer comp shingles, remove & dispose – 3-tab        |  16.77 |  SQ  |  44.27 |   0.00 |    890.89 |  0/25 yrs |  Avg. |   NA |  (0.00) |    890.89 | —               |
| 803–807 | Valley metal / vents / sheathing / copper jack (0 qty)     |      — |   —  |      — |      — |      0.00 |     —     |  Avg. |    — |  (0.00) |      0.00 | —               |
|     808 | R\&R Flashing – pipe jack – lead                           |   0.00 |  EA  | 100.70 |   0.00 |      0.00 |  0/35 yrs |  Avg. |   0% |  (0.00) |      0.00 | —               |
|     809 | Tear off, haul & dispose – 4-ply built-up roofing          |  16.77 |  SQ  |  93.25 |   0.00 |  1,876.56 |  0/30 yrs |  Avg. |   NA |  (0.00) |  1,876.56 | —               |
|     810 | R\&R Fiberboard – 1"                                       |  16.77 |  SF  |   2.14 |   0.58 |     43.77 |  0/20 yrs |  Avg. |   0% |  (0.00) |     43.77 | —               |
|     811 | R\&R Insulation – perlite board – 1-1/2"                   |  16.77 |  SQ  | 352.32 | 126.13 |  7,241.44 | 0/150 yrs |  Avg. |   0% |  (0.00) |  7,241.44 | —               |
|     812 | R\&R Membrane roofing – cant strips – perlite              | 171.80 |  LF  |   3.50 |   4.74 |    727.24 |  0/35 yrs |  Avg. |   0% |  (0.00) |    727.24 | —               |
|     813 | R\&R Built-up 4-ply roofing – in place                     |  16.77 |  SQ  | 595.58 | 150.93 | 12,166.56 |  0/30 yrs |  Avg. |   0% |  (0.00) | 12,166.56 | —               |
|     814 | R\&R Built-up roofing – gravel ballast                     |  16.77 |  SQ  | 123.23 |  21.89 |  2,506.15 | 0/150 yrs |  Avg. |   0% |  (0.00) |  2,506.15 | —               |
|     815 | R\&R Roof scupper – aluminum                               |   0.00 |  EA  | 295.98 |   0.00 |      0.00 |  0/35 yrs |  Avg. |   0% |  (0.00) |      0.00 | —               |
|     816 | Tear off, haul & dispose of comp. shingles – high profile  |  16.77 |  SQ  |  74.63 |   0.00 |  1,501.87 |  0/50 yrs |  Avg. |   NA |  (0.00) |  1,501.87 | —               |
|     817 | Add’l layer comp shingles, remove & dispose – high profile |  16.77 |  SQ  |  49.95 |   0.00 |  1,005.20 |  0/50 yrs |  Avg. |   NA |  (0.00) |  1,005.20 | —               |
|     818 | Laminated – deluxe grade – w/out felt                      |  19.50 |  SQ  | 386.04 | 238.91 |  9,320.03 |  0/50 yrs |  Avg. |   0% |  (0.00) |  9,320.03 | Waste % warning |
|     819 | Hip/Ridge cap – high profile – comp shingles               |  30.00 |  LF  |   7.74 |   7.24 |    287.32 |  0/30 yrs |  Avg. |   0% |  (0.00) |    287.32 | —               |

Roof (Wood shakes heavy & notes 820–824) -
|       # | DESCRIPTION                                      |   QTY | UNIT |          TAX |     O\&P |       RCV | AGE/LIFE | COND. | DEP% | DEPREC. |       ACV | NOTES                     |
| ------: | ------------------------------------------------ | ----: | :--: | -----------: | -------: | --------: | :------: | :---: | ---: | ------: | --------: | ------------------------- |
|     820 | **Remove** wood shakes – heavy (3/4") hand split | 16.77 |  SQ  |        79.30 |     0.00 |  1,595.84 | 0/40 yrs |  Avg. |   NA |  (0.00) |  1,595.84 | —                         |
|     821 | Wood shakes – heavy (3/4") hand split            | 17.44 |  SQ  |     1,584.60 | 1,244.48 | 34,655.88 | 0/40 yrs |  Avg. |   0% |  (0.00) | 34,655.88 | Auto waste 4.0% (0.67 SQ) |
|     822 | Hip/Ridge cap – wood shake shingles              | 30.00 |  LF  |        17.63 |    20.09 |    658.79 | 0/40 yrs |  Avg. |   0% |  (0.00) |    658.79 | —                         |
| 823–824 | Remove/install wood shakes (per shake)           |  0.00 |  EA  | 8.75 / 22.08 |     0.00 |      0.00 | 0/40 yrs |  Avg. |    — |  (0.00) |      0.00 | —                         |


Roof (Tile roofing 825–844) - 
|       # | DESCRIPTION                                       |   QTY | UNIT |                     TAX |     O\&P |       RCV | AGE/LIFE | COND. | DEP% | DEPREC. |       ACV | NOTES         |
| ------: | ------------------------------------------------- | ----: | :--: | ----------------------: | -------: | --------: | :------: | :---: | ---: | ------: | --------: | ------------- |
|     825 | Tile roofing – Detach & reset                     | 16.77 |  SQ  |                1,086.31 |    78.16 | 21,954.70 |   0/NA   |  Avg. |   0% |  (0.00) | 21,954.70 | —             |
| 826–829 | R\&R Tile roofing (Clay/Concrete/Glazed per TILE) |  0.00 |  EA  | 51.47/46.68/51.05/56.63 |     0.00 |      0.00 | 0/75 yrs |  Avg. |   0% |  (0.00) |      0.00 | —             |
|     830 | Tear off, haul & dispose of tile roofing          | 16.77 |  SQ  |                  236.63 |     0.00 |  4,761.95 | 0/75 yrs |  Avg. |   NA |  (0.00) |  4,761.95 | —             |
|     831 | Tear off tile roofing (no haul off)               | 16.77 |  SQ  |                  169.90 |     0.00 |  3,419.06 | 0/75 yrs |  Avg. |   NA |  (0.00) |  3,419.06 | —             |
| 832–835 | Remove tile roofing (Clay/Concrete/Barrel/Glazed) | 16.77 |  SQ  |                  236.63 |     0.00 |  4,761.95 | 0/75 yrs |  Avg. |   NA |  (0.00) |  4,761.95 | Each category |
|     836 | Ice & water barrier                               | 16.77 |  SF  |                    1.94 |     0.51 |     39.64 | 0/30 yrs |  Avg. |   0% |  (0.00) |     39.64 | —             |
|     837 | Tile roofing – Clay – “S” or flat                 | 19.29 |  SQ  |                1,045.90 |   625.52 | 24,961.11 | 0/75 yrs |  Avg. |   0% |  (0.00) | 24,961.11 | —             |
|     838 | Tile roofing – Concrete – “S” or flat             | 19.29 |  SQ  |                  760.71 |   295.44 | 17,963.44 | 0/75 yrs |  Avg. |   0% |  (0.00) | 17,963.44 | —             |
|     839 | Tile roofing – Clay – Barrel (mission)            | 19.29 |  SQ  |                1,308.37 |   929.30 | 31,401.32 | 0/75 yrs |  Avg. |   0% |  (0.00) | 31,401.32 | —             |
|     840 | Tile roofing – Glazed – Barrel or “S”             | 19.29 |  SQ  |                1,413.70 | 1,051.21 | 33,985.78 | 0/75 yrs |  Avg. |   0% |  (0.00) | 33,985.78 | —             |
| 841–843 | Tile clips & nailer boards (0 qty)                |  0.00 |  LF  |      4.33 / 3.43 / 3.33 |     0.00 |      0.00 | 0/75 yrs |  Avg. |   0% |  (0.00) |      0.00 | —             |
|     844 | Hip/Ridge/Rake cap – tile roofing                 | 30.00 |  LF  |                   13.54 |    12.73 |    502.71 | 0/75 yrs |  Avg. |   0% |  (0.00) |    502.71 | —             |


Roof (Tile accessories & soffit/fascia 845–862) - 
|       # | DESCRIPTION                            |   QTY | UNIT |                   TAX | O\&P |      RCV |     AGE/LIFE    | COND. | DEP% | DEPREC. |      ACV | NOTES |
| ------: | -------------------------------------- | ----: | :--: | --------------------: | ---: | -------: | :-------------: | :---: | ---: | ------: | -------: | ----- |
| 845–846 | Bird stop – eave closure (clay/metal)  |  0.00 |  LF  |          10.69 / 4.63 | 0.00 |     0.00 |     0/75 yrs    |  Avg. |   0% |  (0.00) |     0.00 | —     |
|     847 | **Remove** steep roof add >12/12       | 16.77 |  SQ  |                 33.13 | 0.00 |   666.71 |       0/NA      |  Avg. |   NA |  (0.00) |   666.71 | —     |
|     848 | Steep roof add >12/12                  | 16.77 |  SQ  |                112.47 | 0.00 | 2,263.34 |       0/NA      |  Avg. |   0% |  (0.00) | 2,263.34 | —     |
|     849 | **Remove** Flashing – pipe jack        |  1.00 |  EA  |                  7.04 | 0.00 |     8.44 |     0/35 yrs    |  Avg. |   NA |  (0.00) |     8.44 | —     |
| 850–852 | Remove/Install off-ridge vents (0 qty) |  0.00 |  EA  | 8.99 / 15.72 / 106.68 | 0.00 |     0.00 |     0/35 yrs    |  Avg. |    — |  (0.00) |     0.00 | —     |
| 853–862 | Soffit/fascia/vents/paint (0 qty)      |  0.00 |   —  |                     — | 0.00 |     0.00 | 0/50–150/15 yrs |  Avg. |    — |  (0.00) |     0.00 | —     |


Basement (863–866) - 
|   # | DESCRIPTION                               |    QTY | UNIT |    TAX |     O\&P |       RCV |  AGE/LIFE | COND. | DEP% | DEPREC. |       ACV | NOTES                          |
| --: | ----------------------------------------- | -----: | :--: | -----: | -------: | --------: | :-------: | :---: | ---: | ------: | --------: | ------------------------------ |
| 863 | R\&R Block – 4"×8"×16" – in place         | 834.00 |  SF  |  12.26 | 2,074.38 | 12,446.34 | 0/100 yrs |  Avg. |   0% |  (0.00) | 12,446.34 | —                              |
| 864 | R\&R Concrete slab on grade – finished    |   6.17 |  CY  | 887.23 | 1,110.26 |  6,661.52 |  0/50 yrs |  Avg. |   0% |  (0.00) |  6,661.52 | —                              |
| 865 | R\&R Batt insulation – 4" – R13 – unfaced | 394.67 |  SF  |   1.51 |   122.52 |    735.05 | 0/150 yrs |  Avg. |   0% |  (0.00) |    735.05 | —                              |
| 866 | Plaster (parget) foundation               |  16.00 |  SF  |   1.24 |     4.02 |     24.18 | 1/100 yrs |  Avg. |   1% |  (0.20) |     23.98 | Damage to foundation styrofoam |




Totals: Basement  0.32  4.02  24.18  0.20  23.98  

12' 8" 
   ___________________________________________________________________________________________________________________

# HVAC                                                                                                                                                                                            
12' 
384.00 SF Walls 144.00 SF Ceiling 
528.00 SF Walls & Ceiling 144.00 SF Floor
12' 8"12'

16.00 SY Flooring 48.00 LF Floor Perimeter 
48.00 LF Ceil. Perimeter

QUANTITY UNIT HVAC 867. R&R Clothes dryer vent cover 2.00 EA 35.70 damaged by hail  TAX 0.76  O&P 14.44  RCV 86.60  AGE/LIFE 0/30 yrs  COND. Avg.  DEP % 0%  DEPREC. (0.00)  ACV 86.60  

|   # | DESCRIPTION                                       |    QTY | UNIT |      TAX |   O&P |      RCV |  AGE/LIFE | COND. | DEP% | DEPREC. |      ACV | NOTES                                           |
| --: | ------------------------------------------------- | -----: | :--: | -------: | -----: | -------: | :-------: | :---: | ---: | ------: | -------: | ----------------------------------------------- |
| 868 | R\&R Condenser pad – 24" × 24"                    |   1.00 |  EA  |    58.55 |   2.21 |    72.92 |  0/15 yrs |  Avg. |   0% |  (0.00) |    72.92 | —                                               |
| 869 | R\&R Condenser pad – 36" × 36"                    |   1.00 |  EA  |    76.64 |   3.30 |    95.92 |  0/15 yrs |  Avg. |   0% |  (0.00) |    95.92 | —                                               |
| 870 | R\&R Air conditioning cover                       |   1.00 |  EA  |   153.75 |   5.13 |   190.66 |  0/15 yrs |  Avg. |   0% |  (0.00) |   190.66 | Damaged by hail                                 |
| 871 | HVAC Technician – per hour                        |   2.00 |  HR  |   100.01 |   0.00 |   240.02 |    0/NA   |  Avg. |   0% |  (0.00) |   240.02 | Detach/reset HVAC connections for vinyl install |
| 872 | Comb/straighten A/C condenser fins – w/ trip      |   1.00 |  EA  |   183.88 |   0.00 |   220.66 |    0/NA   |  Avg. |   0% |  (0.00) |   220.66 | —                                               |
| 873 | Comb/straighten A/C condenser fins – no trip      |   1.00 |  EA  |    78.78 |   0.00 |    94.54 |    0/NA   |  Avg. |   0% |  (0.00) |    94.54 | Trip charged on first unit                      |
| 874 | Condensate drain line                             |   1.00 |  EA  |    60.71 |   0.55 |    73.52 | 0/150 yrs |  Avg. |   0% |  (0.00) |    73.52 | —                                               |
| 875 | R\&R Ductwork system – hot & cold air (per run)   |   1.00 |  EA  |   470.24 |  10.81 |   577.27 |  0/30 yrs |  Avg. |   0% |  (0.00) |   577.27 | —                                               |
| 876 | R\&R Blown-in insulation – 14" depth – R38        | 144.00 |  SF  |     3.36 |  12.36 |   595.44 | 0/150 yrs |  Avg. |   0% |  (0.00) |   595.44 | —                                               |
| 877 | Central air – condenser unit – 4 ton – 14–15 SEER |   1.00 |  EA  | 2,398.18 | 111.62 | 3,011.76 |  0/15 yrs |  Avg. |   0% |  (0.00) | 3,011.76 | Spec text references 3-ton in notes             |
| 878 | Condenser pad – 36" × 36"                         |   1.00 |  EA  |    69.99 |   3.30 |    87.95 |  0/15 yrs |  Avg. |   0% |  (0.00) |    87.95 | —                                               |
| 879 | Refrigerant lineset – 3/8" × 3/4" – 31'–50'       |   1.00 |  EA  |   422.65 |  14.53 |   524.62 |  0/15 yrs |  Avg. |   0% |  (0.00) |   524.62 | —                                               |
| 880 | Disconnect box – 60A – non-fused                  |   1.00 |  EA  |   140.59 |   1.01 |   169.92 |  0/30 yrs |  Avg. |   0% |  (0.00) |   169.92 | —                                               |
| 881 | #6 gauge copper wire – stranded/solid             |   1.00 |  LF  |     1.30 |   0.03 |     1.59 | 0/150 yrs |  Avg. |   0% |  (0.00) |     1.59 | —                                               |
| 882 | Liquid-tight flexible conduit – 3/4"              |   1.00 |  LF  |     9.89 |   0.09 |    11.98 | 0/150 yrs |  Avg. |   0% |  (0.00) |    11.98 | —                                               |
| 883 | Central air cond. system – refrigerant only       |   1.00 |  LB  |    16.50 |   0.99 |    20.99 |  0/15 yrs |  Avg. |   0% |  (0.00) |    20.99 | —                                               |
| 884 | Central air – condenser unit – 2 ton – ≤13 SEER   |   1.00 |  EA  | 1,233.10 |  55.96 | 1,546.88 |  0/15 yrs |  Avg. |   0% |  (0.00) | 1,546.88 | —                                               |
| 885 | Condenser pad – 36" × 36"                         |   1.00 |  EA  |    69.99 |   3.30 |    87.95 |  0/15 yrs |  Avg. |   0% |  (0.00) |    87.95 | —                                               |
| 886 | Refrigerant lineset – 3/8" × 3/4" – 31'–50'       |   1.00 |  EA  |   422.65 |  14.53 |   524.62 |  0/15 yrs |  Avg. |   0% |  (0.00) |   524.62 | —                                               |
| 887 | Disconnect box – 60A – non-fused                  |   1.00 |  EA  |   140.59 |   1.01 |   169.92 |  0/30 yrs |  Avg. |   0% |  (0.00) |   169.92 | —                                               |
| 888 | #8 gauge copper wire – stranded/solid             |   1.00 |  LF  |     0.94 |   0.02 |     1.14 | 0/150 yrs |  Avg. |   0% |  (0.00) |     1.14 | —                                               |
| 889 | Liquid-tight flexible conduit – 1/2"              |   1.00 |  LF  |     7.71 |   0.07 |     9.34 | 0/150 yrs |  Avg. |   0% |  (0.00) |     9.34 | —                                               |
| 890 | Central air cond. system – refrigerant only       |   1.00 |  LB  |    16.50 |   0.99 |    20.99 |  0/15 yrs |  Avg. |   0% |  (0.00) |    20.99 | —                                               |


# Electrical - 

|   # | DESCRIPTION                                  |  QTY | UNIT |    TAX | O&P |      RCV |  AGE/LIFE | COND. |  DEP% | DEPREC. |      ACV | NOTES                        |
| --: | -------------------------------------------- | ---: | :--: | -----: | ---: | -------: | :-------: | :---: | ----: | ------: | -------: | ---------------------------- |
| 891 | Electrician – per hour                       | 2.00 |  HR  |  95.15 | 0.00 |   228.36 |    0/NA   |  Avg. |    0% |  (0.00) |   228.36 | Detach/reset for siding      |
| 892 | Detach & Reset Exterior light fixture – Std  | 2.00 |  EA  |  69.57 | 0.00 |   166.96 |  0/20 yrs |  Avg. |    0% |  (0.00) |   166.96 | Assist siding install        |
| 893 | Detach & Reset Exterior light fixture – Std  | 2.00 |  EA  |  69.57 | 0.00 |   166.96 |  0/20 yrs |  Avg. |    0% |  (0.00) |   166.96 | Light damaged by hail        |
| 894 | R\&R Clothes dryer vent cover                | 1.00 |  EA  |  35.70 | 0.38 |    43.32 |  2/30 yrs |  Avg. | 6.67% |  (2.16) |    41.16 | Damaged                      |
| 895 | Megohmmeter check – average residence        | 1.00 |  EA  | 988.03 | 0.00 | 1,185.63 |    0/NA   |  Avg. |    0% |  (0.00) | 1,185.63 | —                            |
| 896 | Megohmmeter check – single circuit           | 1.00 |  EA  | 123.50 | 0.00 |   148.20 |    0/NA   |  Avg. |    0% |  (0.00) |   148.20 | —                            |
| 897 | R\&R Light fixture                           | 1.00 |  EA  |  85.94 | 2.16 |   105.72 |  0/20 yrs |  Avg. |    0% |  (0.00) |   105.72 | —                            |
| 898 | R\&R 110V copper wiring run & box – rough-in | 1.00 |  EA  |  72.47 | 1.14 |    88.33 | 0/100 yrs |  Avg. |    0% |  (0.00) |    88.33 | —                            |
| 899 | R\&R 110V copper wiring run, box & switch    | 1.00 |  EA  |  90.81 | 1.33 |   110.56 | 0/100 yrs |  Avg. |    0% |  (0.00) |   110.56 | —                            |
| 900 | R\&R 110V copper wiring run, box & outlet    | 4.00 |  EA  |  90.11 | 5.14 |   438.68 | 0/100 yrs |  Avg. |    0% |  (0.00) |   438.68 | —                            |
| 901 | R\&R Light bar – 4 lights – High grade       | 1.00 |  EA  | 233.65 | 9.30 |   291.55 |  0/20 yrs |  Avg. |    0% |  (0.00) |   291.55 | —                            |
| 902 | R\&R Exhaust fan                             | 1.00 |  EA  | 291.79 | 6.68 |   358.17 |  0/14 yrs |  Avg. |    0% |  (0.00) |   358.17 | —                            |
| 903 | R\&R GFCI outlet                             | 1.00 |  EA  |  42.22 | 1.19 |    52.09 |  0/10 yrs |  Avg. |    0% |  (0.00) |    52.09 | —                            |
| 904 | R\&R 110V copper wiring run, box & switch    | 1.00 |  EA  |  76.80 | 0.66 |    92.98 | 0/100 yrs |  Avg. |    0% |  (0.00) |    92.98 | Attic light & switch damaged |
| 905 | Porcelain light fixture                      | 1.00 |  EA  |  30.79 | 0.33 |    37.34 |  0/20 yrs |  Avg. |    0% |  (0.00) |    37.34 | —                            |


Temporary Operations - 
|   # | DESCRIPTION                                 |  QTY | UNIT |    TAX |  O&P |      RCV | AGE/LIFE | COND. | DEP% | DEPREC. |      ACV | NOTES |
| --: | ------------------------------------------- | ---: | :--: | -----: | ----: | -------: | :------: | :---: | ---: | ------: | -------: | ----- |
| 906 | Dumpster load – \~40 yd, 7–8 tons           | 3.00 |  EA  | 725.10 |  0.00 | 2,610.36 |   0/NA   |  Avg. |   NA |  (0.00) | 2,610.36 | —     |
| 907 | R\&R Temporary power – overhead hookup      | 1.00 |  EA  | 663.84 |  0.00 |   796.62 |   0/NA   |  Avg. |   0% |  (0.00) |   796.62 | —     |
| 908 | Temporary toilet – Minimum rental charge    | 1.00 |  EA  | 125.00 |  0.00 |   150.00 |   0/NA   |  Avg. |   0% |  (0.00) |   150.00 | —     |
| 909 | Temporary toilet (per month)                | 6.00 |  MO  | 134.99 |  0.00 |   971.92 |   0/NA   |  Avg. |   0% |  (0.00) |   971.92 | —     |
| 910 | Temporary power usage (per month)           | 6.00 |  MO  | 127.41 | 45.87 |   972.41 |   0/NA   |  Avg. |   0% |  (0.00) |   972.41 | —     |
| 911 | Taxes, insurance, permits & fees (Bid Item) | 1.00 |  EA  | 650.00 |  0.00 |   780.00 |   0/NA   |  Avg. |   0% |  (0.00) |   780.00 | —     |


# Plumbing 

Fixtures & Rough-In (912–921)

|   # | DESCRIPTION                              |  QTY | UNIT |      TAX |  O\&P |          RCV |  AGE/LIFE |
| --: | ---------------------------------------- | ---: | :--: | -------: | ----: | -----------: | :-------: |
| 912 | R\&R Toilet                              | 1.00 |  EA  |   541.53 | 19.65 |   **673.44** | 0/150 yrs |
| 913 | R\&R Toilet seat                         | 1.00 |  EA  |    60.94 |  1.89 |    **75.41** |  0/9 yrs  |
| 914 | R\&R Fiberglass tub & shower combination | 1.00 |  EA  | 1,381.56 | 49.91 | **1,717.77** |  0/50 yrs |
| 915 | Rough-in plumbing – per fixture          | 3.00 |  EA  |   626.16 | 29.63 | **2,289.73** |  0/80 yrs |
| 916 | R\&R Tub/shower faucet                   | 1.00 |  EA  |   321.90 |  8.79 |   **396.83** |  0/20 yrs |
| 917 | R\&R Sink – single                       | 1.00 |  EA  |   283.20 |  9.87 |   **351.69** |  0/50 yrs |
| 918 | R\&R Sink faucet – Bathroom              | 1.00 |  EA  |   255.97 |  8.91 |   **317.86** |  0/20 yrs |
| 919 | Dishwasher connection                    | 1.00 |  EA  |   131.83 |  2.01 |   **160.60** | 0/100 yrs |
| 920 | R\&R Sink – double basin                 | 1.00 |  EA  |   425.35 | 17.89 |   **531.90** |  0/50 yrs |
| 921 | R\&R Sink faucet – Kitchen               | 1.00 |  EA  |   301.97 | 11.67 |   **376.38** |  0/15 yrs |


Appliances, Water Heaters & Accessories - 

|   # | DESCRIPTION                                                 |  QTY | UNIT |      TAX |   O\&P |      RCV |  AGE/LIFE | COND. | DEP% | DEPREC. |      ACV | NOTES                                    |
| --: | ----------------------------------------------------------- | ---: | :--: | -------: | -----: | -------: | :-------: | :---: | ---: | ------: | -------: | ---------------------------------------- |
| 922 | R\&R Garbage disposal / disposer                            | 1.00 |  EA  |   279.30 |   9.00 |   345.96 |  0/12 yrs |  Avg. |   0% |  (0.00) |   345.96 | —                                        |
| 923 | R\&R Appliance water line – 1/4"                            | 1.00 |  EA  |    93.78 |   2.35 |   115.37 |  0/50 yrs |  Avg. |   0% |  (0.00) |   115.37 | —                                        |
| 924 | Patio/pool Enclosure – Rescreen                             | 0.00 |  SF  |     1.99 |   0.00 |     0.00 |  0/40 yrs |  Avg. |   0% |  (0.00) |     0.00 | —                                        |
| 925 | Patio/pool Enclosure – Full Screen – High grade             | 0.00 |  SF  |     9.59 |   0.00 |     0.00 |  0/40 yrs |  Avg. |   0% |  (0.00) |     0.00 | See note in source                       |
| 926 | Washer – Remove & reset                                     | 1.00 |  EA  |    53.78 |   0.00 |    64.54 |    0/NA   |  Avg. |   0% |  (0.00) |    64.54 | —                                        |
| 927 | Dryer – Remove & reset                                      | 1.00 |  EA  |    41.47 |   0.00 |    49.77 |    0/NA   |  Avg. |   0% |  (0.00) |    49.77 | —                                        |
| 928 | Water heater – Detach                                       | 1.00 |  EA  |    91.10 |   6.56 |   115.88 |    0/NA   |  Avg. |   0% |  (0.00) |   115.88 | On-site storage & labor; reset elsewhere |
| 929 | R\&R Water heater – 40 gal – Electric – 6 yr                | 1.00 |  EA  |   958.93 |  31.18 | 1,188.15 |  0/6 yrs  |  Avg. |   0% |  (0.00) | 1,188.15 | Includes valves, lines, PRV; LEED note   |
| 930 | R\&R Solar water heater system                              | 1.00 |  EA  | 3,977.13 | 118.80 | 4,915.11 |  0/30 yrs |  Avg. |   0% |  (0.00) | 4,915.11 | Single collector panel; LEED note        |
| 931 | Solar water heater panel – Detach & reset                   | 1.00 |  EA  |   701.83 |   0.00 |   842.19 |    0/NA   |  Avg. |   0% |  (0.00) |   842.19 | —                                        |
| 932 | Temporary water heater – (Bid Item)                         | 1.00 |  EA  |     0.00 |   0.00 |     0.00 |    0/NA   |  Avg. |   0% |  (0.00) |     0.00 | —                                        |
| 933 | Water heater – tankless – Detach & reset                    | 1.00 |  EA  |   423.98 |   0.00 |   508.78 |    0/NA   |  Avg. |   0% |  (0.00) |   508.78 | —                                        |
| 934 | R\&R Water heater – tankless – 20.1–36 kW – Electric        | 1.00 |  EA  | 1,479.91 |  48.48 | 1,834.09 |  0/20 yrs |  Avg. |   0% |  (0.00) | 1,834.09 | Includes plumbing & electrical hookups   |
| 935 | R\&R Water heater – tankless – 5–5.9 gpm – Gas – Power vent | 1.00 |  EA  | 1,974.50 |  73.58 | 2,457.70 |  0/20 yrs |  Avg. |   0% |  (0.00) | 2,457.70 | Venting may require adds                 |
| 936 | R\&R Water heater connector line – 3/4" flexible            | 1.00 |  EA  |    61.81 |   0.92 |    75.27 |  0/50 yrs |  Avg. |   0% |  (0.00) |    75.27 | —                                        |
| 937 | R\&R Water heater seismic strap kit – 56–80 gal             | 1.00 |  EA  |    77.34 |   1.49 |    94.61 | 0/100 yrs |  Avg. |   0% |  (0.00) |    94.61 | —                                        |
| 938 | R\&R Water heater – 50 gal – Gas – Power vent               | 1.00 |  EA  | 2,224.42 | 105.43 | 2,795.83 |  0/11 yrs |  Avg. |   0% |  (0.00) | 2,795.83 | PVC venting may be extra                 |
| 939 | R\&R Water heater – flood sensor/shutoff – 3/4"             | 1.00 |  EA  |   233.43 |  11.10 |   293.43 |  0/70 yrs |  Avg. |   0% |  (0.00) |   293.43 | —                                        |
| 940 | R\&R Water heater – 80 gal – Electric – Std grade           | 1.00 |  EA  | 1,452.94 |  59.14 | 1,814.50 |  0/11 yrs |  Avg. |   0% |  (0.00) | 1,814.50 | —                                        |
| 941 | R\&R Solar water heater panel – over 33 SF                  | 1.00 |  EA  | 1,953.83 |  69.57 | 2,428.10 |  0/30 yrs |  Avg. |   0% |  (0.00) | 2,428.10 | —                                        |
| 942 | R\&R Water heater – enclosure – 30" × 30"                   | 1.00 |  EA  |   407.83 |   7.02 |   497.83 |  0/20 yrs |  Avg. |   0% |  (0.00) |   497.83 | —                                        |
| 943 | R\&R Water heater – 140 gal – Gas                           | 1.00 |  EA  | 4,338.35 | 227.88 | 5,479.47 |  0/10 yrs |  Avg. |   0% |  (0.00) | 5,479.47 | —                                        |
| 944 | R\&R Water heater – 100 gal – Residential – Gas             | 1.00 |  EA  | 3,576.71 | 183.05 | 4,511.72 |  0/10 yrs |  Avg. |   0% |  (0.00) | 4,511.72 | —                                        |
| 945 | Water heater – Reset                                        | 1.00 |  EA  |   374.85 |   0.00 |   449.83 |    0/NA   |  Avg. |   0% |  (0.00) |   449.83 | Reset only; detach by others             |
| 946 | R\&R Water heater – 30 gal – Gas – 9 yr                     | 1.00 |  EA  | 1,180.41 |  42.79 | 1,467.86 |  0/9 yrs  |  Avg. |   0% |  (0.00) | 1,467.86 | —                                        |
| 947 | R\&R Water heater platform – wood frame                     | 1.00 |  EA  |   453.21 |   8.91 |   554.54 |  0/50 yrs |  Avg. |   0% |  (0.00) |   554.54 | —                                        |
| 948 | R\&R Water heater – 40 gal – Gas – 6 yr                     | 1.00 |  EA  | 1,128.64 |  39.69 | 1,402.01 |  0/6 yrs  |  Avg. |   0% |  (0.00) | 1,402.01 | —                                        |
| 949 | R\&R Water heater blanket                                   | 1.00 |  EA  |    58.21 |   1.45 |    71.60 |  0/15 yrs |  Avg. |   0% |  (0.00) |    71.60 | —                                        |
| 950 | Clean water heater                                          | 1.00 |  EA  |    24.41 |   1.77 |    31.06 |    0/NA   |  Avg. |   0% |  (0.00) |    31.06 | —                                        |
| 951 | Water heater – Detach & reset                               | 1.00 |  EA  |   549.78 |   0.00 |   659.74 |    0/NA   |  Avg. |   0% |  (0.00) |   659.74 | —                                        |


Siding (Front) -
Geometry: Walls 971.84 SF · Ceiling 681.79 SF · Floor 681.79 SF · Ceiling Perimeter 121.48 LF · Floor Perimeter 121.48 LF · Height 8'
Walls & Ceiling: 1,653.63 SF · Flooring: 75.75 SY

|   # | DESCRIPTION                                     |    QTY | UNIT |   TAX |  O\&P |    RCV |  AGE/LIFE  | COND. |   DEP% |  DEPREC. |        ACV |
| --: | ----------------------------------------------- | -----: | :--: | ----: | ----: | -----: | :--------: | :---: | -----: | -------: | ---------: |
| 952 | R\&R Fiber cement lap siding – 8" (hail damage) |  60.00 |  SF  |  4.11 |  6.48 | 303.70 | 13/150 yrs |  Avg. |  8.67% |  (19.70) | **284.00** |
| 953 | Siding Installer – per hour                     |   1.00 |  HR  | 67.34 |  0.00 |  80.80 |    13/NA   |  Avg. |     0% |   (0.00) |  **80.80** |
| 954 | R\&R Sheathing – OSB – 1/2"                     |  32.00 |  SF  |  1.85 |  0.61 |  71.77 | 13/150 yrs |  Avg. |  8.67% |   (3.60) |  **68.17** |
| 955 | R\&R House wrap (air/moisture barrier)          |  10.00 |  SF  |  0.30 |  0.08 |   3.70 | 13/150 yrs |  Avg. |  8.67% |   (0.24) |   **3.46** |
| 956 | Exterior – seal/prime & prep for paint          |  60.00 |  SF  |  0.59 |  0.40 |  42.96 |  13/15 yrs |  Avg. | 86.67% |  (31.03) |  **11.93** |
| 957 | Clean with pressure/chemical spray              | 971.84 |  SF  |  0.29 | 20.91 | 359.22 |    0/NA    |  Avg. |     0% |   (0.00) | **359.22** |
| 958 | Exterior – paint one coat (prep for paint)      | 971.84 |  SF  |  0.64 |  9.33 | 757.57 |  13/15 yrs |  Avg. | 86.67% | (547.14) | **210.43** |
| 959 | R\&R Siding – vinyl                             |  60.00 |  SF  |  3.63 |  4.86 | 267.20 |  0/50 yrs  |  Avg. |     0% |   (0.00) | **267.20** |
| 960 | R\&R House wrap (air/moisture barrier)          | 681.79 |  SF  |  0.30 |  5.73 | 252.33 |  0/150 yrs |  Avg. |     0% |   (0.00) | **252.33** |


Cleaning & Framing/Sheathing (961–975)

|   # | DESCRIPTION                                          |    QTY | UNIT |   TAX |   O\&P |       RCV |  AGE/LIFE |           ACV |
| --: | ---------------------------------------------------- | -----: | :--: | ----: | -----: | --------: | :-------: | ------------: |
| 961 | Clean with pressure/chemical spray                   | 971.84 |  SF  |  0.29 |  20.91 |    359.22 |    0/NA   |    **359.22** |
| 962 | Clean with pressure/chemical spray – Light           |   1.00 |  SF  |  0.23 |   0.01 |      0.28 |    0/NA   |      **0.28** |
| 963 | R\&R Metal studding, 3 5/8", 16" OC, 20 ga           | 971.84 |  SF  |  4.70 | 148.11 |  5,658.92 | 0/150 yrs |  **5,658.92** |
| 964 | R\&R Metal studding, 6", 24" OC, 20 ga               | 971.84 |  SF  |  5.44 | 198.26 |  6,582.11 | 0/150 yrs |  **6,582.11** |
| 965 | R\&R Hat channel, 16" OC                             | 971.84 |  SF  |  2.44 |  47.23 |  2,902.22 | 0/150 yrs |  **2,902.22** |
| 966 | R\&R Z channel, 16" OC                               | 971.84 |  SF  |  2.70 |  62.39 |  3,223.64 | 0/150 yrs |  **3,223.64** |
| 967 | R\&R Stud wall – 2"×4" – 16" oc                      | 971.84 |  SF  |  3.22 |  63.56 |  3,831.49 | 0/150 yrs |  **3,831.49** |
| 968 | R\&R Wedge anchor bolt – 1/2"×5 1/2"                 |   0.00 |  EA  | 25.28 |   0.00 |      0.00 | 0/150 yrs |      **0.00** |
| 969 | R\&R Joist – 2×8 w/blocking – 16" oc (floor/ceiling) | 681.79 |  SF  |  4.59 |  57.27 |  3,824.02 | 0/150 yrs |  **3,824.02** |
| 970 | R\&R Framing hurricane tie                           |   0.00 |  EA  | 10.95 |   0.00 |      0.00 | 0/150 yrs |      **0.00** |
| 971 | R\&R Rafters – 2×8 – 24" OC (per SF floor)           | 681.79 |  SF  |  4.65 |  51.54 |  3,866.25 | 0/150 yrs |  **3,866.25** |
| 972 | R\&R Framing strap – 24" long                        |   0.00 |  EA  | 35.22 |   0.00 |      0.00 | 0/150 yrs |      **0.00** |
| 973 | R\&R Sheathing – OSB – 5/8" (roof decking)           | 681.79 |  SF  |  2.65 |  37.64 |  2,213.25 | 0/150 yrs |  **2,213.25** |
| 974 | R\&R Add-on for trayed/dropped/coffered ceiling      | 681.79 |  SF  |  4.35 |  49.91 |  3,618.84 | 0/150 yrs |  **3,618.84** |
| 975 | R\&R Block – 8"×8"×16" – in place – reinforced       | 971.84 |  SF  | 16.66 | 295.05 | 19,783.10 | 0/100 yrs | **19,783.10** |


Masonry/Block Adds & Misc (976–983)

|   # | DESCRIPTION                                   |    QTY | UNIT |   TAX |   O\&P |      RCV |  AGE/LIFE |          ACV |
| --: | --------------------------------------------- | -----: | :--: | ----: | -----: | -------: | :-------: | -----------: |
| 976 | Block – Add if vertical reinforcement 24" OC  | 971.84 |  SF  |  5.66 | 151.61 | 6,782.66 | 0/100 yrs | **6,782.66** |
| 977 | Re-point masonry – block                      | 971.84 |  SF  |  3.63 |   3.50 | 4,237.54 |    0/NA   | **4,237.54** |
| 978 | Scaffolding Setup & Take down – per hour      |   0.00 |  HR  | 32.25 |   0.00 |     0.00 |    0/NA   |     **0.00** |
| 979 | Scaffold – per section (per week)             |   0.00 |  WK  | 48.00 |   0.00 |     0.00 |    0/NA   |     **0.00** |
| 980 | R\&R Siding – vinyl                           |  48.00 |  SF  |  3.42 |   3.89 |   201.65 |  0/50 yrs |   **201.65** |
| 981 | R\&R Gutter / downspout – aluminum – up to 5" |  27.00 |  LF  |  5.49 |   4.02 |   182.71 |  0/25 yrs |   **182.71** |
| 982 | R\&R Builder board – 1/2"                     | 971.84 |  SF  |  2.08 |  50.15 | 2,485.90 | 0/150 yrs | **2,485.90** |
| 983 | R\&R House wrap (air/moisture barrier)        | 971.84 |  SF  |  0.45 |  11.08 |   538.09 | 0/150 yrs |   **538.09** |


Siding Options & Finishes (984–1,003)
|         # | DESCRIPTION                                       |    QTY | UNIT |   TAX |   O\&P |       RCV |  AGE/LIFE |           ACV |
| --------: | ------------------------------------------------- | -----: | :--: | ----: | -----: | --------: | :-------: | ------------: |
|       984 | Metal/Vinyl siding – Detach & reset               | 971.84 |  SF  |  2.54 |   1.75 |  2,964.28 |    0/NA   |  **2,964.28** |
|       985 | R\&R Siding – .014" metal – Std grade             | 971.84 |  SF  |  8.15 | 255.40 |  9,811.08 |  0/50 yrs |  **9,811.08** |
|   986–992 | Shutters/vents/wraps (various)                    |   0.00 |   —  |     — |      — |      0.00 |     —     |      **0.00** |
|       993 | R\&R Sheathing – foil faced foam – 1/2"           | 971.84 |  SF  |  2.10 |  41.40 |  2,498.71 | 0/150 yrs |  **2,498.71** |
|       994 | R\&R Siding – board & batten – pine               | 971.84 |  SF  |  6.65 | 182.51 |  7,974.31 | 0/100 yrs |  **7,974.31** |
|       995 | R\&R Siding – board & batten – cedar              | 971.84 |  SF  | 10.65 | 415.75 | 12,919.03 | 0/100 yrs | **12,919.03** |
|       996 | R\&R Siding – board & batten – redwood            | 971.84 |  SF  | 11.42 | 460.65 | 13,870.91 | 0/100 yrs | **13,870.91** |
|       997 | Exterior – stain one coat                         | 971.84 |  SF  |  1.57 |  16.91 |  1,851.24 |  0/15 yrs |  **1,851.24** |
|       998 | Exterior – stain two coats                        | 971.84 |  SF  |  2.57 |  33.24 |  3,037.03 |  0/15 yrs |  **3,037.03** |
| 999–1,000 | Shutters & paint per set                          |   0.00 |   —  |     — |      — |      0.00 |     —     |      **0.00** |
|     1,001 | R\&R Siding – beveled – fiber-cement (clapboard)  | 971.84 |  SF  |  6.56 | 132.95 |  7,809.88 | 0/150 yrs |  **7,809.88** |
|     1,002 | R\&R Vertical siding – fiber cement board – sheet | 971.84 |  SF  |  4.81 | 142.28 |  5,780.21 | 0/150 yrs |  **5,780.21** |
|     1,003 | R\&R Siding – fiber cement – shingle type panel   | 971.84 |  SF  | 10.20 | 333.54 | 12,295.57 | 0/150 yrs | **12,295.57** |


More Finishes & Trim (1,004–1,023)

|           # | DESCRIPTION                                 |    QTY | UNIT |   TAX |   O\&P |       RCV |  AGE/LIFE |           ACV |
| ----------: | ------------------------------------------- | -----: | :--: | ----: | -----: | --------: | :-------: | ------------: |
| 1,004–1,008 | Fiber-cement trims & vinyl gable vent       |   0.00 |   —  |     — |      — |      0.00 |     —     |      **0.00** |
|       1,009 | Seal & paint wood siding                    | 971.84 |  SF  |  2.45 |  32.65 |  2,896.40 |  0/15 yrs |  **2,896.40** |
|       1,010 | Exterior – paint two coats                  | 971.84 |  SF  |  1.57 |  25.07 |  1,861.04 |  0/15 yrs |  **1,861.04** |
|       1,011 | R\&R Siding – hardboard panel – paint grade | 971.84 |  SF  |  3.79 |  89.80 |  4,527.69 | 0/150 yrs |  **4,527.69** |
|       1,012 | R\&R Siding – plywood panel – stain grade   | 971.84 |  SF  |  4.88 | 153.36 |  5,875.14 | 0/100 yrs |  **5,875.14** |
|       1,013 | Paint wood siding – 1 coat                  | 971.84 |  SF  |  1.62 |  20.41 |  1,913.75 |  0/15 yrs |  **1,913.75** |
|       1,014 | R\&R Trim board – 1"×10" (pine)             | 121.48 |  LF  |  9.01 |  44.32 |  1,366.61 | 0/150 yrs |  **1,366.61** |
|       1,015 | R\&R Trim board – 1"×4" (pine)              | 121.48 |  LF  |  4.73 |  15.02 |    707.54 | 0/150 yrs |    **707.54** |
|       1,016 | Seal (1) & paint (1) trim                   | 121.48 |  LF  |  1.96 |   1.09 |    287.03 |  0/15 yrs |    **287.03** |
| 1,017–1,018 | Shutters – wood; Attic vent – wood          |   0.00 |   —  |     — |      — |      0.00 |     —     |      **0.00** |
|       1,019 | R\&R Siding – vinyl – High grade            | 971.84 |  SF  |  6.38 | 138.20 |  7,606.26 |  0/50 yrs |  **7,606.26** |
| 1,020–1,021 | Light/outlet J-block; Vinyl J-vent          |   0.00 |   —  |     — |      — |      0.00 |     —     |      **0.00** |
|       1,022 | R\&R Metal lath & stucco                    | 971.84 |  SF  |  8.95 |  85.13 | 10,539.71 | 0/100 yrs | **10,539.71** |
|       1,023 | Stucco Plasterer – per hour                 |   0.00 |  HR  | 68.01 |   0.00 |      0.00 |    0/NA   |      **0.00** |


Synthetic Stucco -
|     # | DESCRIPTION                                   |    QTY | UNIT |   TAX |   O\&P |       RCV |  AGE/LIFE |           ACV |
| ----: | --------------------------------------------- | -----: | :--: | ----: | -----: | --------: | :-------: | ------------: |
| 1,024 | Synthetic stucco – add for quoins             |   0.00 |  LF  | 11.51 |   0.00 |      0.00 | 0/100 yrs |      **0.00** |
| 1,025 | Synthetic stucco – add for raised trim        | 121.48 |  LF  |  7.29 |  11.15 |  1,076.10 | 0/100 yrs |  **1,076.10** |
| 1,026 | Scaffold – per section (per day)              |   0.00 |  DA  | 27.74 |   0.00 |      0.00 |    0/NA   |      **0.00** |
| 1,027 | R\&R Synthetic stucco on 2" polystyrene board | 971.84 |  SF  | 12.69 | 205.84 | 15,046.17 | 0/100 yrs | **15,046.17** |



# SKETCH5 – Fire
Main area: Walls 459.23 SF · Ceiling 159.76 SF · Walls & Ceiling 618.99 SF · Floor 159.76 SF
Perimeters: Floor 57.40 LF · Ceiling 57.40 LF · Subroom (Stairs) height 9' 2"

|     # | DESCRIPTION                                        |    QTY | UNIT |  TAX |  O\&P |    RCV |  AGE/LIFE | COND. | DEP% | DEPREC. |        ACV |
| ----: | -------------------------------------------------- | -----: | :--: | ---: | ----: | -----: | :-------: | :---: | ---: | ------: | ---------: |
| 1,028 | R\&R Batt insulation – 6" – R19 – paper/foil faced | 549.66 |  SF  | 1.21 | 20.45 | 822.66 | 0/150 yrs |  Avg. |   0% |  (0.00) | **822.66** |
| 1,029 | R\&R Vapor barrier – visqueen – 6 mil              | 175.74 |  SF  | 0.37 |  0.63 |  78.79 | 0/150 yrs |  Avg. |   0% |  (0.00) |  **78.79** |
| 1,030 | Seal floor or ceiling joist system                 | 175.74 |  SF  | 1.19 |  2.43 | 253.86 |  0/15 yrs |  Avg. |   0% |  (0.00) | **253.86** |
| 1,031 | Clean floor or roof joist system                   | 175.74 |  SF  | 0.96 | 12.38 | 214.87 |    0/NA   |  Avg. |   0% |  (0.00) | **214.87** |


# DRYWALL

|     # | DESCRIPTION                                               |    QTY | UNIT |  TAX |  O\&P |      RCV |  AGE/LIFE  | COND. |   DEP% |  DEPREC. |          ACV |
| ----: | --------------------------------------------------------- | -----: | :--: | ---: | ----: | -------: | :--------: | :---: | -----: | -------: | -----------: |
| 1,032 | R\&R 5/8" drywall – hung, taped, floated, ready for paint | 172.01 |  SF  | 2.56 |  5.57 |   535.09 | 16/150 yrs |  Avg. | 10.67% |  (39.85) |   **495.24** |
| 1,033 | R\&R 1/2" drywall – hung, taped, floated, ready for paint | 549.66 |  SF  | 2.48 | 16.49 | 1,655.59 | 16/150 yrs |  Avg. | 10.67% | (123.13) | **1,532.46** |
| 1,034 | R\&R Batt insulation – 4" – R13 – unfaced batt            | 432.66 |  SF  | 0.83 |  9.86 |   442.77 | 16/150 yrs |  Avg. | 10.67% |  (28.28) |   **414.49** |


SEAL/PRIME/PAINT (materials depreciated [M]) -

|     # | DESCRIPTION                                          |    QTY | UNIT |  TAX | O\&P |    RCV |  AGE/LIFE | COND. |      DEP% |  DEPREC. |       ACV |
| ----: | ---------------------------------------------------- | -----: | :--: | ---: | ---: | -----: | :-------: | :---: | --------: | -------: | --------: |
| 1,035 | Seal stud wall for odor control                      | 549.66 |  SF  | 0.75 | 5.61 | 501.44 | 16/15 yrs |  Avg. | 100% \[M] | (417.86) | **83.58** |
| 1,036 | Seal floor or ceiling joist system                   | 172.01 |  SF  | 1.07 | 2.27 | 223.60 | 16/15 yrs |  Avg. | 100% \[M] | (186.32) | **37.28** |
| 1,037 | Seal walls & ceiling w/ latex stain blocker – 1 coat | 721.67 |  SF  | 0.39 | 2.60 | 340.87 | 16/15 yrs |  Avg. | 100% \[M] | (284.05) | **56.82** |
| 1,038 | Paint walls & ceiling – 1 coat                       | 721.67 |  SF  | 0.44 | 4.76 | 386.75 | 16/15 yrs |  Avg. | 100% \[M] | (322.29) | **64.46** |


TRIM -
|     # | DESCRIPTION                                  |   QTY | UNIT |      TAX |  O\&P |      RCV |  AGE/LIFE  | COND. |      DEP% | DEPREC. |        ACV |
| ----: | -------------------------------------------- | ----: | :--: | -------: | ----: | -------: | :--------: | :---: | --------: | ------: | ---------: |
| 1,039 | R\&R Baseboard – 3 1/4"                      | 61.34 |  LF  |     3.29 |  4.27 |   247.30 | 16/150 yrs |  Avg. |    10.67% | (18.98) | **228.32** |
| 1,040 | R\&R Base shoe                               | 61.34 |  LF  |     1.36 |  1.62 |   102.04 | 16/150 yrs |  Avg. |    10.67% |  (7.96) |  **94.08** |
| 1,041 | Seal & paint baseboard – 2 coats\*           | 61.34 |  LF  |     1.27 |  0.37 |    93.93 |  16/15 yrs |  Avg. | 100% \[M] | (78.27) |  **15.66** |
| 1,042 | Seal & paint base shoe / quarter round       | 61.34 |  LF  |     0.67 |  0.33 |    49.71 |  16/15 yrs |  Avg. | 100% \[M] | (41.43) |   **8.28** |
| 1,043 | R\&R Casing – 2 1/4"                         |  0.00 |  LF  |     2.31 |  0.00 |     0.00 | 16/150 yrs |  Avg. |    10.67% |  (0.00) |   **0.00** |
| 1,044 | Seal & paint casing – 2 coats\*              | 16.17 |  LF  |     1.28 |  0.11 |    24.97 |  16/15 yrs |  Avg. | 100% \[M] | (20.81) |   **4.16** |
| 1,045 | R\&R Fireplace mantel – paint grade – custom |  1.00 |  EA  | 1,106.46 | 46.32 | 1,383.34 |  16/75 yrs |   —   |         — |       — |          — |
| 1,046 | Seal & paint fireplace mantel                | 16.00 |  LF  |     4.41 |  0.17 |    84.89 |  16/15 yrs |   —   |         — |       — |          — |
| 1,047 | R\&R Window stool & apron                    |  0.00 |  LF  |     7.85 |  0.00 |     0.00 | 16/150 yrs |   —   |         — |       — |          — |
| 1,048 | Seal & paint window stool & apron            |  7.08 |  LF  |     3.40 |  0.14 |    29.05 |  16/15 yrs |   —   |         — |       — |          — |
| 1,049 | R\&R Window blind – PVC – 2" – 14.1–20 SF    |  4.00 |  EA  |   112.04 | 15.86 |   556.84 |  16/5 yrs  |   —   |         — |       — |          — |


ELECTRICAL (set 1) -

|     # | DESCRIPTION                                           |    QTY | UNIT |    TAX | O\&P |    RCV |  AGE/LIFE  | COND. | DEP% |  DEPREC. |        ACV |
| ----: | ----------------------------------------------------- | -----: | :--: | -----: | ---: | -----: | :--------: | :---: | ---: | -------: | ---------: |
| 1,050 | Megohmmeter check electrical circuits – avg residence |   1.00 |  EA  | 732.72 | 0.00 | 879.26 |    16/NA   |  Avg. |   0% |   (0.00) | **879.26** |
| 1,051 | R\&R Ceiling fan & light – Std grade                  |   1.00 |  EA  | 293.41 | 3.90 | 356.77 |  16/20 yrs |  Avg. |  16% | (102.08) | **134.03** |
| 1,052 | R\&R Recessed light fixture                           |   2.00 |  EA  | 138.63 | 4.26 | 337.84 |  16/20 yrs |  Avg. |  16% |  (53.77) | **284.07** |
| 1,053 | R\&R Rewire – avg residence – copper wiring           | 175.74 |  SF  |   3.61 | 3.59 | 765.61 | 16/100 yrs |  Avg. |   0% |   (0.00) | **765.61** |
| 1,054 | R\&R Smoke detector – Std grade                       |   1.00 |  EA  |  50.41 | 0.99 |  61.68 |  16/10 yrs |  Avg. |  64% |  (39.39) |  **22.29** |
| 1,055 | R\&R Thermostat – Std grade                           |   1.00 |  EA  |  85.52 | 2.03 | 105.07 |  16/35 yrs |  Avg. |  64% |  (67.59) |  **37.48** |
| 1,056 | R\&R Cold air return cover – Large                    |   1.00 |  EA  |  36.93 | 0.95 |  45.46 |  16/25 yrs |  Avg. |  64% |  (29.10) |  **16.36** |
| 1,057 | R\&R Heat/AC register – mechanically attached         |   2.00 |  EA  |  23.79 | 1.08 |  58.40 |  16/25 yrs |  Avg. |  64% |  (37.95) |  **20.45** |


FLOORS (set 1) 

|     # | DESCRIPTION                                  |    QTY | UNIT |  TAX |  O\&P |      RCV |  AGE/LIFE  | COND. |   DEP% |  DEPREC. |        ACV |
| ----: | -------------------------------------------- | -----: | :--: | ---: | ----: | -------: | :--------: | :---: | -----: | -------: | ---------: |
| 1,058 | R\&R Vapor barrier – visqueen – 6 mil        | 175.74 |  SF  | 0.35 |  0.63 |    74.56 | 16/150 yrs |  Avg. | 10.67% |   (7.11) |  **67.45** |
| 1,059 | R\&R Laminate – simulated wood – Std grade\* | 175.74 |  SF  | 5.52 | 22.04 | 1,190.55 |  16/25 yrs |  Avg. |    64% | (761.95) | **428.60** |
| 1,060 | Final cleaning – construction – Residential  | 175.74 |  SF  | 0.19 |  2.40 |    42.47 |    16/NA   |  Avg. |     0% |   (0.00) |  **42.47** |


INSULATION & SEALING (set 2)

|     # | DESCRIPTION                                          |    QTY | UNIT |  TAX | O\&P |    RCV |  AGE/LIFE  | COND. |      DEP% |  DEPREC. |        ACV |
| ----: | ---------------------------------------------------- | -----: | :--: | ---: | ---: | -----: | :--------: | :---: | --------: | -------: | ---------: |
| 1,063 | R\&R Batt insulation – 4" – R13 – unfaced batt       | 234.00 |  SF  | 0.83 | 5.34 | 239.48 | 16/150 yrs |  Avg. |    10.67% |  (25.62) | **213.86** |
| 1,064 | Seal stud wall for odor control                      | 549.66 |  SF  | 0.75 | 5.61 | 501.44 |  16/15 yrs |  Avg. | 100% \[M] | (417.86) |  **83.58** |
| 1,065 | Seal floor or ceiling joist system                   | 172.01 |  SF  | 1.07 | 2.27 | 223.60 |  16/15 yrs |  Avg. | 100% \[M] | (186.32) |  **37.28** |
| 1,066 | Seal walls & ceiling w/ latex stain blocker – 1 coat | 721.67 |  SF  | 0.39 | 2.60 | 340.87 |  16/15 yrs |  Avg. | 100% \[M] | (284.05) |  **56.82** |


DOORS / TRIM (set 2) -

|     # | DESCRIPTION                                         |    QTY | UNIT |    TAX |  O\&P |    RCV |  AGE/LIFE  | COND. |      DEP% |  DEPREC. |        ACV |
| ----: | --------------------------------------------------- | -----: | :--: | -----: | ----: | -----: | :--------: | :---: | --------: | -------: | ---------: |
| 1,067 | R\&R Interior door – Colonist – pre-hung unit       |   2.00 |  EA  | 220.73 | 18.24 | 551.62 | 16/100 yrs |  Avg. |       16% |  (67.55) | **484.07** |
| 1,068 | Paint door/window trim & jamb – 2 coats (per side)  |   2.00 |  EA  |  26.65 |  0.47 |  64.53 |  16/15 yrs |  Avg. | 100% \[M] |  (53.77) |  **10.76** |
| 1,069 | Detach & reset door knob – interior – Std grade     |   2.00 |  EA  |  18.46 |  0.00 |  44.30 |  0/20 yrs  |  Avg. |        0% |   (0.00) |  **44.30** |
| 1,070 | R\&R Exterior door – metal – insulated – Std grade  |   1.00 |  EA  | 273.89 | 10.65 | 341.46 | 16/100 yrs |  Avg. |       16% |  (42.09) | **299.37** |
| 1,071 | Exterior – seal/prime then paint – two finish coats | 549.66 |  SF  |   1.35 | 13.19 | 906.27 |  16/15 yrs |  Avg. | 100% \[M] | (755.23) | **151.04** |
| 1,072 | R\&R Window stool & apron                           |   0.00 |  LF  |   7.85 |  0.00 |   0.00 | 16/150 yrs |   —   |         — |        — |   **0.00** |
| 1,073 | Seal & paint window stool & apron                   |   2.08 |  LF  |   3.40 |  0.04 |   8.53 |  16/15 yrs |   —   |         — |        — |   **1.42** |
| 1,074 | R\&R Window blind – PVC – 2" – 14.1–20 SF           |   1.00 |  EA  | 112.04 |  3.96 | 139.22 |  16/5 yrs  |   —   |         — |        — |  **33.29** |


CABINETS -
|     # | DESCRIPTION                                          |   QTY | UNIT |   TAX |  O&P |      RCV | AGE/LIFE | NOTES                      |          ACV |
| ----: | ---------------------------------------------------- | ----: | :--: | ----: | ----: | -------: | :------: | :------------------------- | -----------: |
| 1,075 | Cabinetry – lower (base) – Detach & reset            | 23.00 |  LF  | 57.55 |  0.00 | 1,588.39 |   16/NA  | cabinets need cleaning     | **1,588.39** |
| 1,076 | Clean cabinetry – lower – inside & out               | 23.00 |  LF  | 12.51 | 20.83 |   366.12 |   16/NA  | —                          |   **366.12** |
| 1,077 | Cabinetry – upper (wall) – Detach & reset            | 13.00 |  LF  | 49.23 |  0.00 |   767.99 |   16/NA  | removed to replace drywall |   **767.99** |
| 1,078 | Clean cabinetry – upper – inside & out               | 13.00 |  LF  | 12.51 | 11.77 |   206.94 |   16/NA  | —                          |   **206.94** |
| 1,079 | Detach & reset countertop – flat-laid PL – Std grade | 31.00 |  LF  | 16.19 |  0.00 |   602.27 | 0/15 yrs | —                          |   **602.27** |


ELECTRICAL & CLEANING (set 3 excerpts)

|     # | DESCRIPTION                                      |       QTY | UNIT |    TAX |  O&P |    RCV |  AGE/LIFE  | COND. |      DEP% |  DEPREC. |        ACV |
| ----: | ------------------------------------------------ | --------: | :--: | -----: | ----: | -----: | :--------: | :---: | --------: | -------: | ---------: |
| 1,080 | R\&R Rewire – avg residence – copper wiring      |    175.74 |  SF  |   3.61 |  3.59 | 765.61 | 16/100 yrs |  Avg. |        0% |   (0.00) | **663.53** |
| 1,081 | R\&R Smoke detector – Std grade                  |      1.00 |  EA  |  50.41 |  0.99 |  61.68 |  16/10 yrs |  Avg. | 100% \[M] |  (43.47) |  **18.21** |
| 1,082 | R\&R Heat/AC register – mechanically attached    |      2.00 |  EA  |  23.79 |  1.08 |  58.40 |  16/25 yrs |  Avg. |       64% |  (30.46) |  **27.94** |
| 1,083 | R\&R Fluorescent – 2-tube – 4' fixture w/ lens   |      1.00 |  EA  | 126.37 |  3.60 | 155.95 |  16/20 yrs |  Avg. |       80% | (124.76) |  **31.19** |
| 1,084 | R\&R Light fixture – Std grade                   |      1.00 |  EA  |  63.96 |  1.03 |  77.97 |  16/20 yrs |  Avg. |       80% |  (62.38) |  **15.59** |
| 1,085 | R\&R Phone/TV/speaker outlet                     |      1.00 |  EA  |  23.95 |  0.31 |  29.12 |  16/25 yrs |  Avg. |       64% |  (18.96) |  **10.16** |
| 1,086 | Clean floor – Heavy                              |    175.74 |  SF  |   0.58 |  7.45 | 129.78 |    16/NA   |  Avg. |        0% |   (0.00) | **129.78** |
| 1,087 | Clean refrigerator – exterior – Heavy            |      1.00 |  EA  |  24.37 |  1.78 |  31.03 |    16/NA   |  Avg. |        0% |   (0.00) |  **31.03** |
| 1,088 | Clean dishwasher – exterior – Heavy              |      1.00 |  EA  |  15.95 |  1.15 |  20.30 |    16/NA   |  Avg. |        0% |   (0.00) |  **20.30** |
| 1,089 | Clean range hood – Heavy                         |      1.00 |  EA  |  21.06 |  1.52 |  26.80 |    16/NA   |  Avg. |        0% |   (0.00) |  **26.80** |
| 1,090 | Clean range – exterior – Heavy                   |      1.00 |  EA  |  38.52 |  2.81 |  49.03 |    16/NA   |  Avg. |        0% |   (0.00) |  **49.03** |
| 1,091 | Clean door hardware – Heavy                      |      2.00 |  EA  |   7.92 |  1.16 |  20.16 |    16/NA   |  Avg. |        0% |   (0.00) |  **20.16** |
| 1,092 | Clean countertop – Heavy                         |     58.00 |  SF  |   0.83 |  3.54 |  61.32 |    16/NA   |  Avg. |        0% |   (0.00) |  **61.32** |
| 1,093 | Clean ductwork – interior – Heavy (per register) |     14.00 |  EA  |  38.83 | 39.21 | 691.57 |    16/NA   |  Avg. |        0% |   (0.00) | **691.57** |
| 1,094 | Deodorize building – Ozone & hydroxyl            | 10,550.00 |  CF  |   0.04 | 30.38 | 536.78 |    16/NA   |  Avg. |        0% |   (0.00) | **536.78** |


FLOORS (set 2)

|     # | DESCRIPTION                        |    QTY | UNIT |  TAX |  O\&P |    RCV |  AGE/LIFE | COND. |      DEP% | DEPREC. |        ACV |
| ----: | ---------------------------------- | -----: | :--: | ---: | ----: | -----: | :-------: | :---: | --------: | ------: | ---------: |
| 1,095 | Seal underlayment for odor control | 175.74 |  SF  | 0.51 |  0.74 | 108.43 | 16/15 yrs |  Avg. | 100% \[M] | (90.37) |  **18.06** |
| 1,096 | R\&R Carpet pad – Std grade        | 175.74 |  SF  | 0.51 |  3.48 | 111.73 | 16/10 yrs |  Avg. | 100% \[M] | <73.78> |  **37.95** |
| 1,097 | Clean walls & ceiling – Heavy      | 721.67 |  SF  | 0.39 | 20.72 | 358.55 |   16/NA   |  Avg. |        0% |  (0.00) | **358.55** |


PAINT (set 2)
|     # | DESCRIPTION                                          |    QTY | UNIT |   TAX | O\&P |    RCV |  AGE/LIFE | COND. |      DEP% |  DEPREC. |        ACV |
| ----: | ---------------------------------------------------- | -----: | :--: | ----: | ---: | -----: | :-------: | :---: | --------: | -------: | ---------: |
| 1,103 | Mask & prep for paint – plastic/paper/tape (per LF)  |  68.57 |  LF  |  1.21 | 1.07 | 100.86 | 16/15 yrs |  Avg. |        0% |   (0.00) | **100.86** |
| 1,104 | Seal walls & ceiling w/ latex stain blocker – 1 coat | 721.67 |  SF  |  0.52 | 3.03 | 453.96 | 16/15 yrs |  Avg. | 100% \[M] | (378.30) |  **75.66** |
| 1,105 | Paint walls & ceiling – 2 coats                      | 721.67 |  SF  |  0.82 | 8.66 | 720.53 | 16/15 yrs |  Avg. | 100% \[M] | (600.43) | **120.10** |
| 1,106 | Paint casing – 2 coats                               |  68.00 |  LF  |  1.24 | 0.49 | 101.77 | 16/15 yrs |  Avg. | 100% \[M] |  (84.81) |  **16.96** |
| 1,107 | Paint door slab only – 2 coats (per side)            |   1.00 |  EA  | 31.79 | 0.39 |  38.62 | 16/15 yrs |  Avg. | 100% \[M] |  (32.18) |   **6.44** |


ELECTRICAL (set 4) - 
|     # | DESCRIPTION                                           |  QTY | UNIT |    TAX | O\&P |    RCV |  AGE/LIFE | COND. | DEP% |  DEPREC. |        ACV |
| ----: | ----------------------------------------------------- | ---: | :--: | -----: | ---: | -----: | :-------: | :---: | ---: | -------: | ---------: |
| 1,108 | Megohmmeter check electrical circuits – avg residence | 1.00 |  EA  | 732.72 | 0.00 | 879.26 |   16/NA   |  Avg. |   0% |   (0.00) | **879.26** |
| 1,109 | R\&R Smoke detector – Std grade                       | 3.00 |  EA  |  50.41 | 2.97 | 185.04 | 16/10 yrs |  Avg. |  64% | (130.41) |  **54.63** |
| 1,110 | R\&R Cold air return cover – Large                    | 1.00 |  EA  |  36.93 | 0.95 |  45.46 | 16/25 yrs |  Avg. |  64% |  (20.22) |  **25.24** |
| 1,111 | R\&R Heat/AC register – mechanically attached         | 2.00 |  EA  |  23.79 | 1.08 |  58.40 | 16/25 yrs |  Avg. |  64% |  (30.46) |  **27.94** |
| 1,112 | R\&R Light fixture                                    | 1.00 |  EA  |  79.82 | 1.98 |  98.16 | 16/20 yrs |  Avg. |  80% |  (78.77) |  **19.39** |


FLOORS (set 3) - 
|     # | DESCRIPTION                                   |    QTY | UNIT |  TAX | O\&P |    RCV |  AGE/LIFE | COND. | DEP% |  DEPREC. |       ACV |
| ----: | --------------------------------------------- | -----: | :--: | ---: | ---: | -----: | :-------: | :---: | ---: | -------: | --------: |
| 1,113 | R\&R Carpet pad – Std grade                   | 175.74 |  SF  | 0.51 | 3.48 | 111.73 | 16/10 yrs |  Avg. |  64% |  (71.10) | **40.63** |
| 1,114 | Carpet – Std grade *(+15% waste)*             |  59.46 |  SF  | 2.34 | 6.35 | 174.59 | 16/10 yrs |  Avg. |  64% | (111.74) | **62.85** |
| 1,115 | Step charge – “waterfall” carpet installation |  16.00 |  EA  | 6.76 | 0.43 | 130.31 | 16/10 yrs |  Avg. |  80% | (104.59) | **25.72** |


CLEAN (set 4) - 
|     # | DESCRIPTION                                            |    QTY | UNIT |   TAX |  O&P |    RCV |  AGE/LIFE | COND. | DEP% | DEPREC. |        ACV |
| ----: | ------------------------------------------------------ | -----: | :--: | ----: | ----: | -----: | :-------: | :---: | ---: | ------: | ---------: |
| 1,116 | Clean walls & ceiling                                  | 721.67 |  SF  |  0.30 | 16.05 | 275.93 |   16/NA   |  Avg. |   0% |  (0.00) | **275.93** |
| 1,117 | Clean trim – wood                                      |  60.00 |  LF  |  0.28 |  1.21 |  21.37 |   16/NA   |  Avg. |   0% |  (0.00) |  **21.37** |
| 1,118 | Clean light fixture                                    |   1.00 |  EA  |  9.00 |  0.65 |  11.45 |   16/NA   |  Avg. |   0% |  (0.00) |  **11.45** |
| 1,119 | Clean outlet or switch                                 |   1.00 |  EA  |  2.95 |  0.22 |   3.77 |   16/NA   |  Avg. |   0% |  (0.00) |   **3.77** |
| 1,120 | Clean baseboard                                        |  68.93 |  LF  |  0.30 |  1.53 |  26.35 |   16/NA   |  Avg. |   0% |  (0.00) |  **26.35** |
| 1,121 | R\&R Stairway – stringers, treads & risers (per tread) |   1.00 |  EA  | 78.14 |  1.16 |  95.16 | 16/50 yrs |  Avg. |  32% | (20.57) |  **74.59** |


DRYWALL / PAINT (set 5) - 
|     # | DESCRIPTION                                         |    QTY | UNIT |   TAX | O\&P |    RCV |  AGE/LIFE  | COND. |      DEP% |  DEPREC. |        ACV |
| ----: | --------------------------------------------------- | -----: | :--: | ----: | ---: | -----: | :--------: | :---: | --------: | -------: | ---------: |
| 1,122 | Mask & prep for paint – plastic/paper/tape (per LF) |  68.57 |  LF  |  1.21 | 1.07 | 100.86 |  16/15 yrs |  Avg. |        0% |   (0.00) | **100.86** |
| 1,123 | Drywall patch / small repair – ready for paint      |   3.00 |  EA  | 65.18 | 0.50 | 235.24 | 16/150 yrs |  Avg. |    10.67% |  (20.91) | **214.33** |
| 1,124 | Seal walls w/ latex stain blocker – 1 coat          | 549.66 |  SF  |  0.52 | 2.31 | 345.75 |  16/15 yrs |  Avg. | 100% \[M] | (288.13) |  **57.62** |
| 1,125 | Paint walls & ceiling – 1 coat                      | 721.67 |  SF  |  0.56 | 4.76 | 490.68 |  16/15 yrs |  Avg. | 100% \[M] | (408.90) |  **81.78** |
| 1,126 | Paint casing – 1 coat                               |  51.00 |  LF  |  0.83 | 0.24 |  51.07 |  16/15 yrs |  Avg. | 100% \[M] |  (42.57) |   **8.50** |


SKETCH6 (Room Package) - 
Sketch: 19' 7" · Floor 315.28 SF (35.03 SY) · Walls 569.33 SF · Walls+Ceiling 884.61 SF · Floor Perimeter 71.17 LF · Ceiling Perimeter 71.17 LF

|     # | DESCRIPTION                                            |    QTY | UNIT |    TAX |  O\&P |      RCV |  AGE/LIFE | COND. | DEP% | DEPREC. |          ACV |
| ----: | ------------------------------------------------------ | -----: | :--: | -----: | ----: | -------: | :-------: | :---: | ---: | ------: | -----------: |
| 1,127 | R\&R Batt insulation – 6" – R19 – paper/foil faced     | 116.00 |  SF  |   2.01 |  6.96 |   288.16 | 0/150 yrs |  Avg. |   0% |  (0.00) |   **288.16** |
| 1,128 | Apply anti-microbial agent to the floor                | 315.28 |  SF  |   0.36 |  9.40 |   145.82 |    0/NA   |  Avg. |   0% |  (0.00) |   **145.82** |
| 1,129 | Clean the walls                                        | 569.33 |  SF  |   0.48 | 20.04 |   348.04 |    0/NA   |  Avg. |   0% |  (0.00) |   **348.04** |
| 1,130 | Paint the walls – 2 coats                              | 569.33 |  SF  |   1.30 |  9.91 |   900.04 |  0/15 yrs |  Avg. |   0% |  (0.00) |   **900.04** |
| 1,131 | Clean door – bifold set (per side)                     |   1.00 |  EA  |  18.97 |  1.40 |    24.17 |    0/NA   |  Avg. |   0% |  (0.00) |    **24.17** |
| 1,132 | Paint bifold door set – slab only – 2 coats (per side) |   1.00 |  EA  |  66.95 |  1.15 |    81.74 |  0/15 yrs |  Avg. |   0% |  (0.00) |    **81.74** |
| 1,133 | R\&R Bifold door set – Colonist – Double               |   1.00 |  EA  | 362.26 | 13.23 |   450.59 | 0/100 yrs |  Avg. |   0% |  (0.00) |   **450.59** |
| 1,134 | R\&R Casing – 3 1/4"                                   |  17.00 |  LF  |   4.41 |  2.68 |    93.19 | 0/150 yrs |  Avg. |   0% |  (0.00) |    **93.19** |
| 1,197 | Remove carpet                                          | 315.28 |  SF  |   0.33 |  0.00 |   124.84 |  0/10 yrs |  Avg. |    — |  (0.00) |   **124.84** |
| 1,135 | Carpet *(+15% waste)*                                  | 362.57 |  SF  |   3.91 | 64.61 | 1,778.72 |  0/10 yrs |  Avg. |   0% |  (0.00) | **1,778.72** |
| 1,136 | R\&R Carpet pad                                        | 315.28 |  SF  |   0.82 | 10.22 |   322.49 |  0/10 yrs |  Avg. |   0% |  (0.00) |   **322.49** |
| 1,137 | R\&R Tackless strip – per LF                           |  71.17 |  LF  |   1.40 |  0.47 |   120.12 |  0/10 yrs |  Avg. |   0% |  (0.00) |   **120.12** |
| 1,138 | Clean concrete floor                                   | 315.28 |  SF  |   0.40 |  9.29 |   160.66 |    0/NA   |  Avg. |   0% |  (0.00) |   **160.66** |
| 1,139 | Clean baseboard                                        |  71.17 |  LF  |   0.49 |  2.55 |    44.40 |    0/NA   |  Avg. |   0% |  (0.00) |    **44.40** |
| 1,140 | R\&R Baseboard – 3 1/4"                                |  71.17 |  LF  |   4.88 |  9.10 |   427.69 | 0/150 yrs |  Avg. |   0% |  (0.00) |   **427.69** |
| 1,141 | Seal & paint baseboard – 1 coat each                   |  71.17 |  LF  |   2.05 |  0.64 |   175.84 |  0/15 yrs |  Avg. |   0% |  (0.00) |   **175.84** |
| 1,142 | Clean door/window opening (per side)                   |   1.00 |  EA  |  20.04 |  1.44 |    25.48 |    0/NA   |  Avg. |   0% |  (0.00) |    **25.48** |
| 1,143 | Seal & paint door/window opening (per side)            |   1.00 |  EA  |  42.94 |  0.37 |    51.97 |  0/15 yrs |  Avg. |   0% |  (0.00) |    **51.97** |
| 1,144 | Contents – move out then reset – extra large room      |   1.00 |  EA  | 226.88 |  0.00 |   272.26 |    0/NA   |  Avg. |   0% |  (0.00) |   **272.26** |
| 1,145 | R\&R Refrigerator – top freezer – 18–22 cf             |   1.00 |  EA  | 970.35 | 54.00 | 1,229.23 |  0/14 yrs |  Avg. |   0% |  (0.00) | **1,229.23** |
| 1,146 | Heat/AC register – mechanically attached – D\&R        |   2.00 |  EA  |  16.16 |  0.00 |    38.78 |    0/NA   |  Avg. |   0% |  (0.00) |    **38.78** |
| 1,147 | R\&R Wallpaper border                                  |  71.17 |  LF  |   4.66 |  6.36 |   405.61 |  0/7 yrs  |  Avg. |   0% |  (0.00) |   **405.61** |
| 1,148 | Window drapery – hardware – D\&R                       |   3.00 |  EA  |  42.96 |  0.00 |   154.66 |    0/NA   |  Avg. |   0% |  (0.00) |   **154.66** |
| 1,149 | Smoke detector – D\&R                                  |   1.00 |  EA  |  54.36 |  0.00 |    65.24 |    0/NA   |  Avg. |   0% |  (0.00) |    **65.24** |
| 1,150 | Tear out tackless strip & bag for disposal             |  71.17 |  LF  |   1.28 |  0.30 |   109.68 |    0/NA   |  Avg. |    — |  (0.00) |   **109.68** |


# Building From Scrach - 

- This is for estimates that calcualtes cost of the constructions cost to build a new house or building. this is mainly for the foundations, frames and preperation jobs.


|  # | DESCRIPTION                                             | QTY    | UNIT |    TAX |  O&P |      RCV |  AGE/LIFE | COND. | DEP% | DEPREC. |          ACV |
| -: | ------------------------------------------------------- | ------ | :--: | -----: | ----: | -------: | :-------: | :---: | ---: | ------: | -----------: |
|  1 | 2" × 4" × 10' #2 & better Fir/Larch (material only)     | 3.00   |  EA  |   6.48 |  1.17 |    24.73 | 0/150 yrs |  Avg. |   0% |  (0.00) |    **24.73** |
|  2 | 2" × 4" × 8' #2 & better Fir/Larch (material only)      | 39.00  |  EA  |   5.18 | 12.12 |   256.96 | 0/150 yrs |  Avg. |   0% |  (0.00) |   **256.96** |
|  3 | 2" × 4" × 92 5/8" pre-cut stud (for 8' wall, mat only)  | 76.00  |  EA  |   5.02 | 22.89 |   485.29 | 0/150 yrs |  Avg. |   0% |  (0.00) |   **485.29** |
|  4 | R\&R Sheathing – OSB – 1/2"                             | 456.00 |  SF  |   2.30 | 15.60 | 1,277.28 | 0/150 yrs |  Avg. |   0% |  (0.00) | **1,277.28** |
|  5 | R\&R Labor to frame 2" × 4" non-bearing wall – 16" o.c. | 520.33 |  SF  |   2.07 |  0.94 | 1,293.63 | 0/150 yrs |  Avg. |   0% |  (0.00) | **1,293.63** |
|  6 | R\&R I-joist – 9 1/2" deep – 1 3/4" flange              | 127.42 |  LF  |   6.39 | 18.20 |   998.92 | 0/150 yrs |  Avg. |   0% |  (0.00) |   **998.92** |
|  7 | R\&R Rim joist – engineered – 1-1/8" × 9-1/2"           | 50.67  |  LF  |   4.11 |  7.17 |   258.51 | 0/150 yrs |  Avg. |   0% |  (0.00) |   **258.51** |
|  8 | R\&R Sheathing – OSB – 3/4" – tongue & groove           | 192.00 |  SF  |   4.35 | 13.02 | 1,017.86 | 0/150 yrs |  Avg. |   0% |  (0.00) | **1,017.86** |
|  9 | R\&R Drilled bottom plate – 2" × 4" treated lumber      | 52.00  |  LF  |  13.46 |  2.84 |   843.30 | 0/150 yrs |  Avg. |   0% |  (0.00) |   **843.30** |
| 10 | R\&R Footings – labor and materials                     | 3.55   |  CY  | 838.32 | 40.20 | 3,619.47 | 0/200 yrs |  Avg. |   0% |  (0.00) | **3,619.47** |
| 11 | Steel rebar – J-bar – #4, 2' 6"                         | 67.00  |  EA  |   5.82 |  4.70 |   473.56 | 0/150 yrs |  Avg. |   0% |  (0.00) |   **473.56** |
| 12 | R\&R Steel rebar – #4 (1/2")                            | —      |   —  |      — |     — |        — |     —     |   —   |    — |       — |            — |

__Roof__

|  # | DESCRIPTION                                             | QTY    | UNIT |   TAX |  O\&P |      RCV |  AGE/LIFE | COND. | DEP% | DEPREC. |        ACV |
| -: | ------------------------------------------------------- | ------ | :--: | ----: | ----: | -------: | :-------: | :---: | ---: | ------: | ---------: |
| 13 | R&R Truss – 4/12 slope                                 | 72.33  |  LF  | 10.63 | 23.57 |   950.92 | 0/150 yrs |  Avg. |   0% |  (0.00) | **950.92** |
| 14 | R&R Sheathing – OSB – 1/2"                             | 178.14 |  SF  |  2.30 |  6.09 | 498.98\* | 0/150 yrs |  Avg. |   0% |  (0.00) | **498.98** |
| 15 | 2" × 4" × 12' #2 & better Fir/Larch (material only)     | 2.00   |  EA  |  7.81 |  0.94 |    19.86 | 0/150 yrs |  Avg. |   0% |  (0.00) |  **19.86** |
| 16 | 2" × 4" × 8' #2 & better Fir/Larch (material only)      | 4.00   |  EA  |  5.18 |  1.24 |    26.34 | 0/150 yrs |  Avg. |   0% |  (0.00) |  **26.34** |
| 17 | R&R Sheathing – OSB – 1/2"                             | 17.80  |  SF  |  2.30 |  0.61 |    49.85 | 0/150 yrs |  Avg. |   0% |  (0.00) |  **49.85** |
| 18 | R&R Labor to frame 2" × 4" non-bearing wall – 16" o.c. | —      |   —  |     — |     — |        — |     —     |   —   |    — |       — |          — |


DESCRIPTION | QTY |  RESET |  REMOVE | REPLACE | TAX | TOTAL

# Chimney

The following line item(s) account for repairing/replacing the masonry chimney on the roof, front, right, back, side.
    
|  # | DESCRIPTION                                             |    QTY | UNIT | RESET | REMOVE |  REPLACE |   TAX |        TOTAL |
| -: | ------------------------------------------------------- | -----: | :--: | ----: | -----: | -------: | ----: | -----------: |
| 34 | R&R Masonry chimney and flue                           |   1.00 |  LF  |     — |      — |   529.92 |  8.11 |   **621.37** |
| 36 | R&R Zero-clearance chimney framing (per vertical LF)   |   1.00 |  LF  |     — |      — |    75.73 |  1.68 |   **116.25** |
| 37 | Add for tall masonry chimney over 15' (per vertical LF) |   1.00 |  LF  |     — |      — |   529.92 |  8.11 |   **621.37** |
| 38 | Block chimney w/ 8"×8" flue liner (per vertical LF)     |   1.00 |  LF  |     — |      — |    58.58 |  1.08 |    **72.17** |
| 40 | Block chimney w/ 8"×12" flue liner (per vertical LF)    |   1.00 |  LF  |     — |      — |    67.56 |  1.34 |    **81.41** |
| 41 | Block chimney w/ 12"×12" flue liner (per vertical LF)   |   1.00 |  LF  |     — |      — |    82.59 |  1.95 |    **97.05** |
| 42 | Fireplace – chimney cap (concrete)                      |   1.00 |  EA  |     — |      — |   348.70 |  2.75 |   **398.37** |
| 43 | Chimney flashing – average (32"×36")                    |   1.00 |  EA  |     — |      — |   589.98 |  6.80 |   **620.23** |
| 45 | Chimney flashing – small (24"×24")                      |   1.00 |  EA  |     — |      — |   468.81 |  3.80 |   **488.25** |
| 46 | Chimney flashing – large (32"×60")                      |   1.00 |  EA  |     — |      — |   779.95 |  9.75 |   **820.98** |
| 47 | Fireplace – chimney chase cover (sheet metal)           |   1.00 |  EA  |     — |      — |   523.34 | 12.72 |   **559.51** |
| 48 | Fireplace – chimney chase cover (stainless steel)       |   1.00 |  EA  |     — |      — |   666.34 | 21.30 |   **711.09** |
| 49 | Fireplace – chimney chase cover (copper)                |   1.00 |  EA  |     — |      — |   962.34 | 39.06 | **1,024.85** |
| 50 | Chimney flashing – average (32"×36") – copper           |   1.00 |  EA  |     — |      — |   911.40 | 26.08 |   **960.93** |
| 51 | Chimney flashing – small (24"×24") – copper             |   1.00 |  EA  | 15.64 |      — |   645.60 | 14.41 |   **675.65** |
| 52 | Chimney flashing – large (32"×60") – copper             |   1.00 |  EA  | 31.28 |      — | 1,314.35 | 41.81 | **1,387.44** |
| 53 | Decorative chimney shroud – metal                       |   1.00 |  EA  | 31.28 |      — |   820.32 | 42.68 |   **894.28** |
| 54 | Decorative chimney shroud – copper                      |   1.00 |  EA  | 31.28 |      — | 1,656.51 | 92.85 | **1,780.64** |
| 55 | Paint brick                                             | 384.00 |  SF  |     — |      — |   392.52 |  8.52 |   **392.52** |
| 57 | Seal brick w/ masonry sealer                            | 384.00 |  SF  |     — |      — |   408.81 |  9.45 |   **408.81** |
  
____

# Deck

The following line item(s) account for repairs to the wood deck(s) on the front, right, back, and left side(s)"

|  # | DESCRIPTION                                              |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| -: | -------------------------------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 58 | R&R 2" × 8" lumber – treated (1.33 BF per LF)            | 1.00 |  LF  |  1.03 |      — |    4.66 | 0.11 |   **5.80** |
| 60 | R&R 2" × 10" lumber – treated (1.67 BF per LF)           | 1.00 |  LF  |  1.18 |      — |    5.23 | 0.14 |   **6.55** |
| 61 | R&R 2" × 12" lumber – treated (2 BF per LF)              | 1.00 |  LF  |  1.36 |      — |    6.39 | 0.19 |   **7.94** |
| 62 | R&R Deck planking – 5/4" cedar (per BF)                  | 1.00 |  BF  |  2.00 |      — |   11.50 | 0.41 |  **13.91** |
| 63 | R&R Deck planking – redwood (per BF)                     | 1.00 |  BF  |  1.25 |      — |   11.55 | 0.52 |  **13.32** |
| 64 | R&R Deck planking – 2×6 wood polymer lumber (per SF)     |    — |  SF  |  2.50 |      — |   24.27 | 0.00 |   **0.00** |
| 65 | R&R 1/2" × 12" wood polymer lumber                       |    — |  LF  |  1.41 |      — |   13.60 | 0.00 |   **0.00** |
| 66 | R&R 1/2" × 8" wood polymer lumber                        |    — |  LF  |  1.25 |      — |    9.96 | 0.00 |   **0.00** |
| 67 | R&R Deck guard rail – cedar                              | 1.00 |  LF  |  1.41 |      — |   71.32 | 2.43 |  **75.16** |
| 68 | R&R Deck guard rail – redwood                            | 1.00 |  LF  |  1.41 |      — |   76.55 | 2.74 |  **80.70** |
| 69 | R&R Deck guard rail – wood polymer lumber                | 1.00 |  LF  |  5.61 |      — |   77.18 | 2.78 |  **85.57** |
| 70 | R&R Post – wood – 4" × 4" fence grade cedar or equal     | 1.00 |  EA  | 18.77 |      — |   86.58 | 3.12 | **108.47** |
| 72 | R&R 4" × 4" wood post – redwood (1.33 BF per LF)         | 1.00 |  LF  |  1.96 |      — |   14.83 | 0.62 |  **17.41** |
| 73 | R&R 4" × 4" post – wood polymer lumber (1.33 BF per LF)  | 1.00 |  LF  |  2.67 |      — |   19.28 | 0.78 |  **22.73** |

- Deck Staining -

|  # | DESCRIPTION                        |    QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| -: | ---------------------------------- | -----: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 74 | Contents – move out then reset     |   1.00 |  EA  |  0.00 |      — |   89.09 | 0.00 |  **89.09** |
| 76 | Clean with pressure/chemical spray |   1.00 |  SF  |  0.00 |      — |    0.51 | 0.00 |   **0.51** |
| 78 | Stain/finish deck                  | 384.00 |  SF  |  0.00 |      — |    1.14 | 7.14 | **444.90** |
| 79 | Stain/finish deck handrail         |   1.00 |  LF  |  0.00 |      — |    8.41 | 0.11 |   **8.52** |

# exterior doors

The following line item(s) account for replacing the exterior door(s) listed below."

|  # | DESCRIPTION                                          |  QTY | UNIT | RESET | REMOVE |  REPLACE |   TAX |        TOTAL |
| -: | ---------------------------------------------------- | ---: | :--: | ----: | -----: | -------: | ----: | -----------: |
| 80 | Exterior door slab – metal – insulated – flush/panel | 1.00 |  EA  | 23.40 |      — |   351.92 | 11.95 |   **377.27** |
| 82 | Exterior door – solid alder – paneled                | 1.00 |  EA  | 26.81 |      — | 1,593.40 | 88.27 | **1,708.48** |
| 83 | Exterior door – solid alder – paneled – slab only    | 1.00 |  EA  | 23.40 |      — | 1,014.53 | 51.71 | **1,079.64** |
| 84 | Exterior door – solid mahogany – paneled             | 1.00 |  EA  | 26.81 |      — | 1,716.97 | 95.69 | **1,839.47** |
| 85 | Exterior door – solid mahogany – paneled – slab only | 1.00 |  EA  | 23.40 |      — | 1,107.19 | 57.27 | **1,177.86** |
| 86 | Door lockset & deadbolt – exterior – Detach & reset  | 1.00 |  EA  |  0.00 |      — |    38.55 |  0.00 |    **38.55** |
| 88 | Door knob/lockset – Detach & reset                   | 1.00 |  EA  |  0.00 |      — |    27.54 |  0.00 |    **27.54** |


|  # | DESCRIPTION                            |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| -: | -------------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 89 | Seal & paint door slab only            | 2.00 |  EA  |  0.00 |      — |   44.91 | 1.21 |  **91.03** |
| 90 | Seal & paint door/window trim & jamb   | 2.00 |  EA  |  0.00 |      — |   37.49 | 0.73 |  **75.71** |
| 91 | Stain & finish door slab only          | 2.00 |  EA  |  0.00 |      — |   69.98 | 1.40 | **141.36** |
| 92 | Stain & finish door/window trim & jamb | 2.00 |  EA  |  0.00 |      — |   49.02 | 0.99 |  **99.03** |

|  # | DESCRIPTION              |  QTY | UNIT | RESET | REMOVE | REPLACE |   TAX |      TOTAL |
| -: | ------------------------ | ---: | :--: | ----: | -----: | ------: | ----: | ---------: |
| 93 | R\&R Storm door assembly | 1.00 |  EA  | 22.07 |      — |  347.24 | 12.59 | **381.90** |


# Carport

The following line item(s) account for repairs to the metal carport on the front, right, back, and left side. The following line item(s) account for replacing the metal carport on the front, right, back, and left side."

|  # | DESCRIPTION                     |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |     TOTAL |
| -: | ------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | --------: |
| 94 | R\&R Patio post – steel tube    | 1.00 |  LF  |  1.96 |      — |   14.97 | 0.64 | **17.57** |
| 96 | R\&R Patio post – aluminum tube | 1.00 |  LF  |  1.96 |      — |    8.31 | 0.24 | **10.51** |
| 97 | R\&R Patio post – scrolled      | 1.00 |  LF  |  1.96 |      — |   13.69 | 0.56 | **16.21** |

|   # | DESCRIPTION                                       |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |     TOTAL |
| --: | ------------------------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | --------: |
|  98 | R\&R Wall/roof panel – ribbed – 26 ga – up to 1"  | 1.00 |  SF  |  0.63 |      — |    4.93 | 0.14 |  **5.70** |
| 100 | R\&R Carport – freestanding metal – light load    | 1.00 |  SF  |  2.55 |      — |   13.74 | 0.35 | **16.64** |
| 101 | R\&R Carport – freestanding metal – moderate load | 1.00 |  SF  |  2.55 |      — |   16.26 | 0.50 | **19.31** |
| 102 | R\&R Carport – freestanding metal – heavy load    | 1.00 |  SF  |  2.55 |      — |   18.70 | 0.65 | **21.90** |

__

# awning

The following line item(s) account for replacing the metal awning(s) listed below:"

|   # | DESCRIPTION                                            |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |     TOTAL |
| --: | ------------------------------------------------------ | ---: | :--: | ----: | -----: | ------: | ---: | --------: |
| 103 | R\&R Awning – window/door – aluminum or steel          | 1.00 |  LF  |  1.15 |      — |   93.48 | 3.61 | **98.24** |
| 104 | R\&R Awning side panels – aluminum/steel (per set)     | 1.00 |  EA  |  9.08 |      — |   74.56 | 2.12 | **85.76** |
| 105 | Awning – aluminum or steel – add for each color stripe | 1.00 |  EA  |  0.00 |      — |    5.50 | 0.33 |  **5.83** |
| 106 | Paint aluminum awning                                  | 1.00 |  SF  |  0.00 |      — |    1.13 | 0.02 |  **1.15** |

__

# AC / HVAC

The following line item(s) accounts for repairs to the A/C condenser fins on the front, right, back, left side(s)."

|   # | DESCRIPTION                                                        |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | ------------------------------------------------------------------ | ---: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 107 | Comb & straighten A/C condenser fins — with trip charge            | 1.00 |  EA  |  0.00 |      — |  274.33 | 0.00 | **274.33** |
| 108 | Comb & straighten A/C condenser fins — without trip charge         | 1.00 |  EA  |  0.00 |      — |  117.52 | 0.00 | **117.52** |
| 109 | Comb & straighten A/C condenser fins — with trip charge — Large    | 1.00 |  EA  |  0.00 |      — |  326.34 | 0.00 | **326.34** |
| 110 | Comb & straighten A/C condenser fins — without trip charge — Large | 1.00 |  EA  |  0.00 |      — |  156.64 | 0.00 | **156.64** |


|   # | DESCRIPTION                                   |  QTY | UNIT | RESET | REMOVE |  REPLACE |    TAX |        TOTAL |
| --: | --------------------------------------------- | ---: | :--: | ----: | -----: | -------: | -----: | -----------: |
| 111 | R\&R Air conditioning security cage           | 1.00 |  EA  | 15.64 |      — |   353.92 |  14.40 |   **383.96** |
| 113 | Central air — condenser repair — fan guard    | 1.00 |  EA  |  0.00 |      — |   205.75 |   9.61 |   **215.36** |
| 114 | Central air — condenser unit — Detach & reset | 1.00 |  EA  |  0.00 |      — |   953.31 |   0.00 |   **953.31** |
| 115 | R\&R Condenser unit — 2 ton — up to 13 SEER   | 1.00 |  EA  | 52.27 |      — | 2,229.60 |  99.60 | **2,381.47** |
| 116 | R\&R Condenser unit — 2 ton — 14–15 SEER      | 1.00 |  EA  | 52.27 |      — | 2,473.00 | 114.20 | **2,639.47** |
| 117 | R\&R Condenser unit — 2 ton — 16–21 SEER      | 1.00 |  EA  | 52.27 |      — | 3,287.60 | 163.08 | **3,502.95** |
| 118 | R\&R Condenser unit — 2.5 ton — 14–15 SEER    | 1.00 |  EA  | 52.27 |      — | 2,511.06 | 116.49 | **2,679.82** |
| 119 | R\&R Condenser unit — 3 ton — up to 13 SEER   | 1.00 |  EA  | 52.27 |      — | 2,598.42 | 108.77 | **2,759.46** |
| 120 | R\&R Condenser unit — 3 ton — 14–15 SEER      | 1.00 |  EA  | 52.27 |      — | 3,229.61 | 146.64 | **3,428.52** |
| 121 | R\&R Condenser unit — 3 ton — 16–21 SEER      | 1.00 |  EA  | 52.27 |      — | 3,820.66 | 182.10 | **4,055.03** |
| 122 | R\&R Condenser unit — 3.5 ton — up to 13 SEER | 1.00 |  EA  | 52.27 |      — | 2,775.66 | 119.40 | **2,947.33** |
| 123 | R\&R Condenser unit — 3.5 ton — 14–15 SEER    | 1.00 |  EA  | 52.27 |      — | 3,302.93 | 151.04 | **3,506.24** |
| 124 | R\&R Condenser unit — 4 ton — up to 13 SEER   | 1.00 |  EA  | 52.27 |      — | 2,988.85 | 128.70 | **3,169.82** |
| 125 | R\&R Condenser unit — 4 ton — 14–15 SEER      | 1.00 |  EA  | 52.27 |      — | 3,383.85 | 152.40 | **3,588.52** |
| 126 | R\&R Condenser unit — 4 ton — 16–21 SEER      | 1.00 |  EA  | 52.27 |      — | 3,993.85 | 189.00 | **4,235.12** |
| 127 | R\&R Condenser unit — 5 ton — up to 13 SEER   | 1.00 |  EA  | 52.27 |      — | 3,457.71 | 152.78 | **3,662.76** |
| 128 | R\&R Condenser unit — 5 ton — 14–15 SEER      | 1.00 |  EA  | 52.27 |      — | 3,783.36 | 172.32 | **4,007.95** |
| 129 | R\&R Condenser unit — 5 ton — 16–21 SEER      | 1.00 |  EA  | 52.27 |      — | 4,578.36 | 220.02 | **4,850.65** |


|   # | DESCRIPTION                                       |  QTY | UNIT |  RESET | REMOVE |  REPLACE |    TAX |        TOTAL |
| --: | ------------------------------------------------- | ---: | :--: | -----: | -----: | -------: | -----: | -----------: |
| 130 | R\&R Central A/C system — 2 ton — up to 13 SEER   | 1.00 |  EA  | 173.44 |      — | 3,584.73 | 132.23 | **3,890.40** |
| 131 | R\&R Central A/C system — 2 ton — 14–15 SEER      | 1.00 |  EA  | 173.44 |      — | 3,828.13 | 146.84 | **4,148.41** |
| 132 | R\&R Central A/C system — 2 ton — 16–21 SEER      | 1.00 |  EA  | 173.44 |      — | 4,642.73 | 195.71 | **5,011.88** |
| 133 | R\&R Central A/C system — 2.5 ton — up to 13 SEER | 1.00 |  EA  | 173.44 |      — | 3,601.33 | 133.23 | **3,908.00** |
| 134 | R\&R Central A/C system — 2.5 ton — 14–15 SEER    | 1.00 |  EA  | 173.44 |      — | 3,866.20 | 149.12 | **4,188.76** |
| 135 | R\&R Central A/C system — 3 ton — up to 13 SEER   | 1.00 |  EA  | 173.44 |      — | 4,259.39 | 146.20 | **4,579.03** |
| 136 | R\&R Central A/C system — 3 ton — 14–15 SEER      | 1.00 |  EA  | 173.44 |      — | 4,890.58 | 184.07 | **5,248.09** |
| 137 | R\&R Central A/C system — 3 ton — 16–21 SEER      | 1.00 |  EA  | 173.44 |      — | 5,481.63 | 219.53 | **5,874.60** |
| 138 | R\&R Central A/C system — 3.5 ton — up to 13 SEER | 1.00 |  EA  | 173.44 |      — | 4,436.63 | 156.83 | **4,766.90** |
| 139 | R\&R Central A/C system — 3.5 ton — 14–15 SEER    | 1.00 |  EA  | 173.44 |      — | 4,963.90 | 188.47 | **5,325.81** |
| 140 | R\&R Central A/C system — 4 ton — up to 13 SEER   | 1.00 |  EA  | 173.44 |      — | 4,997.40 | 176.69 | **5,347.53** |
| 141 | R\&R Central A/C system — 4 ton — 14–15 SEER      | 1.00 |  EA  | 173.44 |      — | 5,392.40 | 200.39 | **5,766.23** |
| 142 | R\&R Central A/C system — 4 ton — 16–21 SEER      | 1.00 |  EA  | 173.44 |      — | 6,002.40 | 236.99 | **6,412.83** |
| 143 | R\&R Central A/C system — 5 ton — up to 13 SEER   | 1.00 |  EA  | 302.69 |      — | 5,738.33 | 207.60 | **6,248.62** |
| 144 | R\&R Central A/C system — 5 ton — 14–15 SEER      | 1.00 |  EA  | 302.69 |      — | 6,063.98 | 227.13 | **6,593.80** |
| 145 | R\&R Central A/C system — 5 ton — 16–21 SEER      | 1.00 |  EA  | 302.69 |      — | 6,858.98 | 274.83 | **7,436.50** |


|   # | DESCRIPTION                                     |    QTY | UNIT | RESET | REMOVE | REPLACE |   TAX |      TOTAL |
| --: | ----------------------------------------------- | -----: | :--: | ----: | -----: | ------: | ----: | ---------: |
| 146 | R\&R Ductwork system — hot & cold air (per run) |   1.00 |  EA  | 41.71 |      — |  541.89 | 10.81 | **594.41** |
| 152 | R\&R Blown-in insulation — 14" depth — R38      | 144.00 |  SF  |  1.33 |      — |    1.92 | 12.36 | **480.36** |

__

# ROOM R&R FULL 

"384.00  SF Walls
528.00  SF Walls & Ceiling
16.00  SY Flooring
48.00  LF Ceil. Perimeter"										"144.00  SF Ceiling
144.00  SF Floor
48.00  LF Floor Perimeter"																						

The following line items account for the repair and/or replacement of the damaged items within this room. Items in this room have been depreciated according to their age and condition unless otherwise noted.
The following line items account for the repair and/or replacement of the damaged items within this room.
Items in this room have been depreciated according to their age and condition unless otherwise noted."


Prep & Protection -

|   # | DESCRIPTION                                         |    QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | --------------------------------------------------- | -----: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 360 | Contents – move out then reset                      |   1.00 |  EA  |  0.00 |      — |   89.09 | 0.00 |  **89.09** |
| 361 | Floor protection – plastic & tape – 10 mil          | 528.00 |  SF  |  0.00 |      — |    0.36 | 3.80 | **193.88** |
| 362 | Mask & prep for paint – tape only (per LF)          |  48.00 |  LF  |  0.00 |      — |    0.73 | 0.14 |  **35.18** |
| 363 | Mask & cover large light fixture                    |   1.00 |  EA  |  0.00 |      — |   23.19 | 0.05 |  **23.24** |
| 364 | Window blind – horizontal/vertical – Detach & reset |   1.00 |  EA  |  0.00 |      — |   41.26 | 0.00 |  **41.26** |


Drywall & Insulation - 

|   # | DESCRIPTION                                               |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |    TOTAL |
| --: | --------------------------------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | -------: |
| 366 | R\&R 5/8" drywall – hung, taped, ready for texture        | 1.00 |  SF  |  0.52 |      — |    2.90 | 0.05 | **3.47** |
| 368 | R\&R 5/8" drywall – hung, taped, floated, ready for paint | 1.00 |  SF  |  0.52 |      — |    3.28 | 0.05 | **3.85** |
| 369 | R\&R 1/2" drywall – hung, taped, ready for texture        | 1.00 |  SF  |  0.52 |      — |    2.75 | 0.05 | **3.32** |
| 370 | R\&R 1/2" drywall – hung, taped, floated, ready for paint | 1.00 |  SF  |  0.52 |      — |    3.14 | 0.05 | **3.71** |
| 371 | R\&R Blown-in insulation – 10" depth – R26                | 1.00 |  SF  |  1.08 |      — |    1.39 | 0.06 | **2.53** |
| 372 | R\&R Batt insulation – 4" – R11 – unfaced                 | 1.00 |  SF  |  0.31 |      — |    0.85 | 0.03 | **1.19** |
| 373 | R\&R Batt insulation – 6" – R19 – unfaced                 | 1.00 |  SF  |  0.35 |      — |    1.44 | 0.06 | **1.85** |
| 374 | Apply anti-microbial agent to surface area                | 1.00 |  SF  |  0.00 |      — |    0.37 | 0.00 | **0.37** |


Textures & Paint (General) -

|   # | DESCRIPTION                             |    QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | --------------------------------------- | -----: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 376 | Texture drywall – machine – knockdown   |   1.00 |  SF  |  0.00 |      — |    1.17 | 0.00 |   **1.17** |
| 377 | Texture drywall – light hand texture    |   1.00 |  SF  |  0.00 |      — |    1.22 | 0.01 |   **1.23** |
| 378 | Texture drywall – heavy hand texture    |   1.00 |  SF  |  0.00 |      — |    1.66 | 0.02 |   **1.68** |
| 379 | Seal/prime (1 coat) then paint (1 coat) |   1.00 |  SF  |  0.00 |      — |    1.13 | 0.01 |   **1.14** |
| 380 | Paint walls & ceiling – one coat        | 528.00 |  SF  |  0.00 |      — |    0.79 | 5.07 | **422.19** |


Plaster & Stucco -

|   # | DESCRIPTION                                    |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | ---------------------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 381 | Thin coat plaster (no lath)                    | 1.00 |  SF  |  0.00 |      — |    8.03 | 0.03 |   **8.06** |
| 383 | R\&R Two-coat plaster (no lath)                | 1.00 |  SF  |  1.12 |      — |   11.76 | 0.06 |  **12.94** |
| 384 | R\&R Two-coat plaster over metal lath          | 1.00 |  SF  |  1.74 |      — |   16.18 | 0.11 |  **18.03** |
| 385 | Tear off plaster on wood lath                  | 1.00 |  SF  |  2.04 |      — |    0.00 | 0.00 |   **2.04** |
| 386 | Plaster – add for ceiling detailing/trim       | 1.00 |  LF  |  0.00 |      — |   47.48 | 0.23 |  **47.71** |
| 387 | R\&R Metal lath & stucco                       | 1.00 |  SF  |  0.93 |      — |    9.49 | 0.08 |  **10.50** |
| 389 | R\&R Two-coat plaster over 1/2" blueboard      | 1.00 |  SF  |  1.36 |      — |   15.02 | 0.12 |  **16.50** |
| 390 | R\&R Thin coat plaster over 1/2" blueboard     | 1.00 |  SF  |  1.36 |      — |   10.31 | 0.07 |  **11.74** |
| 391 | Plaster patch / small repair – ready for paint | 1.00 |  EA  |  0.00 |      — |  599.26 | 0.60 | **599.86** |


Acoustic Ceilings -

|   # | DESCRIPTION                                    |    QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | ---------------------------------------------- | -----: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 392 | R\&R Acoustic ceiling tile                     |   1.00 |  SF  |  0.76 |      — |    4.52 | 0.10 |   **5.38** |
| 394 | R\&R Acoustic ceiling tile furring             |   1.00 |  SF  |  0.38 |      — |    1.02 | 0.02 |   **1.42** |
| 395 | Seal & paint acoustic ceiling tile             | 144.00 |  SF  |  0.00 |      — |    1.44 | 3.46 | **210.82** |
| 401 | Texture drywall – machine                      |   1.00 |  SF  |  0.00 |      — |    0.84 | 0.00 |   **0.84** |
| 402 | Tear off painted acoustic ceiling (popcorn)    | 144.00 |  SF  |  1.14 |      — |    0.00 | 0.00 | **164.16** |
| 403 | Seal surface w/ latex stain blocker – one coat |   1.00 |  SF  |  0.00 |      — |    0.72 | 0.01 |   **0.73** |
| 404 | Acoustic ceiling (popcorn) texture             | 144.00 |  SF  |  0.00 |      — |    1.35 | 0.78 | **195.18** |


Window Blinds (PVC – 2") - 

|   # | DESCRIPTION                               |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | ----------------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 405 | R\&R Window blind – PVC – 2" – 7.1–14 SF  | 1.00 |  EA  | 12.59 |      — |  103.62 | 3.17 | **119.38** |
| 406 | R\&R Window blind – PVC – 2" – up to 7 SF | 1.00 |  EA  | 12.59 |      — |   87.20 | 2.34 | **102.13** |
| 407 | R\&R Window blind – PVC – 2" – 14.1–20 SF | 1.00 |  EA  | 12.59 |      — |  143.04 | 5.37 | **161.00** |
| 408 | R\&R Window blind – PVC – 2" – 20.1–32 SF | 1.00 |  EA  | 12.59 |      — |  178.61 | 6.60 | **197.80** |


Electrical & Fixtures -

|   # | DESCRIPTION                                   |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | --------------------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 409 | R\&R Ceiling fan & light                      | 1.00 |  EA  | 23.61 |      — |  403.33 | 9.07 | **436.01** |
| 411 | R\&R Light fixture                            | 1.00 |  EA  | 10.43 |      — |   82.23 | 2.16 |  **94.82** |
| 412 | R\&R Recessed light fixture                   | 1.00 |  EA  | 13.94 |      — |  147.54 | 2.21 | **163.69** |
| 413 | R\&R Heat/AC register – mechanically attached | 1.00 |  EA  |  3.13 |      — |   34.10 | 0.79 |  **38.02** |
| 414 | R\&R Heat/AC register – floor                 | 1.00 |  EA  |  1.75 |      — |   22.29 | 0.79 |  **24.83** |
| 415 | Prime & paint heat register                   | 1.00 |  EA  |  0.00 |      — |   19.15 | 0.20 |  **19.35** |


Wallcoverings - 

|   # | DESCRIPTION           |   QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | --------------------- | ----: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 416 | R\&R Wallpaper        |  1.00 |  SF  |  1.15 |      — |    2.78 | 0.07 |   **4.00** |
| 418 | R\&R Wallpaper border | 48.00 |  LF  |  0.99 |      — |    3.20 | 4.15 | **205.27** |


Underlayments & Subfloor -

|   # | DESCRIPTION                             |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |    TOTAL |
| --: | --------------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | -------: |
| 419 | R\&R Underlayment – 1/2" OSB            | 1.00 |  SF  |  0.83 |      — |    2.02 | 0.04 | **2.89** |
| 420 | R\&R Underlayment – 5/8" OSB            | 1.00 |  SF  |  0.83 |      — |    2.35 | 0.06 | **3.24** |
| 421 | R\&R Underlayment – 1/2" BC plywood     | 1.00 |  SF  |  2.07 |      — |    2.97 | 0.09 | **5.13** |
| 423 | R\&R Underlayment – 5/8" BC plywood     | 1.00 |  SF  |  0.83 |      — |    3.01 | 0.10 | **3.94** |
| 424 | R\&R Underlayment – 1/2" particle board | 1.00 |  SF  |  0.83 |      — |    2.34 | 0.06 | **3.23** |
| 425 | R\&R Underlayment – 5/8" particle board | 1.00 |  SF  |  0.83 |      — |    2.44 | 0.07 | **3.34** |


Flooring – Carpet & Vinyl -

|   # | DESCRIPTION                                              |    QTY | UNIT | RESET | REMOVE | REPLACE |   TAX |      TOTAL |
| --: | -------------------------------------------------------- | -----: | :--: | ----: | -----: | ------: | ----: | ---------: |
| 426 | Remove tear-out additional layer of vinyl floor covering | 144.00 |  SF  |  0.38 |      — |    0.00 |  0.00 |  **54.72** |
| 427 | R\&R Carpet pad – standard grade                         | 144.00 |  SF  |  0.16 |      — |    0.52 |  3.20 | **101.12** |
| 429 | Remove carpet – standard grade                           | 144.00 |  SF  |  0.35 |      — |    0.00 |  0.00 |  **50.40** |
| 430 | Carpet – standard grade                                  | 165.60 |  SF  |  0.00 |      — |    3.08 | 19.67 | **529.72** |
| 431 | Lift carpet for drying                                   | 144.00 |  SF  |  0.00 |      — |    0.55 |  0.00 |  **79.20** |
| 432 | Carpet – Detach & relay                                  | 144.00 |  SF  |  0.00 |      — |    1.18 |  0.26 | **170.18** |
| 433 | Clean & deodorize carpet                                 | 144.00 |  SF  |  0.00 |      — |    0.69 |  0.09 |  **99.45** |
| 435 | R\&R Carpet – metal transition strip                     |   1.00 |  LF  |  0.94 |      — |    3.99 |  0.12 |   **5.05** |
| 436 | R\&R Vinyl reducer strip – for carpet                    |   1.00 |  LF  |  0.49 |      — |    4.60 |  0.16 |   **5.25** |
| 460 | R\&R Vinyl floor covering (sheet goods) – standard       | 144.00 |  SF  |  1.15 |      — |    3.61 | 15.72 | **701.16** |
| 461 | R\&R Vinyl tile – standard grade                         | 144.00 |  SF  |  1.42 |      — |    3.33 | 12.10 | **696.10** |
| 462 | R\&R Vinyl – metal transition strip                      |   1.00 |  LF  |  0.94 |      — |    3.99 |  0.12 |   **5.05** |
| 463 | Floor prep (scrape rubber back residue)                  |   1.00 |  SF  |  0.00 |      — |    0.90 |  0.00 |   **0.90** |


Flooring – Tile, Stone & Mortar -

|   # | DESCRIPTION                               |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |     TOTAL |
| --: | ----------------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | --------: |
| 464 | Regrout tile                              | 1.00 |  SF  |  0.00 |      — |    5.50 | 0.02 |  **5.52** |
| 466 | R\&R Mortar bed for tile floors           | 1.00 |  SF  |  1.69 |      — |    5.99 | 0.14 |  **7.82** |
| 468 | R\&R Ceramic tile – standard grade        | 1.00 |  SF  |  2.50 |      — |   15.77 | 0.21 | **18.48** |
| 469 | R\&R Marble or granite floor tile         | 1.00 |  SF  |  3.13 |      — |   25.81 | 0.55 | **29.49** |
| 471 | R\&R Threshold – natural marble           | 1.00 |  LF  |  4.09 |      — |   79.77 | 1.68 | **85.54** |
| 472 | R\&R Threshold – cultured marble          | 1.00 |  LF  |  4.09 |      — |   46.25 | 0.60 | **50.94** |
| 473 | R\&R Quarry tile floor                    | 1.00 |  SF  |  3.13 |      — |   20.34 | 0.22 | **23.69** |
| 474 | R\&R Tile floor covering – standard grade | 1.00 |  SF  |  3.13 |      — |   12.35 | 0.20 | **15.68** |


Trim – Baseboard, Shoes, Crown, Chair Rail, Casing -

|   # | DESCRIPTION                                       |   QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | ------------------------------------------------- | ----: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 475 | Detach & reset baseboard – 3 1/4"                 |  1.00 |  LF  |  3.84 |      — |    0.00 | 0.00 |   **3.84** |
| 476 | R\&R Baseboard – 3 1/4"                           |  1.00 |  LF  |  0.57 |      — |    4.85 | 0.13 |   **5.55** |
| 477 | Seal (1) & paint (1) baseboard                    |  1.00 |  LF  |  0.00 |      — |    1.78 | 0.01 |   **1.79** |
| 478 | Paint baseboard – one coat                        | 48.00 |  LF  |  0.00 |      — |    1.13 | 0.32 |  **54.56** |
| 479 | Stain & finish baseboard                          | 48.00 |  LF  |  0.00 |      — |    1.88 | 0.78 |  **91.02** |
| 480 | Detach & reset baseboard – 4 1/4" w/ shoe         |  1.00 |  LF  |  4.51 |      — |    0.00 | 0.00 |   **4.51** |
| 481 | R\&R Baseboard – 4 1/4" w/ shoe                   |  1.00 |  LF  |  0.66 |      — |    7.79 | 0.23 |   **8.68** |
| 482 | Seal (1) & paint (1) baseboard w/ cap and/or shoe |  1.00 |  LF  |  0.00 |      — |    2.12 | 0.02 |   **2.14** |
| 483 | Paint baseboard w/ cap and/or shoe – one coat     | 48.00 |  LF  |  0.00 |      — |    1.36 | 0.66 |  **65.94** |
| 484 | Stain & finish baseboard w/ cap and/or shoe       | 48.00 |  LF  |  0.00 |      — |    2.21 | 0.78 | **106.86** |
| 485 | Detach & reset base shoe                          |  1.00 |  LF  |  2.18 |      — |    0.00 | 0.00 |   **2.18** |
| 486 | R\&R Base shoe                                    |  1.00 |  LF  |  0.21 |      — |    1.98 | 0.05 |   **2.24** |
| 487 | Paint base shoe or quarter round – 1 coat         | 48.00 |  LF  |  0.00 |      — |    0.65 | 0.32 |  **31.52** |
| 488 | Seal & paint base shoe or quarter round           | 48.00 |  LF  |  0.00 |      — |    0.97 | 0.40 |  **46.96** |
| 489 | Stain & finish base shoe or quarter round         | 48.00 |  LF  |  0.00 |      — |    1.52 | 0.78 |  **73.74** |
| 490 | Detach & reset crown molding – 4 1/4"             |  1.00 |  LF  |  5.16 |      — |    0.00 | 0.00 |   **5.16** |
| 491 | R\&R Crown molding – 4 1/4"                       |  1.00 |  LF  |  0.84 |      — |    6.84 | 0.18 |   **7.86** |
| 492 | Seal (1) & paint (1) crown molding                |  1.00 |  LF  |  0.00 |      — |    1.79 | 0.01 |   **1.80** |
| 493 | Paint crown molding – one coat                    | 48.00 |  LF  |  0.00 |      — |    1.19 | 0.43 |  **57.55** |
| 494 | Stain & finish crown molding                      | 48.00 |  LF  |  0.00 |      — |    2.02 | 0.78 |  **97.74** |
| 495 | Detach & reset chair rail – 2 1/2"                |  1.00 |  LF  |  3.21 |      — |    0.00 | 0.00 |   **3.21** |
| 496 | R\&R Chair rail – 2 1/2"                          |  1.00 |  LF  |  0.52 |      — |    4.22 | 0.11 |   **4.85** |
| 497 | Seal (1) & paint (1) chair rail                   |  1.00 |  LF  |  0.00 |      — |    1.72 | 0.01 |   **1.73** |
| 498 | Paint chair rail – one coat                       | 48.00 |  LF  |  0.00 |      — |    1.16 | 0.40 |  **56.08** |
| 499 | Stain & finish chair rail                         | 48.00 |  LF  |  0.00 |      — |    1.88 | 0.78 |  **91.02** |
| 500 | Detach & reset casing – 2 1/4"                    |  1.00 |  LF  |  2.73 |      — |    0.00 | 0.00 |   **2.73** |
| 501 | R\&R Casing – 2 1/4"                              |  1.00 |  LF  |  0.63 |      — |    3.01 | 0.09 |   **3.73** |
| 502 | Detach & reset casing – 3 1/4"                    |  1.00 |  LF  |  2.73 |      — |    0.00 | 0.00 |   **2.73** |
| 503 | R\&R Casing – 3 1/4"                              |  1.00 |  LF  |  0.63 |      — |    4.07 | 0.16 |   **4.86** |
| 504 | Seal (1) & paint (1) casing                       |  1.00 |  LF  |  0.00 |      — |    1.80 | 0.01 |   **1.81** |
| 505 | Paint casing – one coat                           | 48.00 |  LF  |  0.00 |      — |    1.16 | 0.40 |  **56.08** |
| 506 | Detach & reset quarter round – 3/4"               |  1.00 |  LF  |  2.18 |      — |    0.00 | 0.00 |   **2.18** |
| 507 | R\&R Quarter round – 3/4"                         |  1.00 |  LF  |  0.21 |      — |    2.23 | 0.06 |   **2.50** |


Doors & Openings (Interior) - 

|   # | DESCRIPTION                                               |  QTY | UNIT | RESET | REMOVE |  REPLACE |   TAX |        TOTAL |
| --: | --------------------------------------------------------- | ---: | :--: | ----: | -----: | -------: | ----: | -----------: |
| 508 | R\&R Attic entrance cover & trim                          | 1.00 |  EA  |  9.62 |      — |   114.91 |  1.65 |   **126.18** |
| 509 | Interior door – Detach & reset – slab only                | 1.00 |  EA  |  0.00 |      — |    30.54 |  0.00 |    **30.54** |
| 510 | R\&R Interior door – birch – slab only                    | 1.00 |  EA  | 10.43 |      — |   250.12 |  9.51 |   **270.06** |
| 511 | R\&R Interior door – Colonist – slab only                 | 1.00 |  EA  | 10.43 |      — |   202.43 |  6.65 |   **219.51** |
| 512 | R\&R Interior door unit                                   | 1.00 |  EA  | 23.45 |      — |   352.57 | 16.27 |   **392.29** |
| 513 | R\&R Interior double door – Colonist – pre-hung           | 1.00 |  EA  | 26.81 |      — |   592.95 | 28.25 |   **648.01** |
| 514 | R\&R Interior double door – full louvered – pre-hung      | 1.00 |  EA  | 28.87 |      — | 1,138.99 | 61.01 | **1,228.87** |
| 515 | Detach & reset door knob – interior                       | 1.00 |  EA  | 27.54 |      — |     0.00 |  0.00 |    **27.54** |
| 516 | R\&R Door opening (jamb & casing) – 32"–36" – paint grade | 1.00 |  EA  |  7.87 |      — |   202.14 |  7.88 |   **217.89** |
| 517 | Paint door/window trim & jamb – 2 coats (per side)        | 1.00 |  EA  |  0.00 |      — |    37.48 |  0.37 |    **37.85** |
| 518 | Prime & paint door slab only – exterior (per side)        | 1.00 |  EA  |  0.00 |      — |    53.96 |  1.01 |    **54.97** |


Windows, Sills & Paneling -

|   # | DESCRIPTION                                                |    QTY | UNIT | RESET | REMOVE | REPLACE |   TAX |        TOTAL |
| --: | ---------------------------------------------------------- | -----: | :--: | ----: | -----: | ------: | ----: | -----------: |
| 519 | R\&R Window sill                                           |   1.00 |  LF  |  0.87 |      — |    3.98 |  0.06 |     **4.91** |
| 520 | Seal & paint window sill                                   |   1.00 |  LF  |  0.00 |      — |    3.04 |  0.02 |     **3.06** |
| 521 | R\&R Window stool & apron                                  |   1.00 |  LF  |  0.95 |      — |   10.05 |  0.26 |    **11.26** |
| 522 | R\&R Paneling                                              |   1.00 |  SF  |  0.38 |      — |    3.40 |  0.05 |     **3.83** |
| 524 | Sand wood – interior                                       | 384.00 |  SF  |  0.00 |      — |    5.58 |  3.23 | **2,145.95** |
| 525 | Seal & paint paneling                                      | 384.00 |  SF  |  0.00 |      — |    1.40 |  5.53 |   **543.13** |
| 526 | Stain & finish paneling                                    | 384.00 |  SF  |  0.00 |      — |    1.97 | 10.60 |   **767.08** |
| 527 | R\&R Judges paneling – flat panel w/ molding – paint grade |   1.00 |  SF  |  1.26 |      — |   29.26 |  0.31 |    **30.83** |
| 528 | R\&R Judges paneling – raised panel – paint grade          |   1.00 |  SF  |  1.26 |      — |   38.65 |  0.35 |    **40.26** |
| 529 | Sand wood – interior                                       | 384.00 |  SF  |  0.00 |      — |    5.58 |  3.23 | **2,145.95** |
| 530 | Stain & finish wood judges paneling                        | 384.00 |  SF  |  0.00 |      — |    5.68 |  9.22 | **2,190.34** |
| 531 | Seal (1) & paint (1) – judges paneling                     | 384.00 |  SF  |  0.00 |      — |    5.22 |  7.14 | **2,011.62** |


Counters, Toe Kicks & Cabinetry -

|   # | DESCRIPTION                                                |  QTY | UNIT | RESET | REMOVE | REPLACE |   TAX |      TOTAL |
| --: | ---------------------------------------------------------- | ---: | :--: | ----: | -----: | ------: | ----: | ---------: |
| 532 | Countertop – post-formed plastic laminate – Detach & reset | 1.00 |  LF  |  0.00 |      — |   26.46 |  0.01 |  **26.47** |
| 534 | Countertop – cultured marble – Detach & reset              | 1.00 |  SF  |  0.00 |      — |   14.77 |  0.01 |  **14.78** |
| 535 | Countertop – solid surface/granite – Detach & reset        | 1.00 |  SF  |  0.00 |      — |   46.51 |  0.01 |  **46.52** |
| 536 | Countertop – flat-laid plastic laminate – Detach & reset   | 1.00 |  LF  |  0.00 |      — |   26.46 |  0.01 |  **26.47** |
| 537 | Toe kick – Detach & reset                                  | 1.00 |  LF  |  0.00 |      — |   10.64 |  0.01 |  **10.65** |
| 538 | R\&R Toe kick – pre-finished wood – 1/2"                   | 1.00 |  LF  |  2.34 |      — |   11.42 |  0.26 |  **14.02** |
| 539 | Stain & finish toe kick                                    | 1.00 |  LF  |  0.00 |      — |    1.88 |  0.02 |   **1.90** |
| 540 | R\&R Cabinetry – lower (base) units                        | 1.00 |  LF  |  9.40 |      — |  253.58 | 11.92 | **274.90** |
| 541 | R\&R Cabinetry – upper (wall) units                        | 1.00 |  LF  |  9.40 |      — |  182.07 |  7.63 | **199.10** |
| 542 | Stain & finish cabinetry – lower – inside & out            | 1.00 |  LF  |  0.00 |      — |   77.63 |  0.55 |  **78.18** |
| 543 | Stain & finish cabinetry – upper – faces only              | 1.00 |  LF  |  0.00 |      — |   38.02 |  0.30 |  **38.32** |
| 544 | Stain & finish cabinetry – upper – inside & out            | 1.00 |  LF  |  0.00 |      — |   67.06 |  0.51 |  **67.57** |
| 545 | R\&R Vanity                                                | 1.00 |  LF  |  9.40 |      — |  257.43 | 12.15 | **278.98** |


Bath, Laundry & Appliances – D&R - 

|   # | DESCRIPTION                           |  QTY | UNIT |  RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | ------------------------------------- | ---: | :--: | -----: | -----: | ------: | ---: | ---------: |
| 546 | Detach & reset fiberglass shower unit | 1.00 |  EA  | 819.29 |      — |    0.00 | 0.00 | **819.29** |
| 548 | Mirror – plate glass – Detach & reset | 1.00 |  SF  |   0.00 |      — |    7.42 | 0.00 |   **7.42** |
| 550 | Detach & reset medicine cabinet       | 1.00 |  EA  |  69.90 |      — |    0.00 | 0.00 |  **69.90** |
| 551 | Toilet – Detach & reset               | 1.00 |  EA  |   0.00 |      — |  396.19 | 0.55 | **396.74** |
| 552 | Dryer – Remove & reset                | 1.00 |  EA  |   0.00 |      — |   48.85 | 0.00 |  **48.85** |
| 553 | Washer – Remove & reset               | 1.00 |  EA  |   0.00 |      — |   63.36 | 0.00 |  **63.36** |
| 554 | Refrigerator – Remove & reset         | 1.00 |  EA  |   0.00 |      — |   65.12 | 0.00 |  **65.12** |
| 555 | Dishwasher – Detach & reset           | 1.00 |  EA  |   0.00 |      — |  381.84 | 0.00 | **381.84** |
| 556 | Range – electric – Remove & reset     | 1.00 |  EA  |   0.00 |      — |   48.85 | 0.00 |  **48.85** |
| 557 | Range – gas – Remove & reset          | 1.00 |  EA  |   0.00 |      — |  261.77 | 0.00 | **261.77** |
| 558 | Sink – single – Detach & reset        | 1.00 |  EA  |   0.00 |      — |  245.08 | 0.05 | **245.13** |
| 559 | Sink – double basin – Detach & reset  | 1.00 |  EA  |   0.00 |      — |  262.13 | 0.06 | **262.19** |


Cleaning - 

|   # | DESCRIPTION      |    QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |     TOTAL |
| --: | ---------------- | -----: | :--: | ----: | -----: | ------: | ---: | --------: |
| 560 | Clean floor      | 144.00 |  SF  |  0.00 |      — |    0.65 | 0.09 | **93.69** |
| 561 | Clean countertop |   1.00 |  SF  |  0.00 |      — |    1.18 | 0.00 |  **1.18** |
| 562 | Clean toilet     |   1.00 |  EA  |  0.00 |      — |   34.51 | 0.00 | **34.51** |
| 563 | Clean shower     |   1.00 |  EA  |  0.00 |      — |   68.45 | 0.01 | **68.46** |


Electrical – Wiring -

|   # | DESCRIPTION                               |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | ----------------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 564 | R\&R 110v copper wiring run, box & switch | 1.00 |  EA  |  6.72 |      — |   94.31 | 1.33 | **102.36** |
| 565 | R\&R 110v copper wiring run, box & outlet | 1.00 |  EA  |  6.72 |      — |   93.61 | 1.28 | **101.61** |


Cabinet Finishes (Extra) -

|   # | DESCRIPTION                                   |  QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |     TOTAL |
| --: | --------------------------------------------- | ---: | :--: | ----: | -----: | ------: | ---: | --------: |
| 566 | Stain & finish cabinetry – lower – faces only | 1.00 |  LF  |  0.00 |      — |   44.29 | 0.37 | **44.66** |




Cleaning

|   # | DESCRIPTION                         |    QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | ----------------------------------- | -----: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 606 | Clean floor                         | 454.00 |  SF  |  0.00 |      — |    0.43 | 0.00 | **195.22** |
| 612 | Clean stud wall                     | 199.33 |  SF  |  0.00 |      — |    0.86 | 0.12 | **171.54** |
| 621 | Clean floor                         | 454.00 |  SF  |  0.00 |      — |    0.43 | 0.00 | **195.22** |
| 631 | Clean floor                         | 454.00 |  SF  |  0.00 |      — |    0.43 | 0.00 | **195.22** |
| 658 | Clean the floor with pressure steam | 454.00 |  SF  |  0.00 |      — |    1.00 | 3.81 | **457.81** |


Mitigation De-construction

|   # | DESCRIPTION                                                 |    QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | ----------------------------------------------------------- | -----: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 607 | Tear out wet drywall, cleanup, bag, per LF – up to 2' tall  |  99.67 |  LF  |  3.58 |      — |    0.00 | 2.45 | **359.27** |
| 608 | Tear out baseboard                                          |  99.67 |  LF  |  0.50 |      — |    0.00 | 0.00 |  **49.84** |
| 609 | Water extraction from carpeted floor                        | 454.00 |  SF  |  0.00 |      — |    0.53 | 0.00 | **240.62** |
| 610 | Tear out wet non-salvageable carpet, cut & bag for disposal | 454.00 |  SF  |  0.60 |      — |    0.00 | 2.18 | **274.58** |
| 611 | Tear out wet carpet pad and bag for disposal                | 454.00 |  SF  |  0.56 |      — |    0.00 | 2.18 | **256.42** |
| 617 | Tear out wet drywall… – 2' after hours                      |  99.67 |  LF  |  3.55 |      — |    0.00 | 2.21 | **356.04** |
| 618 | Tear out baseboard – after hours                            |  99.67 |  LF  |  0.49 |      — |    0.00 | 0.00 |  **48.84** |
| 619 | Tear out wet non-salvage carpet – after hours               | 454.00 |  SF  |  0.58 |      — |    0.00 | 1.91 | **265.23** |
| 620 | Tear out wet carpet pad – after hours                       | 454.00 |  SF  |  0.55 |      — |    0.00 | 1.91 | **251.61** |
| 626 | Tear out baseboard                                          |  99.67 |  LF  |  0.33 |      — |    0.00 | 0.00 |  **32.89** |
| 627 | Drill holes for wall cavity drying                          |  99.67 |  EA  |  0.00 |      — |    0.44 | 0.00 |  **43.85** |
| 629 | Tear out wet carpet pad and bag for disposal                | 454.00 |  SF  |  0.38 |      — |    0.00 | 1.91 | **174.43** |
| 630 | Lift carpet for drying                                      | 454.00 |  SF  |  0.00 |      — |    0.31 | 0.00 | **140.74** |
| 644 | Tear out wet non-salvage carpet – after hours               | 454.00 |  SF  |  0.58 |      — |    0.00 | 1.91 | **265.23** |
| 645 | Tear out baseboard – after hours                            |  99.67 |  LF  |  0.49 |      — |    0.00 | 0.00 |  **48.84** |
| 646 | Drill holes for wall cavity drying – after hours            |  99.67 |  EA  |  0.00 |      — |    0.62 | 0.00 |  **61.80** |
| 647 | Water extraction from carpeted floor – after hours          | 454.00 |  SF  |  0.00 |      — |    0.69 | 0.00 | **313.26** |
| 648 | Tear out wet carpet pad – after hours                       | 454.00 |  SF  |  0.55 |      — |    0.00 | 1.91 | **251.61** |
| 653 | Tear out wet carpet pad – Category 3 water                  | 454.00 |  SF  |  0.55 |      — |    0.00 | 1.91 | **251.61** |
| 654 | Tear out baseboard & bag for disposal – up to Cat 3         |  99.67 |  LF  |  0.69 |      — |    0.00 | 1.20 |  **69.97** |
| 657 | Tear out wet non-salvageable carpet – Cat 3 water           | 454.00 |  SF  |  0.58 |      — |    0.00 | 1.91 | **265.23** |


Antimicrobial / Disinfectant

|   # | DESCRIPTION                                                     |    QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | --------------------------------------------------------------- | -----: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 613 | Apply anti-microbial agent to more than the floor               | 653.33 |  SF  |  0.00 |      — |    0.25 | 1.57 | **164.90** |
| 623 | Apply anti-microbial agent to more than the floor – after hours | 653.33 |  SF  |  0.00 |      — |    0.30 | 1.18 | **197.18** |


Mitigation-Related Equipment

|   # | DESCRIPTION                                                        |    QTY | UNIT | RESET | REMOVE | REPLACE |   TAX |      TOTAL |
| --: | ------------------------------------------------------------------ | -----: | :--: | ----: | -----: | ------: | ----: | ---------: |
| 614 | Air mover (per 24 hr) – no monitoring (3 days)                     |   3.00 |  EA  |  0.00 |      — |   26.50 |  0.00 |  **79.50** |
| 615 | Dehumidifier (per 24 hr) – X-Large – no monitoring (3 days)        |   3.00 |  EA  |  0.00 |      — |  118.00 |  0.00 | **354.00** |
| 616 | Water extraction from carpeted floor – after hours                 | 454.00 |  SF  |  0.00 |      — |    0.69 |  0.00 | **313.26** |
| 624 | Air mover (per 24 hr) – no monitoring (3 days)                     |   3.00 |  EA  |  0.00 |      — |   26.50 |  0.00 |  **79.50** |
| 625 | Dehumidifier (per 24 hr) – X-Large – no monitoring (3 days)        |   3.00 |  EA  |  0.00 |      — |  118.00 |  0.00 | **354.00** |
| 661 | Air mover (per 24 hr) – no monitoring (3 days)                     |   3.00 |  EA  |  0.00 |      — |   26.50 |  0.00 |  **79.50** |
| 662 | Dehumidifier (per 24 hr) – X-Large – no monitoring (3 days)        |   3.00 |  EA  |  0.00 |      — |  118.00 |  0.00 | **354.00** |
| 663 | Negative air fan/Air scrubber (per 24 hr) – no monitoring (3 days) |   3.00 |  DA  |  0.00 |      — |   73.16 |  0.00 | **219.48** |
| 664 | Add for HEPA filter (for negative air exhaust fan)                 |   1.00 |  EA  |  0.00 |      — |  192.11 | 10.94 | **203.05** |


# Crawlspace (Height: 8')

|   # | DESCRIPTION                                                          |    QTY | UNIT | RESET | REMOVE | REPLACE |  TAX |      TOTAL |
| --: | -------------------------------------------------------------------- | -----: | :--: | ----: | -----: | ------: | ---: | ---------: |
| 665 | Dehumidifier (per 24 hr) – X-Large – no monitoring (3 days)          |   3.00 |  EA  |  0.00 |      — |  118.00 | 0.00 | **354.00** |
| 666 | Water extraction from hard surface floor – Cat 3 water               | 369.00 |  SF  |  0.00 |      — |    1.21 | 0.00 | **446.49** |
| 667 | Tear out & bag wet insulation in confined space – Cat 3              | 369.00 |  SF  |  2.23 |      — |    0.00 | 1.77 | **824.64** |
| 668 | Clean the floor with pressure steam                                  | 369.00 |  SF  |  0.00 |      — |    2.14 | 3.76 | **793.42** |
| 669 | Clean stud wall *(confined space)*                                   | 171.00 |  SF  |  0.00 |      — |    1.98 | 0.21 | **338.79** |
| 670 | Clean floor or roof joist system *(confined space)*                  | 369.00 |  SF  |  0.00 |      — |    2.47 | 0.44 | **911.87** |
| 671 | Apply anti-microbial agent to more than the floor *(confined space)* | 454.50 |  SF  |  0.00 |      — |    0.49 | 1.09 | **223.80** |


Crawlspace Equipment

|   # | DESCRIPTION                                                        |  QTY | UNIT | RESET | REMOVE | REPLACE |   TAX |      TOTAL |
| --: | ------------------------------------------------------------------ | ---: | :--: | ----: | -----: | ------: | ----: | ---------: |
| 672 | Air mover (per 24 hr) – no monitoring (3 days)                     | 3.00 |  EA  |  0.00 |      — |   26.50 |  0.00 |  **79.50** |
| 673 | Negative air fan/Air scrubber (per 24 hr) – no monitoring (3 days) | 3.00 |  DA  |  0.00 |      — |   73.16 |  0.00 | **219.48** |
| 674 | Add for HEPA filter (for negative air exhaust fan)                 | 1.00 |  EA  |  0.00 |      — |  194.36 | 10.94 | **205.30** |

_____________________________________________________________________________________________________

General Guidlines for agent:
use this knowledge base seemlessly without telling the user about sources.

# General Pricing for new construction

* A full kitchen remodel services typically costs $20,000 to $100,000.

* to guttered and remodel a room of 8/8 (remove drywall, )

* A "full bath" remodel from can cost between $5,000 and $75,000+, depending on the type and size of the bathroom. A standard guest bathroom remodel typically costs $14,000–$20,000, while a luxury master bath remodel can reach $35,000 and up.

# Insurace_agent: 
1. In case more then 40% of the surfece (block) of the object is damaged you replace the entire block. ex: if a half of a roof shingles are damaged you replace the entire shingles. if half a floor is flooded by black water you replace the entire flooring.

2. In case of heavy equipment in a room, you give more labor to clear and reset. ex: The garage room may have lots of equipment to take out and bring back in case of a flood.  





"""