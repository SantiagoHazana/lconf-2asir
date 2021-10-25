meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

# 1. Sacar la posición de memoria 2.
print("------1------")
print(meses[2])

# 2. Cambiar el valor de una posición en una lista
print("------2------")
meses[2] = "FEBRERO"
print(meses[2])

# 3. Sacar todos los datos de una lista con un bucle.
print("------3------")
for i in meses:
    print(i, ":", meses.get(i))

# 4. Saca cuantas posiciones tienen datos en la lista
print("------4------")
print(len(meses))

# 5. Añadir contenido al final de la lista
# a. Insertar datos al final.
# b. Insertar datos en una posición de memoria.
print("------5------")
meses[13] = "Otro"
print(meses)
meses[3] = "Otro 2"
print(meses)

# 6. Ordenar las listas con sort
# a. Alfabéticamente
# b. Descendiente
print("------6------")
print("No se puede realizar con sort, pero puedo pedir los items del diccionario y ordenarlos con sort")
print(sorted(meses.values()))
print(sorted(meses.values(), reverse=True))

# 7. Borrado de listas.
# a. De un solo campo.
# b. Borrar el último elemento de una lista.
# c. Borrar lista entera
# d. Vaciado de una lista.
print("------7------")
meses.pop(2)
meses.pop(len(meses)-1)
meses.clear()
del meses

meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

# 8. Mostrar el contenido de la lista:
# a. Un rango de posiciones
# b. Mediante un if, que nos diga si está o no en el rango.
print("------8------")
for i in range(1, 3):
    print(meses[i])

for i in range(1, 100):
    if i >= len(meses):
        break
    print(i, ":", meses[i])

# 9. Copiar lista a otra lista
print("------9------")
meses2 = meses.copy()
print(meses2)

# 10. Unir dos tablas
print("------10------")
meses3 = {
    14: "ENERO",
    15: "FEBRERO",
    16: "MARZO",
    17: "ABRIL"
}
meses4 = meses.copy()
meses4.update(meses3)
print(meses4)

# 11. Contar cuantas veces aparece un nombre en las listas.
print("------11------")
count = 0
for i in meses:
    if meses.get(i) == "Enero":
        count += 1

print("Enero aparece", count, "veces")

count = 0
for i in meses.values():
    if i == "Enero":
        count += 1

print("Enero aparece", count, "veces")
