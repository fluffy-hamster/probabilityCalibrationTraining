import os
import sys

from backend.Database.HelperDatabaseFunctions import *

FILE_DIR = os.path.dirname(os.path.abspath(__file__)) 

DB_NAME = "TEST.db"
DB_PATH = os.path.join(FILE_DIR, "db", DB_NAME)

if __name__ == "__main__":

    db_path = DB_PATH if len(sys.argv) <= 1 else sys.argv[1]

    # Delete if exists
    if os.path.isfile(db_path):
        os.remove(db_path)

    conn = connect_to_database(db_path)
    cursor = conn.cursor()
    
    cursor.execute(USER_TABLE_SCHEMA)
    cursor.execute(SESSION_TABLE_SCHEMA)

    conn.commit()