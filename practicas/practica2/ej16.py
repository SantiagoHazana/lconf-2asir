num1 = int(input("Introduzca un numero: "))
num2 = int(input("Introduzca otro numero para dividir el primero: "))
total = 0

while num1 >= num2:
    total += 1
    num1 -= num2

print("Resultado:", total, "con resto", num1)
print("Resultado: ", total, ",", int(num1*100/num2), sep="")
