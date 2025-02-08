n = int(input())

min = 0
curr = 0

for i in range(n):
    l, b = map(int, input().split())
    curr -= l
    curr += b
    if min < curr:
        min = curr

print(min)