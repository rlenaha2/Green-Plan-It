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
from make_prediction import make_prediction
import matplotlib.pyplot as plt
from regression_helpers import plot_univariate_smooth


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


def create_results_plot(pipe, X_test, y_test):
    '''
    Creates a plot of predicted vs actual results

    Inputs
    --------
    pipe: pipe model from create_model
    X_test: feature dataframe of the hold out data
    y_test: target dataframe of the hold out data

    Outputs
    --------
    Creates a plot of predicted vs actual of the test data
    and stores it in the current working directort
    '''

    energy_prediction = make_prediction(pipe, X_test)
    plt.xlim(0, 400000)
    plt.ylim(0, 400000)
    plt.gca().set_aspect('equal', adjustable='box')
    x = np.linspace(0, 400000)
    plt.plot(x, x, color='black')
    plt.scatter(y_test, energy_prediction**2, alpha=.5)
    plt.ylabel('Predicted Energy Useage')
    plt.xlabel('Reported Energy Usage')
    plt.rcParams["figure.figsize"] = [8, 8]
    plt.savefig('results.png')


def plot_one_univariate(ax, var_name, mask=None):
    '''
    Create a univariate plot including boostrap samples
    and stores it in the current working directory

    Inputs
    -------
    ax: figure to plot on
    var_name: variable to be plotted

    Outputs
    -------
    Univariate plot for selected variable
    '''

    fig, ax = plt.subplots(figsize=(12, 3))

    if mask is None:
        plot_univariate_smooth(ax,
                               X_test[var_name].values.reshape(-1, 1),
                               y_test, bootstrap=200)
    else:
        plot_univariate_smooth(ax,
                               X_test[var_name].values.reshape(-1, 1),
                               y_test, mask=mask, bootstrap=200)

    ax.set_title(var_name)
    plt.ylabel('Reported Energy Use')
    plt.xlabel(var_name)
    plt.savefig(str(var_name) + "_univariate.png")

if __name__ == "__main__":
    df = pd.read_csv("data/recs2009_public.csv")
    df = clean_df(df)
    y = create_target(df)
    X = create_feature_dataframe(df)
    X_train, X_test, y_train, y_test = create_split(X, y)
    pipe = create_model(X_train, y_train)
    create_results_plot(pipe, X_test, y_test)
    fig, ax = plt.subplots(figsize=(12, 3))
    plot_one_univariate(ax, "TOTSQFT")
    fig, ax = plt.subplots(figsize=(12, 3))
    plot_one_univariate(ax, "ACROOMS")
