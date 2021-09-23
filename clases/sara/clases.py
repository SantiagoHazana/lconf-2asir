class Persona:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = 0

    def say_my_name(self):
        print(self.name, self.surname, ", edad:", self.age)


sara = Persona("Sara", "Aguilera")
# print(sara.age)
# sara.age = 26
# print(sara.age)
# sara.say_my_name()


# herencia
class Alumno(Persona):
    # estoy sobreescribiendo el constructor del padre
    def __init__(self, name, surname, iddddddddddddddd):
        super().__init__(name, surname)  # llamo al constructor del padre
        # Persona.__init__(name, surname)  # llamo al constructor del padre
        self.id = iddddddddddddddd

    def give_my_info(self):
        print(self.name, self.surname, ", id:", self.id)

    def algo(self):
        pass  # todo hacer el metodo


# santi = Alumno("Santi", "Hazaña", 69)
# santi.say_my_name()
# santi.give_my_info()
# santi.algo()
