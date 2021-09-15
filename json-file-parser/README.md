# JSON File Parser
Parses JSON and outputs as CSV

## Requires
1. Python 3x (f-strings)
2. Pandas (DataFrame and to_csv)

## Getting Started
Files used for the script:

1. [__main.py__](main.py) - holds calls to every service under services
2. [__constants.py__](constants.py) - holds Constants used throughout the script
3. [__services/parser__](services/parser.py) - manages ArgParse CLI design
4. [__services/process__](services/process.py) - reads, loads and shares JSON
5. [__services/filter__](services/filter.py) - traverses JSON to recursively filter-in desired keys
6. [__services/logger__](services/logger.py) - manages logging setup and disables log output if verbose
7. [__services/output__](services/output.py) - manages how JSON is presented (currently as a CSV

## Commands
```bash
# help
python main.py -h

# parse a JSON file
python main.py <json-file>

# parse with logging
python main.py <json-file> -v

# parse with filters
python main.py <json-file> -f key1:key2:key3

# parse with filters and a custom separator
python main.py <json-file> -f key1;key2 --separator ;

# parse and output as a file
python main.py <json-file> -o <csv-filename>
```

