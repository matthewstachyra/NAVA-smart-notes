'''
Postgresql database to store corpus.

Steps to set up
- first download postgresql with homebrew 'brew install postgresql'
- run 'psql postgres' in the terminal

created: 20 July 2022
last updated: n/a
author: matthew stachyra


TODO
[ ] create database
[ ] figure out how to pass database or connect to database
[ ] figure out how to link database to cli main
'''

import psycopg2

from ..cli.cli import main

class NotesDB:
    def __init__(self):
        self.conn = psycopg2.connect(host='localhost',
                                     user='matt',
                                     password='password')

        self.cur = self.conn.cursor()

    def update(self, note):
        self.cur.execute("""...""")

    def delete(self, note):
        self.cur.execute("""...""")

