n = int(input())

for i in range(n):
    b, p = map(float, input().split())
    min = (60.0 / (p / (b - 1)))
    calc = (60.0/ (p / (b )))
    max = (60.0 / (p / (b + 1)))
    print(f"{min:.4f} {calc:.4f} {max:.4f}")