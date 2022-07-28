'''
Module that contains the command line app.

created: 15 July 2022
last updated: 28 July 2022
author: Matthew Stachyra

TODO
[x] debug creating tables
[ ] enable automatic detection of tags
[ ] add -it or --interactive flag to enable command loop
'''
import argparse
from pyfiglet import Figlet

from .database.db import NAVAdb
from .utils import Embedding, Search

message = "Help: Pass as argument a note of type string."


parser = argparse.ArgumentParser(description='Take in a note.')

# -a to add a note to the databse
parser.add_argument('-a',
                    '--add',
                    metavar='add',
                    type=str,
                    nargs=1,
                    required=True,
                    help='note to be stored in database')

# -s to search notes in the database
parser.add_argument('-s',
                    '--search',
                    metavar='search',
                    type=str,
                    nargs=1,
                    help='keywords to search the database for related notes')

# -it to enter interactive mode and be able to cycle as required
#TODO


def main(args=None):
    f = Figlet(font='rev')
    print(f.renderText('NAVA') + '\n' +  'smart notes, searched for you by NAVA' + '\n' + 'v0.2.0' +'\n')

    arguments = parser.parse_args(args=args)
    note = arguments.add
    search = arguments.search

    db = NAVAdb()
    db.create_tables()
    db.update_with_note(note)

    if arguments.add:
        print(f"Adding... '{note[0]}'")

    if arguments.search:
        print(f"Searching {search[0]}")


