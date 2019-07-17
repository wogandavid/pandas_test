# LinearRegression.py
# Run a linear regression using historical steel production, GDP, and population
# Project production using GDP and population projections

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# read in prepared data from CSV
SteelDataProjectionPrepared = pd.read_csv('modified\SteelDataProjectionPrepared.csv')

# perform regression over one economy as a test
SteelDataProjectionPreparedAUS = SteelDataProjectionPrepared[SteelDataProjectionPrepared.Economy == '01_AUS']

# select features and reshape 
X = SteelDataProjectionPreparedAUS['lnGDPperCapita'].values.reshape(-1,1)

# make a prediction using the model
prediction = reg.predict(X)
prediction_exp = np.exp(prediction)

plt.plot(SteelDataProjectionPreparedAUS['Year'],prediction_exp)

plt.show()