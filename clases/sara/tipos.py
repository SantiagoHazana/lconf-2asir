# name = "Santiago"
# surname = "Hazana"
# print(name)
#
# print(name, surname)
#
# # EL print nos por defecto separa con espacio lo que imprimimos y hace un salto de linea al final, pero esto es
# # configurable
# print(name, surname, sep=' - ')  # reemplazar el espacio por defecto por un -
# print(name, surname, sep=' - ', end='*/')  # reemplazar el salto de linea por defecto por */
# print()

# # tengo que convertirlo a numero poniendo int()
# num = int(input("Ingrese un numero: "))
# if num > 0:
#     print("El numero es positivo")
# elif num < 0:
#     print("El numero es negativo")
# else:
#     print("El numero es 0")

cont = 0
while cont < 10:
    print(cont)
    cont += 1


print("Bucle for")
for i in range(10):  # me recorre de 0 a 10 sin incluir
    print(i)
# el range decimos desde que numero hasta cual queremos un rango (sin incluir el segundo). El tercer parametro me
# dice de cuanto en cuanto avanzo por el range
for i in range(1, 20, 2):  # saca los impares del 1 al 20
    print(i)

for i in range(10):  # muestro los pares pero con un if dentro
    if i % 2 == 0:
        print(i)

lista = ["Hola", "mundo", "Python"]
for i in lista:
    print(i)
