from typing import Optional, List, Tuple

from Backend.Database import HelperDatabaseFunctions
from Backend.SessionUser import SessionUser


class DatabaseApi():

    def __init__(self, path:str):
        self.conn = HelperDatabaseFunctions.connect_to_database(path)
        self.cursor = self.conn.cursor()

        self.userId: Optional[int] = None

    def create_new_user(self, username: str):
        self.cursor.execute(HelperDatabaseFunctions.add_new_user_command(username))
        self.conn.commit()

    def get_user_id(self, username:str) -> int:
        self.cursor.execute(HelperDatabaseFunctions.get_user_id_command(username))
        try:
            return self.cursor.fetchall()[0][0] # [(x,)]
        except:
            return -1

    def get_next_session_id(self, user_id: int) -> int:
        self.cursor.execute(HelperDatabaseFunctions.get_max_session_id_command(user_id))
        return self.cursor.fetchall()[0][0] + 1
    
    def add_session_data(self, user_id: int, session_id:int, session_user: SessionUser):
 
        for interval, score in session_user.data.items():
            correct_answers = score[True] 
            wrong_answers = score[False]

            self.cursor.execute(HelperDatabaseFunctions.add_session_command(session_id, user_id, interval, correct_answers, wrong_answers))
            self.conn.commit()

    def get_all_session_data(self, user_id):

        self.cursor.execute(HelperDatabaseFunctions.get_all_user_sessions_command(user_id))       
        headers: List[str] = [i[0] for i in self.cursor.description]
        result: List[Tuple] = self.cursor.fetchall()

        return (headers, result)
