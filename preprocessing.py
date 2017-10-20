import pandas as pd


def clean_df(df):
'''
Takes the data from the RECS database and returns a dataframe of features and 
target engery consumption

INPUT
------------
Dataframe


Output
------------
X: dataframe of features
y: datafram of energy targets
'''


    df.loc[df['CONDCOOP'] < 0, 'CONDCOOP'] = 0
    df.loc[df['CONVERSION'] < 0, 'CONVERSION'] = 0
    df.loc[df['NUMFLRS'] < 0, 'NUMFLRS'] = 0
    df.loc[df['NUMAPTS'] < 0, 'NUMAPTS'] = 1
    df.loc[df['ROOFTYPE'] < 0, 'ROOFTYPE'] = 0
    df.loc[df['NAPTFLRS'] < 0, 'NAPTFLRS'] = 0
    df.loc[df['STORIES'] == -2, 'STORIES'] = 1
    df.loc[df['STORIES'] == 10, 'STORIES'] = 1
    df.loc[df['STORIES'] == 20, 'STORIES'] = 2
    df.loc[df['STORIES'] == 31, 'STORIES'] = 3
    df.loc[df['STORIES'] == 32, 'STORIES'] = 4
    df.loc[df['STORIES'] == 40, 'STORIES'] = 2
    df.loc[df['STORIES'] == 50, 'STORIES'] = 2
    df.loc[df['BEDROOMS'] < 0, 'BEDROOMS'] = 1
    df.loc[df['CELLAR'] < 0, 'CELLAR'] = 0
    df.loc[df['CRAWL'] < 0, 'CRAWL'] = 0
    df.loc[df['CONCRETE'] < 0, 'CONCRETE'] = 0
    df.loc[df['BASEFIN'] < 0, 'BASEFIN'] = 0
    df.loc[df['BASEHEAT'] < 0, 'BASEHEAT'] = 0
    df.loc[df['PCTBSTHT'] < 0, 'PCTBSTHT'] = 0
    df.loc[df['BASECOOL'] < 0, 'BASECOOL'] = 0
    df.loc[df['PCTBSTCL'] < 0, 'PCTBSTCL'] = 0
    df.loc[df['ATTIC'] < 0, 'ATTIC'] = 0
    df.loc[df['ATTICFIN'] < 0, 'ATTICFIN'] = 0
    df.loc[df['ATTCHEAT'] < 0, 'ATTCHEAT'] = 0
    df.loc[df['PCTATTHT'] < 0, 'PCTATTHT'] = 0
    df.loc[df['ATTCCOOL'] < 0, 'ATTCCOOL'] = 0
    df.loc[df['PCTATTCL'] < 0, 'PCTATTCL'] = 0
    df.loc[df['PRKGPLC1'] < 0, 'PRKGPLC1'] = 0
    df.loc[df['SIZEOFGARAGE'] < 0, 'SIZEOFGARAGE'] = 0
    df.loc[df['GARGHEAT'] < 0, 'GARGHEAT'] = 0
    df.loc[df['GARGCOOL'] < 0, 'GARGCOOL'] = 0
    df.loc[df['STOVENFUEL'] < 0, 'STOVENFUEL'] = 0
    df.loc[df['STOVENFUEL'] == 21, 'STOVENFUEL'] = 3
    df.loc[df['STOVENFUEL'] == 5, 'STOVENFUEL'] = 4
    df.loc[df['STOVEFUEL'] < 0, 'STOVEFUEL'] = 0
    df.loc[df['STOVEFUEL'] == 5, 'STOVEFUEL'] = 3
    df.loc[df['OVENFUEL'] < 0, 'OVENFUEL'] = 0
    df.loc[df['OVENFUEL'] == 5, 'OVENFUEL'] = 3
    df.loc[df['OVENUSE'] < 0, 'OVENUSE'] = 0
    df.loc[df['AMTMICRO'] < 0, 'AMTMICRO'] = 0
    df.loc[df['DEFROST'] < 0, 'DEFROST'] = 0
    df.loc[df['OUTGRILLFUEL'] < 0, 'OUTGRILLFUEL'] = 0
    df.loc[df['OUTGRILLFUEL'] == 21, 'OUTGRILLFUEL'] = 3
    df.loc[df['FUELFOOD'] < 0, 'FUELFOOD'] = 0
    df.loc[df['FUELFOOD'] == 21, 'FUELFOOD'] = 3
    df.loc[df['FUELFOOD'] == 5, 'FUELFOOD'] = 4
    df.loc[df['SIZRFRI1'] < 0, 'SIZRFRI1'] = 0
    df.loc[df['AGERFRI1'] < 0, 'AGERFRI1'] = 0
    df.loc[df['AGERFRI1'] == 1, 'AGERFRI1'] = 1
    df.loc[df['AGERFRI1'] == 2, 'AGERFRI1'] = 3
    df.loc[df['AGERFRI1'] == 3, 'AGERFRI1'] = 7
    df.loc[df['AGERFRI1'] == 41, 'AGERFRI1'] = 12
    df.loc[df['AGERFRI1'] == 41, 'AGERFRI1'] = 17
    df.loc[df['AGERFRI1'] == 5, 'AGERFRI1'] = 25
    df.loc[df['AGERFRI1'] < 0, 'AGERFRI1'] = 0
    df.loc[df['NUMFREEZ'] < 0, 'NUMFREEZ'] = 0
    df.loc[df['SIZFREEZ'] < 0, 'SIZFREEZ'] = 0
    df.loc[df['AGEFRZR'] < 0, 'AGEFRZR'] = 0
    df.loc[df['AGEFRZR'] == 1, 'AGEFRZR'] = 1
    df.loc[df['AGEFRZR'] == 2, 'AGEFRZR'] = 3
    df.loc[df['AGEFRZR'] == 3, 'AGEFRZR'] = 7
    df.loc[df['AGEFRZR'] == 41, 'AGEFRZR'] = 12
    df.loc[df['AGEFRZR'] == 41, 'AGEFRZR'] = 17
    df.loc[df['AGEFRZR'] == 5, 'AGEFRZR'] = 25
    df.loc[df['TVSIZE1'] < 0, 'TVSIZE1'] = 0
    df.loc[df['TVTYPE1'] < 0, 'TVTYPE1'] = 0
    df.loc[df['TVONWD1'] < 0, 'TVONWD1'] = 0
    df.loc[df['TVONWE1'] < 0, 'TVONWE1'] = 0
    df.loc[df['PCTYPE1'] < 0, 'PCTYPE1'] = 0
    df.loc[df['TIMEON1'] < 0, 'TIMEON1'] = 0
    df.loc[df['WELLPUMP'] < 0, 'WELLPUMP'] = 0
    df.loc[df['DIPSTICK'] < 0, 'DIPSTICK'] = 0
    df.loc[df['SWAMPCOL'] < 0, 'SWAMPCOL'] = 0
    df.loc[df['EQUIPM'] < 1, 'EQUIPM'] = 0
    df.loc[df['EQUIPM'] == 21, 'EQUIPM'] = 1
    df.loc[df['FUELHEAT'] < 0, 'FUELHEAT'] = 0
    df.loc[df['FUELHEAT'] == 21, 'FUELHEAT'] = 6
    df.loc[df['EQUIPAGE'] < 0, 'EQUIPAGE'] = 0
    df.loc[df['EQUIPAGE'] == 1, 'EQUIPAGE'] = 1
    df.loc[df['EQUIPAGE'] == 2, 'EQUIPAGE'] = 3
    df.loc[df['EQUIPAGE'] == 3, 'EQUIPAGE'] = 7
    df.loc[df['EQUIPAGE'] == 41, 'EQUIPAGE'] = 12
    df.loc[df['EQUIPAGE'] == 41, 'EQUIPAGE'] = 17
    df.loc[df['EQUIPAGE'] == 5, 'EQUIPAGE'] = 25
    df.loc[df['HEATOTH'] < 0, 'HEATOTH'] = 0
    df.loc[df['EQUIPAUX'] < 0, 'EQUIPAUX'] = 0
    df.loc[df['NGFPFLUE'] < 0, 'NGFPFLUE'] = 0
    df.loc[df['USENGFP'] < 0, 'USENGFP'] = 0
    df.loc[df['DIFFUEL'] < 0, 'DIFFUEL'] = 0
    df.loc[df['DIFFUEL'] == 21, 'DIFFUEL'] = 6
    df.loc[df['EQMAMT'] < 0, 'EQMAMT'] = 0
    df.loc[df['HEATROOM'] < 0, 'HEATROOM'] = 0
    df.loc[df['PROTHERM'] < 0, 'PROTHERM'] = 0
    df.loc[df['AUTOHEATNITE'] < 0, 'AUTOHEATNITE'] = 0
    df.loc[df['AUTOHEATDAY'] < 0, 'AUTOHEDAY'] = 0
    df.loc[df['TEMPHOME'] < 0, 'TEMPHOME'] = 68
    df.loc[df['TEMPGONE'] < 0, 'TEMPGONE'] = 68
    df.loc[df['TEMPNITE'] < 0, 'TEMPNITE'] = 68
    df.loc[df['USEMOISTURE'] < 0, 'USEMOISTURE'] = 0
    df.loc[df['H2OTYPE1'] < 0, 'H2OTYPE1'] = 0
    df.loc[df['FUELH2O'] < 0, 'FUELH2O'] = 0
    df.loc[df['FUELH2O'] == 21, 'FUELH2O'] = 6
    df.loc[df['WHEATOTH'] < 0, 'WHEATOTH'] = 0
    df.loc[df['WHEATSIZ'] < 0, 'WHEATSIZ'] = 0
    df.loc[df['WHEATAGE'] < 0, 'EQUIPAGE'] = 0
    df.loc[df['WHEATAGE'] == 1, 'WHEATAGE'] = 1
    df.loc[df['WHEATAGE'] == 2, 'WHEATAGE'] = 3
    df.loc[df['WHEATAGE'] == 3, 'WHEATAGE'] = 7
    df.loc[df['WHEATAGE'] == 41, 'WHEATAGE'] = 12
    df.loc[df['WHEATAGE'] == 41, 'WHEATAGE'] = 17
    df.loc[df['WHEATAGE'] == 5, 'WHEATAGE'] = 25
    df.loc[df['WHEATBKT'] < 0, 'WHEATBKT'] = 0
    df.loc[df['COOLTYPE'] < 0, 'COOLTYPE'] = 0
    df.loc[df['DUCTS'] < 0, 'DUCTS'] = 0
    df.loc[df['CENACHP'] < 0, 'CENACHP'] = 0
    df.loc[df['ACOTHERS'] < 0, 'ACOTHERS'] = 0
    df.loc[df['AGECENAC'] == 1, 'AGECENAC'] = 1
    df.loc[df['AGECENAC'] == 2, 'AGECENAC'] = 3
    df.loc[df['AGECENAC'] == 3, 'AGECENAC'] = 7
    df.loc[df['AGECENAC'] == 41, 'AGECENAC'] = 12
    df.loc[df['AGECENAC'] == 41, 'AGECENAC'] = 17
    df.loc[df['AGECENAC'] == 5, 'AGECENAC'] = 25
    df.loc[df['ACROOMS'] < 0, 'ACROOMS'] = 0
    df.loc[df['USECENAC'] < 0, 'USECENAC'] = 0
    df.loc[df['PROTHERMAC'] < 0, 'PROTHERMAC'] = 0
    df.loc[df['AUTOCOOLNITE'] < 0, 'AUTOCOOLNITE'] = 0
    df.loc[df['AUTOCOOLDAY'] < 0, 'AUTOCOOLDAY'] = 0
    df.loc[df['TEMPHOMEAC'] < 0, 'TEMPHOMEAC'] = 68
    df.loc[df['TEMPGONEAC'] < 0, 'TEMPGONEAC'] = 68
    df.loc[df['TEMPNITEAC'] < 0, 'TEMPNITEAC'] = 68
    df.loc[df['NUMBERAC'] < 0, 'NUMBERAC'] = 0
    df.loc[df['ESWWAC'] < 0, 'ESWWAC'] = 0
    df.loc[df['USEWWAC'] < 0, 'USEWWAC'] = 0
    df.loc[df['USECFAN'] < 0, 'USECFAN'] = 0
    df.loc[df['USENOTMOIST'] < 0, 'USENOTMOIST'] = 0
    df.loc[df['HIGHCEIL'] < 0, 'HIGHCEIL'] = 0
    df.loc[df['CATHCEIL'] < 0, 'CATHCEIL'] = 0
    df.loc[df['POOL'] < 0, 'POOL'] = 0
    df.loc[df['FUELPOOL'] < 0, 'FUELPOOL'] = 0
    df.loc[df['FUELPOOL'] == 21, 'FUELPOOL'] = 6
    df.loc[df['FUELPOOL'] == 8, 'FUELPOOL'] = 7
    df.loc[df['FUELTUB'] < 0, 'FUELTUB'] = 0
    df.loc[df['FUELTUB'] == 21, 'FUELTUB'] = 6
    df.loc[df['FUELTUB'] == 8, 'FUELTUB'] = 7
    df.loc[df['LGT12EE'] < 0, 'LGT12EE'] = 0
    df.loc[df['LGT4EE'] < 0, 'LGT4EE'] = 0
    df.loc[df['LGT1EE'] < 0, 'LGT1EE'] = 0
    df.loc[df['NOUTLGTNT'] < 0, 'NOUTLGTNT'] = 0
    df.loc[df['LGTOEE'] < 0, 'LGTOEE'] = 0
    df.loc[df['NGASLIGHT'] < 0, 'NGASLIGHT'] = 0
    df.loc[df['WINDOWS'] == 10, 'WINDOWS'] = 2
    df.loc[df['WINDOWS'] == 20, 'WINDOWS'] = 4
    df.loc[df['WINDOWS'] == 30, 'WINDOWS'] = 8
    df.loc[df['WINDOWS'] == 41, 'WINDOWS'] = 14
    df.loc[df['WINDOWS'] == 42, 'WINDOWS'] = 18
    df.loc[df['WINDOWS'] == 50, 'WINDOWS'] = 25
    df.loc[df['WINDOWS'] == 60, 'WINDOWS'] = 40
    df.loc[df['TYPEGLASS'] < 0, 'TYPEGLASS'] = 0
    df.loc[df['ONSITEGRID'] < 0, 'ONSITEGRID'] = 0
    df.loc[df['HUPROJ'] < 0, 'HUPROJ'] = 0
    
    df['HOUSEAGE'] = 2009 - df.YEARMADE

    X = df[['DIVISION_1', 'DIVISION_2', 'DIVISION_3', 'DIVISION_4', 
        'DIVISION_5', 'DIVISION_6', 'DIVISION_7', 'DIVISION_8', 
        'DIVISION_9', 'REPORTABLE_DOMAIN_1','REPORTABLE_DOMAIN_2',
        'REPORTABLE_DOMAIN_3','REPORTABLE_DOMAIN_4','REPORTABLE_DOMAIN_5',
        'REPORTABLE_DOMAIN_6','REPORTABLE_DOMAIN_7','REPORTABLE_DOMAIN_8',
        'REPORTABLE_DOMAIN_9','REPORTABLE_DOMAIN_10','REPORTABLE_DOMAIN_11',
        'REPORTABLE_DOMAIN_12','REPORTABLE_DOMAIN_13','REPORTABLE_DOMAIN_14',
        'REPORTABLE_DOMAIN_15','REPORTABLE_DOMAIN_16','REPORTABLE_DOMAIN_17',
        'REPORTABLE_DOMAIN_18','REPORTABLE_DOMAIN_19','REPORTABLE_DOMAIN_20',
        'REPORTABLE_DOMAIN_21','REPORTABLE_DOMAIN_22','REPORTABLE_DOMAIN_23',
        'REPORTABLE_DOMAIN_24','REPORTABLE_DOMAIN_25','REPORTABLE_DOMAIN_26',
        'TYPEHUQ_1','TYPEHUQ_2','TYPEHUQ_3','TYPEHUQ_4','HDD65','CDD65',
        'Climate_Region_Pub_1', 'Climate_Region_Pub_2', 'Climate_Region_Pub_3',
        'Climate_Region_Pub_4', 'AIA_Zone_1', 'AIA_Zone_2', 'AIA_Zone_3', 
        'AIA_Zone_4', 'CONDCOOP_0', 'CONDCOOP_1', 'HOUSEAGE', 'CONVERSION_0',
        'CONVERSION_1', 'NUMFLRS', 'NUMAPTS', 'WALLTYPE_1', 'WALLTYPE_2',
        'WALLTYPE_3', 'WALLTYPE_4', 'WALLTYPE_5', 'WALLTYPE_6', 'WALLTYPE_7',
        'WALLTYPE_8','ROOFTYPE_0', 'ROOFTYPE_1', 'ROOFTYPE_2', 'ROOFTYPE_3', 
        'ROOFTYPE_4', 'ROOFTYPE_5', 'ROOFTYPE_6', 'ROOFTYPE_7', 'NAPTFLRS',
        'STORIES', 'BEDROOMS', 'NCOMBATH', 'NHAFBATH', 'TOTROOMS','CELLAR',
        'CRAWL', 'CONCRETE', 'BASEFIN' ,'BASEHEAT', 'PCTBSTHT', 'BASECOOL',
        'PCTBSTCL', 'ATTIC', 'ATTICFIN', 'ATTCHEAT', 'PCTATTHT', 'ATTCCOOL',
        'PCTATTCL', 'PRKGPLC1', 'SIZEOFGARAGE', 'GARGHEAT', 'GARGCOOL', 
        'STOVEN', 'STOVENFUEL_0', 'STOVENFUEL_1', 'STOVENFUEL_2', 'STOVENFUEL_3',
        'STOVE', 'STOVEFUEL_0', 'STOVEFUEL_1', 'STOVEFUEL_2', 
        'OVEN', 'OVENFUEL_0', 'OVENFUEL_1', 'OVENFUEL_2', 'OVENUSE_0', 
        'OVENUSE_1', 'OVENUSE_2', 'OVENUSE_3', 'OVENUSE_4',
        'OVENUSE_5', 'MICRO', 'AMTMICRO_0', 'AMTMICRO_1', 'AMTMICRO_2', 
        'AMTMICRO_3', 'DEFROST', 'OUTGRILL', 'OUTGRILLFUEL_0','OUTGRILLFUEL_1',
        'OUTGRILLFUEL_2', 'TOASTER', 'NUMMEAL_0', 'NUMMEAL_1','NUMMEAL_2',
        'NUMMEAL_3', 'NUMMEAL_4','NUMMEAL_5', 'FUELFOOD_0', 'FUELFOOD_1', 
        'FUELFOOD_2', 'FUELFOOD_3', 'NUMFRIG', 'SIZRFRI1', 'AGERFRI1', 
        'SIZRFRI2', 'NUMFREEZ', 'SIZFREEZ', 'AGEFRZR', 'DWASHUSE',
        'AGEDW', 'ESDISHW', 'TVCOLOR','TVSIZE1', 'TVTYPE1_0', 
        'TVTYPE1_1', 'TVTYPE1_2', 'TVTYPE1_3','TVTYPE1_4', 
        'TVAUDIOSYS1', 'TVONWD1', 'TVONWE1', 'TVSIZE2', 'NUMPC', 
        'PCTYPE1_0', 'PCTYPE1_1', 'TIMEON1','WELLPUMP', 'DIPSTICK', 
        'SWAMPCOL', 'AQUARIUM', 'HEATHOME', 'EQUIPM_0', 'EQUIPM_1',
        'EQUIPM_2', 'EQUIPM_3', 'EQUIPM_4', 'EQUIPM_5', 'EQUIPM_6', 'EQUIPM_7',
        'EQUIPM_8', 'EQUIPM_9', 'EQUIPM_10', 'EQUIPM_11','FUELHEAT_0', 
        'FUELHEAT_1', 'FUELHEAT_2', 'FUELHEAT_3', 'FUELHEAT_4','FUELHEAT_5',
        'FUELHEAT_6', 'FUELHEAT_7', 'FUELHEAT_8', 'EQUIPAGE', 'HEATOTH',
        'EQUIPAUX', 'NGFPFLUE_0', 'NGFPFLUE_1', 'USENGFP_0', 'USENGFP_1',
        'USENGFP_2', 'DIFFUEL_0', 'DIFFUEL_1', 'DIFFUEL_2', 'DIFFUEL_3',
        'DIFFUEL_5', 'DIFFUEL_6', 'DIFFUEL_7', 'DIFFUEL_8',
        'EQMAMT_0', 'EQMAMT_1', 'EQMAMT_2', 'HEATROOM', 'PROTHERM', 
        'AUTOHEATNITE', 'AUTOHEATDAY', 'TEMPHOME', 'TEMPGONE', 'TEMPNITE',
        'USEMOISTURE', 'NUMH2ONOTNK', 'NUMH2OHTRS', 'H2OTYPE1_0', 
        'H2OTYPE1_1', 'FUELH2O_0', 'FUELH2O_1',
        'FUELH2O_2', 'FUELH2O_3', 'FUELH2O_4', 'FUELH2O_5', 'FUELH2O_6', 
        'FUELH2O_7', 'WHEATOTH', 'WHEATSIZ', 'WHEATAGE', 'WHEATBKT',
        'COOLTYPE_0','COOLTYPE_1', 'COOLTYPE_2', 'DUCTS', 
        'CENACHP', 'ACOTHERS', 'AGECENAC', 'ACROOMS', 'USECENAC', 
        'PROTHERMAC', 'AUTOCOOLNITE', 'AUTOCOOLDAY', 'TEMPHOMEAC',
        'TEMPGONEAC', 'TEMPNITEAC', 'NUMBERAC', 'ESWWAC', 'USEWWAC',
        'NUMCFAN', 'USECFAN', 'TREESHAD', 'NOTMOIST', 'USENOTMOIST',
        'HIGHCEIL', 'CATHCEIL', 'POOL', 'FUELPOOL_1', 'FUELPOOL_2',
        'FUELPOOL_3',  'FUELPOOL_5', 'FUELPOOL_6',
        'FUELPOOL_7', 'RECBATH', 'FUELTUB_1', 'FUELTUB_2',
        'FUELTUB_3', 'FUELTUB_5', 'FUELTUB_6',
        'FUELTUB_7', 'LGT12', 'LGT12EE', 'LGT4', 'LGT4EE', 'LGT1',
        'LGT1EE', 'NOUTLGTNT', 'LGTOEE', 'NGASLIGHT', 'DOOR1SUM',
        'WINDOWS','TYPEGLASS_0', 'TYPEGLASS_1', 'TYPEGLASS_2',
        'ADQINSUL_1', 'ADQINSUL_2', 'ADQINSUL_3', 'DRAFTY_1',
        'DRAFTY_2', 'DRAFTY_3', 'INSTLWS', 'USESOLAR', 'ONSITE',
        'ONSITEGRID', 'NHSLDMEM', 'HBUSNESS', 'ATHOME', 'OTHWORK',
        'HUPROJ', 'TOTSQFT', 'WSF', 'OA_LAT'
        ]]



    df = pd.get_dummies(df, columns=col_dummies)

    y = df.pop('KWH')
    y_btu = df.pop('TOTALBTU')

 
    return X, y_btu



