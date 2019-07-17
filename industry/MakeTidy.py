# MakeTidy.py
# Take Steel subsector data for GDP, population, and production from 7th Edition
# and reshape in Tidy format
# https://stackoverflow.com/questions/45066873/pandas-melt-with-multiple-value-vars

import numpy as np
import pandas as pd

RawSteelData = pd.read_csv('raw\IS_production7th.csv')
RawSteelData.head()

# using melt to make a tidy set with multiple measured variables - see Table 12 in Tidy Data paper
TidySteel = (pd.melt(RawSteelData, id_vars=['Indicator','Economy'], var_name='Year')
                  .set_index(['Indicator','Economy','Year'])
                  .unstack(level='Indicator')
                  .reset_index())

# another way to do it - see link above
TidySteel = (RawSteelData.set_index(['Economy','Indicator'])
                  .rename_axis(['Year'], axis=1)
                  .stack().unstack('Indicator')
                  .reset_index())

# write to csv
TidySteel.to_csv('modified\TidySteel.csv', index=False)