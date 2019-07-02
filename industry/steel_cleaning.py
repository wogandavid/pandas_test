import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

year = list(range(1980,2016))

# read in CSV
steel = pd.read_csv('IS_production2.csv', index_col=['Indicator','Economy'])
steel_history = steel.loc[:, '1980':'2016']
steel_history = steel_history.stack().unstack(0)

steel_history['GDP_per_capita_ln'] = np.log(steel_history['GDP'].div(steel_history['POP']))
steel_history['Production_per_capita_ln'] = np.log(steel_history['ITM'].div(steel_history['POP']))

steel_history = steel_history.dropna()

X = steel_history['GDP_per_capita_ln'].dropna().values.reshape(-1,1)
y = steel_history['Production_per_capita_ln'].dropna().values.reshape(-1,1)

reg = LinearRegression()
reg.fit(X, y)

print(reg.coef_)
print(reg.intercept_)



# separate historical data from projections
#steel_history = steel.loc[:,'Indicator':'2016']
#steel_projections = steel.loc[:,'2017':'2050']

# separate GDP, population, and steel production
#GDP = steel_history.loc[steel_history['Indicator'] == 'GDP'].drop(['Indicator'], axis=1).set_index('Economy').transpose()
#Pop = steel_history.loc[steel_history['Indicator'] == 'POP'].drop(['Indicator'], axis=1).set_index('Economy').transpose()
#ITM = steel_history.loc[steel_history['Indicator'] == 'ITM'].drop(['Indicator'], axis=1).set_index('Economy').transpose()

#GDP = steel_history.loc[steel_history['Indicator'] == 'GDP'].drop(['Indicator'], axis=1).set_index('Economy').stack()
#Pop = steel_history.loc[steel_history['Indicator'] == 'POP'].drop(['Indicator'], axis=1).set_index('Economy').stack()
#ITM = steel_history.loc[steel_history['Indicator'] == 'ITM'].drop(['Indicator'], axis=1).set_index('Economy').stack()

# divide to find per capita
#GDP_per_capita = GDP.div(Pop)
#Production_per_capita = ITM.div(Pop)

#data = pd.merge(GDP_per_capita, Production_per_capita, how='left')

#GDP_per_capita_ln = np.log(GDP_per_capita).dropna()
#Production_per_capita_ln = np.log(Production_per_capita).dropna()

#data 

# regression
#from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error, r2_score

#X = GDP_per_capita_ln.values.reshape(-1,1)
#y = Production_per_capita_ln.values.reshape(-1,1)

#reg = LinearRegression()
#reg.fit(X, y)

#print(reg.coef_)
#print(reg.intercept_)