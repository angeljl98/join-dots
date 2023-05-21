import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
chars="123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
h, w = [int(i) for i in input().split()]
table=[]
points=[]
for i in range(h):
    row = list(input())
    table.append(row)
    for col,c in enumerate(row):
        if c!=".":
            points.append((c,i,col))

points.sort(key=lambda x:chars.index(x[0]))
#print(points,file=sys.stderr)

_,prevRow,prevCol=points.pop(0)
table[prevRow][prevCol]="o"
for _,row,col in points:
    table[row][col]="o"
    #print(f"joining {prevRow}-{prevCol} to {row}-{col}",file=sys.stderr)
    if row==prevRow:
        # horizontal
        #print(f"horizontal {prevRow}-{prevCol} to {row}-{col}",file=sys.stderr)
        c1=min(col,prevCol)
        c2=max(col,prevCol)
        r=row
        for c in range(c1+1,c2):
            if table[r][c]==".":table[r][c]="-"
            elif table[r][c]=="|":table[r][c]="+"
            elif table[r][c] in "/\\X" :table[r][c]="*"
    elif col==prevCol:
        # vertical
        #print(f"vertical {prevRow}-{prevCol} to {row}-{col}",file=sys.stderr)
        r1=min(row,prevRow)
        r2=max(row,prevRow)
        c=col
        for r in range(r1+1,r2):
            if table[r][c]==".":table[r][c]="|"
            elif table[r][c]=="-":table[r][c]="+"
            elif table[r][c] in "/\\X" :table[r][c]="*"
    else:
        # diagonal
        if prevCol>col:
            c1=col
            c2=prevCol
            r1=row
            r2=prevRow
        else:
            c2=col
            c1=prevCol
            r2=row
            r1=prevRow

        if r1<r2:
            symbol="\\"
            dir=1
        else:
            symbol="/"
            dir=-1
        #print(f"diagonal {r1}-{c1} to {r2}-{c2} {symbol}",file=sys.stderr)
        for i in range(1,c2-c1):
            c=c1+i
            r=r1+i*dir
            if table[r][c]==".":table[r][c]=symbol
            elif table[r][c] in "\\/":table[r][c]="X"
            elif table[r][c] in "|-x" :table[r][c]="*"
    prevRow=row
    prevCol=col
for row in table:
    print("".join(row).replace("."," ").rstrip())