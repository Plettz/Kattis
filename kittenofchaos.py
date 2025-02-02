h = {'b': 'd', 'd': 'b', 'p': 'q','q': 'p'}
v = {'b': 'p', 'd': 'q', 'p': 'b','q': 'd'}

s = list(input())
t = list(input())

horizontal = False
vertical = False

for i in range(len(t)):
    if t[i] == 'h':
        horizontal = not horizontal
    elif t[i] == 'v':
        vertical = not vertical
    elif t[i] == 'r':
        horizontal = not horizontal
        vertical = not vertical

if horizontal:
    for i in range(len(s)):
        s[i] = h[s[i]]

    s.reverse()

if vertical:
    for i in range(len(s)):
        s[i] = v[s[i]]

print(''.join(s))