import numpy as np
import pandas as pd

# read in CSV
steel = pd.read_csv('IS_production2.csv')

# remove 'dummy' information
steel = steel.drop(['Label1', 'Number'], axis=1).loc[steel['Label2'] != 'DUM1'].loc[steel['Label2'] != 'DUM2']
steel = steel.rename(columns={'Label2':'Indicator'}).reset_index(drop=True)

# separate historical data from projections
steel_history = steel.loc[:,'Indicator':'2016']
steel_projections = steel.loc[:,'2017':'2050']

# separate GDP, population, and steel production
GDP = steel_history.loc[steel_history['Indicator'] == 'GDP'].drop(['Indicator'], axis=1).set_index('Economy').transpose()
Pop = steel_history.loc[steel_history['Indicator'] == 'POP'].drop(['Indicator'], axis=1).set_index('Economy').transpose()
ITM = steel_history.loc[steel_history['Indicator'] == 'ITM'].drop(['Indicator'], axis=1).set_index('Economy').transpose()

# divide to find per capita
GDP_per_capita = GDP.div(Pop)
Production_per_capita = ITM.div(Pop)

GDP_per_capita_ln = np.log(GDP_per_capita)
Production_per_capita_ln = np.log(Production_per_capita)

# regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = GDP_per_capita_ln['04_CHL'].values.reshape(-1,1)
y = Production_per_capita_ln['04_CHL'].values.reshape(-1,1)

reg = LinearRegression()
reg.fit(X, y)

print(reg.coef_)
print(reg.intercept_)