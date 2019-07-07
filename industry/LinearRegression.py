# Run a linear regression using historical steel production, GDP, and population
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
X = SteelDataHistoricalPreparedAUS['GDPperCapita'].values.reshape(-1,1)
Y = SteelDataHistoricalPreparedAUS['SteelProductionperCapita'].values.reshape(-1,1)

# define linear regression object to store the model
reg = LinearRegression()
reg.fit(X, Y)

# print results
print(reg.coef_)
print(reg.intercept_)

# make a prediction using the model
prediction = reg.predict(X)

# plot regression
plt.scatter(X,Y)
plt.plot(X,prediction)