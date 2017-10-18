import pandas as pd
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


def clean_df(df):

    df.loc[df['CELLAR'] < 0, 'CELLAR'] = 0
    df.loc[df['CONDCOOP'] < 0, 'CONDCOOP'] = 0
    df.loc[df['GARGCOOL'] < 0, 'GARGCOOL'] = 0
    df.loc[df['GARGHEAT'] < 0, 'GARGHEAT'] = 0
    df.loc[df['ROOFTYPE'] < 0, 'ROOFTYPE'] = 0
    df.loc[df['ORIG1FAM'] < 0, 'ORIG1FAM'] = 0
    df.loc[df['NUMFLRS'] < 0, 'NUMFLRS'] = 1
    df.loc[df['CONCRETE'] < 0, 'CONCRETE'] = 0
    df.loc[df['BASEFIN'] < 0, 'BASEFIN'] = 0
    df.loc[df['BASEHEAT'] < 0, 'BASEHEAT'] = 0
    df.loc[df['BASECOOL'] < 0, 'BASECOOL'] = 0
    df.loc[df['ATTIC'] < 0, 'ATTIC'] = 0
    df.loc[df['ATTCHEAT'] < 0, 'ATTCHEAT'] = 0
    df.loc[df['ATTCCOOL'] < 0, 'ATTCCOOL'] = 0
    df.loc[df['FUELHEAT'] < 0, 'FUELHEAT'] = 0
    df.loc[df['FUELHEAT'] == 21, 'FUELHEAT'] = 6
    df.loc[df['WARMAIR'] < 0, 'WARMAIR'] = 0
    df.loc[df['HEATOTH'] < 0, 'HEATOTH'] = 0
    df.loc[df['USENGFP'] < 0, 'USENGFP'] = 0
    df.loc[df['TEMPGONE'] < 0, 'TEMPGONE'] = 68
    df.loc[df['TEMPHOME'] < 0, 'TEMPHOME'] = 68
    df.loc[df['TEMPNITE'] < 0, 'TEMPNITE'] = 68
    df.loc[df['H2OTYPE1'] < 0, 'H2OTYPE1'] = 0
    df.loc[df['FUELH2O'] < 0, 'FUELH2O'] = 0
    df.loc[df['FUELH2O'] == 21, 'FUELH2O'] = 6
    df.loc[df['COOLTYPE'] < 0, 'COOLTYPE'] = 0
    df.loc[df['ACOTHERS'] < 0, 'ACOTHERS'] = 0
    df.loc[df['USECENAC'] < 0, 'USECENAC'] = 0
    df.loc[df['ACROOMS'] < 0, 'ACROOMS'] = 0
    df.loc[df['USECENAC'] < 0, 'USECENAC'] = 0
    df.loc[df['TEMPGONEAC'] < 0, 'TEMPGONEAC'] = 68
    df.loc[df['TEMPHOMEAC'] < 0, 'TEMPHOMEAC'] = 68
    df.loc[df['TEMPNITEAC'] < 0, 'TEMPNITEAC'] = 68
    df.loc[df['NUMBERAC'] < 0, 'NUMBERAC'] = 0
    df.loc[df['USECFAN'] < 0, 'USECFAN'] = 0
    df.loc[df['HIGHCEIL'] < 0, 'HIGHCEIL'] = 0
    df.loc[df['CATHCEIL'] < 0, 'CATHCEIL'] = 0
    df.loc[df['POOL'] < 0, 'POOL'] = 0
    df.loc[df['FUELPOOL'] < 0, 'FUELPOOL'] = 0
    df.loc[df['FUELPOOL'] == 21, 'FUELPOOL'] = 6
    df.loc[df['FUELPOOL'] == 8, 'FUELPOOL'] = 7
    df.loc[df['FUELTUB'] < 0, 'FUELTUB'] = 0
    df.loc[df['FUELTUB'] == 21, 'FUELTUB'] = 6
    df.loc[df['FUELTUB'] == 8, 'FUELTUB'] = 7
    df.loc[df['NOUTLGTNT'] < 0, 'NOUTLGTNT'] = 0
    df.loc[df['INSTLCFL'] < 0, 'INSTLCFL'] = 0
    df.loc[df['WINDOWS'] == 10, 'WINDOWS'] = 2
    df.loc[df['WINDOWS'] == 20, 'WINDOWS'] = 4
    df.loc[df['WINDOWS'] == 30, 'WINDOWS'] = 8
    df.loc[df['WINDOWS'] == 41, 'WINDOWS'] = 14
    df.loc[df['WINDOWS'] == 42, 'WINDOWS'] = 18
    df.loc[df['WINDOWS'] == 50, 'WINDOWS'] = 25
    df.loc[df['WINDOWS'] == 60, 'WINDOWS'] = 40
    df.loc[df['TYPEGLASS'] < 0, 'TYPEGLASS'] = 0


    df['HOUSEAGE'] = 2009 - df.YEARMADE

    col_dummies = ['REPORTABLE_DOMAIN','TYPEHUQ','WALLTYPE','CONDCOOP','ROOFTYPE','H2OTYPE1',
               'FUELH2O','COOLTYPE','DIVISION','Climate_Region_Pub','AIA_Zone','FUELHEAT',
               'FUELPOOL','FUELTUB','TYPEGLASS','ADQINSUL','DRAFTY']
    df = pd.get_dummies(df, columns=col_dummies)

    y = df.pop('KWH')
    y_btu = df.pop('TOTALBTU')

    X = df[['TOTSQFT', 'HOUSEAGE', 'REPORTABLE_DOMAIN_1','REPORTABLE_DOMAIN_2',
        'REPORTABLE_DOMAIN_3','REPORTABLE_DOMAIN_4','REPORTABLE_DOMAIN_5',
        'REPORTABLE_DOMAIN_6','REPORTABLE_DOMAIN_7','REPORTABLE_DOMAIN_8',
        'REPORTABLE_DOMAIN_9','REPORTABLE_DOMAIN_10','REPORTABLE_DOMAIN_11',
        'REPORTABLE_DOMAIN_12','REPORTABLE_DOMAIN_13','REPORTABLE_DOMAIN_14',
        'REPORTABLE_DOMAIN_15','REPORTABLE_DOMAIN_16','REPORTABLE_DOMAIN_17',
        'REPORTABLE_DOMAIN_18','REPORTABLE_DOMAIN_19','REPORTABLE_DOMAIN_20',
        'REPORTABLE_DOMAIN_21','REPORTABLE_DOMAIN_22','REPORTABLE_DOMAIN_23',
        'REPORTABLE_DOMAIN_24','REPORTABLE_DOMAIN_25','REPORTABLE_DOMAIN_26',
        'TYPEHUQ_1','TYPEHUQ_2','TYPEHUQ_3','TYPEHUQ_4', 'CELLAR', 'GARGCOOL',
        'GARGHEAT', 'AIRCOND', 'WALLTYPE_1', 'WALLTYPE_2', 'WALLTYPE_3', 'WALLTYPE_4',
        'WALLTYPE_5', 'WALLTYPE_6', 'WALLTYPE_7', 'WALLTYPE_8', 'CONDCOOP_0',
        'CONDCOOP_1', 'ROOFTYPE_0', 'ROOFTYPE_1', 'ROOFTYPE_2', 'ROOFTYPE_3', 
        'ROOFTYPE_4', 'ROOFTYPE_5', 'ROOFTYPE_6', 'ROOFTYPE_7', 'DIVISION_1', 
        'DIVISION_2', 'DIVISION_3', 'DIVISION_4', 'DIVISION_5', 'DIVISION_6', 
        'DIVISION_7', 'DIVISION_8', 'DIVISION_9', 'Climate_Region_Pub_1',
        'Climate_Region_Pub_2', 'Climate_Region_Pub_3', 'Climate_Region_Pub_4',
        'HDD65','CDD65', 'AIA_Zone_1', 'AIA_Zone_2', 'AIA_Zone_3', 'AIA_Zone_4',
        'NUMFLRS','TOTROOMS','NCOMBATH','NHAFBATH', 'CONCRETE','BASEFIN',
        'BASEHEAT','BASECOOL','ATTIC','ATTCHEAT', 'ATTCCOOL','HEATHOME',
        'FUELHEAT_0', 'FUELHEAT_1', 'FUELHEAT_2', 'FUELHEAT_3', 'FUELHEAT_4',
        'FUELHEAT_5', 'FUELHEAT_6', 'FUELHEAT_7', 'FUELHEAT_8','WARMAIR',
        'HEATOTH','USENGFP','TEMPHOME','TEMPGONE','TEMPNITE','NUMH2ONOTNK',
        'NUMH2OHTRS','H2OTYPE1_0', 'H2OTYPE1_1', 'FUELH2O_0', 'FUELH2O_1',
        'FUELH2O_2', 'FUELH2O_3', 'FUELH2O_4', 'FUELH2O_5', 'FUELH2O_6', 'FUELH2O_7',
        'COOLTYPE_0', 'COOLTYPE_1', 'COOLTYPE_2', 'ACOTHERS','USECENAC','ACROOMS',
        'TEMPGONEAC','TEMPHOMEAC','TEMPNITEAC','NUMBERAC','NUMCFAN',
        'USECFAN','TREESHAD','NOTMOIST','HIGHCEIL','CATHCEIL','POOL',
        'FUELPOOL_0', 'FUELPOOL_1', 'FUELPOOL_2', 'FUELPOOL_3', 
        'FUELPOOL_5', 'FUELPOOL_6','RECBATH','FUELTUB_0','FUELTUB_1',
        'FUELTUB_2','FUELTUB_3', 'FUELTUB_5', 'FUELTUB_6', 
        'LGT12','LGT1','NOUTLGTNT','INSTLCFL','SLDDRS','WINDOWS','TYPEGLASS_0',
        'TYPEGLASS_1', 'TYPEGLASS_2', 'ADQINSUL_1', 'ADQINSUL_2', 'ADQINSUL_3',
        'DRAFTY_1', 'DRAFTY_2', 'DRAFTY_3', 'INSTLWS','USEWOOD','USESOLAR','ELWARM','ELCOOL','UGWARM',
        'UGWATER','ELFOOD','LPWARM','FOWARM','KRWARM','WDWARM','SOLWARM',
        'SOLWATER','ONSITE','NHSLDMEM','ATHOME','WSF','ELECAUX', 'ELOTHER','OTHWORK']]



    return X, y_btu



