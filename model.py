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
import matplotlib.pyplot as plt


def column_index(df, query_cols):
    """
    Creates indecies from column names to be used in OneHotEncoder

    Input
    -------
    df: Dataframe with all columns
    query_cols: columns which indicies will be returned

    Output
    -------
    Indicies of columns from input Dataframe
    """

    cols = df.columns.values
    sidx = np.argsort(cols)
    return sidx[np.searchsorted(cols, query_cols, sorter=sidx)]


def create_split(X, y):
    '''
    Creates a test train split of the data

    Inputs
    --------
    X: Feature dataframe
    y: targets (TOTALBTU from origin Dataframe)

    Output
    --------
    Dataframes containing a testing set and training set
    '''

    X_train, X_test, y_train, y_test = train_test_split(
                                       X, y, random_state=52)

    return X_train, X_test, y_train, y_test


def create_split_files(X_test, y_test):
    '''
    Creates csv files to be read by plot file
    Inputs
    -------
    X_test: Features that were not trained on
    y_test: Target values to be predicted
    Outputs
    -------
    Writes a CSV to file that can be used later
    '''

    X_test.to_csv('X_test.csv')
    y_test.to_csv('y_test.csv')

    return X_test, y_test

def create_model(X_train, y_train):
    '''
    Creates a Linear Model minimizing the Huber loss

    Inputs
    --------
    X_train: A dataframe with all indicator variables transformed
             into numerical positive values
    y_train: reported energy values

    Outputs
    --------
    Pipe object that can be used to make predictions
    Also created a pickle of the pipe object in the current directory
    '''

    col_index = column_index(X, ['DIVISION', 'REPORTABLE_DOMAIN',
                                 'TYPEHUQ', 'Climate_Region_Pub',
                                 'AIA_Zone', 'CONDCOOP', 'CONVERSION',
                                 'WALLTYPE', 'ROOFTYPE', 'STOVENFUEL',
                                 'STOVEFUEL', 'OVENFUEL', 'OVENUSE',
                                 'AMTMICRO', 'OUTGRILLFUEL', 'NUMMEAL',
                                 'FUELFOOD', 'TVTYPE1', 'PCTYPE1',
                                 'EQUIPM', 'FUELHEAT', 'NGFPFLUE',
                                 'USENGFP', 'DIFFUEL', 'EQMAMT',
                                 'H2OTYPE1', 'FUELH2O', 'COOLTYPE',
                                 'FUELPOOL', 'FUELTUB', 'TYPEGLASS',
                                 'ADQINSUL', 'DRAFTY'])

    pipe = Pipeline([('one_hot_encoder', OneHotEncoder(
                                         categorical_features=col_index)),
                     ('huber_model', HuberRegressor())])
    pipe.fit(X_train, y=np.sqrt(y_train))

    with open('pipe_model.p', 'wb') as f:
        pickle.dump(pipe, f)

    return pipe


if __name__ == "__main__":
    df = pd.read_csv("data/recs2009_public.csv")
    df = clean_df(df)
    y = create_target(df)
    X = create_feature_dataframe(df)
    X_train, X_test, y_train, y_test = create_split(X, y)
    pipe = create_model(X_train, y_train)
    X_test, y_test = create_split_files(X_test, y_test)
