top = 0
player = 0

for i in range(5):
    score = [int(x) for x in input().split()]
    if top < sum(score):
        top = sum(score)
        player = i + 1

print(player, top)