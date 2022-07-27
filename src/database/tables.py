def tables():
    '''returns tables to add to NAVAdb in db.py.
    '''
    commands = (
        f"""
        CREATE TABLE notes (
            id SERIAL PRIMARY KEY,
            note VARCHAR NOT NULL,
        """
    )

    return commands
