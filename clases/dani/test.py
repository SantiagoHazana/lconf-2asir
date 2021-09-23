# import math
# class Figura:
#     def __init__(self, color):
#         self.color = color
#
#     def decirInfoFigura(self):
#         print("Figura de color: ", self.color)
#
# class Circulo(Figura):
#
#     def __init__(self, color, radio):
#         super(Circulo, self).__init__(color)
#         self.radio = radio
#         self.area = 0
#         self.perimetro = 0
#
#     def calcularArea(self):
#         self.area = math.pi*self.radio*self.radio
#
#     def calcularPerimetro(self):
#         self.perimetro = math.pi*2*self.radio
#
#     def decirInfoFigura(self):
#         print("Circulo de radio", self.radio, "perimetro", self.perimetro, "area", self.area)
#
# # class Triangulo(Figura):
# #

try:
    fileName = input("Nombre fichero: ")
    file = open(fileName, "r")
except FileNotFoundError:
    print("El fichero no existe")
