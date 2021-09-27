num = int(input("Introduce un numero: "))
while num > 1:
    num = num % 2
print("El numero es par" if num == 0 else "El numero es impar")
