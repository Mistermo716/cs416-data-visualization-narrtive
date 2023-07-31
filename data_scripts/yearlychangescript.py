import pandas as pd
import numpy as np

# Load the data from the CSV file
data = pd.read_csv('zillowSalePriceAvg_with_fips.csv') 

# List of columns to calculate average yearly rate of change
columns = [
    "2000_Avg_Sale_Price", "2001_Avg_Sale_Price", "2002_Avg_Sale_Price",
    "2003_Avg_Sale_Price", "2004_Avg_Sale_Price", "2005_Avg_Sale_Price",
    "2006_Avg_Sale_Price", "2007_Avg_Sale_Price", "2008_Avg_Sale_Price",
    "2009_Avg_Sale_Price", "2010_Avg_Sale_Price", "2011_Avg_Sale_Price",
    "2012_Avg_Sale_Price", "2013_Avg_Sale_Price", "2014_Avg_Sale_Price",
    "2015_Avg_Sale_Price", "2016_Avg_Sale_Price", "2017_Avg_Sale_Price",
    "2018_Avg_Sale_Price", "2019_Avg_Sale_Price", "2020_Avg_Sale_Price",
    "2021_Avg_Sale_Price", "2022_Avg_Sale_Price", "2023_Avg_Sale_Price"
]


# Replace 0s with NaN to avoid dividing by zero when calculating percentage change
data[columns] = data[columns].replace({0:np.nan})

# Calculate average yearly rate of change and store in new column
# The function apply() is used to apply the function pct_change() to each row of the selected columns
# The function dropna() is used to remove NaN values before calculating the mean
data['Avg_Yearly_Rate_of_Change'] = data[columns].apply(lambda row: row.pct_change().dropna().mean(), axis=1)


# Write the updated DataFrame back to CSV
data.to_csv('saleYearlyRateOfChangeSale.csv', index=False) 
