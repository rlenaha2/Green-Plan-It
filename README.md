# Green Plan-it

## Motivation 
This tool is intended to be used as a way of estimating the energy usage for a structure.  There are a series of questions that need to be answered in a CSV file.  These responses are read in and parsed by the tool and an estimated energy usage is returned.

The model is based on data from the 2009 Residential Energy Consumption Survey (https://www.eia.gov/consumption/residential/data/2009/index.php?view=microdata).  This data contail over 10,000 stuctures ranging from 100 sq ft to over 16,000 sq ft. 

## Model Use
An interactive version of this model can be found at:


## Model Features
The model was trained on a subset of features.  

The model is a linear regression with L2 reguarlization (Ridge).


## Model Performance


![Alt text](relative/path/to/img.jpg?raw=true "Title")

## Set up

## Libraries
* Python 2.7

numpy 1.13.3

pandas 0.20.3

Flask 0.12.2

scikit-learn 0.19.1

Werkzeug 0.12.2

scipy 1.0.0

* To change to Python 3 model.py needs to have "protocol=2" removed from the create_model function
