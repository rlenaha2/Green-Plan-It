
from preprocessing import clean_df
from preprocessing import create_target
from preprocessing import create_feature_dataframe

from model import column_index
from model import create_model

from make_prediction import clean_df_pred
from make_prediction import make_prediction

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  
import pickle
   
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


class Process_Result(object):
    """
    Class that will take a input csv and return a predicted 
    energy usage
    """


    def __init__(self,path_to_pickled_model):
        with open(path_to_pickled_model, 'rb') as f:
            self.model = pickle.load(f)

    def create_pred_df(self, filepath):
        self.df = pd.read_csv(filepath)

    def make_new_prediction(self): 
        self.df = clean_df_pred(self.df)
        self.df = clean_df(self.df)
        self.df = create_feature_dataframe(self.df)
        prediction = make_prediction(self.model, self.df)
   
        return prediction

if __name__ == '__main__': 
    pass    
