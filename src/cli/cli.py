'''
Module that contains the command line app.

Created: 15 July 2022
Author: Matthew Stachyra
'''
import sys
import argparse

from logo import Logo


l = Logo()
l.__str__()

message = "Help: Pass as argument a note of type string."

def string_checker(arg):
    try:
        print("string checker ran")
        s = str(arg)

    except:
        raise argparse.ArgumentTypeError('Help: Pass as argument a note of type string.')

    return s


parser = argparse.ArgumentParser(description='Take in a note.')
parser.add_argument('-n',
                    '--note',
                    metavar='note',
                    type=string_checker,
                    help='note to be stored in database')


def main(args=None):
    arguments = parser.parse_args(args=args)
    note = arguments.note

    # Main logic to be replace below.
    # Below is currently just for testing purposes.
    print("The note you entered is:")
    print("-"*30)
    print(note)

