import numpy
import re
p = []
w = []
d = []
with open("dataPY.txt","r") as data:
    for n in range(10):
        s=(data.readline()).split()
        p.append(int(s[0]))
        w.append(int(s[1]))
        d.append(int(s[2]))

n=len(p)
N=1<<n
F=[0]
ListaL=[[]]

for set in range(1,N):
    sumaP=0
    b=1
    c=0
    #####zliczanie sumy####
    for j in range(n):
        if (set&b):
            c=c+p[j]
        b*=2
    ####DZIALA!!!!!###
    F.append(99999999)
    ListaL.append([])
    b=1
    for j in range(n):
        if (set&b):
            if (F[set]>F[set - b] + w[j] * max(c - d[j], 0)):
                pomocniczy=ListaL[set-b].copy()
                pomocniczy.append(j+1)
                ListaL[set]=pomocniczy.copy()
                F[set]=F[set - b] + w[j] * max(c - d[j], 0)
        b=b*2
print("Jedna z najkrótszych kombinacji: ",ListaL[-1])
print("O długości: ",F[-1])







