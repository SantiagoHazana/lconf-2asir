file_name = ""

try:
    file_name = input("Ingrese el nombre de un fichero: ")
    file = open(file_name, 'x')
    file.close()
except FileExistsError:
    print("El fichero existe, se utilizara")


file = open(file_name, 'r')
