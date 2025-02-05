n = int(input())

helped = False

curr = int(input())
if curr != 1:
    print("1")
    
for i in range(n):
    next = int(input())
    if curr + 1 != next:
        print(curr + 1)
        helped = True
    curr = next

if not helped:
    print("good job")