import random


class Persona:
    # No son necesarios, se crean en el constructor cuando se utilizan por primera vez
    __nombre = ''
    __apellido = ''
    edad = 0

    def __init__(self, nombre, apellido):
        # Para hacer privadas las cosas se pone doble guion bajo __
        self.__nombre = nombre
        self.__apellido = apellido
        self.edad = random.randint(15, 25)

    def decirMisDatos(self):
        print('Soy', self.nombre, self.apellido, 'y tengo', self.edad, 'años')

    def __algo(self):
        print('Soy privado')


sara = Persona('Sara', 'Aguilera')
sara.decirMisDatos()