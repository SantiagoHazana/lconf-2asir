# para abrir un fichero usamos la funcion open(), recibe dos cosas, el nombre del fichero y el modo en el que lo abrimos
# r - lectura
# w - escritura, abre y vacia el fichero para escribir nuevamente, lo crea si no existe
# a - concatenar / append, agregar al final del fichero contenido
# x - crear, si existe nos da un error

# # lo abro en modo W para que lo cree y escribir en el
# file = open("primero.txt", "w")  # cuando abro el fichero se vacia
# # para escibir
# file.write("Hola mundo\n")  # el \n me hace un salto de linea
# # siempre al finalizar hay que cerrar el fichero
# file.close()

# # lo abro en modo A
# file = open("primero.txt", "a")
# # escribimos algo nuevo
# file.write("Hola mundo 2\n")
# file.close()

# # leer un fichero
# file = open("primero.txt", "r")
# contenido = file.read()  # leo el contenido y lo guardo en una variable
# print(contenido)
# file.close()

# # Como leer X cantidad de caracteres
# file = open("primero.txt", "r")
# leer5 = file.read(5)  # esto lee los primeros 5 caracteres
# print(leer5)

# # Como leer una linea completa
# file = open("primero.txt", "r")
# linea = file.readline()  # leo la primera linea
# print(linea)
# linea = file.readline(3)  # leo 3 caracteres de la segunda linea
# print(linea)

# # Leer todas las lineas de un fichero
# file = open("primero.txt", "r")
# for i in file:  # i va leyendo y guardando el valor de cada una de las lineas
#     print(i)

# # Como guardarnos todas las lineas del fichero
# file = open("primero.txt", "r")
# lineas = file.readlines()
# print(lineas)
# for i in lineas:
#     print(i)

# file = open("primero.txt", "r")
# lineas = file.readlines()
# # Quiero mostrar solo las primeras 5 lineas
# for i in range(5):
#     print(lineas[i], end="")

# # Quiero mostrar la mitad superior del fichero
# file = open("primero.txt", "r")
# lineas = file.readlines()
# mitad = len(lineas)//2
# for i in range(mitad):
#     print(lineas[i], end="")

# # Mostrar la parte inferior del fichero
# file = open("primero.txt", "r")
# lineas = file.readlines()
# for i in range((len(lineas)//2), len(lineas)):
#     print(lineas[i], end="")

# # Como modificar una sola linea del fichero
# file = open("primero.txt", "r")
# lineas = file.readlines()
# # Quiero cambiar la tercera linea
# lineas[2] = "Tercera linea modificada\n"
# # Tengo que cerrar el fichero
# file.close()
# # Lo vuelvo a abrir en modo W
# file = open("primero.txt", "w")
# file.writelines(lineas)
# file.close()

# # como pedir al usuario 5 frases y escribirlas en un fichero
# file = open("frases.txt", "w")
# for i in range(5):
#     phrase = input("Ingrese una frase loca: ")
#     file.write(phrase + "\n")
#
# file.close()
