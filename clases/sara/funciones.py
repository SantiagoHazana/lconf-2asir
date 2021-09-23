def sumar(num1=2, num2=5):
    res = num1 + num2 + sumar2(num1, num2, 5)
    print(res)


def sumar2(num1, num2, num3):
    return num1 + num2 + num3


sumar()
sumar(30, 5)

x = y = z = 7

print(7 // 2)
print(7 / 2)
