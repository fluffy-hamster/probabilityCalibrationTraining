import sqlite3

USER_TABLE_SCHEMA = '''
CREATE TABLE User
(
    userId INTEGER PRIMARY KEY, 
    username TEXT
)
'''

SESSION_TABLE_SCHEMA = '''
CREATE TABLE Session 
(
    id INTEGER PRIMARY KEY,
    sessionId INTEGER,
    userId INTEGER,
    interval DECIMAL,
    correctAnswers INTEGER, 
    wrongAnswers INTEGER,
    FOREIGN KEY(userId) REFERENCES User(UserId)
)
'''
#FOREIGN KEY UserId REFERENCES USER(UserId)

def connect_to_database(db_path: str):
    return sqlite3.connect(db_path)
