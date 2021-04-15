from Database.HelperDatabaseFunctions import *

DB_NAME = "TEST"

if __name__ == "__main__":

    conn = connect_to_database(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(CREATE_USER_TABLE_SCHEMA)
    cursor.execute(CREATE_SESSION_TABLE_SCHEMA)
    cursor.execute(CREATE_INTERVAL_TABLE_SCHEMA)

    conn.commit()

