'''
Module that contains the command line app.

created: 15 July 2022
last updated: 10 August 2022
author: matthew stachyra

TODO
[x] debug creating tables
[x] make params mutually exclusive
[ ] add param to add a unique (to defaults) path to search for notes
[ ] test creating corpus
[ ] enable automatic detection of semver / tags
'''
import argparse
from pyfiglet import Figlet

from .database.db import NAVAdb
from .utils.corpus import Corpus
from .utils.embedding import Embed
from .utils.search import Search

message = "Help: Pass as argument a note as a string."


parser = argparse.ArgumentParser(description='Take in a note.')
group = parser.add_mutually_exclusive_group(required=True)

# ---------------mutually exclusive params---------------

# -a to add a note to the databse
group.add_argument('-a',
                    '--add',
                    metavar='add',
                    type=str,
                    nargs=1,
                    help='note to be stored in database')

# -s to search notes in the database
group.add_argument('-s',
                    '--search',
                    metavar='search',
                    type=str,
                    nargs=1,
                    help='keywords to search the database for related notes')


def main(args=None):
    f = Figlet(font='rev')
    print(f.renderText('NAVA') + '\n' +  'smart notes, searched for you by NAVA' + '\n' + 'v0.2.0' +'\n')

    arguments = parser.parse_args(args=args)
    note = arguments.add
    search = arguments.search

    if arguments.add:
        print(f"Adding... '{note[0]}'")

    if arguments.search:
        c = Corpus()
        c.readin()
        print(f"Searching... {search[0]}")


