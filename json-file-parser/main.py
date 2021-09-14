from services.parser import Parser
from services.process import Process
options = Parser(description="Parse JSON files with filtering options").parse()

filename = options.filename

json = Process()\
    .set_file(with_filename=filename)\
    .read()\
    .build()

