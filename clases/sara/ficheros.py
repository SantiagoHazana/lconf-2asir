# modos de abrir
# r -> lectura - si no existe el fichero lo crea
# w -> escritura - cuando abrimos el fichero lo borra y luego escribimos lo que queremos - si no existe el fichero lo crea
# a -> concatenar / append - no borra el fichero, sino que escribe al final del fichero - si no existe el fichero lo crea
# x -> crea el fichero, si existe da error

# # abrir y leer contenido completo del fichero
# file = open("hola.txt", "r")
# print(file.read())
# file.close()
#
# # abrir y escribir sobre el fichero borrando lo anterior
# file = open("hola.txt", "w")
# file.write("Hola\n")
# file.write("como\n")
# file.write("estas\n")
# file.close()
#
# # abrir y escribir al final del fichero, manteniendo lo anterior
# file = open("hola.txt", "a")
# file.write("adios")
# file.close()

# Al abrir un fichero que existe me da el error FileExistsError, lo manejamos con try except
# file = open("hola.txt", "x")

# # Diferentes formas de leer el fichero
# file = open("hola.txt", "r")
# # para leer el fichero completo, usamos read()
# contenido = file.read()
# print(contenido)
# # si queres leer X cantidad de caracteres
# contenido = file.read(3)  # cuando leo, el puntero queda donde termino de leer
# print(contenido)
# contenido = file.read(3)  # lee los siguientes 3 caracteres, no los 3 primeros nuevamente
# print(contenido)
# # quiero leer una linea
# linea = file.readline()  # cuando leo, el puntero queda donde termino de leer
# print(linea)
# linea = file.readline()  # lee la siguiente linea, no la primera nuevamente
# print(linea)

# leo todas las lineas y lo guardo en una lista
# lineas = file.readlines()
# print(lineas)
# # para saber cuantas lineas tiene el fichero
# print("El fichero tiene", len(lineas), "lineas")
#
# # mostrar las lineas pares
# print("\nLas lineas pares son:")
# numLineas = len(lineas)
# for i in range(0, numLineas, 2):
#     print(lineas[i], end="")
#
# # mostrar las lineas impares
# print("\nLas lineas impares son:")
# numLineas = len(lineas)
# for i in range(1, numLineas, 2):
#     print(lineas[i], end="")

# # imprimir la mitad superior del fichero
# numLineas = len(file.readlines())
# mitad = numLineas//2
# file.seek(0)  # esto me mueve el puntero de lectura al comienzo del fichero
# for i in range(0, mitad):
#     print(file.readline(), end="")
#
# # imprimir la mitad inferior
# file.seek(0)
# lineas = file.readlines()
# for i in range(mitad, numLineas):
#     print(lineas[i], end="")  # utilizo la lista de lineas para poder sacar la posicion especifica de linea

# # como escribir muchas lineas al mismo tiempo
# file = open("hola.txt", "w")
# lineas = ["Hola2\n", "como2\n", "estas2\n", "adios2\n", "chau2\n"]
# file.writelines(lineas)

# # pedir al usuario que escriba 5 lineas en el fichero
# file = open("frases.txt", "w")
# for i in range(5):
#     frase = input("Escriba una frase: ")
#     file.write(frase + "\n")
#
# file.close()

# Pedirle la usuario el nombre del fichero donde escribira, si existe pedirle otro nombre. Luego pedirle cuantas
# lineas va a escribir, comprobando que ingresa correctamente un numero y que sea entre 4 y 10.
# Pedirle ese numero de lineas y escribirlo en el fichero creado anteriormente
# Por ultimo, mostrarle el contenido del fichero y preguntarle si quiere modificar alguna linea (respuesta de si o no).
# En caso de querer modificar una linea, preguntarle cual linea, que contenido quiere escribir y escribirla.
# Mostrar el contenido del fichero.
