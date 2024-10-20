n = int(input())

v = 7

for x in range(n):
    tmp = input()
    if tmp == "Skru op!" and v != 10:
        v += 1
    elif tmp == "Skru ned!" and v != 0:
        v -= 1

print(v)