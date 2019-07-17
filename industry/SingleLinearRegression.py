# SingleLinearRegression.py
# Run a linear regression for one economy using historical steel production, GDP, and population
# Project production using GDP and population projections

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# read in prepared data from CSV
SteelDataHistoricalPrepared = pd.read_csv('modified\SteelDataHistoricalPrepared.csv')

# perform regression over one economy as a test
SteelDataHistoricalPreparedAUS = SteelDataHistoricalPrepared[SteelDataHistoricalPrepared.Economy == '01_AUS']

# select features and reshape 
X = SteelDataHistoricalPreparedAUS['lnGDPperCapita'].values.reshape(-1,1)
Y = SteelDataHistoricalPreparedAUS['lnSteelProductionperCapita'].values.reshape(-1,1)

# define linear regression object to store the model
reg = LinearRegression()
reg.fit(X, Y)

# print results
print(reg.coef_)
print(reg.intercept_)

# make a prediction using the historical data
prediction = reg.predict(X)
prediction_exp = np.exp(prediction)

# make a prediction based on future GDP per capita
SteelDataProjectionPrepared = pd.read_csv('modified\SteelDataProjectionPrepared.csv')
SteelDataProjectionPreparedAUS = SteelDataProjectionPrepared[SteelDataProjectionPrepared.Economy == '01_AUS']
FutureProduction = SteelDataProjectionPreparedAUS['lnGDPperCapita'].values.reshape(-1,1)

# make a prediction using the model
FutureProductionResults = reg.predict(FutureProduction)
FutureProductionResults_exp = np.exp(FutureProductionResults)

# plot model and plot prediction results
fig1 = plt.figure()
plt.scatter(X,Y)
plt.plot(X,prediction)
plt.xlabel('ln(Production)')
plt.ylabel('ln(GDP per capita)')

fig2 = plt.figure()
plt.plot(SteelDataHistoricalPreparedAUS['Year'],prediction_exp, 'r')
plt.plot(SteelDataProjectionPreparedAUS['Year'],FutureProductionResults_exp, 'b')
plt.xlabel('Year')
plt.ylabel('Production per capita - million tons')
plt.show()





