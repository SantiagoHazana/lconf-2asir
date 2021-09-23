# num = input("Ingrese un numero: ")
# try:
#     res = num/2
#     print(res)
# except TypeError:
#     print("Manejo de error")
# except Exception:
#     print("Cualquier otra excepcion")
#
# print("Algo al final")

# try:
#     num = int(input("Ingrese un numero: "))
# except ValueError:
#     print("No ingresaste un numero")
#     num = 0
#
# res = num/2
# print(res)
# print("Algo al final")


# # como pedir un numero hasta que se ingrese correctamente
# while True:
#     try:
#         num = int(input("Ingrese un numero: "))
#         break
#     except ValueError:
#         print("No ingresaste un numero, bobo")
#
# print("Ingresaste correctamente el numero", num)
#
# # pedir un numero entero y positivo
# while True:
#     try:
#         num = int(input("Ingrese un numero: "))
#         if num > 0:
#             break
#         else:
#             print("El numero debe ser positivo")
#     except ValueError:
#         print("No ingresaste un numero, bobo")
#
# print("Ingresaste correctamente el numero", num)

# # pedir 5 numeros positivos enteros
# for i in range(5):
#     while True:
#         try:
#             num = int(input("Ingrese un numero: "))
#             if num > 0:
#                 break
#             else:
#                 print("El numero debe ser positivo")
#         except ValueError:
#             print("No ingresaste un numero, bobo")
#
#     print("Ingresaste correctamente el", (i + 1), "numero: ", num)
#
# print("Termino el bucle")

try:
    num = int(input("Ingrese un numero: "))
except ValueError:
    print("No ingresaste un numero, bobo")
else:  # solo se ejecuta cuando NO hay errores
    print("Ingresaste algo correcto!!")
finally:  # se ejecuta SIEMPRE cuando termina el try except, pase lo que pase
    print("Lo ultimo ejecutado")

# TODO Ejercicio Dani
# Pedir al usuario cuantos numeros desea ingresar. Luego pedir esos numeros y guardarlos en una lista. Mostrar todos
# los valores ordenados, mostrar el mayor, el menor y la media de todos los numeros.
# Contabilizar los intentos del usuario e informarlo al final. Manejar las excepciones
