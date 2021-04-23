import os

from Backend.Database.HelperDatabaseFunctions import *

FILE_DIR = os.path.dirname(os.path.abspath(__file__)) 

DB_NAME = "TEST.db"
DB_PATH = os.path.join(FILE_DIR, "db", DB_NAME)

if __name__ == "__main__":

    if os.path.isfile(DB_PATH):
        os.remove(DB_PATH)

    conn = connect_to_database(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(USER_TABLE_SCHEMA)
    cursor.execute(SESSION_TABLE_SCHEMA)

    conn.commit()