# this script separates historical data from future projections
# historical = before 2016
# projection = 2016-2050

# import libraries
import numpy as np
import pandas as pd

# read in tidy steel data
SteelData = pd.read_csv('modified\molten.csv')

# rename the columns
NewNames = {'ITM':'SteelProduction','POP':'Population'}
SteelData.rename(columns=NewNames, inplace=True)

# store all values up up to, and including, 2016 in one dataframe
SteelDataHistorical = SteelData[SteelData.Year <= 2016]

# store all values after 2016 as projections
SteelDataProjection = SteelData[SteelData.Year > 2016]

# write separated dataframes to csv
SteelDataHistorical.to_csv('modified\SteelDataHistorical.csv', index=False)
SteelDataProjection.to_csv('modified\SteelDataprojection.csv', index=False)