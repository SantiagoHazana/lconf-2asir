num = int(input("Introduce un numero: "))
exp = int(input("Introduce el exponente: "))
total = 1
for i in range(exp):
    total *= num
print(total)
