import math


def sumatoria(n):
    nums = []
    k = 1
    while len(nums) != n:
        nums.append((math.sqrt(3) / 4) * (1 + ((3 * math.pow(4, k - 1)) / (math.pow(9, k)))))
        k += 1
    return nums


sumatoriaNums = sumatoria(10)
print("Los 10 primeros valores de la sumatoria son: ")
for i in sumatoriaNums:
    print(i, end=" ")

print()
print("La sumatoria de los 10 valores es:", sum(sumatoriaNums))
