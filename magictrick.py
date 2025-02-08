word = list(input())
check = set()

for i in range(len(word)):
    if word[i] in check:
        print("0")
        exit()
    else:
        check.add(word[i])

print("1")