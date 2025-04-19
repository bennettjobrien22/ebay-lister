import unittest
import os
import csv
import sys
from unittest.mock import patch, mock_open

# Add the parent directory to the path so we can import the module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.csv_processor import read_csv_file, process_csv

class TestCSVProcessor(unittest.TestCase):
    """Test cases for the CSV processor module."""
    
    @patch('os.path.exists', return_value=False)
    def test_read_csv_file_file_not_found(self, mock_exists):
        """Test that read_csv_file handles FileNotFoundError correctly."""
        with self.assertRaises(FileNotFoundError):
            read_csv_file("nonexistent.csv")


    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data="header1,header2\nvalue1,value2\nvalue3,value4")
    def test_read_csv_file(self, mock_file, mock_exists):
        """Test that the read_csv_file function works correctly."""
        # Call the function with a mock file
        result = read_csv_file("dummy.csv")
        
        # Check that the file was opened with the correct path
        mock_file.assert_called_once_with("dummy.csv")
        
        # Check that the result is correct
        expected = [["header1", "header2"], ["value1", "value2"], ["value3", "value4"]]
        self.assertEqual(result, expected)
    

    @patch('src.csv_processor.read_csv_file')
    def test_process_csv_simple(self, mock_read_csv):
        """Test that the process_csv function works correctly."""
        mock_read_csv.return_value = [
            ["Michael Jordan Rookie", "$20,000"],
            ["Michael Jordan Skybox", "$10,000"],
        ]
        
        summary = process_csv("dummy.csv")
        
        mock_read_csv.assert_called_once_with("dummy.csv")
        
        self.assertEqual(summary["total_cards"], 2)
        self.assertEqual(summary["unique_cards"], 2)
        self.assertEqual(summary["total_value"], 30000)


    @patch('src.csv_processor.read_csv_file')
    def test_process_csv_duplicates(self, mock_read_csv):
        """Test that the process_csv function works correctly with duplicates."""
        mock_read_csv.return_value = [
            ["Michael Jordan 97", "$20,000"],
            ["Michael Jordan 98", "$10,000"],
            ["Michael Jordan 96", "$15,000"],
            ["Michael Jordan 96", "$15,000"],
        ]
        
        summary = process_csv("dummy.csv")
        
        mock_read_csv.assert_called_once_with("dummy.csv")

        self.assertEqual(summary["total_cards"], 4)
        self.assertEqual(summary["unique_cards"], 3)
        self.assertEqual(summary["total_value"], 60000)


if __name__ == '__main__':
    unittest.main() 