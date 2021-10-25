meses = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"}

# 1. Sacar la posición de memoria 2.
print("------1------")
print("No puedo mostrar una posicion espeficia de un conjunto, no hay indices")

# 2. Cambiar el valor de una posición en una lista
print("------2------")
print("No puedo cambiar el valor de una posicion porque no hay posiciones")

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
meses.add("Otro")
print(meses)
print("No puedo agregar en una posicion especifica porque no hay posiciones")

# 6. Ordenar las listas con sort
# a. Alfabéticamente
# b. Descendiente
print("------6------")
print("No hay sort porque no hay un orden dentro del conjunto, pero puedo utilizar la funcion sorted()")
print(sorted(meses))
print(sorted(meses, reverse=True))

# 7. Borrado de listas.
# a. De un solo campo.
# b. Borrar el último elemento de una lista.
# c. Borrar lista entera
# d. Vaciado de una lista.
print("------7------")
meses.remove("Otro")
meses.pop()
meses.clear()
del meses

meses = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"}

# 8. Mostrar el contenido de la lista:
# a. Un rango de posiciones
# b. Mediante un if, que nos diga si está o no en el rango.
print("------8------")
print("No puedo recorrer un rango porque no hay indices")

# 9. Copiar lista a otra lista
print("------9------")
meses2 = meses.copy()
print(meses2)

# 10. Unir dos tablas
print("------10------")
meses3 = {"ENERO", "FEBRERO", "MARZO", "ABRIL"}
meses4 = meses.union(meses3)
print(meses4)

# 11. Contar cuantas veces aparece un nombre en las listas.
print("------11------")
count = 0
for i in meses:
    if i == "Enero":
        count += 1

print("Enero aparece", count, "veces")
