num = int(input())

readings = list(map(int, input().split()))

total = 0

for x in range(num):
    total += readings[x]

print(total//num)