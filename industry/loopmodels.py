# create linear models for all 21 economies

# step 1: create dictionary of model instances
# step 2: loop over economy, model pairs

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#read csv
SteelDataHistoricalPrepared = pd.read_csv('modified\SteelDataHistoricalPrepared.csv')

# get list of economies
economies = SteelDataHistoricalPrepared.Economy.unique()

# create economy-model pairs
models = {economy: LinearRegression() for economy in economies}

# set Economy as index and set target vector
df = (SteelDataHistoricalPrepared.set_index('Economy')
                                 .drop(['Year','GDP','SteelProduction','Population'], axis=1))

# loop over economy-model pairs
for economy, model in models.items():
        model.fit(df.loc[economy, :].drop('SteelProductionperCapita', axis=1),df.loc[economy, 'SteelProductionperCapita'])
        print(model.coef_)

# loop over economy-model pairs
for economy, model in models.items():
        model.predict(df.loc[economy, :].drop('SteelProductionperCapita', axis=1))