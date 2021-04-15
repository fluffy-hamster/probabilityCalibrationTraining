import sqlite3

CREATE_USER_TABLE_SCHEMA = '''
CREATE TABLE USER
([generated_id] INTEGER PRIMARY KEY, [username] text, [Session_ID] integer)
'''

CREATE_SESSION_TABLE_SCHEMA = '''
CREATE TABLE SESSION 
([username], [interval_ID] text)
'''

CREATE_INTERVAL_TABLE_SCHEMA = '''
CREATE TABLE INTERVAL 
([interval_ID] text, [True] integer, [False] integer)
'''


def connect_to_database(db_name: str):
    return sqlite3.connect(f'{db_name}.db')
