n = int(input())

knots = map(int, input().split())

learned = map(int, input().split())

print((set(knots) - set(learned)).pop())