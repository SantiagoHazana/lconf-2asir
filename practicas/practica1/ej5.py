import math

a = float(input("Introduzca el valor de a: "))
b = float(input("Introduzca el valor de b: "))
c = float(input("Introduzca el valor de c: "))
sqrt = (b * b) - (4 * a * c)
if sqrt < 0:
    print("No hay raices reales")
elif sqrt == 0:
    x = (-b) / (2*a)
    print("Unica raiz =", x)
else:
    x1 = (-b + math.sqrt(sqrt)) / (2 * a)
    x2 = (-b - math.sqrt(sqrt)) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)
