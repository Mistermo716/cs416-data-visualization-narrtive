import csv

def calculate_yearly_average(row):
    yearly_averages = []
    for year in range(2000, 2024):
        monthly_prices = []
        recorded_months = 0
        for month in range(1, 13):
            day = 31
            if month == 2:  # February
                day = 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
            elif month in {4, 6, 9, 11}:
                day = 30

            key = f"{year}-{month:02d}-{day:02d}"
            if key in row and row[key]:  # Check if the key exists and the value is not empty
                monthly_prices.append(float(row[key]))
                recorded_months += 1

        avg = sum(monthly_prices) / recorded_months if recorded_months else 0
        yearly_averages.append(avg)
    return yearly_averages

def add_yearly_average(input_file, output_file):
    with open(input_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    header = list(data[0].keys())
    for year in range(2000, 2024):
        header.append(f"{year}_Avg_Sale_Price")

    for row in data:
        yearly_averages = calculate_yearly_average(row)
        for i, yearly_avg in enumerate(yearly_averages):
            row[f"{2000 + i}_Avg_Sale_Price"] = yearly_avg

    with open(output_file, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(header)
        for row_data in data:
            writer.writerow(row_data.values())

if __name__ == "__main__":
    input_file = "zillowSalePrice_with_fips.csv"
    output_file = "zillowSalePriceAvg_with_fips.csv"

    add_yearly_average(input_file, output_file)
