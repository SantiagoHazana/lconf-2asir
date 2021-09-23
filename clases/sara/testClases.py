# importo todo lo que tengo en el archivo clases.py
import clases

# quiero crear una persona
sara = clases.Persona("Sara", "Aguilera")  # esta sara es de este fichero, testClases.py
sara.say_my_name()

clases.sara.age = 26
clases.sara.say_my_name()  # accedo a la variable sara que esta en el archivo clases.py

santi = clases.Alumno("Santiago", "Hazaña", 666)
santi.give_my_info()
