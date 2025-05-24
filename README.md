# API Performance Monitor

A tool for monitoring and benchmarking REST and GraphQL API endpoints. This tool allows you to configure and run periodic performance tests against your APIs and collect metrics about their response times and reliability.

## Features

- Support for both REST and GraphQL APIs
- Configurable test frequencies
- Detailed performance metrics
- JSON-based test configurations
- Automatic results storage
- Customizable timeout settings

## Project Structure

```
api-performance-monitor/
├── benchmarks/
│   ├── rest_tests.json      # REST API test configurations
│   └── graphql_tests.json   # GraphQL test configurations
├── results/                 # Test results are saved here
├── src/
│   └── monitor.py          # Core monitoring logic
├── run.py                  # Main script to run tests
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Installation

1. Clone the repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### REST API Tests

Edit `benchmarks/rest_tests.json` to configure REST API endpoints. Example configuration:

```json
{
    "tests": [
        {
            "name": "Get Users List",
            "url": "https://api.example.com/users",
            "method": "GET",
            "headers": {
                "Content-Type": "application/json"
            },
            "expected_status": 200,
            "frequency": 60,
            "timeout": 5000
        }
    ]
}
```

### GraphQL API Tests

Edit `benchmarks/graphql_tests.json` to configure GraphQL endpoints. Example configuration:

```json
{
    "tests": [
        {
            "name": "Get User Profile",
            "endpoint": "https://api.example.com/graphql",
            "query": "query GetUser($id: ID!) { user(id: $id) { id name email } }",
            "variables": {
                "id": "123"
            },
            "frequency": 60,
            "timeout": 5000
        }
    ]
}
```

## Usage

Run the monitor with default configurations:
```bash
python run.py
```

Specify custom configuration files:
```bash
python run.py --rest-config path/to/rest_config.json --graphql-config path/to/graphql_config.json
```

Specify custom results directory:
```bash
python run.py --results-dir path/to/results
```

## Results

Test results are saved in the `results/` directory with timestamps and test names. Each result file contains:
- Test name
- Timestamp
- Success status
- Response time (ms)
- Status code (REST) or error presence (GraphQL)
- Any error messages if the test failed

## License

MIT License 