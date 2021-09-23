import mysql

file = open("personas.txt", "r")
hombres = open("hombres.txt", "w")
mujeres = open("mujeres.txt", "w")
contenido = file.readlines()

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="nation"
)

for i in contenido:
    datos = i.split()
    if datos[4] == 'm':
        hombres.write(i)
    else:
        mujeres.write(i)


file.close()
hombres.close()
mujeres.close()

file = open("hombres.txt", "r")
filas = file.readlines()

for i in filas:
    datos = i.split()
    database.cursor().execute("insert into hombres value('" + datos[0] + "', '" + datos[1] + "', '" + datos[2] + "', " + datos[3] + ", " + datos[5] + ")")

file = open("mujeres.txt", "r")
filas = file.readlines()

for i in filas:
    datos = i.split()
    database.cursor().execute("insert into mujeres value('" + datos[0] + "', '" + datos[1] + "', '" + datos[2] + "', " + datos[3] + ", " + datos[5] + ")")


