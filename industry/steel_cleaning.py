import numpy as np
import pandas as pd

# read in CSV
steel = pd.read_csv('IS_production.csv', delimiter=',')

# remove 'dummy' information
steel = steel.drop(['Label1', 'Number'], axis=1).loc[steel['Label2'] != 'DUM1'].loc[steel['Label2'] != 'DUM2']
steel = steel.rename(columns={'Label2':'Indicator'}).reset_index(drop=True)

# separate historical data from projections
steel_history = steel.loc[:,'Indicator':'2016']
steel_projections = steel.loc[:,'2017':'2050']

# separate GDP, population, and steel production
GDP = steel_history.loc[steel_history['Indicator'] == 'GDP'].drop(['Indicator'], axis=1).set_index('Economy')
Pop = steel_history.loc[steel_history['Indicator'] == 'POP'].drop(['Indicator'], axis=1).set_index('Economy')
ITM = steel_history.loc[steel_history['Indicator'] == 'ITM'].drop(['Indicator'], axis=1).set_index('Economy').replace({'-1':'0'})

# divide to find per capita - doesn't work
GDP.div(Pop)