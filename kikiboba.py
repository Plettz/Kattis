word = input()

k = 0
b = 0

for x in word:
    if x == 'k':
        k = k + 1
        
    if x == 'b':
        b = b + 1
        
if k == 0 and b == 0:
    print("none")
elif k > b:
    print("kiki")
elif b > k:
    print("boba")
elif k is b:
    print("boki")
