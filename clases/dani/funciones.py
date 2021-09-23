import random


def menor(num1, num2, num3):
    print(min(num1, num2, num3))


def menor2(*nums):
    menor = nums[0]
    for i in nums:
        if i < menor:
            menor = i

    print(menor)


# menor2(2, 6, 1, -4, 0, 109, 200, -123, 4, 8, -123)


def mensajeBienvenida():
    print("Hola!")


mensajeBienvenida()


def mensajeBienvenidaCustom(mensaje):
    print(mensaje)


mensajeBienvenidaCustom("Bienvenidos!")


def suma(num1, num2):
    resultado = num1 + num2
    return resultado


resSuma = suma(5, 3)
print("La suma es", resSuma)


def caraCruz():
    coin = random.randint(0, 1)
    return coin


print(caraCruz())

