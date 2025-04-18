import csv

# Path to your CSV file
csv_file = 'data.csv'

def read_csv_file(file_path):
    """
    Read a CSV file and return its contents.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        list: List of rows from the CSV file
    """
    rows = []
    with open(file_path) as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    return rows

def main():
    """Main function to read and process the CSV file."""
    rows = read_csv_file(csv_file)
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
