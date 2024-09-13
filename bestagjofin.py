guests = int(input())

topNum = 0
topName = ""

for x in range(guests):
    input_str = input()
    parts = input_str.split()
    tempName = parts[0]
    tempNum = int(parts[1])

    if topNum < tempNum:
        topNum = tempNum
        topName = tempName

print(topName)
