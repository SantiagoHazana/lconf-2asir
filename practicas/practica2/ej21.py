num = int(input("Introduce un numero: "))
for i in range(2, num//2):
    if num % i == 0:
        print("No es un numero primo")
        exit(0)

print("Es un numero primo")
