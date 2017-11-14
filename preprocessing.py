import pandas as pd


def clean_df(df):
    '''
    Takes the data from the RECS database and returns a dataframe of features
    and target engery consumption

    INPUT
    ------------
    df: Dataframe of input CSV

    Output
    ------------
    X: dataframe of features
    y: dataframe of energy targets
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

    df = df[df.HBUSNESS != 1]
    df = df[df.EQUIPAUX != 1]

    if 'YEARMADE' in df.columns:
        df['HOUSEAGE'] = 2009 - df.YEARMADE

    else:
        df['HOUSEAGE'] = df['HOUSEAGE']

    return df


def create_target(df):
    """"
    Creates energy target from dataframe that contains energy targets
    Input
    -------
    df: Dataframe containing column TOTALBTU

    Output
    -------
    Dataframe with targets removed
    Energy targets
    """

    y = df.pop('TOTALBTU')
    return y


def create_feature_dataframe(df):
    """
    Creates dataframe of features
    Input
    -------
    Cleaned dataframe (no negative values)

    Output
    -------
    Dataframe of features to be used by the model
    """

    X = df[['DIVISION', 'REPORTABLE_DOMAIN', 'TYPEHUQ', 'HDD65', 'CDD65',
            'Climate_Region_Pub', 'AIA_Zone', 'CONDCOOP', 'HOUSEAGE',
            'CONVERSION', 'NUMFLRS', 'NUMAPTS', 'WALLTYPE', 'ROOFTYPE',
            'NAPTFLRS', 'STORIES', 'BEDROOMS', 'NCOMBATH', 'NHAFBATH',
            'TOTROOMS', 'CELLAR', 'CRAWL', 'CONCRETE', 'BASEFIN', 'BASEHEAT',
            'PCTBSTHT', 'BASECOOL', 'PCTBSTCL', 'ATTIC', 'ATTICFIN',
            'ATTCHEAT', 'PCTATTHT', 'ATTCCOOL', 'PCTATTCL', 'PRKGPLC1',
            'SIZEOFGARAGE', 'GARGHEAT', 'GARGCOOL', 'STOVEN', 'STOVENFUEL',
            'STOVE', 'STOVEFUEL', 'OVEN', 'OVENFUEL', 'OVENUSE', 'MICRO',
            'AMTMICRO', 'DEFROST', 'OUTGRILL', 'OUTGRILLFUEL', 'TOASTER',
            'NUMMEAL', 'FUELFOOD', 'NUMFRIG', 'SIZRFRI1', 'AGERFRI1',
            'NUMFREEZ', 'SIZFREEZ', 'AGEFRZR', 'TVCOLOR', 'TVSIZE1',
            'TVTYPE1', 'TVONWD1', 'TVONWE1', 'NUMPC', 'PCTYPE1',
            'TIMEON1', 'WELLPUMP', 'DIPSTICK', 'SWAMPCOL', 'AQUARIUM',
            'HEATHOME', 'EQUIPM', 'FUELHEAT', 'EQUIPAGE', 'HEATOTH',
            'NGFPFLUE', 'USENGFP', 'DIFFUEL', 'EQMAMT', 'HEATROOM',
            'PROTHERM', 'AUTOHEATNITE', 'AUTOHEATDAY', 'TEMPHOME',
            'TEMPGONE', 'TEMPNITE', 'USEMOISTURE', 'NUMH2ONOTNK',
            'NUMH2OHTRS', 'H2OTYPE1', 'FUELH2O', 'WHEATOTH', 'WHEATSIZ',
            'WHEATAGE', 'WHEATBKT', 'COOLTYPE', 'DUCTS', 'CENACHP',
            'ACOTHERS', 'AGECENAC', 'ACROOMS', 'USECENAC', 'PROTHERMAC',
            'AUTOCOOLNITE', 'AUTOCOOLDAY', 'TEMPHOMEAC', 'TEMPGONEAC',
            'TEMPNITEAC', 'NUMBERAC', 'ESWWAC', 'USEWWAC', 'NUMCFAN',
            'USECFAN', 'TREESHAD', 'NOTMOIST', 'USENOTMOIST', 'HIGHCEIL',
            'CATHCEIL', 'POOL', 'FUELPOOL', 'RECBATH', 'FUELTUB', 'LGT12',
            'LGT12EE', 'LGT4', 'LGT4EE', 'LGT1', 'LGT1EE', 'NOUTLGTNT',
            'LGTOEE', 'NGASLIGHT', 'DOOR1SUM', 'WINDOWS', 'TYPEGLASS',
            'ADQINSUL', 'DRAFTY', 'INSTLWS', 'USESOLAR', 'ONSITE',
            'ONSITEGRID', 'NHSLDMEM', 'ATHOME', 'OTHWORK', 'HUPROJ',
            'TOTSQFT', 'WSF', 'OA_LAT'
            ]]

    return X

if __name__ == '__main__':
    df = pd.read_csv('data/recs2009_public.csv')
