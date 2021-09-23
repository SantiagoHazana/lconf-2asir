import random

file = open("frases.txt", "r")
# # Leer el fichero completo y guardarlo en una variable
# todoContenido = file.read()
# print(todoContenido)

# # Leemos la primera y segunda linea
# primeraLinea = file.readline()
# print(primeraLinea, end="")
# segundaLinea = file.readline()
# print(segundaLinea, end="")

# # Leer todas las lineas, linea a linea
# for i in file:
#     print(i, end="")

# Guardar todas las lineas en una lista
# lineas = file.readlines()
# print("El fichero tiene", len(lineas), "lineas")
# print(lineas[2], end="")
# print(lineas)
# lineas[5] = "Adios\n"  # modificar una linea
# print(lineas)

# Mostrar el contenido del fichero pero poniendo el numero de linea
# lineas = file.readlines()
# contador = 0
# for i in lineas:
#     contador += 1
#     print(contador, "-", i, end="")
#
# for i in range(len(lineas)):
#     print(i+1, lineas[i], end="")
