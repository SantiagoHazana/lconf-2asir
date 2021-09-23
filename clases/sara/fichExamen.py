file = open("frases.txt", 'r')
lines = file.readlines()
file2 = open("primeras.txt", 'w')
file3 = open("segundas.txt", 'w')
num = int(input("Numero de lineas a guardar en primeras: "))
if num > len(lines):
    print("Numero de lineas incorrecto")
else:
    file2.writelines(lines[:num])
    file3.writelines(lines[num:])


