# this script separates historical data from future projections
# historical = before 2016
# projection = 2016-2050

# read in tidy steel data
SteelData = pd.read_csv('molten.csv')

# store all values up up to, and including, 2016 in one dataframe
SteelDataHistorical = SteelData[SteelData.Year <= 2016]

# store all values after 2016 as projections
SteelDataProjection = SteelData[SteelData.Year > 2016]

# write separated dataframes to csv
SteelDataHistorical.to_csv(r'C:\GitHub\pandas_test\tidy\SteelDataHistorical.csv', index=False)
SteelDataProjection.to_csv(r'C:\GitHub\pandas_test\tidy\SteelDataprojection.csv', index=False)