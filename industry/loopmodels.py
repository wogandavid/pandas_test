# LoopModels.py
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
SteelDataProjectionPrepared = pd.read_csv('modified\SteelDataProjectionPrepared.csv')

# get list of economies
economies = SteelDataHistoricalPrepared.Economy.unique()

# create economy-model pairs
models = {economy: LinearRegression() for economy in economies}

# set Economy as index and set target vector by dropping all other columns except lnGDPperCapita and lnSteelProductionperCapita
df = (SteelDataHistoricalPrepared.set_index('Economy')
                                 .drop(['GDP','SteelProduction','Population','GDPperCapita','SteelProductionperCapita'], axis=1))

# loop over economy-model pairs to fit regression
for economy, model in models.items():
        model.fit(df.loc[economy, :].drop('lnSteelProductionperCapita', axis=1),df.loc[economy, 'lnSteelProductionperCapita'])
#        print(model.coef_)

FuturelnGDPperCapita = (SteelDataProjectionPrepared.set_index('Economy')
                                                   .drop(['GDP','Population','GDPperCapita'], axis=1))     


# loop over economy-model pairs to make prediction and write prediction to csv, one for each economy
#index2 = SteelDataHistoricalPrepared[['Economy','Year']]
df2 = SteelDataProjectionPrepared[['Economy','Year']]
filelist = []
#series_list = []
for economy, model in models.items():
#        prediction = model.predict(df.loc[economy, :].drop('lnSteelProductionperCapita', axis=1))
        prediction = model.predict(FuturelnGDPperCapita.loc[economy,:])
#        series_list.append(pd.Series(data=prediction, index = index2))
        results = df2[df2.Economy == economy]
        results['prediction'] = prediction
        results['prediction exp'] = np.exp(prediction)
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
dfResults.to_csv('alleconomies.csv')

# plot using seaborn
import seaborn as sns
g = (sns.lmplot(x="Year", 
               y="prediction exp", 
               col="Economy", 
               data=dfResults, 
               col_wrap=3,
               height= 3, 
               aspect=1, 
               sharex= False,
               sharey= False,
               fit_reg = False)
        .set_axis_labels("Year", "Steel production - million tons"))

# try using matplotlib
fig = plt.figure(figsize=[8,16])

for economy,num in zip(economies, range(1,19)):
    df0=dfResults[dfResults['Economy']==economy]
    ax = fig.add_subplot(7,3,num)
# add historical prediction
    ax.plot(df0['Year'], df0[['prediction exp']],'b')
    ax.set_title(economy)

#plt.tight_layout()
plt.show()