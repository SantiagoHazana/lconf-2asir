num = float(input("Ingrese un monto: "))
ivas = [3, 16, 30, 72]
for i in ivas:
    print("El IVA de", i, "% es:", num*i/100)
