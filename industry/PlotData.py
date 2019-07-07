# this script creates plots of GDP per capita vs steel production for each economy
# https://seaborn.pydata.org/generated/seaborn.lmplot.html

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read in prepared data from CSV
SteelDataHistoricalPrepared = pd.read_csv('modified\SteelDataHistoricalPrepared.csv')

# plot using seaborn
g = sns.lmplot(x="GDPperCapita", 
               y="SteelProductionperCapita", 
               col="Economy", 
               data=SteelDataHistoricalPrepared, 
               col_wrap=3,
               height= 3, 
               aspect=1, 
               sharex= False,
               sharey= False,
               fit_reg = False)