class Persona:
    # Constructor, inicializa/crea nuestra clase con los valores que pidamos
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = 0

    def cambiarEdad(self, edad):
        self.edad = edad

    def decirMiInfo(self):
        print(self.nombre, self.apellido, "y tengo", self.edad, "años")


class Alumno(Persona):

    def __init__(self, matricula, nombre, apellido):  # constructor de Alumno, pide lo necesario de alumno Y de persona
        super().__init__(nombre, apellido)  # llamado al constructor del padre (Persona)
        # Persona.__init__(nombre, apellido)  # llamado al constructor del padre (Persona)
        self.matricula = matricula

    # Redefinimos la funcion del padre, utilizando la del padre
    def decirMiInfo(self):
        super().decirMiInfo()  # llamar a la misma funcion del padre, para utilizar su contenido
        print("Mi matricula es", self.matricula)

    # esta es una funcion que SOLO la tiene alumno
    def infoAlumno(self):
        print("Alumno", self.matricula)


def menor(num1, num2, num3):
    print(min(num1, num2, num3))


def menor2(*nums):
    menor = nums[0]
    for i in nums:
        if i < menor:
            menor = i

    print(menor)
