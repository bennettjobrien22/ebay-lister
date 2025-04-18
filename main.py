import csv

# Path to your CSV file
csv_file = 'data.csv'

# Open and read the CSV file
with open(csv_file) as file:
    reader = csv.reader(file)
    
    # Loop through each row in the CSV
    for row in reader:
        print(row)
