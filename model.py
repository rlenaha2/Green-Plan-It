import pandas as pd
from sklean.model_selection import train_test_split
from sklean.linear_model import Ridge
import numpy as np



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

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state = 52)

    ridge_model = Ridge(alpha = 3)
    ridge_model.fit(X_train, np.log(y_train))
    energy_predictions = ridge_model.predict(X_test)

    return ridge_model


