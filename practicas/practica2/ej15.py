num = int(input("Introduce un numero: "))
max = num
min = num
while num != 0:
    if num > max:
        max = num
    if num < min:
        min = num
    num = int(input("Introduce un numero: "))

print("El maximo es:", max)
print("El minimo es:", min)
