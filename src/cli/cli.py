'''
Module that contains the command line app.

Created: 15 July 2022
Author: Matthew Stachyra
'''
import sys
import argparse

from .logo import Logo


l = Logo()
l.__str__()

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
    arguments = parser.parse_args(args=args)
    note_to_add = arguments.add
    search_terms = arguments.search

    # Below is currently just for testing purposes.
    print("The note you entered is:")
    print("-"*30)
    print(note_to_add[0])

