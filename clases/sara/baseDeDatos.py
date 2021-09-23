import mysql.connector

# # Como conectarse a mysql y crear una base de datos
# database = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=""
# )
#
# cursor = database.cursor()
#
# cursor.execute("drop database if exists python;")
# cursor.execute("create database python;")

# Como conectarse a mysql y a una base de datos directamente
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="nation"
)

# Como realizar querys de creacion, insercion, etc
cursor = database.cursor()
cursor.execute("create table if not exists test2(id int primary key, frase text);")

# Como hacer consultas
cursor.execute("select name, area, national_day from countries limit 10;")
resultado = cursor.fetchall()  # te trae todos los resultados en forma de lista, el cursor queda libre

# Imprimo todas las lineas, me las da en forma de tuplas
for linea in resultado:
    print(linea)

# Con el bucle me guardo en variables los valores de las columnas, para todas las lineas
for nombre, area, dia in resultado:
    print(nombre, "con un area de:", area, "y dia nacional:", dia)

# Como lee una sola linea
cursor.execute("select name, area, national_day from countries limit 10;")
un_resultado = cursor.fetchone()  # leo una sola linea, al cursor le quedan 9 lineas dentro
print("----------------Un solo resultado------------------")
print(un_resultado)

# Traer varias lineas, si el cursor tiene resultados, tengo que vaciarlo
cursor.fetchall()  # pido todas las lineas restantes y las descarto (al no guardarlo en ningun lado) y vacio el cursor
cursor.execute("select name, area, national_day from countries;")
varios_resultados = cursor.fetchmany(3)
print("----------------Varios resultados------------------")
for linea in varios_resultados:
    print(linea)
