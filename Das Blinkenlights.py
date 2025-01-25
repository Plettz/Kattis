from math import gcd

p, q, s = [int(x) for x in input().split()]

if (p * q) // gcd(p, q) <= s:
    print("yes")
else:
    print("no")