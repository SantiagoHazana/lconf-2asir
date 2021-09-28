n1 = int(input("Introduce un numero: "))
n2 = int(input("Introduce otro numero: "))
if n1 > n2:
    x = n2
    n2 = n1
    n1 = x

for i in range(n1, n2+1):
    print(i, "^2 = ", i*i, sep="")
