r = list(input())

p = 0
n = 1
a = 0
b = 0
win = 11

while True:
    try:
        player = r[p]
        points = r[n]
    except:
        break

    if player == "A":
        a += int(points)
    elif player == "B":
        b += int(points)
    
    if a == (win - 1) and b == (win - 1):
        win += 1
    elif a >= win:
        print("A")
        break
    elif b >= win:
        print("B")
        break

    p += 2
    n += 2