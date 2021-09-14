from services.parser import Parser
options = Parser(description="Parse JSON files with filtering options").parse()

filename = options.filename

