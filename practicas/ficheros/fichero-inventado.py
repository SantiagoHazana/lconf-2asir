import random

fichero = ""
while True:
    try:
        fichero = input("Ingrese un fichero que no exista: ")
        file = open(fichero, "r")
        print("El fichero existe")
    except FileNotFoundError:
        print("El fichero no existe, se creara")
        file = open(fichero, "w")
        break

for i in range(5):
    line = input("Ingrese la " + (i+1).__str__() + " linea: ")
    file.write(line + "\n")

file.close()
file = open(fichero, "r")
lines = file.readlines()

for i in lines:
    print(i, end="")

line = input("Ingrese el nuevo contenido de la linea 2: ")
lines.pop(1)
lines.insert(1, line + "\n")
file.close()
file = open(fichero, "w")
file.writelines(lines)
file.close()

file = open(fichero, "r")
lines = file.readlines()
for i in lines:
    print(i, end="")

file.close()
file = open(fichero, "w")

randLine = random.randint(0, 4)
line = input("Ingrese el nuevo contenido de la linea " + (randLine+1).__str__() + ": ")
lines.pop(randLine)
lines.insert(randLine, line + "\n")
file.writelines(lines)

for i in range(6, 9):
    line = input("Ingrese la " + i.__str__() + " linea: ")
    file.write(line + "\n")

file.close()
file = open(fichero, "r")

for i in file.readlines():
    print(i, end="")

