# JSON File Parser
Parses JSON and outputs as CSV

## Requires
1. Python 3x (f-strings)
2. Pandas (DataFrame and to_csv)

## Getting Started


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

