num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el primer numero: "))
num3 = float(input("Introduce el primer numero: "))

if (num1 > num2) and (num1 > num3):
    print("El mayor numero es", num1)
elif (num2 > num1) and (num2 > num3):
    print("El mayor numero es", num2)
elif (num3 > num1) and (num3 > num2):
    print("El mayor numero es", num3)
else:
    print("Alguna otra opcion")
