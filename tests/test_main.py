import unittest
import os
import csv
import sys
from unittest.mock import patch, mock_open

# Add the parent directory to the path so we can import the main module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main

class TestMain(unittest.TestCase):
    """Test cases for the main module."""
    
    def test_csv_file_exists(self):
        """Test that the CSV file exists."""
        self.assertTrue(os.path.exists(main.csv_file), f"CSV file {main.csv_file} does not exist")
    
    @patch('builtins.open', new_callable=mock_open, read_data="header1,header2\nvalue1,value2\nvalue3,value4")
    def test_read_csv_file(self, mock_file):
        """Test that the read_csv_file function works correctly."""
        # Call the function with a mock file
        result = main.read_csv_file("dummy.csv")
        
        # Check that the file was opened with the correct path
        mock_file.assert_called_once_with("dummy.csv")
        
        # Check that the result is correct
        expected = [["header1", "header2"], ["value1", "value2"], ["value3", "value4"]]
        self.assertEqual(result, expected)
    
    @patch('main.read_csv_file')
    @patch('builtins.print')
    def test_main_function(self, mock_print, mock_read_csv):
        """Test that the main function works correctly."""
        # Set up the mock to return some data
        mock_read_csv.return_value = [["header1", "header2"], ["value1", "value2"]]
        
        # Call the main function
        main.main()
        
        # Check that read_csv_file was called with the correct path
        mock_read_csv.assert_called_once_with(main.csv_file)
        
        # Check that print was called for each row
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call(["header1", "header2"])
        mock_print.assert_any_call(["value1", "value2"])

if __name__ == '__main__':
    unittest.main() 