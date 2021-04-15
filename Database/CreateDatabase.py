from Database.HelperDatabaseFunctions import *

DB_NAME = "TEST"

if __name__ == "__main__":

    conn = connect_to_database(DB_NAME)
    
    conn.execute(CREATE_USER_TABLE_SCHEMA)
    conn.execute(CREATE_SESSION_TABLE_SCHEMA)
    conn.execute(CREATE_INTERVAL_TABLE_SCHEMA)


    conn.commit()

