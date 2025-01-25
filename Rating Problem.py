judges, voted = [int(x) for x in input().split()]

max = []
min = []

for i in range(judges):
    if i < voted:
        n = int(input())
        max.append(n)
        min.append(n)
    else:
        max.append(3)
        min.append(-3)

print(sum(min) / judges, sum(max) / judges)