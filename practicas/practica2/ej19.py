num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
total = 0
for i in range(num2):
    total += num1

print(num1, "*", num2, "=", total)