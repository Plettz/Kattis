while True:
    n = int(input())
    if n == -1:
        break

    totalMiles = 0
    prevTime = 0

    for i in range(n):
        s, t = [int(x) for x in input().split()]
        if totalMiles == 0:
            totalMiles = s * t
            prevTime = t
        else:
            totalMiles += (t - prevTime) * s
            prevTime = t

    print(totalMiles, "miles")