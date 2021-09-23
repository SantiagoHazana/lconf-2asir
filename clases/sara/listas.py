# las listas se declaran con [], son ordenadas (indices), permiten duplicados y se pueden agregar o sacar elementos y
# cambiar el valor de los elementos
nombres = ["sara", "santiago", "sara", "diego", "maria"]
print(nombres)  # imprimi la lista entera

# largo de la lista len(lista)
print(len(nombres))

# las listas puede tener cualquier tipo de variables y no deben ser todas del mismo tipo
listaVariada = [1, "hola", False]
print(listaVariada)

# acceder e imprimir un solo elemento de la lista
print(nombres[1])
# cambiar el valor de una lista
nombres[2] = "carlos"
print(nombres)

# si quiero imprimir el ultimo elemento
print(nombres[len(nombres)-1])
print(nombres[-1])  # al poner un - comienza desde el final

# si quiero imprimir un rango de valores de la lista
print(nombres[1:4])
# si quiero imprimir desde una posicion hasta el final de la lista, al no poner hasta donde, sigue hasta el final
print(nombres[2:])
# si quiero imprimir desde el primero hasta el que diga, al no poner desde donde, comienza desde el primero
print(nombres[:4])

# comprobar si un elemento existe en la lista
if "sara" in nombres:
    print("existe sara en la lista")

# agregar un elemento nuevo, al final de la lista
nombres.append("marina")
print(nombres)

# agregar un elemento en una posicion especifica
nombres.insert(1, 'sergio')
print(nombres)

nombres2 = ["paco", "rosalia", "pedrito"]
# si quiero agregar todos los valores de una lista a otra lista
nombres.extend(nombres2)
print(nombres)

# eliminar un elemento de la lista, elimina el primero que encuentre
nombres.remove("pedrito")

# eliminar una posicion especifica
nom = nombres.pop(4)  # si no recibe indice, elimina el ultimo, nos devuelve el valor que hubiera en esa posicion
print(nom)

# eliminar una posicion dara
del nombres[2]
print(nombres)

# recorrer cada uno de los elementos de una lista
# for i in nombres:
#     print(i)

# si quiero ordenar una lista, todos los elementos deben ser del mismo tipo
nombres.sort()  # ordena de menor a mayor
nombres.sort(reverse=True)  # ordena de mayor a menor
print(nombres)

# si quiero invertir una lista
nombres.reverse()
print(nombres)

# si queres copiar una lista, debemos utilizar la funcion copy(), porque de no hacerlo solo estamos copiando la
# referencia de la variable

nombres2 = nombres  # al igualar solo estoy copiando la direccion en memoria de la lista, entonces ambas apuntan a lo mismo
nombres2 = nombres.copy()  # asi estoy copiando la lista entera
nombres2 = list(nombres)  # utilizo el constructor de lista
nombres2.pop()
nombres2.pop()
nombres2.pop()
print("nombres 2", nombres2)
print("nombres", nombres)

# unir dos listar en otra
nombres3 = nombres + nombres2
print(nombres3)

# vaciar una lista
nombres.clear()
print(nombres)

# eliminar la lista
del nombres  # deja de existir la variable nombres


#
# abc = []
# for char in range(97, 123):
#     abc.append(chr(char))
#
# print(abc)
