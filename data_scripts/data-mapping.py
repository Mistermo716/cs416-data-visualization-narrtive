import pandas as pd

# Load Zillow data
zillow_df = pd.read_csv('./data/zillowavg-yearlyCounty.csv')

# Load FIPS data
fips_df = pd.read_csv('https://www2.census.gov/geo/docs/reference/codes/files/national_county.txt', header=None, names=['state', 'state_code', 'county_code', 'county_name', 'class_code'], dtype={'state_code': str, 'county_code': str})

# Add leading zeros to the 'county_code' to make it three digits
fips_df['county_code'] = fips_df['county_code'].str.zfill(3)

# Combine 'state_code' and 'county_code' to create a single 'fips' column
fips_df['fips'] = fips_df['state_code'] + fips_df['county_code']

# Clean the county names in both dataframes to ensure they match
zillow_df['CountyName'] = zillow_df['CountyName'].str.lower().str.replace(' county', '')
fips_df['county_name'] = fips_df['county_name'].str.lower().str.replace(' county', '')

# Clean the state names in both dataframes to ensure they match
zillow_df['State'] = zillow_df['State'].str.lower()
fips_df['state'] = fips_df['state'].str.lower()

# Merge the two dataframes based on the county name and state
zillow_df = pd.merge(zillow_df, fips_df, left_on=['CountyName', 'State'], right_on=['county_name', 'state'], how='left')

print(zillow_df)

zillow_df.to_csv('zillowavg-yearlyCounty.csv', index=False)
