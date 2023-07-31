import pandas as pd

def calc_rate_of_change(df, year):
    # Extract columns for specific year
    cols_for_year = [col for col in df.columns if isinstance(col, pd.Timestamp) and col.year == year]
    
    # Check if there are enough columns for the given year
    if len(cols_for_year) < 2:
        raise ValueError(f"Not enough data for the given year: {year}")
    
    # Calculate rate of change
    first_col = df[cols_for_year[0]]
    last_col = df[cols_for_year[-1]]
    
    rate_of_change = ((last_col - first_col) / first_col) * 100
    return rate_of_change

file_path = 'zillowRentPrice.csv'
df = pd.read_csv(file_path)

# Set the first row as the column names
df.columns = df.iloc[0]

# Drop the first row
df = df.drop(df.index[0])

# Convert string dates in column names to datetime, errors='ignore' leaves non-dates unchanged
df.columns = pd.to_datetime(df.columns, errors='ignore', format='%m/%d/%Y')

# Convert data to float
for column in df.columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# Calculate rate of change for each year
for year in range(2015, 2024):
    try:
        print(f"Rate of change for year {year}: {calc_rate_of_change(df, year)}")
    except ValueError as ve:
        print(ve)
