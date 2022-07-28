def tables():
    '''returns tables to add to NAVAdb in db.py.
    '''
    commands = (
        """CREATE TABLE IF NOT EXISTS notes (id SERIAL PRIMARY KEY, note VARCHAR NOT NULL);"""
    )

    return commands
