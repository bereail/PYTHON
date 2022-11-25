import sqlite3

from estudiante import Estudiante ##importo sqlite

conn = sqlite3.connect('universidad.db') ##conecto con base de datps
c = conn.cursor() ##creo el cursor para hacer query

c.execute(""" CREATE TABLE IF NOT EXISTS estudiantes (
    matricula TEXT PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    promedio REAL NOT NULL) """)


# CREO ESTUDIANTE 
#c.execute("INSERT INTO estudiantes VALUES ('111', 'roberto', 'cruz', 9.5)") 

conn.commit()

#creo estudiantes a traves del objeto Estudiantes
est_1 = Estudiante('22', 'bere', 'solohaga', 9.5)
est_2 = Estudiante('333', 'lucia', 'vazquez', 7.5)
est_3 = Estudiante('444', 'sofia', 'sanchez', '5')
est_4 = Estudiante('58', 'maria', 'gomez', '8')
est_5 = Estudiante('98', 'lorena', 'garcia', '7')

#insertar usuarios de tipo tupla
#c.execute("INSERT INTO estudiantes VALUES (?, ?, ?, ?)", 
#         (est_1.matricula, est_1.nombre, est_1.apellido, est_1.promedio))


#insertar usuarios de tipo diccionario
#c.execute("INSERT INTO estudiantes VALUES (:matricula, :nombre, :apellido, :promedio)", {
#    'matricula': est_2.matricula, 
#    'nombre': est_2.nombre,
#    'apellido': est_2.apellido,
#    'promedio': est_2.promedio
#})


#c.execute("INSERT INTO estudiantes (matricula, nombre, apellido) VALUES (?, ?, ?)",
#        (est_3.matricula, est_4.nombre, est_5.apellido))

#c.execute("SELECT * FROM estudiantes ") #selecciona todo los estudiantes
#estudiantes = c.fetchall() #printea todos los estudiantes


#printea solo el primer estudiante     
# estudiantes = c.fetchone() 

many_students = [
    (est_1.matricula, est_1.nombre, est_1.apellido, est_1.promedio),
    (est_2.matricula, est_2.nombre, est_2.apellido, est_2.promedio),
    (est_3.matricula, est_3.nombre, est_3.apellido, est_3.promedio),
    (est_4.matricula, est_4.nombre, est_4.apellido, est_4.promedio)
]

#c.executemany("INSERT INTO estudiantes VALUES (?, ?, ?, ?)", many_students)

c.execute("SELECT * FROM estudiantes WHERE matricula=?", ('e',))
estudiantes = c.fetchone()
print(estudiantes)

#c.execute("SELECT * FROM estudiantes")
#estudiantes = c.fetchmany(5)#le indicamos la cantidad que queremos ver
#print(estudiantes)


conn.close() ##cierro db