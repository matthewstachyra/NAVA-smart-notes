import os
from configparser import ConfigParser

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.ini')

def config(filename=file, section='postgresql'):
    parser = ConfigParser()
    parser.read(file)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for params in params:
            db[params[0]] = params[1]
    else:
        raise Exception(f'Section {section} not found in the {file} file')

    return db
