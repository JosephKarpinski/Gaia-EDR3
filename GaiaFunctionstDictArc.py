
def getStarLy(rtarget):
    value = tDict.get(rtarget)
    if value != None:
        #print(str(value))
        return float(tDict[rtarget]['LY'])
    else:
        #print(str(value))
        return float(99999)


def getStarCount(rtarget):
    value = tDict.get(rtarget)
    if value != None:
        return str(tDict[rtarget]['Stars'])
    else:
        return str('1000')


def getStarArc(rtarget):
    value = tDict.get(rtarget)
    if value != None:
        return str(tDict[rtarget]['Arc'])
    else:
        return str('60')


def getStarWiki(rtarget):
    value = tDict.get(rtarget)
    if value != None:
        return str(tDict[rtarget]['Wiki'])
    else:
        return str('Messier_1')


tDict = {
         'm2': {'Stars':'150000', 'LY':'55000','Arc':'1.86','Wiki':'Messier_2'}, # V NGC 7089 GC 16__arcmins
         'm3': {'Stars':'9086', 'LY':'33900','Arc':'18','Wiki':'Messier_3'},     # NGC 5272 GC 18__arcmins
         'm4': {'Stars':'10000', 'LY':'7175','Arc':'26','Wiki':'Messier_4'},     # NGC 6121 GC 26__arcmins
         'm5': {'Stars':'3476', 'LY':'24500','Arc':'23','Wiki':'Messier_5'},     # NGC 5904 GC 23__arcmins
         'm6': {'Stars':'544', 'LY':'1508','Arc':'20','Wiki':'Messier_6'},       # OC V NGC 6405 Butterfly Cluster
         'm7': {'Stars':'874', 'LY':'913','Arc':'80','Wiki':'Messier_7'},        # OC Par NGC 6475 80__Ptolemy Cluster
         'm9': {'Stars':'1000000', 'LY':'25800','Arc':'9.3','Wiki':'Messier_9'}, # NGC 6333 GC 9.3__arcmins
    
        'm2L': {'Stars':'150000', 'LY':'55000','Arc':'1.86','Wiki':'Messier_2'}, # V NGC 7089 GC 16__arcmins
        'm3L': {'Stars':'9086', 'LY':'33900','Arc':'18','Wiki':'Messier_3'},     # NGC 5272 GC 18__arcmins
        'm4L': {'Stars':'10000', 'LY':'7175','Arc':'26','Wiki':'Messier_4'},     # NGC 6121 GC 26__arcmins
        'm5L': {'Stars':'3476', 'LY':'24500','Arc':'23','Wiki':'Messier_5'},     # NGC 5904 GC 23__arcmins
        'm6L': {'Stars':'544', 'LY':'1508','Arc':'20','Wiki':'Messier_6'},       # OC V NGC 6405 Butterfly Cluster
        'm7L': {'Stars':'874', 'LY':'913','Arc':'80','Wiki':'Messier_7'},        # OC Par NGC 6475 80__Ptolemy Cluster
        'm9L': {'Stars':'1000000', 'LY':'25800','Arc':'9.3','Wiki':'Messier_9'}, # NGC 6333 GC 9.3__arcmins
         
         'm10': {'Stars':'100000', 'LY':'14300','Arc':'20','Wiki':'Messier_10'},  # NGC 6254 GC 20__arcmins
         'm11': {'Stars':'2900', 'LY':'7638','Arc':'22.8','Wiki':'Messier_11'},   # OC Par NGC 6705 22.8__Wild Duck Cluster
        'm10L': {'Stars':'100000', 'LY':'14300','Arc':'20','Wiki':'Messier_10'},  # NGC 6254 GC 20__arcmins
        'm11L': {'Stars':'2900', 'LY':'7638','Arc':'22.8','Wiki':'Messier_11'},   # OC Par NGC 6705 22.8__Wild Duck Cluster
         'm12': {'Stars':'3127', 'LY':'15700','Arc':'16','Wiki':'Messier_12'},    # NGC 6218 GC 16__arcmins
        'm12L': {'Stars':'3127', 'LY':'15700','Arc':'16','Wiki':'Messier_12'},    # NGC 6218 GC 16__arcmins
         'm13': {'Stars':'10311', 'LY':'22200','Arc':'20','Wiki':'Messier_13'},   # NGC 6205 GC 20 arcmins Hercules GC
        'm13L': {'Stars':'10311', 'LY':'22200','Arc':'20','Wiki':'Messier_13'},   # NGC 6205 GC 20 arcmins Hercules GC
         'm14': {'Stars':'300000', 'LY':'30300','Arc':'11','Wiki':'Messier_14'},  # NGC 6402 GC 11__arcmins
        'm14L': {'Stars':'300000', 'LY':'30300','Arc':'11','Wiki':'Messier_14'},  # NGC 6402 GC 11__arcmins
         'm15': {'Stars':'100000', 'LY':'33000','Arc':'18','Wiki':'Messier_15'},  # NGC 7078 GC 18__arcmins
        'm15L': {'Stars':'100000', 'LY':'33000','Arc':'18','Wiki':'Messier_15'},  # NGC 7078 GC 18__arcmins
         'm16': {'Stars':'8100', 'LY':'5762','Arc':'5.05','Wiki':'Messier_16'},   # OC V NGC 6611 OC Eagle Nebula
         'm17': {'Stars':'800', 'LY':'5500','Arc':'11','Wiki':'Messier_17'},    # OC V NGC 6618 Omega Nebula
         'm18': {'Stars':'188', 'LY':'5096','Arc':'5','Wiki':'Messier_18'},       # OC V Par NGC 6613 
         'm19': {'Stars':'1000000', 'LY':'28700','Arc':'17','Wiki':'Messier_19'}, # NGC 6273 GC 17__arcmins
    
        'm16L': {'Stars':'8100', 'LY':'5762','Arc':'5.05','Wiki':'Messier_16'},   # OC V NGC 6611 OC Eagle Nebula
        'm17L': {'Stars':'800', 'LY':'5500','Arc':'1.63','Wiki':'Messier_17'},    # OC V NGC 6618 Omega Nebula
        'm18L': {'Stars':'188', 'LY':'5096','Arc':'5','Wiki':'Messier_18'},       # OC V Par NGC 6613 
        'm19L': {'Stars':'1000000', 'LY':'28700','Arc':'17','Wiki':'Messier_19'}, # NGC 6273 GC 17__arcmins

         'm21': {'Stars':'1000', 'LY':'4087','Arc':'14','Wiki':'Messier_21'},     # OC V Par NGC 6531
         'm22': {'Stars':'9542', 'LY':'10600','Arc':'6.52','Wiki':'Messier_22'},  # V NGC 6656 GC          
         'm23': {'Stars':'413', 'LY':'2409','Arc':'29','Wiki':'Messier_23'},      # OC Par NGC 6494 
         'm24': {'Stars':'70000', 'LY':'13000','Arc':'90','Wiki':'Messier_24'},   # Sagittarius Star Cloud 120__arcmins
         'm25': {'Stars':'1000', 'LY':'2000','Arc':'36','Wiki':'Messier_25'},     # IC 4725  OC
         'm26': {'Stars':'1000', 'LY':'5160','Arc':'14','Wiki':'Messier_26'},     # NGC 6694 OC
         'm28': {'Stars':'10000', 'LY':'17900','Arc':'11.2','Wiki':'Messier_28'}, # NGC 6626 GC
         'm29': {'Stars':'10000', 'LY':'3740','Arc':'7','Wiki':'Messier_29'},     # NGC 6913 OC 7__arcmins
    
        'm21L': {'Stars':'1000', 'LY':'4087','Arc':'14','Wiki':'Messier_21'},     # OC V Par NGC 6531
        'm22L': {'Stars':'9542', 'LY':'10600','Arc':'6.52','Wiki':'Messier_22'},  # V NGC 6656 GC          
        'm23L': {'Stars':'413', 'LY':'2409','Arc':'29','Wiki':'Messier_23'},      # OC Par NGC 6494 
        'm24L': {'Stars':'70000', 'LY':'13000','Arc':'90','Wiki':'Messier_24'},   # Sagittarius Star Cloud 120__arcmins
        'm25L': {'Stars':'1000', 'LY':'2000','Arc':'36','Wiki':'Messier_25'},     # IC 4725  OC
        'm26L': {'Stars':'1000', 'LY':'5160','Arc':'14','Wiki':'Messier_26'},     # NGC 6694 OC
        'm28L': {'Stars':'10000', 'LY':'17900','Arc':'11.2','Wiki':'Messier_28'}, # NGC 6626 GC
        'm29L': {'Stars':'10000', 'LY':'3740','Arc':'7','Wiki':'Messier_29'},     # NGC 6913 OC 7__arcmins

         'm30': {'Stars':'1016', 'LY':'27140','Arc':'12','Wiki':'Messier_30'},     # NGC 7099 GC 12__arcmins
         'm34': {'Stars':'400', 'LY':'1500','Arc':'35','Wiki':'Messier_34'},       # NGC 1039 OC 35__arcmins
         'm35': {'Stars':'1000', 'LY':'3870','Arc':'28','Wiki':'Messier_35'},      # NGC 2168 OC 28 arcmins
         'm36': {'Stars':'100', 'LY':'4340','Arc':'10','Wiki':'Messier_36'},       # NGC 1930 OC 10__Pinwheel Cluster
         'm37': {'Stars':'1000', 'LY':'4511','Arc':'24','Wiki':'Messier_37'},      # NGC 2099 OC 24__arcmins
         'm38': {'Stars':'100', 'LY':'3480','Arc':'21','Wiki':'Messier_38'},       # NGC 1912 OC 21__arcmin
         'm39': {'Stars':'248', 'LY':'1010','Arc':'29','Wiki':'Messier_39'},       # NGC 7092 OC 29__arcmins
    
        'm30L': {'Stars':'1016', 'LY':'27140','Arc':'12','Wiki':'Messier_30'},     # NGC 7099 GC 12__arcmins
        'm34L': {'Stars':'400', 'LY':'1500','Arc':'35','Wiki':'Messier_34'},       # NGC 1039 OC 35__arcmins
        'm35L': {'Stars':'1000', 'LY':'3870','Arc':'28','Wiki':'Messier_35'},      # NGC 2168 OC 28 arcmins
        'm36L': {'Stars':'100', 'LY':'4340','Arc':'10','Wiki':'Messier_36'},       # NGC 1930 OC 10__Pinwheel Cluster
        'm37L': {'Stars':'1000', 'LY':'4511','Arc':'24','Wiki':'Messier_37'},      # NGC 2099 OC 24__arcmins
        'm38L': {'Stars':'100', 'LY':'3480','Arc':'21','Wiki':'Messier_38'},       # NGC 1912 OC 21__arcmin
        'm39L': {'Stars':'248', 'LY':'1010','Arc':'29','Wiki':'Messier_39'},       # NGC 7092 OC 29__arcmins
         
         'm41': {'Stars':'100', 'LY':'2300','Arc':'38','Wiki':'Messier_41'},       # NGC 2287 OC 38__arcmins
         'm42': {'Stars':'1000', 'LY':'1344','Arc':'65','Wiki':'Messier_42'},      # NGC 1976 Orion Nebula 65x60 arcmins
         'm44': {'Stars':'771', 'LY':'577','Arc':'95','Wiki':'Messier_44'},        # NGC 2632 OC 95__Beehive Cluster Praesepe
        
         'm45': {'Stars':'1059', 'LY':'444','Arc':'110','Wiki':'Messier_45'},      # Pleiades OC 110 arcmins Melotte22
         'm46': {'Stars':'500', 'LY':'4920','Arc':'22.8','Wiki':'Messier_46'},     # NGC 2437 OC 22.8__arcmins
         'm47': {'Stars':'572', 'LY':'1600','Arc':'30','Wiki':'Messier_47'},       # NGC 2422 OC 30__arcmins
         'm48': {'Stars':'374', 'LY':'2500','Arc':'30','Wiki':'Messier_48'},       # NGC 2548 OC 30__arcmins
        
        'm41L': {'Stars':'100', 'LY':'2300','Arc':'38','Wiki':'Messier_41'},       # NGC 2287 OC 38__arcmins
        'm42L': {'Stars':'1000', 'LY':'1344','Arc':'65','Wiki':'Messier_42'},      # NGC 1976 Orion Nebula 65x60 arcmins
        'm44L': {'Stars':'771', 'LY':'577','Arc':'95','Wiki':'Messier_44'},        # NGC 2632 OC 95__Beehive Cluster Praesepe
        'm45L': {'Stars':'1059', 'LY':'444','Arc':'110','Wiki':'Messier_45'},      # Pleiades OC 110 arcmins Melotte22
        'm46L': {'Stars':'500', 'LY':'4920','Arc':'22.8','Wiki':'Messier_46'},     # NGC 2437 OC 22.8__arcmins
        'm47L': {'Stars':'572', 'LY':'1600','Arc':'30','Wiki':'Messier_47'},       # NGC 2422 OC 30__arcmins
        'm48L': {'Stars':'374', 'LY':'2500','Arc':'30','Wiki':'Messier_48'},       # NGC 2548 OC 30__arcmins
        
         'm50': {'Stars':'372', 'LY':'2870','Arc':'16','Wiki':'Messier_50'},       # NGC 2323 OC 16__arcmins
         'm52': {'Stars':'200', 'LY':'4600','Arc':'13','Wiki':'Messier_52'},       # NGC 7654 OC 13__arcmins
         'm53': {'Stars':'500000', 'LY':'58000','Arc':'13','Wiki':'Messier_53'},   # NGC 5024 OC 13__arcmins
         'm54': {'Stars':'1M', 'LY':'87400','Arc':'12','Wiki':'Messier_54'},       # NGC 6715 OC 12__arcmins
         'm55': {'Stars':'8073', 'LY':'17600','Arc':'19','Wiki':'Messier_55'},     # NGC 6809 GC
         'm56': {'Stars':'20000', 'LY':'32900','Arc':'8.8','Wiki':'Messier_56'},   # NGC 6779 GC
    
        'm50L': {'Stars':'372', 'LY':'2870','Arc':'16','Wiki':'Messier_50'},       # NGC 2323 OC 16__arcmins
        'm52L': {'Stars':'200', 'LY':'4600','Arc':'13','Wiki':'Messier_52'},       # NGC 7654 OC 13__arcmins
        'm53L': {'Stars':'500000', 'LY':'58000','Arc':'13','Wiki':'Messier_53'},   # NGC 5024 OC 13__arcmins
        'm54L': {'Stars':'1M', 'LY':'87400','Arc':'12','Wiki':'Messier_54'},       # NGC 6715 OC 12__arcmins
        'm55L': {'Stars':'8073', 'LY':'17600','Arc':'19','Wiki':'Messier_55'},     # NGC 6809 GC
        'm56L': {'Stars':'20000', 'LY':'32900','Arc':'8.8','Wiki':'Messier_56'},   # NGC 6779 GC
    
         'm67': {'Stars':'1194', 'LY':'2800','Arc':'30','Wiki':'Messier_67'}, # NGC 2682 OC 30__Mass 1090-1400 W Dwarfs 150
         'm68': {'Stars':'20000', 'LY':'33600','Arc':'11','Wiki':'Messier_68'},    # NGC 4590 GC
         'm69': {'Stars':'20000', 'LY':'29000','Arc':'10.8','Wiki':'Messier_69'},  # NGC 6637 GC
    
        'm67L': {'Stars':'1194', 'LY':'2800','Arc':'30','Wiki':'Messier_67'}, # NGC 2682 OC 30__Mass 1090-1400 W Dwarfs 150
        'm68L': {'Stars':'20000', 'LY':'33600','Arc':'11','Wiki':'Messier_68'},    # NGC 4590 GC
        'm69L': {'Stars':'20000', 'LY':'29000','Arc':'10.8','Wiki':'Messier_69'},  # NGC 6637 GC
    
         'm70': {'Stars':'20000', 'LY':'29400','Arc':'8','Wiki':'Messier_70'},     # NGC 6681 GC
         'm71': {'Stars':'20000', 'LY':'13000','Arc':'7.2','Wiki':'Messier_71'},   # NGC 6838 GC 7.2__arcmins
         'm72': {'Stars':'20000', 'LY':'54570','Arc':'6.6','Wiki':'Messier_72'},   # NGC 6981 GC
         'm75': {'Stars':'20000', 'LY':'68000','Arc':'6.8','Wiki':'Messier_75'},   # NGC 6864 GC
         'm79': {'Stars':'20000', 'LY':'12900','Arc':'8.7','Wiki':'Messier_79'},   # NGC 1904 GC
    
         'm70L': {'Stars':'20000', 'LY':'29400','Arc':'8','Wiki':'Messier_70'},     # NGC 6681 GC
         'm71L': {'Stars':'20000', 'LY':'13000','Arc':'7.2','Wiki':'Messier_71'},   # NGC 6838 GC 7.2__arcmins
         'm72L': {'Stars':'20000', 'LY':'54570','Arc':'6.6','Wiki':'Messier_72'},   # NGC 6981 GC
         'm75L': {'Stars':'20000', 'LY':'68000','Arc':'6.8','Wiki':'Messier_75'},   # NGC 6864 GC
         'm79L': {'Stars':'20000', 'LY':'12900','Arc':'8.7','Wiki':'Messier_79'},   # NGC 1904 GC
    
         'm80': {'Stars':'20000', 'LY':'32600','Arc':'10','Wiki':'Messier_80'},    # NGC 6093 GC
        'm80L': {'Stars':'20000', 'LY':'32600','Arc':'10','Wiki':'Messier_80'},    # NGC 6093 GC
    
         'm92': {'Stars':'1431', 'LY':'26700','Arc':'14','Wiki':'Messier_92'},     # NGC 6341 GC 14__arcmins
         'm93': {'Stars':'1431', 'LY':'3380','Arc':'10','Wiki':'Messier_93'},      # NGC 6341 OC 
    
        'm92L': {'Stars':'1431', 'LY':'26700','Arc':'14','Wiki':'Messier_92'},     # NGC 6341 GC 14__arcmins
        'm93L': {'Stars':'1431', 'LY':'3380','Arc':'10','Wiki':'Messier_93'},      # NGC 6341 OC 
    
         'm103': {'Stars':'1000', 'LY':'10000','Arc':'6','Wiki':'Messier_103'},    # NGC 581 OC
         'm107': {'Stars':'10000', 'LY':'20900','Arc':'10','Wiki':'Messier_107'},  # NGC 6171 GC
    
        'm103L': {'Stars':'1000', 'LY':'10000','Arc':'6','Wiki':'Messier_103'},    # NGC 581 OC
        'm107L': {'Stars':'10000', 'LY':'20900','Arc':'10','Wiki':'Messier_107'},  # NGC 6171 GC

         'NGC104': {'Stars':'21580', 'LY':'13000','Arc':'30.9','Wiki':'NGC_104'},  # 47 Tucanae GC 30.9__arcmins
        'NGC104L': {'Stars':'21580', 'LY':'13000','Arc':'30.9','Wiki':'NGC_104'},  # 47 Tucanae GC 30.9__arcmins
         'NGC188': {'Stars':'956', 'LY':'6455','Arc':'15','Wiki':'NGC_188'},       # OC Par
        'NGC188L': {'Stars':'956', 'LY':'6455','Arc':'15','Wiki':'NGC_188'},       # OC Par
         'NGC0188': {'Stars':'956', 'LY':'6455','Arc':'15','Wiki':'NGC_188'},      # OC Par
    
         'NGC0225': {'Stars':'100', 'LY':'2278','Arc':'12','Wiki':'NGC_225'},      # OC Par
         'NGC288': {'Stars':'1953', 'LY':'28700','Arc':'13.8','Wiki':'NGC_288'},   # GC 13.8
        'NGC288L': {'Stars':'1953', 'LY':'28700','Arc':'13.8','Wiki':'NGC_288'},   # GC 13.8
        
         'NGC362': {'Stars':'1737', 'LY':'27700','Arc':'12.9','Wiki':'NGC_362'},   # GC 12.9
        'NGC362L': {'Stars':'1737', 'LY':'27700','Arc':'12.9','Wiki':'NGC_362'},   # GC 12.9
         'NGC381': {'Stars':'100', 'LY':'3851','Arc':'7','Wiki':'NGC_381'},       # OC Par
         'NGC0381': {'Stars':'100', 'LY':'3851','Arc':'7','Wiki':'NGC_381'},       # OC Par
    
         'NGC581': {'Stars':'100', 'LY':'8744','Arc':'6','Wiki':'Messier_103'},   # OC Par M103
         'NGC0581': {'Stars':'100', 'LY':'8744','Arc':'6','Wiki':'Messier_103'},   # OC Par M103
         
         'NGC752': {'Stars':'259', 'LY':'1462','Arc':'75','Wiki':'NGC_752'},       # OC Par 75__arcmins
        'NGC752L': {'Stars':'259', 'LY':'1462','Arc':'75','Wiki':'NGC_752'},       # OC Par 75__arcmins
         'NGC0752': {'Stars':'259', 'LY':'1462','Arc':'75','Wiki':'NGC_752'},      # OC Par 75__arcmins

         'NGC869': {'Stars':'300', 'LY':'6800','Arc':'30','Wiki':'NGC_869'},       # OC 30__arcmins
        'NGC869L': {'Stars':'300', 'LY':'6800','Arc':'30','Wiki':'NGC_869'},       # OC 30__arcmins
         'NGC884': {'Stars':'300', 'LY':'7500','Arc':'30','Wiki':'NGC_884'},       # OC 30__arcmins
        'NGC884L': {'Stars':'300', 'LY':'7500','Arc':'30','Wiki':'NGC_884'},       # OC 30__arcmins
         'NGC901': {'Stars':'1000', 'LY':'1354','Arc':'40','Wiki':'NGC_1901'},     # OC 
        'NGC901L': {'Stars':'1000', 'LY':'1354','Arc':'40','Wiki':'NGC_1901'},     # OC 
         
         'NGC1039': {'Stars':'497', 'LY':'1670','Arc':'35','Wiki':'NGC_1039'},     # OC Par M34 35__arcmins
        'NGC1039L': {'Stars':'497', 'LY':'1670','Arc':'35','Wiki':'NGC_1039'},     # OC Par M34 35__arcmins
         'NGC1220': {'Stars':'100', 'LY':'10982','Arc':'60','Wiki':'NGC_1220'},     # OC Par
         'NGC1261': {'Stars':'10000', 'LY':'53500','Arc':'12.9','Wiki':'NGC_1261'}, # GC 12.9__arcmins
        'NGC1261L': {'Stars':'10000', 'LY':'53500','Arc':'12.9','Wiki':'NGC_1261'}, # GC 12.9__arcmins
         'NGC1528': {'Stars':'100', 'LY':'3440','Arc':'23','Wiki':'NGC_1528'},     # OC Par
         'NGC1545': {'Stars':'1000', 'LY':'2386','Arc':'23','Wiki':'NGC_1545'},    # OC Par 23__arcmins
         'NGC1582': {'Stars':'100', 'LY':'3281','Arc':'60','Wiki':'NGC_1582'},     # OC Par
         'NGC1662': {'Stars':'1000', 'LY':'1359','Arc':'20','Wiki':'NGC_1662'},    # OC Par 20__arcmins
         'NGC1664': {'Stars':'100', 'LY':'4443','Arc':'18','Wiki':'NGC_1664'},     # OC Par
         'NGC1750': {'Stars':'100', 'LY':'2396','Arc':'107','Wiki':'NGC_1750'},    # OC Par
         'NGC1758': {'Stars':'100', 'LY':'2957','Arc':'60','Wiki':'NGC_1758'},     # OC Par
         'NGC1851': {'Stars':'744', 'LY':'39500','Arc':'11','Wiki':'NGC_1851'},    # GC 11__arcmins
        'NGC1851L': {'Stars':'744', 'LY':'39500','Arc':'11','Wiki':'NGC_1851'},    # GC 11__arcmins
         'NGC1901': {'Stars':'100', 'LY':'1383','Arc':'15','Wiki':'NGC_1901'},     # OC Par Class B: 173
        'NGC1901L': {'Stars':'100', 'LY':'1383','Arc':'15','Wiki':'NGC_1901'},     # OC Par Class B: 5717
         'NGC1912': {'Stars':'100', 'LY':'3732','Arc':'21','Wiki':'Messier_38'},   # OC Par M38 21__arcmin
         'NGC1960': {'Stars':'100', 'LY':'3906','Arc':'10','Wiki':'Messier_36'},   # OC Par M36
         
         'NGC2158': {'Stars':'241', 'LY':'17794','Arc':'5','Wiki':'NGC_2158'},     # OC Par
         'NGC2168': {'Stars':'418', 'LY':'2886','Arc':'28','Wiki':'Messier_35'},   # OC Par
         'NGC2184': {'Stars':'100', 'LY':'1908','Arc':'6.6','Wiki':'NGC_2184'},    # OC Par
         'NGC2215': {'Stars':'100', 'LY':'3194','Arc':'52','Wiki':'NGC_2215'},     # OC Par
         'NGC2232': {'Stars':'241', 'LY':'1305','Arc':'9.9','Wiki':'NGC_2232'},    # OC 
         'NGC2251': {'Stars':'1000', 'LY':'4957','Arc':'5.7','Wiki':'NGC_2251'},   # OC Par
        'NGC2264': {'Stars':'1000', 'LY':'2600','Arc':'20','Wiki':'NGC_2251'},     # OC 
         'NGC2281': {'Stars':'100', 'LY':'1720','Arc':'10.8','Wiki':'NGC_2281'},   # OC Par
         'NGC2287': {'Stars':'100', 'LY':'2398','Arc':'38','Wiki':'Messier_41'},   # OC Par M41  
         'NGC2298': {'Stars':'1500', 'LY':'34900','Arc':'11','Wiki':'NGC_2298'},   # GC Unknown 11__arcmins
        
         'NGC2302': {'Stars':'100', 'LY':'4077','Arc':'60','Wiki':'NGC_2302'},     # OC Par
         'NGC2323': {'Stars':'372', 'LY':'3258','Arc':'16','Wiki':'NGC_2323'},     # OC Par M50 13__Mass 285 Age 140 Myr
         'NGC2343': {'Stars':'100', 'LY':'3632','Arc':'7.5','Wiki':'NGC_2343'},    # OC Par
         'NGC2353': {'Stars':'100', 'LY':'3997','Arc':'20','Wiki':'NGC_2353'},     # OC Par
         'NGC2358': {'Stars':'100', 'LY':'3074','Arc':'9.6','Wiki':'NGC_2358'},    # OC Par
         'NGC2360': {'Stars':'848', 'LY':'3617','Arc':'13','Wiki':'NGC_2360'},     # OC Par 13__arcmins
         'NGC2362': {'Stars':'60', 'LY':'4396','Arc':'6','Wiki':'NGC_2362'},       # OC Par 8__arcmins
         'NGC2374': {'Stars':'100', 'LY':'4291','Arc':'19','Wiki':'NGC_2374'},     # OC Par
         'NGC2383': {'Stars':'100', 'LY':'11484','Arc':'4.2','Wiki':'NGC_2383'},   # OC Par
         'NGC2396': {'Stars':'100', 'LY':'4995','Arc':'6.6','Wiki':'NGC_2396'},    # OC Par Large
    
         'NGC2419': {'Stars':'10000', 'LY':'275000','Arc':'6','Wiki':'NGC_2419'},   # GC 6__Mass 900,000
         'NGC2420': {'Stars':'100', 'LY':'8985','Arc':'7.5','Wiki':'NGC_2420'},     # OC Par
         'NGC2422': {'Stars':'572', 'LY':'1576','Arc':'30','Wiki':'NGC_2422'},      # OC Par M47 Mass 453 Age 78 Myr
         'NGC2423': {'Stars':'100', 'LY':'3125','Arc':'11.7','Wiki':'NGC_2423'},    # OC Par
         'NGC2425': {'Stars':'100', 'LY':'12691','Arc':'5.4','Wiki':'NGC_2425'},    # OC Par
         'NGC2432': {'Stars':'100', 'LY':'6616','Arc':'5.4','Wiki':'NGC_2432'},     # OC Par
         'NGC2447': {'Stars':'681', 'LY':'3396','Arc':'10','Wiki':'NGC_2447'},      # OC Par M93 Mass 723 Age 387 Myr
         'NGC2448': {'Stars':'100', 'LY':'3715','Arc':'6','Wiki':'NGC_2448'},       # OC Par
         'NGC2451': {'Stars':'311', 'LY':'600','Arc':'37.5','Wiki':'NGC_2451'},     # OC
         'NGC2451A': {'Stars':'100', 'LY':'631','Arc':'37.5','Wiki':'NGC_2451'},    # OC Par
         'NGC2451B': {'Stars':'100', 'LY':'1200','Arc':'37.5','Wiki':'NGC_2451'},   # OC Par
         'NGC2477': {'Stars':'1000', 'LY':'3600','Arc':'27','Wiki':'NGC_2477'},     # OC 27__arcmins
         'NGC2482': {'Stars':'100', 'LY':'4530','Arc':'23','Wiki':'NGC_2482'},      # OC Par
    
         'NGC2516': {'Stars':'1727', 'LY':'1352','Arc':'24.3','Wiki':'NGC_2516'},   # OC Par 30__arcmins
         'NGC2527': {'Stars':'100', 'LY':'2123','Arc':'20','Wiki':'NGC_2527'},      # OC Par
         'NGC2546': {'Stars':'100', 'LY':'3154','Arc':'16.5','Wiki':'NGC_2546'},    # OC Par
         'NGC2547': {'Stars':'404', 'LY':'1282','Arc':'20','Wiki':'NGC_2547'},      # OC Par 20__arcmins
         'NGC2548': {'Stars':'374', 'LY':'2500','Arc':'30','Wiki':'Messier_48'},    # M48 OC 30__arcmins
         'NGC2567': {'Stars':'100', 'LY':'6018','Arc':'19','Wiki':'NGC_2567'},      # OC Par
         'NGC2632': {'Stars':'771', 'LY':'607','Arc':'95','Wiki':'Beehive_Cluster'}, # OC Par M44 95__Beehive Cluster Praesepe
         'NGC2645': {'Stars':'100', 'LY':'6236','Arc':'6.6','Wiki':'NGC_2645'},     # OC Par
         'NGC2658': {'Stars':'100', 'LY':'16556','Arc':'7.2','Wiki':'NGC_2658'},    # OC Par
         'NGC2659': {'Stars':'100', 'LY':'7216','Arc':'2.7','Wiki':'NGC_2659'},     # OC Par
         'NGC2669': {'Stars':'100', 'LY':'3860','Arc':'8.4','Wiki':'NGC_2669'},     # OC Par 
         'NGC2682': {'Stars':'1194', 'LY':'2880','Arc':'25','Wiki':'Messier_67'},   # OC V Par M67 30_Mass 1090-1400 WD 150
         
         'NGC2808': {'Stars':'10000', 'LY':'31300','Arc':'13.8','Wiki':'NGC_2808'}, # GC 13.8__arcmins
         'NGC2818': {'Stars':'100', 'LY':'12026','Arc':'10','Wiki':'NGC_2818'},     # OC Par Large
         'NGC2866': {'Stars':'100', 'LY':'9944','Arc':'2.7','Wiki':'NGC_2866'},     # OC Par
         'NGC2910': {'Stars':'100', 'LY':'4372','Arc':'4.8','Wiki':'NGC_2910'},     # OC Par Large
         'NGC2925': {'Stars':'100', 'LY':'2518','Arc':'7.5','Wiki':'NGC_2925'},     # OC Par 
         'NGC2972': {'Stars':'100', 'LY':'6753','Arc':'3.6','Wiki':'NGC_2972'},     # OC Par
         
         'NGC3201': {'Stars':'1M', 'LY':'16300','Arc':'18.2','Wiki':'NGC_3201'},    # GC 18.2_arc Mass 254,000 Age 10.24 GYs
        'NGC3201L': {'Stars':'1M', 'LY':'16300','Arc':'18.2','Wiki':'NGC_3201'},    # GC 18.2_arc Mass 254,000 Age 10.24 GYs
         'NGC3228': {'Stars':'100', 'LY':'1605','Arc':'11','Wiki':'NGC_3228'},      # OC Par
         'NGC3330': {'Stars':'100', 'LY':'5909','Arc':'10','Wiki':'NGC_3330'},      # OC Par
         'NGC3496': {'Stars':'100', 'LY':'8341','Arc':'10','Wiki':'NGC_3496'},      # OC Par
         'NGC3532': {'Stars':'1802', 'LY':'1579','Arc':'25','Wiki':'NGC_3532'},     # OC Par
         
         'NGC4103': {'Stars':'100', 'LY':'6895','Arc':'12','Wiki':'NGC_4103'},      # OC Par
         'NGC4147': {'Stars':'10000', 'LY':'60000','Arc':'1.7','Wiki':'NGC_4147'},  # GC 1.7__arcmins
         'NGC4349': {'Stars':'100', 'LY':'6656','Arc':'12','Wiki':'NGC_4349'},      # OC Par
         'NGC4372': {'Stars':'10000', 'LY':'18900','Arc':'18','Wiki':'NGC_4372'},   # GC 18__arcmins
         'NGC4439': {'Stars':'100', 'LY':'6881','Arc':'10','Wiki':'NGC_4439'},      # OC Par
         'NGC4463': {'Stars':'100', 'LY':'6236','Arc':'10','Wiki':'NGC_4463'},      # OC Par
         'NGC4609': {'Stars':'100', 'LY':'4942','Arc':'13','Wiki':'NGC_4609'},      # OC V Par
         'NGC4833': {'Stars':'10000', 'LY':'21500','Arc':'13.5','Wiki':'NGC_4833'}, # GC 13.5__arcmins
         'NGC4852': {'Stars':'100', 'LY':'4337','Arc':'10','Wiki':'NGC_4852'},      # OC Par
                  
         'NGC5053': {'Stars':'10000', 'LY':'17400','Arc':'10.5','Wiki':'NGC_5053'}, # GC 10.5__arcmins
         'NGC5138': {'Stars':'100', 'LY':'6395','Arc':'10','Wiki':'NGC_5138'},      # OC Par
         'NGC5139': {'Stars':'10000', 'LY':'15800','Arc':'36.3','Wiki':'Omega_Centauri'}, # GC Omega Centaur
        'NGC5139L': {'Stars':'10000', 'LY':'15800','Arc':'36.3','Wiki':'Omega_Centauri'}, # GC Omega Centaur
         'NGC5272': {'Stars':'9086', 'LY':'33900','Arc':'18','Wiki':'Messier_3'},   # m3 GC 10.5__arcmins
         'NGC5281': {'Stars':'100', 'LY':'5409','Arc':'7','Wiki':'NGC_5281'},      # OC V Par
         'NGC5286': {'Stars':'10000', 'LY':'35900','Arc':'4','Wiki':'NGC_5286'},    # GC  Caldwell 84
         'NGC5316': {'Stars':'570', 'LY':'4905','Arc':'14','Wiki':'NGC_5316'},      # OC V Par
         'NGC5460': {'Stars':'100', 'LY':'2434','Arc':'23','Wiki':'NGC_5460'},      # OC Par
         'NGC5466': {'Stars':'10000', 'LY':'51900','Arc':'11','Wiki':'NGC_5466'},   # GC
         'NGC5617': {'Stars':'100', 'LY':'8154','Arc':'10','Wiki':'NGC_5617'},      # OC V Par
         'NGC5634': {'Stars':'10000', 'LY':'82000','Arc':'4.5','Wiki':'NGC_5634'},  # GC
         'NGC5694': {'Stars':'10000', 'LY':'114100','Arc':'3.6','Wiki':'NGC_5694'}, # GC Caldwell 66
         'NGC5749': {'Stars':'100', 'LY':'3664','Arc':'10','Wiki':'NGC_5749'},      # OC Par
         'NGC5822': {'Stars':'100', 'LY':'2748','Arc':'35','Wiki':'NGC_5822'},      # OC Par
         'NGC5824': {'Stars':'10000', 'LY':'104400','Arc':'6.2','Wiki':'NGC_5824'}, # GC
         'NGC5897': {'Stars':'10000', 'LY':'24100','Arc':'9.9','Wiki':'NGC_5897'},  # GC
         'NGC5904': {'Stars':'3476', 'LY':'24500','Arc':'23','Wiki':'Messier_5'},   # m5 GC 23'
         'NGC5927': {'Stars':'10000', 'LY':'25100','Arc':'12','Wiki':'NGC_5927'},   # GC
         'NGC5946': {'Stars':'10000', 'LY':'34600','Arc':'3.6','Wiki':'NGC_5946'},  # GC
         'NGC5986': {'Stars':'10000', 'LY':'33900','Arc':'5','Wiki':'NGC_5986'},    # GC
         
         'NGC6005': {'Stars':'100', 'LY':'9010','Arc':'10','Wiki':'NGC_6005'},      # OC Par
         'NGC6025': {'Stars':'431', 'LY':'2579','Arc':'12','Wiki':'NGC_6025'},      # OC Par Caldwell 95
         'NGC6087': {'Stars':'100', 'LY':'3182','Arc':'12','Wiki':'NGC_6087'},      # OC Par
         'NGC6101': {'Stars':'10000', 'LY':'47600','Arc':'10.7','Wiki':'NGC_6101'}, # GC
         'NGC6139': {'Stars':'10000', 'LY':'32900','Arc':'1.6','Wiki':'NGC_6139'},  # GC
         'NGC6144': {'Stars':'10000', 'LY':'27700','Arc':'1.8','Wiki':'NGC_6144'},  # GC
         'NGC6152': {'Stars':'100', 'LY':'5490','Arc':'43','Wiki':'NGC_6152'},      # OC Par
         'NGC6192': {'Stars':'100', 'LY':'5712','Arc':'10','Wiki':'NGC_6192'},      # OC Par
         
         'NGC6204': {'Stars':'100', 'LY':'4052','Arc':'5','Wiki':'NGC_6204'},       # OC V Par
         'NGC6205': {'Stars':'10311', 'LY':'22200','Arc':'20','Wiki':'Messier_13'}, # m13 GC Hercules GC
         'NGC6208': {'Stars':'100', 'LY':'3930','Arc':'18','Wiki':'NGC_6208'},      # OC Par
         'NGC6218': {'Stars':'3127', 'LY':'15700','Arc':'16','Wiki':'Messier_12'},  # m12 GC 
         'NGC6229': {'Stars':'10000', 'LY':'99100','Arc':'4.5','Wiki':'NGC_6229'},  # GC
         'NGC6235': {'Stars':'10000', 'LY':'37200','Arc':'8.9','Wiki':'Messier_1'}, # GC
         'NGC6242': {'Stars':'100', 'LY':'4320','Arc':'25','Wiki':'NGC_6242'},      # OC Par
         'NGC6249': {'Stars':'100', 'LY':'4139','Arc':'5','Wiki':'NGC_6249'},       # OC V Par
         'NGC6256': {'Stars':'10000', 'LY':'27400','Arc':'4.1','Wiki':'NGC_6256'},  # GC
         'NGC6281': {'Stars':'534', 'LY':'1611','Arc':'25','Wiki':'NGC_6281'},      # OC
         'NGC6284': {'Stars':'10000', 'LY':'49900','Arc':'6.2','Wiki':'NGC_6284'},  # GC
         'NGC6287': {'Stars':'10000', 'LY':'30300','Arc':'4.8','Wiki':'NGC_6287'},  # GC
         'NGC6293': {'Stars':'10000', 'LY':'31000','Arc':'7.9','Wiki':'NGC_6293'},  # GC

         'NGC6304': {'Stars':'10000', 'LY':'19200','Arc':'3.8','Wiki':'NGC_6304'}, # GC
         'NGC6316': {'Stars':'10000', 'LY':'35900','Arc':'4.9','Wiki':'NGC_6316'}, # GC
         'NGC6325': {'Stars':'10000', 'LY':'25000','Arc':'4.3','Wiki':'NGC_6325'}, # GC
         'NGC6333': {'Stars':'10000', 'LY':'25800','Arc':'9.3','Wiki':'Messier_9'}, # GC M9
         'NGC6341': {'Stars':'1431', 'LY':'26700','Arc':'14','Wiki':'Messier_92'}, # m92 GC 14__arcmins
         'NGC6342': {'Stars':'10000', 'LY':'28000','Arc':'4.4','Wiki':'NGC_6342'}, # GC
         'NGC6352': {'Stars':'10000', 'LY':'19570','Arc':'7.1','Wiki':'NGC_6352'}, # GC
         'NGC6355': {'Stars':'10000', 'LY':'31000','Arc':'4.2','Wiki':'NGC_6355'}, # GC
         'NGC6356': {'Stars':'10000', 'LY':'49200','Arc':'10','Wiki':'NGC_6356'}, # GC
         'NGC6362': {'Stars':'10000', 'LY':'24800','Arc':'9','Wiki':'NGC_6362'}, # GC
        'NGC6362L': {'Stars':'10000', 'LY':'24800','Arc':'9','Wiki':'NGC_6362'}, # GC
         'NGC6366': {'Stars':'10000', 'LY':'11700','Arc':'13','Wiki':'NGC_6366'}, # GC
         'NGC6380': {'Stars':'10000', 'LY':'35500','Arc':'12.1','Wiki':'NGC_6380'}, # GC
         'NGC6388': {'Stars':'10000', 'LY':'32300','Arc':'6.2','Wiki':'NGC_6388'}, # GC
         'NGC6397': {'Stars':'10055', 'LY':'7800','Arc':'15.3','Wiki':'NGC_6397'}, # GC 
         'NGC6397L': {'Stars':'10055', 'LY':'7800','Arc':'15.3','Wiki':'NGC_6397'}, # GC 
         

         'NGC6401': {'Stars':'10000', 'LY':'24450','Arc':'4.8','Wiki':'NGC_6401'},  # GC
         'NGC6405': {'Stars':'544', 'LY':'1508','Arc':'20','Wiki':'Butterfly_Cluster'}, # OC V Par M6 25__Butterfly Cluster
         'NGC6426': {'Stars':'10000', 'LY':'67200','Arc':'4.2','Wiki':'NGC_6426'},  # GC
         'NGC6440': {'Stars':'10000', 'LY':'27700','Arc':'6.3','Wiki':'NGC_6440'},  # GC
         'NGC6441': {'Stars':'10000', 'LY':'44000','Arc':'9.6','Wiki':'NGC_6441'},  # GC
         'NGC6453': {'Stars':'10000', 'LY':'37800','Arc':'21.5','Wiki':'NGC_6453'}, # GC
         'NGC6475': {'Stars':'874', 'LY':'913','Arc':'80','Wiki':'Messier_7'},      # OC Par M7 80__Ptolemy Cluster 980-1013
         'NGC6494': {'Stars':'100', 'LY':'2409','Arc':'29','Wiki':'NGC_6494'},      # OC Par M23
         'NGC6496': {'Stars':'10000', 'LY':'36900','Arc':'5.6','Wiki':'NGC_6496'},  # GC

         'NGC6517': {'Stars':'10000', 'LY':'35200','Arc':'10','Wiki':'Messier_1'},  # GC
         'NGC6522': {'Stars':'10000', 'LY':'25100','Arc':'16.4','Wiki':'NGC_6522'}, # GC
         'NGC6528': {'Stars':'10000', 'LY':'25800','Arc':'16.6','Wiki':'NGC_6528'}, # GC
         'NGC6531': {'Stars':'100', 'LY':'4087','Arc':'14','Wiki':'NGC_6531'},      # OC V Par M21
         'NGC6535': {'Stars':'10000', 'LY':'22200','Arc':'25','Wiki':'NGC_6535'},   # GC
         'NGC6539': {'Stars':'10000', 'LY':'25400','Arc':'7.9','Wiki':'NGC_6539'},  # GC
         'NGC6540': {'Stars':'10000', 'LY':'17300','Arc':'9.5','Wiki':'NGC_6540'},  # GC
         'NGC6541': {'Stars':'10000', 'LY':'22800','Arc':'15','Wiki':'NGC_6541'},   # GC
         'NGC6544': {'Stars':'10000', 'LY':'9450','Arc':'1','Wiki':'NGC_6544'},     # GC
         'NGC6553': {'Stars':'10000', 'LY':'19600','Arc':'8.2','Wiki':'NGC_6553'},  # GC
         'NGC6558': {'Stars':'10000', 'LY':'24100','Arc':'10.4','Wiki':'NGC_6558'}, # GC
         'NGC6569': {'Stars':'10000', 'LY':'35500','Arc':'7','Wiki':'NGC_6569'},    # GC
         'NGC6584': {'Stars':'10000', 'LY':'45000','Arc':'7.9','Wiki':'NGC_6584'},  # GC

         'NGC6611': {'Stars':'8100', 'LY':'5762','Arc':'5.05','Wiki':'Messier_16'},   # OC V NGC 6611 OC Eagle Nebula
         'NGC6613': {'Stars':'188', 'LY':'5096','Arc':'5','Wiki':'Messier_18'},       # OC V Par NGC 6613 
         'NGC6618': {'Stars':'800', 'LY':'5500','Arc':'1.63','Wiki':'Messier_17'},    # OC V NGC 6618 Omega Nebula
         'NGC6624': {'Stars':'10000', 'LY':'25800','Arc':'8.8','Wiki':'NGC_6624'},    # GC
         'NGC6626': {'Stars':'10000', 'LY':'17900','Arc':'11.2','Wiki':'Messier_28'}, # M28 GC
         'NGC6633': {'Stars':'100', 'LY':'1293','Arc':'27','Wiki':'NGC_6633'},        # OC Par 
         'NGC6638': {'Stars':'10000', 'LY':'31300','Arc':'2','Wiki':'NGC_6638'},      # GC
         'NGC6642': {'Stars':'10000', 'LY':'26400','Arc':'1','Wiki':'NGC_6642'},      # GC
         'NGC6652': {'Stars':'10000', 'LY':'32600','Arc':'6.7','Wiki':'Messier_1'},   # GC
         'NGC6656': {'Stars':'9542', 'LY':'10600','Arc':'6.52','Wiki':'Messier_22'},  # V M22 GC 
         
         'NGC6704': {'Stars':'100', 'LY':'7515','Arc':'10','Wiki':'NGC_6704'},     # OC Par
         'NGC6705': {'Stars':'2900', 'LY':'7638','Arc':'22.8','Wiki':'Wild_Duck_Cluster'}, # OC Par M11 
         'NGC6709': {'Stars':'100', 'LY':'3580','Arc':'13','Wiki':'NGC_6709'},     # OC Par
         'NGC6712': {'Stars':'10000', 'LY':'26400','Arc':'7.2','Wiki':'NGC_6712'}, # GC
         'NGC6716': {'Stars':'100', 'LY':'2321','Arc':'10','Wiki':'NGC_6716'},     # OC Par
         'NGC6717': {'Stars':'10000', 'LY':'23100','Arc':'9.9','Wiki':'NGC_6717'}, # GC
         'NGC6723': {'Stars':'10000', 'LY':'28400','Arc':'11','Wiki':'NGC_6723'},  # GC
         'NGC6728': {'Stars':'100', 'LY':'6085','Arc':'16','Wiki':'NGC_6728'},     # OC Par
         'NGC6749': {'Stars':'10000', 'LY':'25800','Arc':'5.1','Wiki':'Messier_1'}, # GC
         'NGC6752': {'Stars':'10779', 'LY':'13000','Arc':'20.4','Wiki':'NGC_6752'}, # GC
         'NGC6760': {'Stars':'10000', 'LY':'24100','Arc':'9.6','Wiki':'NGC_6760'}, # GC
         'NGC6774': {'Stars':'165', 'LY':'1003','Arc':'60','Wiki':'Ruprecht_147'}, # OC Par
         'NGC6791': {'Stars':'100', 'LY':'16987','Arc':'16','Wiki':'NGC_6791'},    # OC Par
         'NGC6793': {'Stars':'271', 'LY':'1956','Arc':'18','Wiki':'Messier_1'},    # OC Par
         
         'NGC6800': {'Stars':'100', 'LY':'3422','Arc':'16','Wiki':'NGC_6800'},     # OC Par
         'NGC6809': {'Stars':'8073', 'LY':'17600','Arc':'19','Wiki':'Messier_55'}, # M55 GC
         'NGC6811': {'Stars':'100', 'LY':'3749','Arc':'13','Wiki':'NGC_6811'},     # OC Par
         'NGC6819': {'Stars':'100', 'LY':'9161','Arc':'5','Wiki':'NGC_6819'},      # OC Par 
         'NGC6830': {'Stars':'100', 'LY':'7692','Arc':'10','Wiki':'NGC_6830'},     # OC Par 
         'NGC6866': {'Stars':'100', 'LY':'4754','Arc':'7','Wiki':'NGC_6866'},      # OC Par 
         
         'NGC6934': {'Stars':'10000', 'LY':'52000','Arc':'1.2','Wiki':'NGC_6934'}, # GC
         'NGC6940': {'Stars':'100', 'LY':'3444','Arc':'25','Wiki':'NGC_6940'},     # OC Par
         'NGC6997': {'Stars':'100', 'LY':'2894','Arc':'25','Wiki':'NGC_6997'},     # OC Par

         'NGC7006': {'Stars':'10000', 'LY':'137000','Arc':'2.8','Wiki':'NGC_7006'}, # GC
         'NGC7058': {'Stars':'100', 'LY':'1195','Arc':'10','Wiki':'NGC_7058'},      # OC Par 
         'NGC7063': {'Stars':'100', 'LY':'2208','Arc':'10','Wiki':'NGC_7063'},      # OC Par 
         'NGC7092': {'Stars':'248', 'LY':'977','Arc':'29','Wiki':'Messier_39'},     # M39 OC Par
         'NGC7099': {'Stars':'1016', 'LY':'27140','Arc':'12','Wiki':'Messier_30'},  # M30 GC 12'
         'NGC7209': {'Stars':'100', 'LY':'3977','Arc':'25','Wiki':'NGC_7209'},      # OC Par
         'NGC7235': {'Stars':'100', 'LY':'12593','Arc':'10','Wiki':'NGC_7235'},     # OC Par
         'NGC7243': {'Stars':'100', 'LY':'2922','Arc':'21','Wiki':'NGC_7243'},      # OC Par
         'NGC7281': {'Stars':'100', 'LY':'7550','Arc':'24','Wiki':'NGC_7281'},      # OC Par
         'NGC7296': {'Stars':'100', 'LY':'8257','Arc':'10','Wiki':'NGC_7296'},      # OC Par
         'NGC7492': {'Stars':'10000', 'LY':'85700','Arc':'8.4','Wiki':'Messier_1'}, # GC
         'NGC7654': {'Stars':'10000', 'LY':'5472','Arc':'13','Wiki':'Messier_52'},  # OC Par
         'NGC7788': {'Stars':'100', 'LY':'10871','Arc':'10','Wiki':'NGC_7788'},     # OC Par
    
         'Cl Alessi 1': {'Stars':'100', 'LY':'2346','Arc':'60','Wiki':'Messier_1'},   # OC Par
        'Alessi1': {'Stars':'100', 'LY':'2346','Arc':'60','Wiki':'Messier_1'},        # OC Par
        'Alessi1L': {'Stars':'100', 'LY':'2346','Arc':'60','Wiki':'Messier_1'},       # OC Par
        'Alessi1M': {'Stars':'100', 'LY':'2346','Arc':'60','Wiki':'Messier_1'},       # OC Par
         'Cl Alessi 2': {'Stars':'100', 'LY':'2052','Arc':'62','Wiki':'Messier_1'},   # OC Par
        'Alessi2': {'Stars':'100', 'LY':'2052','Arc':'62','Wiki':'Messier_1'},        # OC Par
        'Alessi2L': {'Stars':'100', 'LY':'2052','Arc':'62','Wiki':'Messier_1'},       # OC Par
        'Alessi2M': {'Stars':'100', 'LY':'2052','Arc':'62','Wiki':'Messier_1'},       # OC Par
         'Cl Alessi 5': {'Stars':'100', 'LY':'1304','Arc':'84','Wiki':'Messier_1'},   # OC Par
        'Alessi5': {'Stars':'100', 'LY':'1304','Arc':'84','Wiki':'Messier_1'},        # OC Par
        'Alessi5L': {'Stars':'100', 'LY':'1304','Arc':'84','Wiki':'Messier_1'},       # OC Par
        'Alessi5M': {'Stars':'100', 'LY':'1304','Arc':'84','Wiki':'Messier_1'},       # OC Par
         'Cl Alessi 6': {'Stars':'100', 'LY':'2965','Arc':'76','Wiki':'Messier_1'},   # OC Par
        'Alessi6': {'Stars':'100', 'LY':'2965','Arc':'76','Wiki':'Messier_1'},        # OC Par
        'Alessi6L': {'Stars':'100', 'LY':'2965','Arc':'76','Wiki':'Messier_1'},       # OC Par
        'Alessi6M': {'Stars':'100', 'LY':'2965','Arc':'76','Wiki':'Messier_1'},       # OC Par
         'Cl Alessi 8': {'Stars':'100', 'LY':'2205','Arc':'60','Wiki':'Messier_1'},   # OC Par
        'Alessi8': {'Stars':'100', 'LY':'2205','Arc':'60','Wiki':'Messier_1'},        # OC Par
        'Alessi8L': {'Stars':'100', 'LY':'2205','Arc':'60','Wiki':'Messier_1'},       # OC Par
        'Alessi8M': {'Stars':'100', 'LY':'2205','Arc':'60','Wiki':'Messier_1'},       # OC Par
         'Cl Alessi 10': {'Stars':'100', 'LY':'1461','Arc':'63','Wiki':'Messier_1'},  # OC Par
        'Alessi10': {'Stars':'100', 'LY':'1461','Arc':'63','Wiki':'Messier_1'},       # OC Par
        'Alessi10L': {'Stars':'100', 'LY':'1461','Arc':'63','Wiki':'Messier_1'},      # OC Par
        'Alessi10M': {'Stars':'100', 'LY':'1461','Arc':'63','Wiki':'Messier_1'},      # OC Par
         'Cl Alessi 12': {'Stars':'100', 'LY':'1796','Arc':'126','Wiki':'Messier_1'}, # OC Par
        'Alessi12': {'Stars':'100', 'LY':'1796','Arc':'126','Wiki':'Messier_1'},      # OC Par
        'Alessi12L': {'Stars':'100', 'LY':'1796','Arc':'126','Wiki':'Messier_1'},     # OC Par
        'Alessi12M': {'Stars':'100', 'LY':'1796','Arc':'126','Wiki':'Messier_1'},     # OC Par
         'Cl Alessi 19': {'Stars':'100', 'LY':'1907','Arc':'60','Wiki':'Messier_1'},  # OC Par
        'Alessi19': {'Stars':'100', 'LY':'1907','Arc':'60','Wiki':'Messier_1'},       # OC Par
        'Alessi19L': {'Stars':'100', 'LY':'1907','Arc':'60','Wiki':'Messier_1'},      # OC Par
        'Alessi19M': {'Stars':'100', 'LY':'1907','Arc':'60','Wiki':'Messier_1'},      # OC Par
         'Cl Alessi 21': {'Stars':'100', 'LY':'1896','Arc':'66','Wiki':'Messier_1'},  # OC Par
        'Alessi21': {'Stars':'100', 'LY':'1896','Arc':'66','Wiki':'Messier_1'},       # OC Par
        'Alessi21L': {'Stars':'100', 'LY':'1896','Arc':'66','Wiki':'Messier_1'},      # OC Par
        'Alessi21M': {'Stars':'100', 'LY':'1896','Arc':'66','Wiki':'Messier_1'},      # OC Par
         'Cl Alessi 24': {'Stars':'100', 'LY':'1584','Arc':'60','Wiki':'Messier_1'},  # OC Par Alessi 24 = ASCC 89
        'Alessi24': {'Stars':'100', 'LY':'1584','Arc':'60','Wiki':'Messier_1'},       # OC Par Alessi 24 = ASCC 89
        'Alessi24L': {'Stars':'100', 'LY':'1584','Arc':'60','Wiki':'Messier_1'},      # OC Par Alessi 24 = ASCC 89
        'Alessi24M': {'Stars':'100', 'LY':'1584','Arc':'60','Wiki':'Messier_1'},      # OC Par Alessi 24 = ASCC 89
         'Cl Alessi 37': {'Stars':'100', 'LY':'2357','Arc':'60','Wiki':'Messier_1'},  # OC Par
        'Alessi37': {'Stars':'100', 'LY':'2357','Arc':'60','Wiki':'Messier_1'},       # OC Par
        'Alessi37L': {'Stars':'100', 'LY':'2357','Arc':'60','Wiki':'Messier_1'},      # OC Par
        'Alessi37M': {'Stars':'100', 'LY':'2357','Arc':'60','Wiki':'Messier_1'},      # OC Par
         'Cl Alessi 60': {'Stars':'100', 'LY':'9707','Arc':'60','Wiki':'Messier_1'},  # OC Par
        'Alessi60': {'Stars':'100', 'LY':'9707','Arc':'60','Wiki':'Messier_1'},       # OC Par
        'Alessi60L': {'Stars':'100', 'LY':'9707','Arc':'60','Wiki':'Messier_1'},      # OC Par
        'Alessi60M': {'Stars':'100', 'LY':'9707','Arc':'60','Wiki':'Messier_1'},      # OC Par
         'Cl Alessi 62': {'Stars':'100', 'LY':'2050','Arc':'60','Wiki':'Messier_1'},  # OC Par
        'Alessi62': {'Stars':'100', 'LY':'2050','Arc':'60','Wiki':'Messier_1'},       # OC Par
        'Alessi62L': {'Stars':'100', 'LY':'2050','Arc':'60','Wiki':'Messier_1'},      # OC Par
        'Alessi62M': {'Stars':'100', 'LY':'2050','Arc':'60','Wiki':'Messier_1'},      # OC Par
    
         'NAME Alessi Teutsch 3': {'Stars':'100', 'LY':'2301','Arc':'60','Wiki':'Messier_1'},  # OC Par
        'AlessiTeutsch3': {'Stars':'100', 'LY':'2301','Arc':'60','Wiki':'Messier_1'},          # OC Par
        'AlessiTeutsch3L': {'Stars':'100', 'LY':'2301','Arc':'60','Wiki':'Messier_1'},         # OC Par
        'AlessiTeutsch3M': {'Stars':'100', 'LY':'2301','Arc':'60','Wiki':'Messier_1'},         # OC Par
         'NAME Alessi Teutsch 11': {'Stars':'100', 'LY':'2146','Arc':'60','Wiki':'Messier_1'}, # OC Par
        'AlessiTeutsch11': {'Stars':'100', 'LY':'2146','Arc':'60','Wiki':'Messier_1'},         # OC Par
        'AlessiTeutsch11L': {'Stars':'100', 'LY':'2146','Arc':'60','Wiki':'Messier_1'},        # OC Par
        'AlessiTeutsch11M': {'Stars':'100', 'LY':'2146','Arc':'60','Wiki':'Messier_1'},        # OC Par
         'NAME Alessi Teutsch 12': {'Stars':'100', 'LY':'1998','Arc':'60','Wiki':'Messier_1'}, # OC Par
        'AlessiTeutsch12': {'Stars':'100', 'LY':'1998','Arc':'60','Wiki':'Messier_1'},         # OC Par
        'AlessiTeutsch12L': {'Stars':'100', 'LY':'1998','Arc':'60','Wiki':'Messier_1'},        # OC Par
        'AlessiTeutsch12M': {'Stars':'100', 'LY':'1998','Arc':'60','Wiki':'Messier_1'},        # OC Par
    
         'ASCC6': {'Stars':'100', 'LY':'5252','Arc':'60','Wiki':'Messier_1'},   # OC Par [KPR2005] 6
        'ASCC6L': {'Stars':'100', 'LY':'5252','Arc':'60','Wiki':'Messier_1'},   # OC Par [KPR2005] 6
        'ASCC6M': {'Stars':'100', 'LY':'5252','Arc':'60','Wiki':'Messier_1'},   # OC Par [KPR2005] 6
         'ASCC10': {'Stars':'100', 'LY':'2235','Arc':'97','Wiki':'Messier_1'},  # OC Par [KPR2005] 10
        'ASCC10L': {'Stars':'100', 'LY':'2235','Arc':'97','Wiki':'Messier_1'},  # OC Par [KPR2005] 10
        'ASCC10M': {'Stars':'100', 'LY':'2235','Arc':'97','Wiki':'Messier_1'},  # OC Par [KPR2005] 10
         'ASCC13': {'Stars':'100', 'LY':'3632','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 13
        'ASCC13L': {'Stars':'100', 'LY':'3632','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 13
        'ASCC13M': {'Stars':'100', 'LY':'3632','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 13
         'ASCC16': {'Stars':'100', 'LY':'1149','Arc':'70','Wiki':'Messier_1'},  # OC Par [KPR2005] 16
        'ASCC16L': {'Stars':'100', 'LY':'1149','Arc':'70','Wiki':'Messier_1'},  # OC Par [KPR2005] 16
        'ASCC16M': {'Stars':'100', 'LY':'1149','Arc':'70','Wiki':'Messier_1'},  # OC Par [KPR2005] 16
         'ASCC19': {'Stars':'100', 'LY':'1138','Arc':'96','Wiki':'Messier_1'},  # OC Par [KPR2005] 19
        'ASCC19L': {'Stars':'100', 'LY':'1138','Arc':'96','Wiki':'Messier_1'},  # OC Par [KPR2005] 19
        'ASCC19M': {'Stars':'100', 'LY':'1138','Arc':'96','Wiki':'Messier_1'},  # OC Par [KPR2005] 19
         'ASCC21': {'Stars':'100', 'LY':'1630','Arc':'66','Wiki':'Messier_1'},  # OC Par [KPR2005] 21
        'ASCC21L': {'Stars':'100', 'LY':'1630','Arc':'66','Wiki':'Messier_1'},  # OC Par [KPR2005] 21
        'ASCC21M': {'Stars':'100', 'LY':'1630','Arc':'66','Wiki':'Messier_1'},  # OC Par [KPR2005] 21
         'ASCC22': {'Stars':'100', 'LY':'4890','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 22
        'ASCC22L': {'Stars':'100', 'LY':'4890','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 22
        'ASCC22M': {'Stars':'100', 'LY':'4890','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 22
         'ASCC23': {'Stars':'100', 'LY':'2046','Arc':'112','Wiki':'Messier_1'}, # OC Par [KPR2005] 23
        'ASCC23L': {'Stars':'100', 'LY':'2046','Arc':'112','Wiki':'Messier_1'}, # OC Par [KPR2005] 23
        'ASCC23M': {'Stars':'100', 'LY':'2046','Arc':'112','Wiki':'Messier_1'}, # OC Par [KPR2005] 23
         'ASCC29': {'Stars':'100', 'LY':'3455','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 29
        'ASCC29L': {'Stars':'100', 'LY':'3455','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 29
        'ASCC29M': {'Stars':'100', 'LY':'3455','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 29
         'ASCC32': {'Stars':'100', 'LY':'2652','Arc':'89','Wiki':'Messier_1'},  # OC Par [KPR2005] 32
        'ASCC32L': {'Stars':'100', 'LY':'2652','Arc':'89','Wiki':'Messier_1'},  # OC Par [KPR2005] 32
        'ASCC32M': {'Stars':'100', 'LY':'2652','Arc':'89','Wiki':'Messier_1'},  # OC Par [KPR2005] 32
         'ASCC41': {'Stars':'100', 'LY':'973','Arc':'89','Wiki':'Messier_1'},   # OC Par [KPR2005] 41
        'ASCC41L': {'Stars':'100', 'LY':'973','Arc':'89','Wiki':'Messier_1'},   # OC Par [KPR2005] 41
        'ASCC41M': {'Stars':'100', 'LY':'973','Arc':'89','Wiki':'Messier_1'},   # OC Par [KPR2005] 41
         'ASCC58': {'Stars':'100', 'LY':'1583','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 58
        'ASCC58L': {'Stars':'100', 'LY':'1583','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 58
        'ASCC58M': {'Stars':'100', 'LY':'1583','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 58
         'ASCC71': {'Stars':'100', 'LY':'4150','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 71
        'ASCC71L': {'Stars':'100', 'LY':'4150','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 71
        'ASCC71M': {'Stars':'100', 'LY':'4150','Arc':'60','Wiki':'Messier_1'},  # OC Par [KPR2005] 71
         'ASCC101': {'Stars':'100', 'LY':'1311','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 101
        'ASCC101L': {'Stars':'100', 'LY':'1311','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 101
        'ASCC101M': {'Stars':'100', 'LY':'1311','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 101
         'ASCC105': {'Stars':'100', 'LY':'1829','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 105
        'ASCC105L': {'Stars':'100', 'LY':'1829','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 105
        'ASCC105M': {'Stars':'100', 'LY':'1829','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 105
         'ASCC108': {'Stars':'100', 'LY':'3892','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 108
        'ASCC108L': {'Stars':'100', 'LY':'3892','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 108
        'ASCC108M': {'Stars':'100', 'LY':'3892','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 108
         'ASCC112': {'Stars':'100', 'LY':'2146','Arc':'61','Wiki':'Messier_1'}, # OC Par [KPR2005] 112
        'ASCC112L': {'Stars':'100', 'LY':'2146','Arc':'61','Wiki':'Messier_1'}, # OC Par [KPR2005] 112
        'ASCC112M': {'Stars':'100', 'LY':'2146','Arc':'61','Wiki':'Messier_1'}, # OC Par [KPR2005] 112
         'ASCC113': {'Stars':'100', 'LY':'1851','Arc':'74','Wiki':'Messier_1'}, # OC Par [KPR2005] 113
        'ASCC113L': {'Stars':'100', 'LY':'1851','Arc':'74','Wiki':'Messier_1'}, # OC Par [KPR2005] 113
        'ASCC113M': {'Stars':'100', 'LY':'1851','Arc':'74','Wiki':'Messier_1'}, # OC Par [KPR2005] 113
         'ASCC114': {'Stars':'100', 'LY':'3060','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 114
        'ASCC114L': {'Stars':'100', 'LY':'3060','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 114
        'ASCC114M': {'Stars':'100', 'LY':'3060','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 114
         'ASCC115': {'Stars':'100', 'LY':'2487','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 115
        'ASCC115L': {'Stars':'100', 'LY':'2487','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 115
        'ASCC115M': {'Stars':'100', 'LY':'2487','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 115
         'ASCC124': {'Stars':'100', 'LY':'2357','Arc':'54','Wiki':'Messier_1'}, # OC Par [KPR2005] 124
        'ASCC124L': {'Stars':'100', 'LY':'2357','Arc':'54','Wiki':'Messier_1'}, # OC Par [KPR2005] 124
        'ASCC124M': {'Stars':'100', 'LY':'2357','Arc':'54','Wiki':'Messier_1'}, # OC Par [KPR2005] 124
         'ASCC128': {'Stars':'100', 'LY':'2161','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 128
        'ASCC128L': {'Stars':'100', 'LY':'2161','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 128
        'ASCC128M': {'Stars':'100', 'LY':'2161','Arc':'60','Wiki':'Messier_1'}, # OC Par [KPR2005] 128
    
         'Cl Basel11b': {'Stars':'100', 'LY':'6108','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'Basel11b': {'Stars':'100', 'LY':'6108','Arc':'10','Wiki':'Messier_1'},         # OC Par
        'Basel11bL': {'Stars':'100', 'LY':'6108','Arc':'10','Wiki':'Messier_1'},        # OC Par
         'Cl Basel4': {'Stars':'100', 'LY':'11404','Arc':'10','Wiki':'Messier_1'},      # OC Par
        'Basel4': {'Stars':'100', 'LY':'11404','Arc':'10','Wiki':'Messier_1'},          # OC Par
        'Basel4L': {'Stars':'100', 'LY':'11404','Arc':'10','Wiki':'Messier_1'},         # OC Par
         'Cl Berkeley58': {'Stars':'100', 'LY':'11566','Arc':'10','Wiki':'Messier_1'},  # OC Par
        'Berkeley58': {'Stars':'100', 'LY':'11566','Arc':'10','Wiki':'Messier_1'},      # OC Par
        'Berkeley58L': {'Stars':'100', 'LY':'11566','Arc':'10','Wiki':'Messier_1'},     # OC Par
         'Cl Berkeley61': {'Stars':'100', 'LY':'10555','Arc':'10','Wiki':'Messier_1'},  # OC Par
        'Berkeley61': {'Stars':'100', 'LY':'10555','Arc':'10','Wiki':'Messier_1'},      # OC Par
        'Berkeley61L': {'Stars':'100', 'LY':'10555','Arc':'10','Wiki':'Messier_1'},     # OC Par
         'Cl Blanco1': {'Stars':'10000', 'LY':'774','Arc':'1.5','Wiki':'Blanco_1'},     # OC Par
        'Blanco1': {'Stars':'10000', 'LY':'774','Arc':'1.5','Wiki':'Blanco_1'},         # OC Par
        'Blanco1L': {'Stars':'10000', 'LY':'774','Arc':'1.5','Wiki':'Blanco_1'},        # OC Par
         'Cl Bochum3': {'Stars':'100', 'LY':'7280','Arc':'10','Wiki':'Messier_1'},      # OC Par
        'Bochum3': {'Stars':'100', 'LY':'7280','Arc':'10','Wiki':'Messier_1'},          # OC Par
        'Bochum3L': {'Stars':'100', 'LY':'7280','Arc':'10','Wiki':'Messier_1'},         # OC Par
    
         'ESO 166-4': {'Stars':'100', 'LY':'3766','Arc':'10','Wiki':'Messier_1'},       # OC Par 
        'ESO166_4': {'Stars':'100', 'LY':'3766','Arc':'10','Wiki':'Messier_1'},         # OC Par 
        'ESO166_4L': {'Stars':'100', 'LY':'3766','Arc':'10','Wiki':'Messier_1'},        # OC Par 
         'ESO 368-11': {'Stars':'100', 'LY':'7603','Arc':'10','Wiki':'Messier_1'},      # OC Par
        'ESO368_11': {'Stars':'100', 'LY':'7603','Arc':'10','Wiki':'Messier_1'},        # OC Par
        'ESO368_11L': {'Stars':'100', 'LY':'7603','Arc':'10','Wiki':'Messier_1'},       # OC Par
    
         'Cl Collinder140': {'Stars':'100', 'LY':'1270','Arc':'10','Wiki':'Messier_1'}, # OC Par
        'Collinder140': {'Stars':'100', 'LY':'1270','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'Collinder140L': {'Stars':'100', 'LY':'1270','Arc':'10','Wiki':'Messier_1'},    # OC Par
         'Cl Collinder185': {'Stars':'100', 'LY':'5210','Arc':'10','Wiki':'Messier_1'}, # OC Par
        'Collinder185': {'Stars':'100', 'LY':'5210','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'Collinder185L': {'Stars':'100', 'LY':'5210','Arc':'10','Wiki':'Messier_1'},    # OC Par
         'Cl Collinder258': {'Stars':'100', 'LY':'4269','Arc':'10','Wiki':'Messier_1'}, # OC Par
        'Collinder258': {'Stars':'100', 'LY':'4269','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'Collinder258L': {'Stars':'100', 'LY':'4269','Arc':'10','Wiki':'Messier_1'},    # OC Par
         'Cl Collinder268': {'Stars':'100', 'LY':'9136','Arc':'10','Wiki':'Messier_1'}, # OC Par
        'Collinder268': {'Stars':'100', 'LY':'9136','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'Collinder268L': {'Stars':'100', 'LY':'9136','Arc':'10','Wiki':'Messier_1'},    # OC Par
         'Cl Collinder292': {'Stars':'100', 'LY':'6177','Arc':'10','Wiki':'Messier_1'}, # OC Par
        'Collinder292': {'Stars':'100', 'LY':'6177','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'Collinder292L': {'Stars':'100', 'LY':'6177','Arc':'10','Wiki':'Messier_1'},    # OC Par
         'Cl Collinder338': {'Stars':'100', 'LY':'2144','Arc':'10','Wiki':'Messier_1'}, # OC Par
        'Collinder338': {'Stars':'100', 'LY':'2144','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'Collinder338L': {'Stars':'100', 'LY':'2144','Arc':'10','Wiki':'Messier_1'},    # OC Par
         'Cl Collinder394': {'Stars':'100', 'LY':'2349','Arc':'10','Wiki':'Messier_1'}, # OC Par
        'Collinder394': {'Stars':'100', 'LY':'2349','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'Collinder394L': {'Stars':'100', 'LY':'2349','Arc':'10','Wiki':'Messier_1'},    # OC Par
         'Cl Collinder463': {'Stars':'100', 'LY':'2868','Arc':'10','Wiki':'Messier_1'}, # OC Par
        'Collinder463': {'Stars':'100', 'LY':'2868','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'Collinder463L': {'Stars':'100', 'LY':'2868','Arc':'10','Wiki':'Messier_1'},    # OC Par
    
         'Cl Czernik12': {'Stars':'100', 'LY':'6766','Arc':'10','Wiki':'Messier_1'},    # OC Par
        'Czernik12': {'Stars':'100', 'LY':'6766','Arc':'10','Wiki':'Messier_1'},        # OC Par
        'Czernik12L': {'Stars':'100', 'LY':'6766','Arc':'10','Wiki':'Messier_1'},       # OC Par
         'Cl Czernik19': {'Stars':'100', 'LY':'8887','Arc':'10','Wiki':'Messier_1'},    # OC Par
        'Czernik19': {'Stars':'100', 'LY':'8887','Arc':'10','Wiki':'Messier_1'},        # OC Par
        'Czernik19L': {'Stars':'100', 'LY':'8887','Arc':'10','Wiki':'Messier_1'},       # OC Par
         'Cl Czernik25': {'Stars':'100', 'LY':'7446','Arc':'10','Wiki':'Messier_1'},    # OC Par
        'Czernik25': {'Stars':'100', 'LY':'7446','Arc':'10','Wiki':'Messier_1'},        # OC Par
        'Czernik25L': {'Stars':'100', 'LY':'7446','Arc':'10','Wiki':'Messier_1'},       # OC Par
         'Cl Czernik27': {'Stars':'100', 'LY':'14758','Arc':'10','Wiki':'Messier_1'},   # OC Par
        'Czernik27': {'Stars':'100', 'LY':'14758','Arc':'10','Wiki':'Messier_1'},       # OC Par
        'Czernik27L': {'Stars':'100', 'LY':'14758','Arc':'10','Wiki':'Messier_1'},      # OC Par
         'Cl Czernik31': {'Stars':'100', 'LY':'11056','Arc':'10','Wiki':'Messier_1'},   # OC Par
        'Czernik31': {'Stars':'100', 'LY':'11056','Arc':'10','Wiki':'Messier_1'},       # OC Par
        'Czernik31L': {'Stars':'100', 'LY':'11056','Arc':'10','Wiki':'Messier_1'},      # OC Par
    
         'Cl Ferrero 11': {'Stars':'100', 'LY':'2629','Arc':'10','Wiki':'Messier_1'},   # OC
        'Ferrero11': {'Stars':'100', 'LY':'2629','Arc':'10','Wiki':'Messier_1'},        # OC
        'Ferrero11L': {'Stars':'100', 'LY':'2629','Arc':'10','Wiki':'Messier_1'},       # OC
    
         '[FSR2007] 0357': {'Stars':'100', 'LY':'14885','Arc':'10','Wiki':'Messier_1'}, # OC
        'FSR0357': {'Stars':'100', 'LY':'14885','Arc':'10','Wiki':'Messier_1'},         # OC
        'FSR0357L': {'Stars':'100', 'LY':'14885','Arc':'10','Wiki':'Messier_1'},        # OC
         '[FSR2007] 0716': {'Stars':'100', 'LY':'12936','Arc':'10','Wiki':'Messier_1'}, # OC
        'FSR0716': {'Stars':'100', 'LY':'12936','Arc':'10','Wiki':'Messier_1'},         # OC
        'FSR0716L': {'Stars':'100', 'LY':'12936','Arc':'10','Wiki':'Messier_1'},        # OC
         '[FSR2007] 0735': {'Stars':'100', 'LY':'10316','Arc':'10','Wiki':'Messier_1'}, # OC
        'FSR0735': {'Stars':'100', 'LY':'10316','Arc':'10','Wiki':'Messier_1'},         # OC
        'FSR0735L': {'Stars':'100', 'LY':'10316','Arc':'10','Wiki':'Messier_1'},        # OC
         '[FSR2007] 0771': {'Stars':'100', 'LY':'5275','Arc':'10','Wiki':'Messier_1'},  # OC
        'FSR0771': {'Stars':'100', 'LY':'5275','Arc':'10','Wiki':'Messier_1'},          # OC
        'FSR0771L': {'Stars':'100', 'LY':'5275','Arc':'10','Wiki':'Messier_1'},         # OC
         '[FSR2007] 0866': {'Stars':'100', 'LY':'4015','Arc':'10','Wiki':'Messier_1'},  # OC
        'FSR0866': {'Stars':'100', 'LY':'4015','Arc':'10','Wiki':'Messier_1'},          # OC
        'FSR0866L': {'Stars':'100', 'LY':'4015','Arc':'10','Wiki':'Messier_1'},         # OC
         '[FSR2007] 0951': {'Stars':'100', 'LY':'5895','Arc':'10','Wiki':'Messier_1'},  # OC
        'FSR0951': {'Stars':'100', 'LY':'5895','Arc':'10','Wiki':'Messier_1'},          # OC
        'FSR0951L': {'Stars':'100', 'LY':'5895','Arc':'10','Wiki':'Messier_1'},         # OC
         '[FSR2007] 0968': {'Stars':'100', 'LY':'8534','Arc':'10','Wiki':'Messier_1'},  # OC
        'FSR0968': {'Stars':'100', 'LY':'8534','Arc':'10','Wiki':'Messier_1'},          # OC
        'FSR0968L': {'Stars':'100', 'LY':'8534','Arc':'10','Wiki':'Messier_1'},         # OC
         '[FSR2007] 1063': {'Stars':'100', 'LY':'8295','Arc':'10','Wiki':'Messier_1'},  # OC
        'FSR1063': {'Stars':'100', 'LY':'8295','Arc':'10','Wiki':'Messier_1'},          # OC
        'FSR1063L': {'Stars':'100', 'LY':'8295','Arc':'10','Wiki':'Messier_1'},         # OC
         '[FSR2007] 1085': {'Stars':'100', 'LY':'5470','Arc':'10','Wiki':'Messier_1'},  # OC
        'FSR1085': {'Stars':'100', 'LY':'5470','Arc':'10','Wiki':'Messier_1'},          # OC
        'FSR1085L': {'Stars':'100', 'LY':'5470','Arc':'10','Wiki':'Messier_1'},         # OC
         '[FSR2007] 1144': {'Stars':'100', 'LY':'6367','Arc':'10','Wiki':'Messier_1'},  # OC
        'FSR1144': {'Stars':'100', 'LY':'6367','Arc':'10','Wiki':'Messier_1'},          # OC
        'FSR1144L': {'Stars':'100', 'LY':'6367','Arc':'10','Wiki':'Messier_1'},         # OC
         '[FSR2007] 1211': {'Stars':'100', 'LY':'11319','Arc':'10','Wiki':'Messier_1'}, # OC
        'FSR1211': {'Stars':'100', 'LY':'11319','Arc':'10','Wiki':'Messier_1'},         # OC
        'FSR1211L': {'Stars':'100', 'LY':'11319','Arc':'10','Wiki':'Messier_1'},        # OC
         '[FSR2007] 1252': {'Stars':'100', 'LY':'12395','Arc':'10','Wiki':'Messier_1'}, # OC
        'FSR1252': {'Stars':'100', 'LY':'12395','Arc':'10','Wiki':'Messier_1'},         # OC
        'FSR1252L': {'Stars':'100', 'LY':'12395','Arc':'10','Wiki':'Messier_1'},        # OC
         '[FSR2007] 1360': {'Stars':'100', 'LY':'8693','Arc':'10','Wiki':'Messier_1'},  # OC
        'FSR1360': {'Stars':'100', 'LY':'8693','Arc':'10','Wiki':'Messier_1'},          # OC
        'FSR1360L': {'Stars':'100', 'LY':'8693','Arc':'10','Wiki':'Messier_1'},         # OC
         '[FSR2007] 1723': {'Stars':'100', 'LY':'5078','Arc':'10','Wiki':'Messier_1'},  # OC
        'FSR1723': {'Stars':'100', 'LY':'5078','Arc':'10','Wiki':'Messier_1'},          # OC
        'FSR1723L': {'Stars':'100', 'LY':'5078','Arc':'10','Wiki':'Messier_1'},         # OC
    
         'Cl Gulliver 1': {'Stars':'100', 'LY':'10098','Arc':'25','Wiki':'Messier_1'},  # OC
         'Cl Gulliver 2': {'Stars':'100', 'LY':'4686','Arc':'25','Wiki':'Messier_1'},   # OC
         'Cl Gulliver 3': {'Stars':'100', 'LY':'17076','Arc':'25','Wiki':'Messier_1'},  # OC
         'Cl Gulliver 4': {'Stars':'100', 'LY':'10872','Arc':'25','Wiki':'Messier_1'},  # OC
         'Cl Gulliver 5': {'Stars':'100', 'LY':'8033','Arc':'25','Wiki':'Messier_1'},   # OC
         'Cl Gulliver 6': {'Stars':'100', 'LY':'1378','Arc':'25','Wiki':'Messier_1'},   # OC
         'Cl Gulliver 21': {'Stars':'100', 'LY':'2169','Arc':'25','Wiki':'Messier_1'},  # OC
    
         'Cl Haffner3': {'Stars':'100', 'LY':'8602','Arc':'10','Wiki':'Messier_1'},     # OC
         'Cl Haffner6': {'Stars':'100', 'LY':'9956','Arc':'10','Wiki':'Messier_1'},     # OC
         'Cl Haffner9': {'Stars':'100', 'LY':'10432','Arc':'10','Wiki':'Messier_1'},    # OC
         'Cl Haffner13': {'Stars':'100', 'LY':'2328','Arc':'45','Wiki':'Messier_1'},    # OC
         'Cl Haffner14': {'Stars':'100', 'LY':'15650','Arc':'10','Wiki':'Messier_1'},   # OC
         'Cl Haffner21': {'Stars':'100', 'LY':'9620','Arc':'10','Wiki':'Messier_1'},    # OC
         'Cl Haffner22': {'Stars':'100', 'LY':'9115','Arc':'10','Wiki':'Messier_1'},    # OC
         'Cl Haffner23': {'Stars':'100', 'LY':'3260','Arc':'24','Wiki':'Messier_1'},    # OC
         'Cl Haffner26': {'Stars':'100', 'LY':'3260','Arc':'12','Wiki':'Messier_1'},    # OC
        
         'Cl Harvard5': {'Stars':'100', 'LY':'4267','Arc':'25','Wiki':'Messier_1'},     # OC
         'Cl Harvard10': {'Stars':'100', 'LY':'4277','Arc':'25','Wiki':'Messier_1'},    # OC
    
         'IC1369': {'Stars':'100', 'LY':'12448','Arc':'10','Wiki':'IC_2391'},           # OC Par
         'IC2157': {'Stars':'100', 'LY':'7280','Arc':'10','Wiki':'IC_2157'},            # OC Par
         'IC2391': {'Stars':'10000', 'LY':'494','Arc':'50','Wiki':'IC_2391'},           # OC Par
         'IC2488': {'Stars':'100', 'LY':'4542','Arc':'18','Wiki':'IC_2488'},            # OC Par
         'IC2602': {'Stars':'10000', 'LY':'496','Arc':'50','Wiki':'IC_2602'},           # OC Par
         'IC2714': {'Stars':'10000', 'LY':'4536','Arc':'12','Wiki':'IC_2714'},          # OC Par
         'IC4651': {'Stars':'10000', 'LY':'3093','Arc':'10','Wiki':'IC_4651'},          # OC Par
         'IC4665': {'Stars':'100', 'LY':'1127','Arc':'45','Wiki':'IC_4665'},            # OC Par
         'IC4725': {'Stars':'100', 'LY':'2168','Arc':'36','Wiki':'Messier_25'},         # OC Par M25
         'IC4756': {'Stars':'10000', 'LY':'1557','Arc':'40','Wiki':'IC_4756'},          # OC Par
    
         'Cl King4': {'Stars':'100', 'LY':'8628','Arc':'10','Wiki':'Messier_1'},        # OC Par
         'Cl King6': {'Stars':'100', 'LY':'2423','Arc':'10','Wiki':'Messier_1'},        # OC Par
         'Cl King20': {'Stars':'100', 'LY':'6575','Arc':'10','Wiki':'Messier_1'},       # OC Par
    
         'Cl Loden1194': {'Stars':'100', 'LY':'2454','Arc':'22','Wiki':'Messier_1'},    # OC Par
         'Cl Lynga1': {'Stars':'100', 'LY':'7728','Arc':'10','Wiki':'Messier_1'},       # OC Par
         'Cl Lynga2': {'Stars':'100', 'LY':'3154','Arc':'10','Wiki':'Messier_1'},       # OC Par
    
         'Cl Mamajek4': {'Stars':'100', 'LY':'1466','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'Mamajek4': {'Stars':'100', 'LY':'1466','Arc':'10','Wiki':'Messier_1'},         # OC Par
    
         'Melotte20': {'Stars':'21580', 'LY':'570','Arc':'187','Wiki':'Alpha_Persei_Cluster'}, # OC Par
         'Melotte22': {'Stars':'1059', 'LY':'442','Arc':'110','Wiki':'Messier_45'},     # OC Par Pleiades
         'Melotte71': {'Stars':'1059', 'LY':'7515','Arc':'60','Wiki':'Messier_1'},      # OC Par
    
         'Cl Pismis4': {'Stars':'100', 'LY':'2307','Arc':'10','Wiki':'Messier_1'},      # OC Par
         'Cl Platais 3': {'Stars':'100', 'LY':'580','Arc':'10','Wiki':'Messier_1'},     # OC Par
         'Cl Platais 9': {'Stars':'100', 'LY':'597','Arc':'10','Wiki':'Messier_1'},     # OC Par
         'Cl Platais 10': {'Stars':'100', 'LY':'784','Arc':'10','Wiki':'Messier_1'},    # OC Par
    
         'NAME Pozzo 1': {'Stars':'100', 'LY':'1143','Arc':'10','Wiki':'Messier_1'},    # OC Par
    
         'Cl Roslund 3': {'Stars':'100', 'LY':'5575','Arc':'10','Wiki':'Messier_1'},    # OC Par
         'Cl Roslund 6': {'Stars':'100', 'LY':'1161','Arc':'10','Wiki':'Messier_1'},    # OC Par
    
         'Cl Ruprecht1': {'Stars':'100', 'LY':'5169','Arc':'10','Wiki':'Messier_1'},    # OC Par
         'Cl Ruprecht 108': {'Stars':'100', 'LY':'3338','Arc':'10','Wiki':'Messier_1'}, # OC Par
         'Cl Ruprecht115': {'Stars':'100', 'LY':'8911','Arc':'5','Wiki':'Messier_1'},   # OC V Par
         'Cl Ruprecht151': {'Stars':'100', 'LY':'3762','Arc':'10','Wiki':'Messier_1'},  # OC Par
         'Cl Ruprecht 161': {'Stars':'100', 'LY':'3003','Arc':'10','Wiki':'Messier_1'}, # OC Par
         'Cl Ruprecht 176': {'Stars':'100', 'LY':'9736','Arc':'3','Wiki':'Messier_1'},  # OC V Par
         'Cl Ruprecht 29': {'Stars':'100', 'LY':'7413','Arc':'10','Wiki':'Messier_1'},  # OC Par
         'Cl Ruprecht 34': {'Stars':'100', 'LY':'9136','Arc':'10','Wiki':'Messier_1'},  # OC Par
         'Cl Ruprecht 44': {'Stars':'100', 'LY':'21458','Arc':'10','Wiki':'Messier_1'}, # OC Par
         'Cl Ruprecht 50': {'Stars':'100', 'LY':'7878','Arc':'10','Wiki':'Messier_1'},  # OC Par
         'Cl Ruprecht 58': {'Stars':'100', 'LY':'12262','Arc':'10','Wiki':'Messier_1'}, # OC Par
         'Cl Ruprecht 67': {'Stars':'100', 'LY':'5227','Arc':'10','Wiki':'Messier_1'},  # OC Par
         'Cl Ruprecht 76': {'Stars':'100', 'LY':'6999','Arc':'10','Wiki':'Messier_1'},  # OC Par
         'Cl Ruprecht 82': {'Stars':'100', 'LY':'7585','Arc':'10','Wiki':'Messier_1'},  # OC Par
         'Cl Ruprecht 84': {'Stars':'100', 'LY':'6643','Arc':'10','Wiki':'Messier_1'},  # OC Par
         'Cl Ruprecht 93': {'Stars':'100', 'LY':'7481','Arc':'10','Wiki':'Messier_1'},  # OC Par
         'Cl Ruprecht 98': {'Stars':'100', 'LY':'1596','Arc':'10','Wiki':'Messier_1'},  # OC Par
    
         'Cl Stephenson 1': {'Stars':'100', 'LY':'1174','Arc':'10','Wiki':'Messier_1'}, # OC Par
    
         'Cl Stock 1': {'Stars':'100', 'LY':'1333','Arc':'10','Wiki':'Messier_1'},      # OC Par
         'Cl Stock 10': {'Stars':'100', 'LY':'1182','Arc':'10','Wiki':'Messier_1'},     # OC Par
         'Cl Stock 12': {'Stars':'100', 'LY':'1443','Arc':'10','Wiki':'Messier_1'},     # OC Par
         'Cl Stock 23': {'Stars':'100', 'LY':'2022','Arc':'10','Wiki':'Messier_1'},     # OC Par
    
         'Cl Tombaugh 1': {'Stars':'100', 'LY':'8791','Arc':'10','Wiki':'Messier_1'},   # OC Par
    
         'Cl Trumpler 1': {'Stars':'100', 'LY':'9372','Arc':'10','Wiki':'Messier_1'},   # OC Par
         'Cl Trumpler 2': {'Stars':'100', 'LY':'2278','Arc':'10','Wiki':'Messier_1'},   # OC Par
         'Cl Trumpler 7': {'Stars':'100', 'LY':'5887','Arc':'10','Wiki':'Messier_1'},   # OC Par
         'Cl Trumpler 9': {'Stars':'100', 'LY':'9621','Arc':'10','Wiki':'Messier_1'},   # OC Par
    
         'Cl Trumpler 10': {'Stars':'100', 'LY':'1441','Arc':'10','Wiki':'Messier_1'},  # OC Par
         'Cl Trumpler 11': {'Stars':'100', 'LY':'13151','Arc':'10','Wiki':'Messier_1'}, # OC Par
         'Cl Trumpler 12': {'Stars':'100', 'LY':'12892','Arc':'10','Wiki':'Messier_1'}, # OC Par
         'Cl Trumpler 18': {'Stars':'100', 'LY':'5227','Arc':'10','Wiki':'Messier_1'},  # OC Par
    
         'Cl Trumpler 21': {'Stars':'100', 'LY':'4517','Arc':'5','Wiki':'Messier_1'},   # OC V Par
         'Cl Trumpler 22': {'Stars':'100', 'LY':'8450','Arc':'10','Wiki':'Messier_1'},  # OC V Par
         'Cl Trumpler 26': {'Stars':'100', 'LY':'5235','Arc':'10','Wiki':'Messier_1'},  # OC Par
         'Cl Trumpler 29': {'Stars':'100', 'LY':'4846','Arc':'10','Wiki':'Messier_1'},  # OC Par
    
         'Cl Trumpler 30': {'Stars':'100', 'LY':'4613','Arc':'10','Wiki':'Messier_1'},  # OC par
    
         'Cl VDBH 99': {'Stars':'100', 'LY':'1466','Arc':'10','Wiki':'Messier_1'},      # OC Par
        'BH99': {'Stars':'100', 'LY':'1466','Arc':'10','Wiki':'Messier_1'},             # OC Par
         'Cl VDBH 111': {'Stars':'100', 'LY':'9621','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'BH111': {'Stars':'100', 'LY':'9621','Arc':'10','Wiki':'Messier_1'},            # OC Par
         'Cl VDBH 164': {'Stars':'100', 'LY':'1380','Arc':'10','Wiki':'Messier_1'},     # OC Par
        'BH164': {'Stars':'100', 'LY':'1380','Arc':'10','Wiki':'Messier_1'},            # OC Par
        
         'Cl Waterloo 7': {'Stars':'100', 'LY':'12080','Arc':'10','Wiki':'Messier_1'},  # OC Par
    
    
         'Hyades': {'Stars':'10000', 'LY':'155','Arc':'330','Wiki':'Messier_1'}, # OC Cl Melotte 25
    
         'OmegaCentauri': {'Stars':'10000', 'LY':'15800','Arc':'36.3','Wiki':'Omega_Centauri'}, # GC 'NGC5139'
    
         'Praesepe': {'Stars':'771', 'LY':'607','Arc':'95','Wiki':'Beehive_Cluster'}, # NGC2632 M44 OC 95__Beehive Cluster
    
         '47Tucanae': {'Stars':'21580', 'LY':'13000','Arc':'30.9','Wiki':'NGC_104'},  # NGC 104 GC 30.9__arcmins
        '47TucanaeL': {'Stars':'21580', 'LY':'13000','Arc':'30.9','Wiki':'NGC_104'},  # NGC 104 GC 30.9__arcmins
    
         'LMC4':  {'Stars':'100', 'LY':'163000','Arc':'207.6','Wiki':'Large_Magellanic_Cloud'},
         'LMC7':  {'Stars':'100', 'LY':'163000','Arc':'207.6','Wiki':'Large_Magellanic_Cloud'},
         'LMC9':  {'Stars':'100', 'LY':'163000','Arc':'207.6','Wiki':'Large_Magellanic_Cloud'},
         'LMC11': {'Stars':'100', 'LY':'163000','Arc':'207.6','Wiki':'Large_Magellanic_Cloud'},
         'LMC12': {'Stars':'100', 'LY':'163000','Arc':'225.6','Wiki':'Large_Magellanic_Cloud'},
         'LMC13': {'Stars':'100', 'LY':'163000','Arc':'225.6','Wiki':'Large_Magellanic_Cloud'},
    
        'LMC11L': {'Stars':'100', 'LY':'491642','Arc':'207.6','Wiki':'Large_Magellanic_Cloud'},
        'LMC12L': {'Stars':'100', 'LY':'139486','Arc':'225.6','Wiki':'Large_Magellanic_Cloud'},

        'ORION': {'Stars':'100',   'LY':'1329','Arc':'170.4','Wiki':'Messier_1'},
        'ORIONA': {'Stars':'100',   'LY':'1329','Arc':'170.4','Wiki':'Messier_1'},
        'ORIONA_B': {'Stars':'100', 'LY':'1329','Arc':'148.8','Wiki':'Messier_1'},
        'ORIONA_C': {'Stars':'100', 'LY':'1329','Arc':'165.6','Wiki':'Messier_1'},
        'ORIONA_D': {'Stars':'100', 'LY':'1329','Arc':'163.2','Wiki':'Messier_1'},
        'ORIONA_E': {'Stars':'100', 'LY':'1329','Arc':'177.6','Wiki':'Messier_1'},
    
        'ORIONB': {'Stars':'100',   'LY':'1329','Arc':'165.6','Wiki':'Messier_1'},
        'ORIONB_A': {'Stars':'100', 'LY':'1329','Arc':'174','Wiki':'Messier_1'},
        'ORIONB_B': {'Stars':'100', 'LY':'1329','Arc':'166.8','Wiki':'Messier_1'},
    
        'ORIONC': {'Stars':'100',   'LY':'1329','Arc':'151.2','Wiki':'Messier_1'},
        'ORIOND': {'Stars':'100',   'LY':'1329','Arc':'163.2','Wiki':'Messier_1'},
        'ORIONE': {'Stars':'100',   'LY':'1329','Arc':'177.6','Wiki':'Messier_1'},
    
        'ORIONOB1AB': {'Stars':'100',   'LY':'1264','Arc':'177.6','Wiki':'Messier_1'},
        'ORIONOB1AB_A': {'Stars':'100',   'LY':'1264','Arc':'172.8','Wiki':'Messier_1'},
        'ORIONOB1AB_B': {'Stars':'100',   'LY':'1264','Arc':'175.2','Wiki':'Messier_1'},
        'ORIONOB1AB_C': {'Stars':'100',   'LY':'1264','Arc':'176.4','Wiki':'Messier_1'},
        'ORIONOB1AB_D': {'Stars':'100',   'LY':'1264','Arc':'172.8','Wiki':'Messier_1'},
        'ORIONOB1AB_E': {'Stars':'100',   'LY':'1264','Arc':'165.6','Wiki':'Messier_1'},
        'ORIONOB1AB_F': {'Stars':'100',   'LY':'1264','Arc':'174','Wiki':'Messier_1'},
         
        'LAMBDAORI': {'Stars':'100',   'LY':'1467','Arc':'178.8','Wiki':'Messier_1'},
        'LAMBDAORI_A': {'Stars':'100',   'LY':'1467','Arc':'178.8','Wiki':'Messier_1'},
        'LAMBDAORI_B': {'Stars':'100',   'LY':'1467','Arc':'177.6','Wiki':'Messier_1'},
        'LAMBDAORI_C': {'Stars':'100',   'LY':'1467','Arc':'176.4','Wiki':'Messier_1'},
    
        'PLEIADES': {'Stars':'100',   'LY':'4401','Arc':'192','Wiki':'Messier_1'},
        'PLEIADES-E': {'Stars':'100',   'LY':'4401','Arc':'192','Wiki':'Messier_1'},
        'PLEIADES-W': {'Stars':'100',   'LY':'4401','Arc':'184.8','Wiki':'Messier_1'},
    
        'ALPHAPER': {'Stars':'100',   'LY':'561','Arc':'265','Wiki':'Messier_1'},
    
        'TAUL1495': {'Stars':'100',   'LY':'424','Arc':'190.8','Wiki':'Messier_1'},
    
        '006_02': {'Stars':'100',   'LY':'15000','Arc':'116.4','Wiki':'Messier_1'},
    
        '180_00': {'Stars':'100',   'LY':'15000','Arc':'116.4','Wiki':'Messier_1'},
        '180_04': {'Stars':'100',   'LY':'15000','Arc':'116.4','Wiki':'Messier_1'},
        '180_08': {'Stars':'100',   'LY':'15000','Arc':'116.4','Wiki':'Messier_1'},
        '180_12': {'Stars':'100',   'LY':'15000','Arc':'116.4','Wiki':'Messier_1'},
    
    
    

}