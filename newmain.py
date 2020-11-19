import sqlite3


conn=sqlite3.connect(r"newdbs.db")
cur=conn.cursor()
"""
bookTable = "books" 
"""
bid = '3'
title = 'ssd'
author ='gg'
status = 'avail'
status = status.lower()
data=(bid,title,author,status)
try:
    conn = sqlite3.connect(r"newdbs.db")
    cur=conn.cursor()
    print(sqlite3.version)
    sqlite_insert_query = """INSERT INTO books
                        (bid,title,author,status)
                        VALUES(?,?,?,?);"""

    cur.execute(sqlite_insert_query,(bid,title,author,status))
    print('Success',"Book added successfully")
    cur.execute('select * from books')
    data=cur.fetchall()
    for row in data:
        print(row)
    conn.commit()
except:
    print("Error","Can't add data into Database")
finally:
    if conn:
        conn.close()
