num = float(input("Introduce la nota: "))
if 0 >= num < 5:
    print("Suspenso")
elif 5 >= num < 6:
    print("Suficiente")
elif 6 >= num < 7:
    print("Notable")
elif 7 >= num < 9:
    print("Bien")
elif 9 >= num < 10:
    print("Excelente")
elif num == 10:
    print("Sobresaliente")
else:
    print("Nota fuera de rango")
