# los diccionarios son ordenados, permiten cambios y no permiten duplicados
diccionario = {
    "clave": "valor",
    "clave2": "valor",
    "clave3": "valor2"
}
print(diccionario)

# acceder a un valor de un diccionario
print(diccionario["clave2"])
print(diccionario.get("clave2"))

# cambiar el valor del un elemento
diccionario["clave2"] = 100

# agregar un elemento
diccionario["nuevaClave"] = "nuevo"

print(len(diccionario))
print(diccionario)

# pedir todas las claves del diccionario
claves = diccionario.keys()  # no copia las claves, esta apuntando a las claves del diccionario, si se agrega, se actualiza
print(claves)

diccionario["nueva2"] = 102

print(claves)

# pedir todos los valores
valores = diccionario.values()  # funciona de la misma manera que las claves, apunta a los valores y se actualiza si se agregan
print(valores)

# obtener las claves y valores del diccionario, esto me devuelve una lista de tuplas
items = diccionario.items()  # tambien es solo un puntero, si se actualiza el diccionario se actualiza la variable
# me da una lista con tuplas dentro con las claves y valores en cada tupla
print(items)

# comprobar si existe una clave
if "nueva2" in diccionario:
    print("existe esa clave")

# eliminar un elemento del diccionario
diccionario.pop("nueva2")
print(diccionario)

for i in diccionario:
    print(i)  # imprime las claves

# imprimir los valores
for i in diccionario:
    print(diccionario[i])

# otras manera de recorrer valores
for i in diccionario.values():
    print(i)

# otras manera de recorrer claves
for i in diccionario.keys():
    print(i)

# imprimir claves y valores
for i, j in diccionario.items():
    print(i, j)
