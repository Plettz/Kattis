n, a, b = map(int, input().split())

fizz = 0
buzz = 0
fizzbuzz = 0

for i in range(n):
    i += 1
    if (i % a == 0) and (i % b == 0):
        fizzbuzz += 1
    elif (i % a == 0):
        fizz += 1
    elif (i % b == 0):
        buzz += 1

print(fizz, buzz, fizzbuzz)