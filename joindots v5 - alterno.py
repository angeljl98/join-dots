from collections import defaultdict

h, w = map(int, input().split())
dots = [(dot_id, (x, y)) for y in range(h) for x, dot_id in enumerate(input()) if dot_id != '.']
dots = [(x, y) for _, (x, y) in sorted(dots)]

picture = defaultdict(list, {dot:['o'] for dot in dots})
for i in range(len(dots) - 1):
    x1, y1 = dots[i]
    x2, y2 = dots[i + 1]
    if x1 != x2 and y1 != y2:
        symbol = '/\\'[((x2 - x1) > 0) == ((y2 - y1) > 0)]
    else:
        symbol = '|-'[x1 != x2]

    dx = 0 if (x2 - x1) == 0 else abs(x2 - x1) / (x2 - x1)
    dy = 0 if (y2 - y1) == 0 else abs(y2 - y1) / (y2 - y1)

    for i in range(max(abs(x2 - x1), abs(y2 - y1)) - 1):
        x1 += dx
        y1 += dy
        picture[(x1, y1)].append(symbol)

for loc in picture:
    if len(picture[loc]) > 1:
        needed_substitution = ''.join(sorted(picture[loc]))
        picture[loc] = [{'-|': '+', '/\\': 'X'}.get(needed_substitution, '*')]

for y in range(h):
    print(''.join([picture[(x, y)][0] if (x, y) in picture else ' ' for x in range(w)]).rstrip())