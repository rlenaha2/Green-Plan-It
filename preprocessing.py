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
    df.loc[df['FUELTUB'] < 0, 'FUELTUB'] = 0
    df.loc[df['FUELTUB'] == 21, 'FUELTUB'] = 6
    df.loc[df['NOUTLGTNT'] < 0, 'NOUTLGTNT'] = 0
    df.loc[df['INSTLCFL'] < 0, 'INSTLCFL'] = 0
    df.loc[df['WINDOWS'] == 10, 'WINDOWS'] = 1
    df.loc[df['WINDOWS'] == 20, 'WINDOWS'] = 2
    df.loc[df['WINDOWS'] == 30, 'WINDOWS'] = 3
    df.loc[df['WINDOWS'] == 41, 'WINDOWS'] = 4
    df.loc[df['WINDOWS'] == 42, 'WINDOWS'] = 5
    df.loc[df['WINDOWS'] == 50, 'WINDOWS'] = 6
    df.loc[df['WINDOWS'] == 60, 'WINDOWS'] = 7
    df.loc[df['TYPEGLASS'] < 0, 'TYPEGLASS'] = 0
    
    df['HOUSEAGE'] = 2017 - df.YEARMADE

    y = df.pop('KWH')
    y_btu = df.pop('TOTALBTU')


    X = df[['TOTSQFT', 'HOUSEAGE', 'CELLAR', 'GARGCOOL','GARGHEAT',
            'AIRCOND', 'WALLTYPE','ROOFTYPE','DIVISION','Climate_Region_Pub', 
            'HDD65','CDD65','AIA_Zone','NUMFLRS','TOTROOMS','NCOMBATH', 
            'NHAFBATH','CONCRETE','BASEFIN','BASEHEAT','BASECOOL','ATTIC', 
            'ATTCHEAT','ATTCCOOL','HEATHOME','FUELHEAT','WARMAIR','HEATOTH', 
            'USENGFP','TEMPHOME','TEMPGONE','TEMPNITE','NUMH2ONOTNK', 
            'NUMH2OHTRS','H2OTYPE1','FUELH2O','COOLTYPE','ACOTHERS', 
            'USECENAC','ACROOMS','TEMPGONEAC','TEMPHOMEAC','TEMPNITEAC',
            'NUMBERAC','NUMCFAN','USECFAN','TREESHAD','NOTMOIST','HIGHCEIL', 
            'CATHCEIL','POOL','FUELPOOL','RECBATH','FUELTUB','LGT12','LGT1', 
            'NOUTLGTNT','INSTLCFL','SLDDRS','WINDOWS','TYPEGLASS','ADQINSUL',
            'DRAFTY','INSTLWS','USEWOOD','USESOLAR','ELWARM','ELCOOL',
            'UGWARM','UGWATER','ELFOOD','LPWARM','FOWARM','KRWARM',
            'WDWARM','SOLWARM','SOLWATER','ONSITE','NHSLDMEM','ATHOME','WSF']]


    return(X, y_btu)



