import random

num1 = random.randint(-100, 100)
num2 = random.randint(-100, 100)
print((str(num1) + " > " + str(num2)) if num1 > num2 else str(num2) + " > " + str(num1))
