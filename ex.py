import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
         sqlite_insert_query = """INSERT INTO books
                          (bid,title,author,status) 
                           VALUES 
                          (1,'James','jack','avail')"""

    count = cursor.execute(sqlite_insert_query)
    conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"newdbs.db")
