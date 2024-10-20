translate = {}

while True:
    try:
        e, f = input().split()
    except:
        break

    translate[f] = e

while True:
    try:
        word = input()
    except:
        break

    if word in translate:
        print(translate[word])
    else:
        print("eh")

