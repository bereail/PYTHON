import sqlite3 as sql


def createDB():
    conn = sql.connect("streames.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streames (
            name text,
            followers integer,
            subs integer
        )"""
    )    
    conn.commit()
    conn.close()

def insertRow(nombre, followers, subs):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES('{nombre}', {followers}, {subs})"
    conn.commit()
    conn.close()
    


if __name__ == "__main__":
    #createDB()
    #createTable()
    insertRow("Ibai", 70000, 25000)