import sys
import math
import numpy as np

class Dot:
  x: int
  y: int
  i: int
  val: int

  def __init__(self, x: int, y: int, i: int, val: int):
    self.x = x
    self.y = y
    self.i = i
    self.val = val

  def __repr__(self):
    return f"Dot(x={self.x}, y={self.y}, i={self.i}, val={self.val})"

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

arr=([])
h, w = [int(i) for i in input().split()]
struc=np.empty((0,0))
texto=""
texto_sn=""
for i in range(h):
    row = input()
    arr=(arr,row)
    struc=np.append(struc,row)
    texto=texto+"\n"+row
    texto_sn=texto_sn+row
    #print(row,file=sys.stderr,flush=True)

#print("vector",arr,file=sys.stderr,flush=True)
#print("estructura",struc,file=sys.stderr,flush=True)
print("texto",texto,file=sys.stderr,flush=True)

texto_ascii=[ord(c) for c in texto]
texto_ascii= ["/n" if texto_ascii==10 else texto_ascii for texto_ascii in texto_ascii]

texto_ascii_sn=[ord(c) for c in texto_sn]

#print(type(texto_ascii),file=sys.stderr,flush=True)

#print("texto ascii",texto_ascii,file=sys.stderr,flush=True)
#print("texto ascii sin n",texto_ascii_sn,file=sys.stderr,flush=True)

diccionario1 = {
  "x": 0,
  "y": 0,
  "i": 0,
  "val": 0,
}

diccionario=list()
diccionario_pts=list()
punto=Dot(0,0,0,0)

ct1=0

for m in range(h):
    for n in range(w):
        diccionario.append(Dot(m,n,ct1,texto_ascii_sn[ct1]))
        if texto_ascii_sn[ct1]!=46:
            diccionario_pts.append(diccionario[ct1])
        punto.x=m
        punto.y=n
        punto.i=ct1
        punto.val=texto_ascii_sn[ct1]
        ct1=ct1+1
# ordenar
diccionario_pts=sorted(diccionario_pts, key=lambda Dot : Dot.val)

if __name__ == "__main__":
    #print("diccionario:", diccionario, file=sys.stderr, flush=True)
    print("diccionario puntos::", len(diccionario_pts), file=sys.stderr, flush=True)

#recorrido de puntos
ct1=0
for ct1 in range(len(diccionario_pts)-1): 
    diccionario_pts[ct1].val=111
    diccionario_pts[ct1+1].val=111
    #selección del punto
    x1=diccionario_pts[ct1].x
    x2=diccionario_pts[ct1+1].x
    y1=diccionario_pts[ct1].y
    y2=diccionario_pts[ct1+1].y
    #
    #ir a la derecha
    if y2>y1 and x1==x2:
        for i in range(y1,y2):
            for t in diccionario:
                if t.y==i and t.x==x1:
                    if t.val==46:
                        t.val=45
                    if t.val==124:
                        t.val=43
    #ir a la izquierda
    if y1>y2 and x1==x2:
        for i in range(y2,y1):
            for t in diccionario:
                if t.y==i and t.x==x1:
                    if t.val==46:
                        t.val=45
                    elif t.val==124:
                        t.val=43
                    elif t.val==92:
                        t.val=42
    # abajo
    if x2>x1 and y1==y2:
        for i in range(x1,x2):
            for t in diccionario:
                if t.x==i and t.y==y1:
                    if t.val==46:
                        t.val=124
                    elif t.val==45:
                        t.val=43
    # arriba
    if x1>x2 and y1==y2:
        for i in range(x2,x1):
            for t in diccionario:
                if t.x==i and t.y==y1:
                    if t.val==46:
                        t.val=124
                    elif t.val==45:
                        t.val=43
    
    #diagonal abajo a la izquierda
    if x2>x1 and y1>y2:
        #print("depurador*:", x1,y1,x2,y2, file=sys.stderr, flush=True)
        d1=0
        for cu1 in range(0,2):
            for t in diccionario:
                if t.x==x2:
                    break
                if t.x==x1+d1 and t.y==y1-d1:
                    if t.val==46:
                        t.val=47
                        #print("depurador:","pt1:",x1,y1,"pt2",x2,y2, file=sys.stderr, flush=True)
                        #print("depurador*:", x1,y1,x2,y2, file=sys.stderr, flush=True)
                    elif t.val==92:
                        t.val=88
                    elif t.val==43:
                        t.val=42
                    elif t.val==124 or t.val==45:
                        t.val=42
                    d1=d1+1
                    cu1=0
    # diagonal abajo a la derecha
    if x2>x1 and y2>y1:
        #print("depurador*:", x1,y1,x2,y2, file=sys.stderr, flush=True)
        d1=0
        for cu1 in range(0,2):
            for t in diccionario:
                if t.x==x2:
                    break
                if t.x==x1+d1 and t.y==y1+d1:
                    if t.val==46:
                        t.val=92
                        #print("depurador:","pt1:",x1,y1,"pt2",x2,y2, file=sys.stderr, flush=True)
                        #print("depurador*:", x1,y1,x2,y2, file=sys.stderr, flush=True)
                    elif t.val==47:
                        t.val=88
                    elif t.val==43:
                        t.val=42
                    elif t.val==124 or t.val==45:
                        t.val=42
                    d1=d1+1
                    cu1=0

    # diagonal arriba a la derecha
    if x2<x1 and y2>y1:
        #print("depurador*+:", x1,y1,x2,y2, file=sys.stderr, flush=True)
        d1=0
        for cu1 in range(0,2):
            for t in diccionario[::-1]:
                if t.x==x2:
                    break
                if t.x==x1-d1 and t.y==y1+d1:
                    if t.val==46:
                        t.val=47
                        #print("depurador:","pt1:",x1,y1,"pt2",x2,y2, file=sys.stderr, flush=True)
                        #print("depurador*:", x1,y1,x2,y2, file=sys.stderr, flush=True)
                    elif t.val==92:
                        t.val=88
                    elif t.val==43:
                        t.val=42
                    elif t.val==124 or t.val==45:
                        t.val=42
                    d1=d1+1
                    cu1=0

    # diagonal arriba a la izquierda
    if x2>x1 and y2>y1:
        #print("depurador+*:", x1,y1,x2,y2, file=sys.stderr, flush=True)
        d1=0
        for cu1 in range(0,2):
            for t in diccionario[::-1]:
                if t.x==x1+d1 and t.y==y1+d1:
                    if t.val==46:
                        t.val=92
                        #print("depurador:","pt1:",x1,y1,"pt2",x2,y2, file=sys.stderr, flush=True)
                        #print("depurador*:", x1,y1,x2,y2, file=sys.stderr, flush=True)
                    elif t.val==47:
                        t.val=88
                    elif t.val==43:
                        t.val=42
                    elif t.val==124 or t.val==45:
                        t.val=42
                    d1=d1+1
                    cu1=0


    # diagonal arriba a la izquierda 2
    if x2<x1 and y2<y1:
        #print("depurador+*:", x1,y1,x2,y2, file=sys.stderr, flush=True)
        d1=0
        for cu1 in range(0,2):
            for t in diccionario[::-1]:
                #if t.x==x2:
                #    cu1=2
                if t.x==x1-d1 and t.y==y1-d1:
                    if t.x== x2:
                        break
                    if t.val==46:
                        t.val=92
                        #print("depurador:","pt1:",x1,y1,"pt2",x2,y2, file=sys.stderr, flush=True)
                        #print("depurador*:", x1,y1,x2,y2, file=sys.stderr, flush=True)
                    elif t.val==47:
                        t.val=88
                    elif t.val==43:
                        t.val=42
                    elif t.val==124 or t.val==45:
                        t.val=42
                    d1=d1+1
                    cu1=0

#print("diccionario:", diccionario, file=sys.stderr, flush=True)
#print("diccionario puntos:", diccionario_pts, file=sys.stderr, flush=True)

out=""
ct3=0
for t2 in diccionario:
    out=out+chr(t2.val)
    ct3=ct3+1
    if ct3==w:
        out=out+"\n"
        ct3=0   

print("ancho:",w,"\n"+"salida \n"+out,file=sys.stderr,flush=True)

print("0:",ord("0"),file=sys.stderr,flush=True)
print("9:",ord("9"),file=sys.stderr,flush=True)
print("A:",ord("A"),file=sys.stderr,flush=True)
print("Z:",ord("Z"),file=sys.stderr,flush=True)
print("o:",ord("o"),file=sys.stderr,flush=True)
print(".:",ord("."),file=sys.stderr,flush=True)
print("-:",ord("-"),file=sys.stderr,flush=True)
print("|:",ord("|"),file=sys.stderr,flush=True)
print("\\:",ord("\\"),file=sys.stderr,flush=True)
print("/:",ord("/"),file=sys.stderr,flush=True)
print("+:",ord("+"),file=sys.stderr,flush=True)
print("X:",ord("X"),file=sys.stderr,flush=True)
print("*:",ord("*"),file=sys.stderr,flush=True)
print(len(texto_ascii_sn),file=sys.stderr,flush=True)
print(h,file=sys.stderr,flush=True)
print(w,file=sys.stderr,flush=True)

texto_ascii_snbk=[]
for i in range(len(texto_ascii_sn)):
    p=texto_ascii_snbk.append(texto_ascii_sn[i])

t=texto_ascii_sn.sort()
vector_bandera=[]

for m in range(len(texto_ascii_sn)):
    if texto_ascii_sn[m] != 46:
        p=vector_bandera.append(texto_ascii_sn[m])

#print("texto ordenado ascii:vector bandera",vector_bandera,file=sys.stderr,flush=True)

LVec=len(texto_ascii_sn)
Ancho=w
Largo=h
T0=""
ct1=0
ct2=0
v1=vector_bandera[ct1]

#coordenada del primer punto
p=0
dot1=Dot(0,0,0,vector_bandera[p])
dot2=Dot(0,0,0,vector_bandera[p+1])
pos1=0
pos2=0
ct1=0
for m in range(h):
    for n in range(w):
        if texto_ascii_snbk[ct1]==dot1.val:
            dot1.i=ct1
            dot1.x=m
            dot1.y=n
        if texto_ascii_snbk[ct1]==dot2.val:
            dot2.i=ct1
            dot2.x=m
            dot2.y=n
        ct1=ct1+1

#print("contador",dot1,dot2,ct1,texto_ascii_snbk,file=sys.stderr,flush=True)

# pintar y la trayectoria es del primer cuadrante
# x
p1=dot2.x
p2=dot1.x
p3=dot2.y
p4=dot2.y
if (dot2.x>dot1.x and dot2.y==dot1.y):
    ct1=0
    pos_f=0
    pos_x=0
    pos_y=0
    for m in range(h):
        for n in range (w):
            if m==dot1.x+1 and n==dot1.y:
                pos_f=ct1
                pos_x=n
                pos_y=m
            ct1=ct1+1

solucion=out.replace("."," ")
print(solucion,file=sys.stderr,flush=True)