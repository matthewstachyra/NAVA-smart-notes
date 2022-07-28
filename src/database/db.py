'''
Postgresql database to store notes corpus.

set up
- first download postgresql with homebrew 'brew install postgresql'
- run 'psql postgres' in the terminal

postgres commands
- '\l' shows all databases
- 'CREATE DATABASE {db name}' creates a database
- 'DROP DATABASE {db name}' deletes database
- '\c {db name}' opens the database in terminal
- '\dt' shows the tables in the database

created: 20 July 2022
last updated: 28 July 2022
author: matthew stachyra
more: https://www.postgresqltutorial.com/postgresql-python/

TODO
[x] write skeleton db class
[x] update db class to delete database
[x] update db class to update database with note
[x] debug db
[x] figure out how to inspect database
[ ] tag v0.2.0 once database is working
[ ] enable embedding of database
[ ] enable searching
[ ] tag v0.3.0 once search works
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
        try:
            self.cur.execute(tables())
            self.conn.commit()
        except Exception as e:
            print(e)

    def update_with_note(self, note):
        self.cur.execute(f"INSERT INTO notes VALUES (DEFAULT, '{note[0]}')")
        self.conn.commit()

    def delete(self):
        self.cur.execute(f"DROP DATABASE {type(self).__name__}")
        self.conn.commit()

    #TODO
    # def delete_note(self, note):
    #     self.cur.execute("""...""")

