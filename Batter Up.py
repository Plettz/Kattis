at_bat = int(input())

hits = [int(x) for x in input().split()]
useful_hits = []

for n in hits:
    if n == -1:
        at_bat -= 1
    else:
        useful_hits.append(n)


print(sum(useful_hits) / at_bat)