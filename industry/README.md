# Steel Industry Regression example
This is an example of taking a raw dataset of GDP, population, and steel production and estimating a model using linear regression. Each step in the process is repeatable. The steps in each script are documented using comments.

The steps are:

1. MakeTidy - imports the raw data and reshapes it as "Tidy Data". Saves the new "Tidy Data" separately from the raw data.
2. SeparateHistorical - separates historical data and projections. Saves these as two separate dataframes.
3. InspectData - plots the data to check for outliers (zeros, NaNs, negative numbers, etc). Plot function is used. Zeros and NaNs are removed. Saves the cleaned data as a new file.
4. PlotData - Plots the cleaned data.
5. LinearRegression - runs a linear regression. Plot the results.

**Note**: the raw data is stored in its own folder called "raw". This file should not be modified. All modifications to the data (cleaning, reshaping, adding columns, creating new datasets) should be saved in "modified".

To run these files, you will need:
- [Anaconda](https://www.anaconda.com/)
- [Visual Studio Code](https://code.visualstudio.com/)

I used the following links to help build this example:

<https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/>

<https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/>

<https://stackoverflow.com/questions/45066873/pandas-melt-with-multiple-value-vars>

<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html>

<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isnull.html>

<https://chrisalbon.com/python/data_wrangling/pandas_replace_values/>