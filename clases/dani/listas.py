lista = [5, 3, 7, 8, 8]
print(lista)
print(lista[2])
lista[2] = 17
print(lista[2])
print("En la lista hay:",
      len(lista))  # len te dice la cantidad de elementos, para saber la posicion del ultimo elemento hago len()-1

lista.insert(1, 55)  # insertar en la posicion dada el valor dado, mueve el resto de valores
print(lista)
lista.append(69)  # agrega el valor dado al final de la lista
print(lista)
lista.remove(55)  # borra el valor (no la posicion) que le demos, si hay varios, borra el primero que encuentre
print(lista)
lista.remove(8)
print(lista)
num = lista.pop()  # saca el valor de la posicion dada (lo elimina) y te lo devuele, entonces te permite guardarlo en una variable si queres, si no se especifica posicion, saca el ultimo elemento
print(lista)
print(num)
# lista.clear()  # vacia la lista
# print(lista)

# Ejemplo de lista con varios tipos
persona = ["Daniel", "Sanchez", 20, 170, True]
persona2 = ["Santiago", "Hazana", 25, 172, True]
personas = [persona, persona2]
# print(persona)
# Saco una persona, la modifico y la vuelvo a agregar
print(personas)
pers = personas.pop(0)
print(personas)
pers[3] = 178
personas.append(pers)
print(personas)

lista.sort()  # ordena de menor a mayor, todos los elementos tiene que ser del mismo tipo
print(lista)
lista.sort(reverse=True)  # ordena inversamente
print(lista)

for i in lista:
    print(i)
