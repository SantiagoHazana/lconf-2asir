primeros = open("primeros.txt", "w")
ultimos = open("ultimos.txt", "w")

while True:
    try:
        fichero = input("Ingrese un fichero que exista: ")
        file = open(fichero, "r")
        break
    except FileNotFoundError:
        print("El fichero no existe")


lines = file.readlines()
while True:
    print("El fichero tiene", len(lines), "lineas. Seleccione una entre 1 y", len(lines))
    try:
        num = int(input("Seleccione una linea: "))
    except TypeError:
        print("No ingreso un numero")

    if 0 < num <= len(lines):
        break
    print("No ingreso un numero entre 1 y", len(lines))

primeros.writelines(lines[:num])
ultimos.writelines(lines[num:])
