import sqlite3

USER_TABLE_SCHEMA = '''
CREATE TABLE User
(
    userId INTEGER PRIMARY KEY, 
    username TEXT UNIQUE
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


def connect_to_database(db_path: str) -> sqlite3.Connection:
    return sqlite3.connect(db_path)


def add_new_user_command(username: str) -> str:
    return f"""
    INSERT INTO User (username)
    VALUES ("{username}")
    """


def add_session_command(session_id: int, user_id: int, interval: float, correct_answers: int, wrong_answers: int) -> str:
    return f"""
    INSERT INTO Session (sessionId, userId, interval, correctAnswers, wrongAnswers)
    VALUES ({session_id}, {user_id}, {interval}, {correct_answers}, {wrong_answers})
    """


def get_max_session_id_command(user_id:int) -> str:
    return f"""
    SELECT MAX(sessionId) FROM Session WHERE userId={user_id}
    """


def get_all_user_sessions_command(user_id:int) -> str:
    return f"""
    SELECT * FROM Session WHERE userId={user_id}
    """


def get_user_id_command(username:str) -> str:
    return f"""
    SELECT userId FROM user WHERE username="{username}"
    """ 