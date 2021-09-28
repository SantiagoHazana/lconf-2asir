num = int(input("Introduce un numero"))
pos = 0
neg = 0
while num != 0:
    if num > 0:
        pos += 1
    else:
        neg += 1

print("Positivos:", pos)
print("Negativos:", neg)
