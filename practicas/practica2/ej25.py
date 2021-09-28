priceInd = int(input("Introduce el precio del producto: "))
for i in range(1, 101):
    if 1 <= i < 15:
        print("Precio por", i, "unidades =", i*priceInd)
    elif 15 <= i < 30:
        print("Precio por", i, "unidades (10% desc) =", i*priceInd*0.9)
    elif 30 <= i < 50:
        print("Precio por", i, "unidades (15% desc) =", i*priceInd*0.85)
    else:
        print("Precio por", i, "unidades (20% desc) =", i*priceInd*0.8)
