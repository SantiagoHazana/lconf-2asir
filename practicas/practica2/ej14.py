total = 0
num = float(input("Intorduce un numero: "))
cont = 0
while num != 0:
    total += num
    cont += 1
    num = float(input("Intorduce un numero: "))
print(total/cont)
