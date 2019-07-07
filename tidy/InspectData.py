# Inspect data and prepare for regression

# import Pandas so we can manipulate data
# import sklean so we can run the regression
# import matplotlib so we can plot

import pandas as pd
import matplotlib.pyplot as plt

# read in historical data
SteelDataHistorical = pd.read_csv('SteelDataHistorical.csv')

# Calculate GDP per capita and production per capita
SteelDataHistorical['GDPperCapita'] = SteelDataHistorical['GDP'].div(SteelDataHistorical['Population'])
SteelDataHistorical['SteelProductionperCapita'] = SteelDataHistorical['SteelProduction'].div(SteelDataHistorical['Population'])

# visual inspection of data
plt.scatter(SteelDataHistorical['GDPperCapita'],SteelDataHistorical['SteelProductionperCapita'])

# Drop NaN 
SteelDataHistorical.dropna(inplace=True)

# replace negative values with NaN
SteelDataHistorical[SteelDataHistorical.SteelProductionperCapita < 0] = np.NaN

# write prepared data to csv
SteelDataHistorical.to_csv(r'C:\GitHub\pandas_test\tidy\SteelDataHistoricalPrepared.csv', index=False)
