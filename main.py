#!/usr/bin/env python3
"""
Entry point for the ebay-lister application.
"""
from src.csv_processor import process_csv

csv_file = 'data/basketball-cards.csv'

def main():
    """Main function to read and process the CSV file."""
    summary = process_csv(csv_file)

    print(f"Total cards: {summary['total_cards']}")
    print(f"Unique cards: {summary['unique_cards']}")
    print(f"Total value: {summary['total_value']}")
    print(f"Average value: {summary['total_value'] / summary['total_cards']}")


if __name__ == "__main__":
    main()
