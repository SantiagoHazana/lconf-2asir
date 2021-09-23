# meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
# print(meses[2])
#
# meses[2] = "Marzoooo"
# print(meses[2])
#
#
# for i in meses:
#     print(i)
#
# print(len(meses))
#
# meses.insert(len(meses), "Otro")
# meses.insert(2, "Otro")
# print(meses)
#
# meses.sort()
# print(meses)
#
# meses.sort(reverse=True)
# print(meses)

# valores = [[0] * 3] * 2
#
# for f in range(0, 2):
#     a = int(input("A: "))
#     b = int(input("B: "))
#     c = int(input("C: "))
#
#     valores[f] = [a, b, c]
#
# print(valores)

# def createGenerator(x):
#     mylist = range(x)
#     for i in mylist:
#         yield i * i
#
#
# mygenerator = createGenerator(5)
#
# for i in mygenerator:
#     print(i)


# def primo(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# print(primo(11))

def get_next_multiple(n):
    x = 1
    while x < 50:
        if x % n == 0:
            yield x
        x = x + 1


multi = get_next_multiple(2)
for i in multi:
    print(i)
