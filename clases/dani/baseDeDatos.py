# importo el connector
import mysql.connector

# Creo la conexion a la base de datos
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

# Como realizar consultas de creacion, insercion, etc
cursor = database.cursor()  # creamos un cursor que permite trabajar sobre la base de datos
cursor.execute("drop table if exists dani")
cursor.execute("create table dani(id int primary key, frase text)")
cursor.execute("insert into dani value (1, 'Daniel Sanchez')")

# Como leer los resultados de un select
cursor.execute("select * from jorge")
resultado = cursor.fetchall()  # Me devuelve todos los datos en una lista
print(resultado)  # mostramos el resultado

# Quiero mostrar linea a linea
for i in resultado:
    print(i)

# Imprimir dato a dato, linea a linea
for id, frase in resultado:
    print("Linea con id", id, "y frase", frase)
