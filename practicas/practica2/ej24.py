num = int(input("Introduce un numero para calcular su factorial: "))
copyNum = num
total = 1
for i in range(num):
    total *= num
    num -= 1

print("Factorial de",copyNum, "=", total)