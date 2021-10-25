meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

# 1. Sacar la posición de memoria 2.
print("------1------")
print(meses[2])

# 2. Cambiar el valor de una posición en una lista
print("------2------")
print("No se puede realizar en tuplas")

# 3. Sacar todos los datos de una lista con un bucle.
print("------3------")
for i in meses:
    print(i)

# 4. Saca cuantas posiciones tienen datos en la lista
print("------4------")
print(len(meses))

# 5. Añadir contenido al final de la lista
# a. Insertar datos al final.
# b. Insertar datos en una posición de memoria.
print("------5------")
print("No se puede realizar en tuplas")

# 6. Ordenar las listas con sort
# a. Alfabéticamente
# b. Descendiente
print("------6------")
print("No se puede realizar con sort, pero si con la funcion sorted()")
print(sorted(meses))
print(sorted(meses, reverse=True))

# 7. Borrado de listas.
# a. De un solo campo.
# b. Borrar el último elemento de una lista.
# c. Borrar lista entera
# d. Vaciado de una lista.
print("------7------")
print("No se puede eliminar elementos de las tuplas")
del meses

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

# 8. Mostrar el contenido de la lista:
# a. Un rango de posiciones
# b. Mediante un if, que nos diga si está o no en el rango.
print("------8------")
for i in range(1, 3):
    print(meses[i])

for i in range(100):
    if i >= len(meses):
        break
    print(i+1, ":", meses[i])

# 9. Copiar lista a otra lista
print("------9------")
meses2 = tuple(meses)
print(meses2)

# 10. Unir dos tablas
print("------10------")
meses3 = ("ENERO", "FEBRERO", "MARZO", "ABRIL")
meses4 = meses + meses3
print(meses4)

# 11. Contar cuantas veces aparece un nombre en las listas.
print("------11------")
print("Enero aparece:", meses.count("Enero"), "veces")

