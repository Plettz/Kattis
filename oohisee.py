def check(i, j, treasure):
    if treasure[i+1][j] == '0':
        return False
    elif treasure[i-1][j] == '0':
        return False
    elif treasure[i+1][j+1] == '0':
        return False
    elif treasure[i-1][j+1] == '0':
        return False
    elif treasure[i+1][j-1] == '0':
        return False
    elif treasure[i-1][j-1] == '0':
        return False
    elif treasure[i][j+1] == '0':
        return False
    elif treasure[i][j-1] == '0':
        return False
    else:
        return True

rows, cols = map(int, input().split())

treasure = [[0] * cols for i in range(rows)]

found = list(list())

for i in range(rows):
    tmp = input()
    for j in range(cols):
        treasure[i][j] = tmp[j]

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if treasure[i][j] == '0':
            if check(i,j,treasure):
                found.append([i+1,j+1])

if len(found) > 1:
    print(f"Oh no! {len(found)} locations")
elif len(found) == 0:
    print("Oh no!")
else:
    print(found[0][0], found[0][1])    
