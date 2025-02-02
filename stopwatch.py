n = int(input())

if n % 2 != 0:
    print("still running")
    exit()

start = 0
total = 0
for i in range(n):
    if i % 2 == 0:
        start = int(input())
    else:
        total += int(input()) - start

print(total)