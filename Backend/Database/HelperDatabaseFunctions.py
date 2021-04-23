import sqlite3

CREATE_USER_TABLE_SCHEMA = '''
CREATE TABLE USER
(
    [UserId] INTEGER PRIMARY KEY, 
    [username] TEXT
)
'''

CREATE_SESSION_TABLE_SCHEMA = '''
CREATE TABLE SESSION 
(
    [interval(%)] DECIMAL PRIMARY KEY,
    [CorrectAnswers] INTEGER, 
    [WrongAnswers] INTEGER
)
'''
#FOREIGN KEY UserId REFERENCES USER(UserId)

def connect_to_database(db_path: str):
    return sqlite3.connect(db_path)
