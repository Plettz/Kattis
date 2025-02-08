t = int(input())

for i in range(t):
    name = list(input())
    abr = list(input())
    sus = False

    for j in range(len(abr)):
        if abr[j] in name:
            continue
        else:
            sus = True

    if not sus:
        print("YES")
    else:
        print("NO")

    
