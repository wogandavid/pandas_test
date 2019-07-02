import numpy as numpy
import pandas as pd

dfreligion = pd.read_csv('religion.csv')

religion = pd.melt(dfreligion, id_vars='Religion', value_vars=['<$10k','$10{20k','$20{30k','$30{40k','$40{50k','$50{75k'])
religion.head()