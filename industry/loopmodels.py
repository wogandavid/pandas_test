# LoopModels.py
# create linear models for all 21 economies

# step 1: create dictionary of model instances
# step 2: loop over economy, model pairs

# for future:
# https://www.dataquest.io/blog/settingwithcopywarning/

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns

# define functions to perform regressions and predictions

# loop over economy-model pairs to fit regression
def run_regression(models, economies, df):
        for economy, model in models.items():
                (model.fit(df.loc[economy, :]
                      .drop('lnSteelProductionperCapita', axis=1),
                    df.loc[economy, 'lnSteelProductionperCapita']))
        return models            

# create function for performing prediction and writing results
# loop over economy-model pairs to make prediction and write prediction to csv, one for each economy
def run_prediction(models, economies, years, df):
        filelist = []
        for economy, model in models.items():
                prediction = model.predict(df.loc[economy,:])
                results = years[years.Economy == economy]
                results['prediction'] = prediction
                results['prediction exp'] = np.exp(prediction)
                newfilename = '%sPrediction.csv' %economy
                results.to_csv('results\%s' %newfilename, header=True)
                filelist.append(newfilename)

        # read in all csv and combine to one df
        df_list =[]
        for economy in economies:
                newfilename = '%sPrediction.csv' %economy
                df_list.append(pd.read_csv('results\%s' %newfilename))
        dfResults = pd.concat(df_list).drop('Unnamed: 0', axis=1)
        dfResults['GDPperCapita'] = SteelDataHistoricalPrepared['GDPperCapita']
        dfResults.to_csv('results\SteelPredictionsAll.csv')
        
        return dfResults

# Now use the above functions for running regression and making predictions
#read csv
SteelDataHistoricalPrepared = pd.read_csv('modified\SteelDataHistoricalPrepared.csv')
SteelDataProjectionPrepared = pd.read_csv('modified\SteelDataProjectionPrepared.csv')

# get list of economies and create economy-model pairs
economies = SteelDataHistoricalPrepared.Economy.unique()
models = {economy: LinearRegression() for economy in economies}

# set Economy as index and set target vector by dropping all other columns except lnGDPperCapita and lnSteelProductionperCapita
df1 = (SteelDataHistoricalPrepared.set_index('Economy')
                                 .drop(['GDP','SteelProduction','Population','GDPperCapita','SteelProductionperCapita'], axis=1))

# run regression
SteelRegressionModel = run_regression(models, economies, df1)

# make predictions using future values of GDP per capita
HistoricalYears = SteelDataHistoricalPrepared[['Economy','Year']]
HistoricallnGDPperCapita = (SteelDataHistoricalPrepared.set_index('Economy')
                                 .drop(['GDP','SteelProduction','Population','GDPperCapita','SteelProductionperCapita','lnSteelProductionperCapita'], axis=1))
HistoricalPredictionResults = run_prediction(SteelRegressionModel, economies, HistoricalYears, HistoricallnGDPperCapita)

# make predictions using future values of GDP per capita
FutureYears = SteelDataProjectionPrepared[['Economy','Year']]
FuturelnGDPperCapita = (SteelDataProjectionPrepared.set_index('Economy')
                                                   .drop(['GDP','Population','GDPperCapita'], axis=1))     
ProjectionResults = run_prediction(SteelRegressionModel, economies, FutureYears, FuturelnGDPperCapita)

# define function to plot using matplotlib
def plot_results(economies, df1, df2):
        fig = plt.figure(figsize=[8,16])

        for economy,num in zip(economies, range(1,20)):
                df11=df1[df1['Economy']==economy]
                df21=df2[df2['Economy']==economy]
                ax = fig.add_subplot(7,3,num)
                ax.plot(df11['Year'], df11[['prediction exp']],'r')
                ax.plot(df21['Year'], df21[['prediction exp']],'b')
                ax.set_title(economy)

                #plt.tight_layout()
        plt.show()

# plot historical and future predictions
plot_results(economies, HistoricalPredictionResults, ProjectionResults)


