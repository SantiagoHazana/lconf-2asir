import random

total = 0
for i in range(5):
    rand = random.randint(1, 10)
    total += rand
    print(rand, end=" ")
    if i != 4:
        print(" + ", end="")

print(" =", total)
