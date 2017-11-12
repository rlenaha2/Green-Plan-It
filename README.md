# Green Plan-it

## Overview 
Current technologies to determine annual energy usage are time consuming and difficult to use. The purpose of this tool is to make a tool that anyone can use to predict the annual energy usage of thier house.  This could be used for new structures as well as renovations.  The hope is that people will become more aware of thier energy usage, and hopefully reduce thier overall energy usage.


## Data Source
The model is based on data from the 2009 Residential Energy Consumption Survey (https://www.eia.gov/consumption/residential/data/2009/index.php?view=microdata).  This data contail over 10,000 stuctures ranging from 100 sq ft to over 16,000 sq ft. 


## Model Overview
The model that is used is a linear model that minimized Huber loss.  Additional information on the model performance and evaluation are discussed in crispdm.mkd.

## Model Execution
The model.py file in the base directory includes a train/test split to judge model performance.  The model.py file in the website/ directory does not include any split, and when run will create a pipe_model.p file that is trained on all of the data.  When the model.py file is run it will also produce the plots that are shown in crispdm.mkd (univariate plots for number of rooms with A/C, univariate plot of total square footage, and actual versus predicted).


## Repo Structure
<pre>Green-Plan-It/  
 ┬  
 ├ .gitignore (file containing extensions ignored by git)
 ├ README.md (explaination of the repo)
 ├ basis_expansions.py (python file used to support creation of univariate plots) 
 ├ crispdm.mkd (CRISP-DM framework for this project) 
 ├ make_plots.py (python file to create plots shown in CRISP-DM write-up)
 ├ model.py (file to generate the pipe object) 
 ├ pipe_model.p (pipe model used to make predictions)
 ├ preprocessing.py (python file to clean data for use in modeling)
 ├ [DIR] data
     ┬  
     └ recs2009_public.csv (CSV file containing all of the data from the RECS)  
 ├ [DIR] images  
     ┬  
     ├ ACROOMS_univariate.png (univariate plot of number of rooms with A/C)  
     ├ TOTSQFT_univariate.png (univariate plot of total square feet)
     ├ results.png (plot comparing actual vs predicted based on a train/test split)  
     └ crispdm.png (visualization of the CRISP-DM process) 
 └ [DIR] website  
     ┬  
     ├ app.py (flask app to create website)
     ├ final_pipeline.py (python class used to make predictions)
     ├ green_plan_it_input.csv (csv file contianing one structure to be predicted) 
     ├ make_prediction.py (python file to preprocess CSV to be predicted) 
     ├ model.py (model used by the website, uses all data) 
     ├ pipe_model.p (pipe model used to make predictions)    
     ├ preprocessing.py (python file clean data for use in modeling)
     ├ recs2009_public.csv.csv (csv file contianing all of the data)
     ├ [DIR] static  
         ┬  
         ├ [DIR] css
             ┬  
             ├ default.css (css used for the website)
             ├ font.css (css for fonts on website)    
             └ [DIR] fonts (unchanged from template)
         └ [DIR] images
             ┬  
             ├ banner.jpg (banner image on website)
             └ green-planet.jpg (picture of green planet at top of website)   
     └ [DIR] templates  
         ┬  
         └ index.html (html for the website)
 
</pre>

## Set up

### Libraries
Python 2.7

numpy 1.13.3

pandas 0.20.3

Flask 0.12.2

scikit-learn 0.19.1

Werkzeug 0.12.2

scipy 1.0.0
