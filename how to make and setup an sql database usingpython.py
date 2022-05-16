import sqlite3 as sl
con = sl.connect('test.db')

def newtable():
    with con:
        con.execute("""
                    CREATE TABLE LOGININFO (
                    USERNAME TEXT PRIMARY KEY,
                    PASSWORD VARCHAR(255),
                    AGE INTEGER
                    );
                """)
    inputing()

def inputing():
    sql = 'INSERT INTO logininfo (USERNAME, PASSWORD, AGE) values(?, ?, ?)'
    data = [
        ('user', 'password123', 22),
    ]
    with con:
        con.executemany(sql, data)
    searching()

def searching():
    query = "user"
    with con:
        data = con.execute(f"SELECT * FROM LOGININFO WHERE USERNAME like '{query}'")
        for row in data:
            print(row)
        query = "admin"
        data = con.execute(f"SELECT * FROM LOGININFO WHERE USERNAME like '{query}'")
        for row in data:
            print(row)

searching()