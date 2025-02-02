t = int(input())

for i in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    min = nums[0]
    max = nums[n-1]

    print((max - min) * 2)