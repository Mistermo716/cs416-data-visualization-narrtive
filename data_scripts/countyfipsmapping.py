import pandas as pd

# Load the data
data = pd.read_csv('zillowSalePrice.csv')

# Combine the 'StateCodeFIPS' and 'MunicipalCodeFIPS' columns into a new 'FIPS' column
# We convert the 'StateCodeFIPS' and 'MunicipalCodeFIPS' to string, then fill in leading zeros to ensure they're 2 and 3 digits respectively
data['FIPS'] = data['StateCodeFIPS'].astype(str).str.zfill(2) + data['MunicipalCodeFIPS'].astype(str).str.zfill(3)

# Export the data to a new csv file
data.to_csv('zillowSalePrice_with_fips.csv', index=False)
