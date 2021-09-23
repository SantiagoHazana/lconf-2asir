# las clases u objetos buscan representar conceptos o cosas de la realidad con sus caracteristicas y funcionalidades
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


dani = Persona("Daniel", "Sanchez")  # creamos una persona que se llama Daniel Sanches y tiene edad 0
# dani.decirMiInfo()
# dani.cambiarEdad(20)
# dani.decirMiInfo()
#
santi = Persona("Santiago", "Hazaña")
# santi.decirMiInfo()


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


aluDani = Alumno(69420, "Daniel", "Sanchez")
# aluDani.decirMiInfo()
aluSanti = Alumno(666, "Santiago", "Hazaña")

# meto las dos personas y los dos alumnos en una lista
listado = [dani, santi, aluDani, aluSanti]
# mostrar toda la info de todas las personas en el listado
for i in listado:
    print("------------------")
    i.decirMiInfo()

# 1. Crear una clase Figura que tendra un solo atributo llamado 'color'. Tendra una sola funcion que dira la informacion
# de la figura de la siguiente manera: "Figura de color: 'color'"
# 2. Crear la clase Circulo que hereda de Figura, debera tener tres atributos llamados 'radio', 'area', 'perimetro',
# los dos ultimo se ponen por defecto a 0. Luego tendra dos funciones para calcular y guardar el valor del area y
# del perimetro. Por ultimo la funcion que nos dira la informacion del circulo de la siguiente
# manera: "Circulo de radio: 'radio', area: 'area' y permimetro: 'perimetro'"
# 3. Crear la clase Tringulo que hereda de Figura, debera tener dos atributos llamados 'altura' y 'area',
# el area por defecto a 0. Luego tendra una funcion para calcular y guardar el valor del area. Por ultimo la funcion
# que nos dira la informacion del circulo de la siguiente manera: "Triangulo de altura: 'altura'y area: 'area'"
