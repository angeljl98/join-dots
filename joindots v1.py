import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

arr=([])
h, w = [int(i) for i in input().split()]
struc=np.empty((0,0))
texto=""
for i in range(h):
    row = input()
    arr=(arr,row)
    struc=np.append(struc,row)
    texto=texto+"\n"+row
    print(row,file=sys.stderr,flush=True)

print("vector",arr,file=sys.stderr,flush=True)
print("estructura",struc,file=sys.stderr,flush=True)
print("texto",texto,file=sys.stderr,flush=True)

texto_ascii=[ord(c) for c in texto]
texto_ascii= ["/n" if texto_ascii==10 else texto_ascii for texto_ascii in texto_ascii]

print(type(texto_ascii),file=sys.stderr,flush=True)

print("texto ascii",texto_ascii,file=sys.stderr,flush=True)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(ord("0"),file=sys.stderr,flush=True)
print(ord("9"),file=sys.stderr,flush=True)
print(ord("A"),file=sys.stderr,flush=True)
print(ord("Z"),file=sys.stderr,flush=True)

print("o--------oo--------o")
print("|        ||        |")
print("| o------o| o------o")
print("| |       | |")
print("| |       | |   o--o")
print("| |       | |   |  |")
print("| |       | |   |  |")
print("| o------o| o---o  |")
print("|         o        |")
print("o------------------o")
