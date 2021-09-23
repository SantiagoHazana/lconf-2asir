import math
import random


# def num_aleatorios():
#     pares = list()
#     impares = list()
#     for i in range(10):
#         num = random.randint(1, 50)
#         if num % 2 == 0:
#             pares.append(num)
#         else:
#             impares.append(num)
#
#     mostrar_listas(pares, impares)
#
#
# def mostrar_listas(pares, impares):
#     pares.sort()
#     impares.sort(reverse=True)
#     print(pares)
#     print(impares)
#
#
# num_aleatorios()

# phi = (1 + math.sqrt(5)) / 2
# print(phi)
# lista = list()
# for n in range(1, 11):
#     fn = (pow(phi, n) - pow((1 - phi), n)) / math.sqrt(5)
#     lista.append(fn)
#
# print(lista)

def factorial(n):
    fact = 1
    for x in range(1, n + 1):
        fact *= x
    return fact


def fibonnaciSecuancial(n):
    prevPrevNum = 0
    prevNum = 0
    currentNum = 1

    for i in range(1, n):
        print(currentNum)
        prevPrevNum = prevNum
        prevNum = currentNum
        currentNum = prevPrevNum + prevNum

    return currentNum


def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n - 1) + fib(n - 2)


lista = list()
for i in range(20):
    num = fib(i)
    lista.append(num)
    print(num, end=" ")

print()
print(lista)
