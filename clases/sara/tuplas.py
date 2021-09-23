# conjunto de valores que tienen orden pero ese orden no se puede cambiar, no se puede agregar o sacar y no se permite
# cambiar el valor, permite duplicados
tupla = (3, 5, 3, 10, 8)
print(tupla)
# largo de la tupla, con len()
print(len(tupla))

# imprimir el segundo valor
print(tupla[2])

# imprimir el ultimo valor
print(tupla[-1])
# imprmir rango de valores
print(tupla[1:3])

# cambiar el valor a un elemento de la tupla
lista = list(tupla)
lista[2] = 7
tupla = tuple(lista)
print(tupla)
# agregar elementos
lista = list(tupla)
lista.append(17)
tupla = tuple(lista)
print(tupla)
# para eliminar hacemos lo mismo pero eliminando

# para recorrer la tupla
for i in tupla:
    print(i, end="  ")
print()
# unir dos tuplas
tupla2 = (6, 8, 11)
tupla3 = tupla + tupla2
print(tupla3)

# multiplicar el contenido
tupla4 = tupla3 * 2
print(tupla4)

# como ordenar la tupla
lista = list(tupla)
lista.sort()
tupla = tuple(lista)
print(tupla)
