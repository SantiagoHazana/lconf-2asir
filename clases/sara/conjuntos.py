# los conjuntos no tiene orden (no indexados), no permite duplicados, no se puede cambiar el valor de los elementos,
# pero si se puede agregar y sacar valores
conjunto = {2, 5, 76, 10}
print(conjunto)
print(len(conjunto))

# podemos agregar valores
conjunto.add(9)
print(conjunto)
conjunto.add(-10)
print(conjunto)
conjunto.add(1)
print(conjunto)
conjunto.add(-5)
print(conjunto)
conjunto.add(-7)
print(conjunto)

# no permite duplicados, si intentamos agregar uno, lo ignora
conjunto.add(5)
print(conjunto)

# como saber si un elemento esta en el conjunto
# num = int(input("Ingrese un numero: "))
# if num in conjunto:
#     print("Ya existe ese elemento en el conjunto")
# else:
#     conjunto.add(num)
# print(conjunto)

# mostrar los elementos del conjunto es con un for, al no estar ordenados
for i in conjunto:
    print(i)

# agregar un conjunto a otro
otro = {3, 5, 13, -10}
conjunto.update(otro)
print(conjunto)

# quedarte SOLO los repetidos
otro = {4, 5, 10, 11}
otro.intersection_update(conjunto)  # este actualiza la misma tupla con los valores duplicados
print(otro)

otro = {4, 5, 10, 11}
otro2 = otro.intersection(conjunto)  # este devuelve un conjunto con los duplicados
print(otro2)

# quedarse con todos menos los duplicados
otro = {4, 5, 10, 11}
otro.symmetric_difference_update(conjunto)  # se queda con los elementos de ambos conjuntos que NO estan repetidos
print(otro)

# cambiar el valor de un elemento del conjunto
lista = list(conjunto)
lista[0] = 666
conjunto = set(lista)
print(conjunto)
