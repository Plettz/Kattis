x1, y1 = input().split()
x2, y2 = input().split()

moves = 0

if x1 != x2:
    moves += 1

if y1 != y2:
    moves += 1

print(moves)
