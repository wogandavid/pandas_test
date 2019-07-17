# InspectProjection.py
# inspect projection data
# prepare for using in prediction

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read in historical data  and drop empty column
SteelDataProjection = pd.read_csv('modified\SteelDataProjection.csv').drop(['SteelProduction'], axis=1)

# create GDP per capita
SteelDataProjection['GDPperCapita'] = SteelDataProjection['GDP'].div(SteelDataProjection['Population'])

# plot GDP per capita projection using seaborne
h = sns.lmplot(x="Year", 
               y="GDPperCapita", 
               col="Economy", 
               data=SteelDataProjection, 
               col_wrap=3,
               height= 3, 
               aspect=1, 
               sharex= False,
               sharey= False,
               fit_reg = False)

# create natural log of GDP per capita and steel production
SteelDataProjection['lnGDPperCapita'] = np.log(SteelDataProjection['GDPperCapita'])

# write prepared data to csv
SteelDataProjection.to_csv('modified\SteelDataProjectionPrepared.csv', index=False)


                                                                 
