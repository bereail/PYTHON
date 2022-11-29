import mysql.connector
#CONEXION BASE DE DATOS
try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='sarita508',
        db='berenice'
    )
except Exception as ex:
    print(ex)



#IMPRIME POR PANTALLA LOS ELMENTOS DE UNA FILA
def readRows():
    #conn = sql.connect("berenice.db")
    cursor = connection.cursor()
    instruccion = "SELECT * from articulos"
    cursor.execute(instruccion)
    array= cursor.fetchall()
    for x in array:
        print(x)

    connection.close()

readRows()