import random


class Persona:

    # funcion que inicializa mi clase, pido por parametros lo que yo crea necesario para crearla
    def __init__(self, nombre, apellido):
        # Dentro, me asigno el nombre y apellido que me dan, poniendo una edad aleatoria
        self.nombre = nombre
        self.apellido = apellido
        self.edad = random.randint(15, 50)

    # Esta funcion me permite cambiar mi edad, la puedo utilizar cuando yo quiera
    def cambiar_edad(self, edad):
        self.edad = edad

    # Esta funcion da la informacion de la persona
    def decir_mi_informacion(self):
        print("Soy", self.nombre, self.apellido, "y tengo", self.edad, "años")


daniel = Persona("Daniel", "Sanchez")  # se inicializo una persona con sus datos especificos
daniel.decir_mi_informacion()
daniel.cambiar_edad(21)
daniel.decir_mi_informacion()


# Crear una clase llamada Pedrito que tenga una funcion que me abra un fichero y me ponga las lineas pares en un
# fichero y las imapres en otro fichero. Crear una funcion que me muestre el contenido de ambos ficheros

class Pedrito:

    def dividir_fichero(self, nombre_fichero):
        fichero = open(nombre_fichero, "r")
        pares = open("pares.txt", "w")
        impares = open("impares.txt", "w")
        lineas = fichero.readlines()
        for i in range(len(lineas)):
            # Lo que hago es decir que si la linea es impar en el fichero pero en mi lista es una posicion par,
            # la meto en impares
            if i % 2 == 0:
                impares.write(lineas[i])
            else:
                pares.write(lineas[i])
        fichero.close()
        pares.close()
        impares.close()

    def mostrar_fichero(self, nombre_fichero):
        print("-----------", nombre_fichero, "-----------")
        fichero = open(nombre_fichero, "r")
        print(fichero.read())
        fichero.close()
        print("")


# kaka = Pedrito()
# kaka.dividir_fichero("frases.txt")
# kaka.mostrar_fichero("frases.txt")
# kaka.mostrar_fichero("pares.txt")
# kaka.mostrar_fichero("impares.txt")