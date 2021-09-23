# import sqlite3
#
# connection = sqlite3.connect("concesionario")
#
# cursor = connection.cursor()
#
# cursor.execute("insert into clientes values (123456, 'Juan', 'Perez', 'Malaga', '1982-06-15')")
#
# connection.close()


file = open("test.txt", "r")
lineasList = file.readlines()
lineas = len(lineasList)
mitadLineas = int(lineas/2)
lineasList.insert(mitadLineas, (input("Algo nuevo") + "\n"))
file = open("test.txt", "w")
file.writelines(lineasList)
print(mitadLineas)
