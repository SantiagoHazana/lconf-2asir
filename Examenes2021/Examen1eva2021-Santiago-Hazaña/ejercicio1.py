import random


def generateRand():
    numList = []
    while len(numList) != 10:
        rand = random.randint(1, 100)
        if rand % 5 == 0:
            numList.append(rand)

    return numList


def showNumsAndInterval(nums: list):
    print("Numeros de la lista")
    for i in nums:
        print(i, end=" ")
    print()
    nums.sort()
    print("Numeros entre", nums[0], "y", nums[len(nums)-1])
    for i in range(nums[0], nums[len(nums)-1]):
        print(i, end=" ")


showNumsAndInterval(generateRand())
