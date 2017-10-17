import numpy as np
from model.py import ridge_model




def make_predition(VARS TO BE DETERMINED):
'''
Function to create predicitons based on user input for a new house.
Inputs
--------
TOTSQFT
HOUSEAGE
WALLTPYE
TYPEGLASS
TEMPHOME
TEMPGONE
DIVISION

NUMROOMS
CELLAR => Do you have a basement
GARGHEAT => Do you have heat in your garage
ROOFTYPE
NUMFLOORS
WARMAIR
ACROOMS
HIGHCEIL
POOL
USECENAC


Outputs
--------
Yearly energy usage in BTU
'''

    energy_prediction = ridge_model.predict(VARS)
    energy_prediction = np.exp(energy_prediction)
    return energy_prediction









