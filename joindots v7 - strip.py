import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

h, w = [int(i) for i in input().split()]
alpha = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
g = ''
for i in range(h):g+=input()
o = []
p = []
j = 0
while j < len(alpha) and alpha[j]in g:
    p.append([*divmod(g.find(alpha[j]),w)])
    j += 1
for i in range(h):
    o.append([])
    for j in range(w):
        o[-1].append(' ')
y,x = p.pop(0)
o[y][x]='o'
while len(p):
    Y,X = p.pop(0)
    o[Y][X]='o'
    dY = Y-y
    dX = X-x
    dy = (dY>0)-(dY<0)
    dx = (dX>0)-(dX<0)
    if dy==-dx:
        c = '/'
        x += dx
        y += dy
        while X-x:
            if o[y][x]==' ':o[y][x]=c
            elif o[y][x]=='\\':o[y][x]='X'
            else:o[y][x]='*'
            x += dx
            y += dy
    elif dy==dx:
        c = '\\'
        x += dx
        y += dy
        while X-x:
            if o[y][x]==' ':o[y][x]=c
            elif o[y][x]=='/':o[y][x]='X'
            else:o[y][x]='*'
            x += dx
            y += dy
    elif dy:
        c = '|'
        y += dy
        while Y-y:
            if o[y][x]==' ':o[y][x]=c
            elif o[y][x]=='-':o[y][x]='+'
            else:o[y][x]='*'
            y += dy
    elif dx:
        c = '-'
        x += dx
        while X-x:
            if o[y][x]==' ':o[y][x]=c
            elif o[y][x]=='|':o[y][x]='+'
            else:o[y][x]='*'
            x += dx
[print(''.join(['.',*i]).strip()[1:])for i in o]