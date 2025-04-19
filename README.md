# ebay-lister

Python program to list items to ebay

Meant to take csv files as input

## Project Structure

```
ebay-lister/
├── data/
│   └── basketball-cards.csv
├── src/                  # Source code
│   ├── __init__.py       # Package initialization
│   └── csv_processor.py  # CSV processing functionality
├── tests/                # Test suite
│   └── test_csv_processor.py
├── main.py               # Entry point
├── pytest.ini            # Pytest configuration
└── requirements.txt      # Dependencies
├── run_mutation_tests.py # Mutation testing runner
├── setup.cfg             # Mutmut configuration
```

## Usage

To run the application:

```bash
./main.py
```

## Testing

This project includes a test suite to ensure the functionality works as expected.

### Running Tests

To run the tests, you can use the provided test runner:

```bash
./run_tests.py
```

Or use pytest directly:

```bash
pytest
```

For test coverage:

```bash
pytest --cov=src
```

### Coverage Requirements

The project has a minimum coverage requirement of 80%. Tests will fail if coverage falls below this threshold.

### Mutation Testing

This project uses mutation testing to ensure test quality. Mutation testing introduces small changes to your code and checks if your tests can detect these changes.

To run mutation tests:

```bash
./run_mutation_tests.py
```

This will:
1. Generate mutations of your code
2. Run your tests against each mutation
3. Report which mutations survived (indicating gaps in your test suite)

### Test Structure

The tests are located in the `tests` directory and follow the standard Python unittest pattern.