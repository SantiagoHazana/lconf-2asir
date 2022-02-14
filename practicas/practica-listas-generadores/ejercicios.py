import random

# Ejercicio 1
print("-----Ejercicio 1-----")
nums = random.sample(range(0, 1000), 10)
print(nums)

# Ejercicio 2
print("-----Ejercicio 2-----")
nums.reverse()
print(nums)

# Ejercicio 3
print("-----Ejercicio 3-----")
for i in range(0, len(nums) - 1, 2):
    print(nums[i], end=", ")
print()

# Ejercicio 4
print("-----Ejercicio 4-----")
for i in range(1, len(nums), 2):
    print(nums[i], end=", ")
print()

# Ejercicio 5
print("-----Ejercicio 5-----")
even = 0
odd = 0
for i in range(0, len(nums)):
    if i % 2 == 0:
        even += nums[i]
    else:
        odd += nums[i]

print("Son mayores los pares", even) if even > odd else print("Son mayores los impares", odd)

# Ejercicio 6
print("-----Ejercicio 6-----")
print("El mayor numero es", max(nums), "y esta en la posicion", nums.index(max(nums)))

# Ejercicio 7
print("-----Ejercicio 7-----")

# Ejercicio 8
print("-----Ejercicio 8-----")

# Ejercicio 9
print("-----Ejercicio 9-----")

# Ejercicio 10
print("-----Ejercicio 10-----")

# Ejercicio 11
print("-----Ejercicio 11-----")

# Ejercicio 12
print("-----Ejercicio 12-----")

# Ejercicio 13
print("-----Ejercicio 13-----")

# Ejercicio 14
print("-----Ejercicio 14-----")

# Ejercicio 15
print("-----Ejercicio 15-----")
