def fibonacci(n):
    fib = [0, 1]
    i = 1
    while fib[i]+fib[i-1] < n:
        i += 1
        fib.append(fib[i-1] + fib[i-2])

    return fib


fib1000 = fibonacci(1000)
print(fib1000)
for i in fib1000:
    print(i, end="  ")

print()
fib100 = fibonacci(100)
print(fib100)

for i in fib100:
    print(i, end=", ")

print()