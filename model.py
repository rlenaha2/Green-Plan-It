import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import HuberRegressor 
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
import pickle
from preprocessing import clean_df
from preprocessing import create_target
from preprocessing import create_feature_dataframe

def column_index(df, query_cols):
    """
    Creates indecies from column names to be used in OneHotEncoder
    Input 
    ------- 
    Dataframe with all columns
    query_cols columns which indicies will be returned

    Output
    -------
    Indicies of columns from input
    """


    cols = df.columns.values
    sidx = np.argsort(cols)
    return sidx[np.searchsorted(cols,query_cols,sorter=sidx)]


def create_model(X, y):
    '''
    Creates a Ridge Model
    Inputs
    --------
    X: A dataframe with all indicator variables transformed into numerical positive values
    y: reported energy values

    Outputs
    --------


    '''
    
    col_dummies_index = column_index(X, ['DIVISION','REPORTABLE_DOMAIN',
               'TYPEHUQ','Climate_Region_Pub',
               'AIA_Zone','CONDCOOP','CONVERSION','WALLTYPE','ROOFTYPE',
               'STOVENFUEL','STOVEFUEL','OVENFUEL', 'OVENUSE','AMTMICRO',
               'OUTGRILLFUEL', 'NUMMEAL','FUELFOOD', 'TVTYPE1','PCTYPE1',
               'EQUIPM', 'FUELHEAT', 'NGFPFLUE','USENGFP','DIFFUEL','EQMAMT',
               'H2OTYPE1', 'FUELH2O', 'COOLTYPE', 'FUELPOOL','FUELTUB','TYPEGLASS',
               'ADQINSUL','DRAFTY'])

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state = 52)

    pipe = Pipeline([('one_hot_encoder', OneHotEncoder(categorical_features=
                                                           col_dummies_index)),
               ('ridge_model', HuberRegressor(epsilon = 1.3))])
    pipe.fit(X_train, y = (y_train))
    
    with open('pipe_model.p', 'wb') as f:  
        pickle.dump(pipe, f, protocol = 2)



    return pipe 


if __name__=="__main__":
    df = pd.read_csv("recs2009_public.csv")
    df = clean_df(df)
    y = create_target(df)
    X = create_feature_dataframe(df)
    pipe = create_model(X,y)


