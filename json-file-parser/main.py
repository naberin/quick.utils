from services.output import Output
from services.filter import Filter
from services.parser import Parser
from services.process import Process
from services.logger import setup as logger

# Parse
options = Parser(description="Parse JSON files with filtering options").parse()

filename = options.filename
filters = options.filter
separator = options.separator
verbose = options.verbose
output = options.output

# Setup Logger
logger(verbose)

# Read, load and get JSON
unfiltered_json = Process()\
    .set_file(with_filename=filename)\
    .read()\
    .build()\
    .get()

# Filter
filtered_json = Filter(separator=separator, filters=filters)\
    .filter(unfiltered_json)

# Output
Output().flatten(filtered_json).display(as_file=output)





