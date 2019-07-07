# https://stackoverflow.com/questions/45066873/pandas-melt-with-multiple-value-vars

import numpy as numpy
import pandas as pd

df_steel = pd.read_csv('raw\IS_production7th.csv')
df_steel.head()

# using melt
steel_molten = (pd.melt(df_steel, id_vars=['Indicator','Economy'], var_name='Year')
                  .set_index(['Indicator','Economy','Year'])
                  .unstack(level='Indicator')
                  .reset_index())

# another way to do it
molten = (df_steel.set_index(['Economy','Indicator'])
                  .rename_axis(['Year'], axis=1)
                  .stack().unstack('Indicator')
                  .reset_index())

# write to csv
molten.to_csv('modified\molten.csv', index=False)