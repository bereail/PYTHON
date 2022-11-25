from asyncore import read
import sqlite3 as sql


#CREO base de datos
def createDB():
    conn = sql.connect("stock.db")
    conn.commit()
    conn.close()

def readOrdered(field):
    conn = sql.connect("stock.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * from stock ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)     


#Inserto elemnto sen databse
def createTable():
    conn = sql.connect("stock.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE stock (
            name text,
            cantidad integer,
            precio integer
        )"""
    )
    conn.commit()
    conn.close()

#fucnion para agregar elementos a al fila
def insertRow(name, cantidad, precio):
    conn = sql.connect("stock.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO  stock VALUES('{name}', {cantidad}, {precio})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


#imprime por pantalla los elemtnos de fila
def readRows():
    conn = sql.connect("stock.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM stock"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    print("\n")


#insertar lista de productos
def insertRows(stockList):
    conn = sql.connect("stock.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO stock VALUES (?, ?, ?)"
    cursor.executemany(instruccion, stockList)
    conn.commit()
    conn.close()



#devulve los elementos d ela fila ingresando el nombre de la columnna
def search():
    conn = sql.connect("stock.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM  stock  WHERE name like '45%'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

#crear una alerta cuando se encuntra bajo el stock
def alertBajaCantidad():
    conn = sql.connect("stock.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM stock WHERE cantidad < 20 ORDER BY cantidad DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


#actualizar campor de un fila existente
def updateFields():
    conn = sql.connect("stock.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE stock SET cantidad=40 WHERE name like '450'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


#borrar da
def deleteRow():
    conn = sql.connect("stock.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM stock WHERE name='210'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    print("Borraor exitosamente")



if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow("85A", 10, 3500)
    #insertRow("450", 20, 4200)
    #readRow()
    stock = [
        ("2370", 20, 3620),
        ("210", 5, 2800),
        ("19", 15, 3200)
    ]
    #insertRows(stock)
    #readOrdered("cantidad")
    #search()
    #alertBajaCantidad()
    deleteRow()