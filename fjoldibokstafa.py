letters = 0
readIn = input()

for c in readIn:
    if c.isalpha():
        letters += 1
        
print(letters)
