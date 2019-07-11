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
                                 .drop(['GDP','SteelProduction','Population'], axis=1))

# loop over economy-model pairs to fit regression
for economy, model in models.items():
        model.fit(df.loc[economy, :].drop('SteelProductionperCapita', axis=1),df.loc[economy, 'SteelProductionperCapita'])
#        print(model.coef_)

# loop over economy-model pairs to make prediction and write prediction to csv, one for each economy
#index2 = SteelDataHistoricalPrepared[['Economy','Year']]
df2 = SteelDataHistoricalPrepared[['Economy','Year']]
filelist = []
#series_list = []
for economy, model in models.items():
        prediction = model.predict(df.loc[economy, :].drop('SteelProductionperCapita', axis=1))
#        series_list.append(pd.Series(data=prediction, index = index2))
        results = df2[df2.Economy == economy]
        results['prediction'] = prediction
#        results = pd.Series(data=prediction, index=df.loc[economy,'Year'])
        newfilename = '%sPrediction.csv' %economy
        results.to_csv('results\%s' %newfilename, header=True)
#        results_df.to_csv('results\%s' %newfilename, header=True)
        filelist.append(newfilename)

# read in all csv and combine to one df
df_list =[]
for economy in economies:
        newfilename = '%sPrediction.csv' %economy
        df_list.append(pd.read_csv('results\%s' %newfilename))
dfResults = pd.concat(df_list).drop('Unnamed: 0', axis=1)
dfResults['GDPperCapita'] = SteelDataHistoricalPrepared['GDPperCapita']

# plot using seaborn
import seaborn as sns
g = sns.lmplot(x="GDPperCapita", 
               y="prediction", 
               col="Economy", 
               data=dfResults, 
               col_wrap=3,
               height= 3, 
               aspect=1, 
               sharex= False,
               sharey= False,
               fit_reg = False)

