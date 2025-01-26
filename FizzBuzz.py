x, y, n = [int(x) for x in input().split()]

nums = []

for i in range(n):
    c = i + 1
    if (c % x) == 0 and (c % y) == 0:
        print("FizzBuzz")
    elif (c % x) == 0:
        print("Fizz")
    elif (c % y) == 0:
        print("Buzz")
    else:
        print(c)
