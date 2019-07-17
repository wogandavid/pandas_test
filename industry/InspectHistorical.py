# InspectHistorical.py
# Inspect data and prepare for regression

# import Pandas so we can manipulate data
# import sklean so we can run the regression
# import matplotlib so we can plot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read in historical data
SteelDataHistorical = pd.read_csv('modified\SteelDataHistorical.csv')

# Calculate GDP per capita and production per capita
SteelDataHistorical['GDPperCapita'] = SteelDataHistorical['GDP'].div(SteelDataHistorical['Population'])
SteelDataHistorical['SteelProductionperCapita'] = SteelDataHistorical['SteelProduction'].div(SteelDataHistorical['Population'])

HistoricalPlot = sns.lmplot(x="GDPperCapita", 
               y="SteelProductionperCapita", 
               col="Economy", 
               data=SteelDataHistorical, 
               col_wrap=3,
               height= 3, 
               aspect=1, 
               sharex= False,
               sharey= False,
               fit_reg = False)

# write prepared data to csv
SteelDataHistorical.to_csv('modified\SteelDataHistoricalNeedsCleaning.csv', index=False)             
