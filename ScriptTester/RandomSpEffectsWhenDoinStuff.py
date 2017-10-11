from DarkSoulsScriptingBundle import *
import System
import random
import cmath
import time

everySpEffectEver = [50,80,500,510,520,530,540,550,560,620,630,640,1000,1010,1020,1040,1050,1060,1070,1080,1081,1082,1083,1090,1120,1130,1140,1150,1160,1170,1200,1210,1220,1230,1330,1340,1500,1510,1520,1530,1600,1610,1620,1630,1720,1800,1810,1980,1981,2000,2010,2013,2020,2021,2022,2023,2024,2030,2031,2034,2040,2050,2060,2080,2090,2100,2101,2110,2111,2120,2121,2130,2131,2140,2190,2200,2210,2230,2240,2241,2250,2260,2270,2290,2300,2310,2320,2330,2340,2350,2976,2977,2978,2979,2980,2981,2982,2983,2984,2985,2986,2987,2988,2989,2990,2991,2992,2993,2994,2995,2996,2997,2998,3000,3020,3021,3022,3023,3024,3025,3026,3027,3040,3041,3050,3051,3060,3061,3070,3071,3080,3090,3091,3100,3110,3120,3121,3130,3140,3150,3151,3160,3170,3180,3190,3191,3210,3231,3250,3270,3271,3272,3273,3274,3275,3276,3277,3278,3279,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3330,3950,3951,3952,3953,3954,3955,3956,3957,3958,3959,3960,3961,3962,3963,3964,3965,3966,3967,3968,3969,3970,3971,3972,3973,3974,3975,3976,3977,3978,4100,4130,4140,4160,4161,
                     # infinite gate 3979,
                     # rijenereito resonance 570,571,572,573,574,
                     # more events/territory/etc 4170,4500,4501,4600,4601,
                     # resonance 40,41,42,43,44,
                     # "anti- magic" 600,610,611,
                     # HP recovery#_resonance 1400,1401,1402,1403,1404,1410,1411,1412,1413,1414,1420,1421,1422,1423,1424,1430,1431,1432,1433,1434,
                     # evil eye (keeps showing up in failed test results): 63,64,65,
                     # vagrant souls/humanity: 3290,3291,3292,3293,3294,3295,3296,3297,3298,3299,3300,
                     # treatments: 1300,1301,1302,1303,1320,1321,
                     # "Inner door key to general-purpose" 4150,
                     # recovery and qwc: 100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,201,202,203,206,207,208,211,212,221,222,231,232,236,237,311,312,321,322,331,332,336,337,
                     # curse 
                     33,34,71,72,73,74,
                     # "recovery" stuff: 1986,1987,1988,1989,1990,
                     # ally estus: 3030,3031,3032,3033,3034,3035,3036,3037,
                     # invader shit 1983,1984,1985,
                     # White/black relief detection: 1700,1710,
                     # PG test: 52,53,54,55,57,
                     # Cooperation: 59,60,61,62,
                     # Binoculars: 3240,
                     # System: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,28,30,31,32,
                     # Invalid states/throws: 35,36,37,38,39,
                     # Battle of Stoicism (causes crashes): 4510,4511,4512,4513,4514,4515,4516,4517,4518,4519,4520,4521,4522,4523,4524,4525,4526,4527,4528,4529,4530,4531,4532,4533,4534,4535,
                     # Battle of Stoicism (causes crashes): 4610,4611,4612,4613,
                     # Battle of Stoicism Visual Effects (safe probably): 
                     #  4614,4615,4616,4617,4618,
                     # Homeward bone: 3220,3221,3222,3223,3224,3225,
                     # Homeward: 580,581,
                     # dark sign 3226,
                     # ephemeral eye stone: 3230,
                     5000,5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,5021,5022,5023,5024,5025,5026,5027,5028,5029,5030,5031,5032,5033,5034,5035,5036,5037,5038,5039,5040,5041,5042,5043,5044,5045,5046,5047,5048,5049,5050,5051,5052,5053,5055,5057,5060,5061,5062,5063,5064,5065,5066,5067,5068,5069,5070,5071,5072,5073,5074,5075,5076,5077,5078,5079,5080,5081,5082,5083,5084,5101,5102,5103,5104,5105,5110,5111,5120,5130,5131,5132,5133,5140,5141,5142,5150,5151,5152,5160,5161,5162,5163,5170,5171,5180,5210,5211,5212,5213,5214,5220,5221,5222,5230,5231,5232,5233,5234,5235,5236,5250,5251,5252,5253,5254,5255,5260,5261,5262,5263,5264,5265,5269,5270,5271,5272,5273,5274,5275,5279,5280,5281,5282,5283,5284,5290,5291,5292,5293,5294,5295,5296,5300,5301,5302,5303,5304,5305,5306,5307,5308,5309,5320,5321,5322,5323,5324,5325,5326,5327,5328,5329,5330,5331,5332,5333,5334,5335,5336,5337,5360,5361,5362,5363,5364,5400,5401,5402,5403,5410,5411,5412,5413,5420,5421,5422,5423,5424,5430,5431,5432,5433,5434,5435,5436,5440,5441,5442,5443,5444,5445,5446,5447,5450,5451,5452,5460,5466,5470,5471,5480,5490,5491,5492,5493,5494,5495,5496,5500,5510,5511,5520,5521,5522,5530,5540,5541,5542,5550,5560,5561,5570,5571,5580,5581,5582,5590,6000,6010,6011,6200,6201,6202,6203,6210,6211,6212,6213,6220,6221,6222,6223,6230,6231,6232,6233,6300,6310,6320,6330,6340,6400,6401,6402,6403,6404,6405,6410,6420,6500,6501,6502,6503,6504,6505,6600,6601,6602,6603,6604,6605,6610,6620,6621,6630,6700,6702,6710,6711,6712,6713,6720,6730,6740,6750,6760,6800,6810,6820,6830,6840,6850,6860,6870,6880,6890,6900,6910,6920,6930,6940,6950,6960,6961,6970,6980,6990,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7100,7401,7402,7403,7404,7405,7406,7407,7408,7409,7410,7411,7412,7413,7414,7415,7500,7501,7510,7511,7600,7601,7602,7610,7611,7650,7651,7700,7800,7801,8000,8001,71100,71110,71111,80000,80011,80101,80111,81001,81011,81101,81111,
                     # Dangerous: ,90000,90001,90010,90011,90100,90101,90110,90111,91000,91001,91010,91011,91100,91101,91110,91111
                     # Bleed: 
                     5054,5056,5058,5059,
                     # DS2 gassman resident?? 
                     5100,
                     # sustained damage: 
                     4000,4001,4002,4003,4004,4005,4006,4011,4012,4013,4014,4015,4016,4017,4020,4021,4030,4031,
                     ]

oldAnim = -1

oldPlayerHP = -1

while True:
    while Utils.IsGameLoading():
        ex.Wait(33)
    curAnim = Misc.PlayerCurrentAnimation
    if curAnim != oldAnim and curAnim != -1:
        randSpEffect = everySpEffectEver[random.randint(0, everySpEffectEver.Count - 1)]
        oldPlayerHP = Chr.Player.HP
        f.SetEventSpecialEffect_2(10000, randSpEffect)
        print ">>>>>>>>>>>>>>>>>>>> " + str(randSpEffect) + " <<<<<<<<<<<<<<<<<<<<"
        if Chr.Player.HP < oldPlayerHP:
            print "------------------------------ PLAYER HP LOWERED ------------------------------"
    oldAnim = curAnim
    ex.Wait(33)