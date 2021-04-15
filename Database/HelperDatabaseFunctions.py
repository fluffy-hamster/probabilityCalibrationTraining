import sqlite3

CREATE_USER_TABLE_SCHEMA = '''
CREATE TABLE USER
(
    [UserId] INTEGER PRIMARY KEY, 
    [username] TEXT, 
    [SessionId] INTEGER NOT NULL
)
'''

CREATE_SESSION_TABLE_SCHEMA = '''
CREATE TABLE SESSION 
(
    [SessionId] INTEGER NOT NULL,
    [interval] TEXT,
    [True] INTEGER, 
    [False] INTEGER,
    FOREIGN KEY (SessionId) REFERENCES USER(SessionId)
)
'''

def connect_to_database(db_name: str):
    return sqlite3.connect(f'{db_name}.db')
