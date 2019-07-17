# CleanData.py
# this script cleans the dataset by removing negative values, replacing them with NaN, then dropping all rows that contain NaN
# Then, plot cleaned data for each economy
# https://seaborn.pydata.org/generated/seaborn.lmplot.html

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read in prepared data from CSV
SteelDataHistorical = pd.read_csv('modified\SteelDataHistoricalNeedsCleaning.csv')

# replace negative values with NaN
SteelDataHistorical[SteelDataHistorical.SteelProductionperCapita < 0] = np.NaN

# Drop NaN 
SteelDataHistorical.dropna(inplace=True)

# ensure that years are stored as integers
SteelDataHistorical = SteelDataHistorical.astype({"Year": int})

# create natural log of GDP per capita and steel production
SteelDataHistorical['lnGDPperCapita'] = np.log(SteelDataHistorical['GDPperCapita'])
SteelDataHistorical['lnSteelProductionperCapita'] = np.log(SteelDataHistorical['SteelProductionperCapita'])

# plot using seaborn
HistoricalPlotCleaned = sns.lmplot(x="lnGDPperCapita", 
                        y="lnSteelProductionperCapita", 
                        col="Economy", 
                        data=SteelDataHistorical, 
                        col_wrap=3,
                        height= 3, 
                        aspect=1, 
                        sharex= False,
                        sharey= False,
                        fit_reg = False)

# write prepared data to csv
SteelDataHistorical.to_csv('modified\SteelDataHistoricalPrepared.csv', index=False)             
