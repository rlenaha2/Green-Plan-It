# Green Plan-it

## Overview 
Current technologies to determine annual energy usage are time consuming and difficult to use. The purpose of this tool is to make a tool that anyone can use to predict the annual energy usage of thier house.  This could be used for new structures as well as renovations.  The hope is that people will become more aware of thier energy usage, and hopefully reduce thier overall energy usage.


## Data Source
The model is based on data from the 2009 Residential Energy Consumption Survey (https://www.eia.gov/consumption/residential/data/2009/index.php?view=microdata).  This data contail over 10,000 stuctures ranging from 100 sq ft to over 16,000 sq ft. 


## Model Overview
The model that is used is a linear model that minimized Huber loss.  


## Repo Structure
<pre>/Green-Plan-It/  
 ┬  
 ├ crispdm.mkd (CRISP-DM framework for this project) 
 ├ dftransformers.py (file to transform dataframes used for univariate plots)  
 ├ pipe_model.p (pipe model used to make predictions)
 ├ model.py (file to generate the pipe object)
 ├ [DIR] data
     ┬  
     ├ recs2009_public.csv (CSV file containing all of the data from the RECS)  
 ├ [DIR] website  
     ┬  
     ├ model.py (model used by the website, uses all data)  
     ├ app.py (flask app to create website)
     ├ green_plan_it_input.csv (csv file contianing one structure to be predicted)     
     ├ [DIR] static  
         ┬  
         ├ [DIR] css
             ┬  
             ├ default.css (css used for the website)
             └ font.css (css for fonts on website)             
         └ [DIR] images
             ┬  
             ├ banner.jpg (banner image on website)
             └ green-planet.jpg (picture of green planet at top of website) 
         
     ├ [DIR] templates  
         ┬  
         ├ T
         └ TBD 
     ├ model.py (model used by the website, uses all data)  
     └ TBD  
 ├ [DIR] images  
     ┬  
     ├ ACROOMS_univariate.png (univariate plot of number of rooms with A/C)  
     ├ TOTSQFT_univariate.png (univariate plot of total square feet)
     ├ act_vs_pred.png (plot comparing actual vs predicted based on a train/test split)  
     └ crispdm.png (visualization of the CRISP-DM process)  
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
