#!/usr/bin/env python3
"""
Entry point for the ebay-lister application.
"""
from src.csv_processor import process_csv

csv_file = 'data/basketball-cards.csv'

def main():
    """Main function to read and process the CSV file."""
    process_csv(csv_file)

if __name__ == "__main__":
    main()
