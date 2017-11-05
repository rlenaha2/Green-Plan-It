import numpy as np
import pandas as pd


def read_df_pred(filepath):
    """
    Creates a pandas dataframe from the input csv
    Input
    -------
    Path to the csv

    Output
    -------
    Pandas dataframe
    """

    df_pred = pd.read_csv(filepath)

    return df_pred


def clean_df_pred(df_pred):
    """
    Cleans the input.csv and returns a df to be used to make predictions
    Input
    -------
    df from input csv

    Output
    -------
    Cleaned Dataframe
    """

    df_pred = df_pred.T
    new_header = df_pred.iloc[0]
    df_pred = df_pred[1:]
    df_pred.columns = new_header
    df_pred = df_pred.iloc[[3]]

    return df_pred


def make_prediction(pipe, df_pred):
    """
    Function to create predicitons based on user input for a new house.
    Inputs
    --------
    Pipe object which contains predicitive model
    Cleaned dataframe which contains instance to be predicted

    Outputs
    --------
    Yearly energy usage in BTU
    """

    energy_prediction = pipe.predict(df_pred)

    return energy_prediction
