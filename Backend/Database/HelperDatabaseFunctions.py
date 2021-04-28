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


def connect_to_database(db_path: str):
    return sqlite3.connect(db_path)


def addUserCommand(username: str) -> str:
    return f"""
    INSERT INTO User (username)
    VALUES ("{username}")
    """

def addSessionCommand(session_id: int, user_id: int, interval: float, correct_answers: int, wrong_answers: int) -> str:
    return f"""
    INSERT INTO Session (sessionId, userId, interval, correctAnswers, wrongAnswers)
    VALUES ({session_id}, {user_id}, {interval}, {correct_answers}, {wrong_answers})
    """
