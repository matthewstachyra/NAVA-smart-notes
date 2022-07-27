'''
Postgresql database to store notes corpus.

set up
- first download postgresql with homebrew 'brew install postgresql'
- run 'psql postgres' in the terminal

postgres commands
- '\l' shows all databases
- 'CREATE DATABASE name' creates a database
- 'DROP DATABASE name' deletes database

created: 20 July 202q
last updated: 26 July 2022
author: matthew stachyra
more: https://www.postgresqltutorial.com/postgresql-python/

TODO
[x] write skeleton db class
[x] update db class to delete database
[x] update db class to update database with note
[ ] debug db
[ ] update db class to delete a note
[ ] figure out how get python code to create database if it doesn't exist
'''


import psycopg2

from .config import config
from .tables import tables

class NAVAdb:
    def __init__(self):
        self.params = config()
        self.conn = psycopg2.connect(**self.params)
        self.cur = self.conn.cursor()

    def create_tables(self):
        self.cur.execute(tables)

    def update_with_note(self, note):
        self.cur.execute(f"INSERT INTO notes VALUES ('{notes[0]}')")

    def delete(self):
        self.cur.execute(f"DROP DATABASE {type(self).__name__}")

    #TODO
    # def delete_note(self, note):
    #     self.cur.execute("""...""")

