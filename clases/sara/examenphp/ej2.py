import random

mat1 = list()
submat1 = list()
mat2 = list()
submat2 = list()

matRes = [[0]*10]*10

for i in range(10):
    for j in range(10):
        submat1.append(random.randint(1, 9))
        submat2.append(random.randint(1, 9))
    mat1.append(submat1.copy())
    mat2.append(submat2.copy())
    submat1.clear()
    submat2.clear()

print("MATRIZ 1")
for i in range(len(mat1)):
    for j in range(len(mat1[i])):
        print(mat1[i][j], end=" | ")
    print()


print("MATRIZ 2")
for i in range(len(mat2)):
    for j in range(len(mat2[i])):
        print(mat2[i][j], end=" | ")
    print()


print("MATRIZ RES")
for i in range(len(matRes)):
    for j in range(len(matRes[i])):
        print(matRes[i][j], end=" | ")
    print()
