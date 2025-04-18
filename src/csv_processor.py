import csv
import os


def read_csv_file(file_path):
    """
    Read a CSV file and return its contents.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        list: List of rows from the CSV file
        
    Raises:
        FileNotFoundError: If the file does not exist
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
        
    rows = []
    with open(file_path) as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    return rows


def process_csv(file_path=None):
    """
    Process a CSV file and print its contents.
    
    Args:
        file_path (str, optional): Path to the CSV file. Defaults to the global csv_file.
    """
    rows = read_csv_file(file_path)
    for row in rows:
        print(row)

