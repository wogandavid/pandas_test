# maketidy.py
# take population data from 7th edition and reshape in tidy format

import numpy as numpy
import pandas as pd

rawPopulation = pd.read_excel(r'tidy pop\raw\Population_8th_2019_07_02 - raw.xlsx')
rawPopulation.head()

rawPopulation.rename(columns={'Year':'Economy'}, inplace=True)

# define list of years
year_list = list(range(1990,2050,1))

# use melt to collapse the year columns in to a new column
TidyPopulation = pd.melt(rawPopulation, id_vars='Economy', value_vars=year_list)

# rename columns
TidyPopulation.rename(columns={'variable':'Year','value':'Population'}, inplace=True)


# write to csv
TidyPopulation.to_csv(r'tidy pop\modified\TidyPopulation.csv', index=False)