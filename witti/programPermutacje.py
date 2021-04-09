import numpy
import re
import itertools
import timeit
start = timeit.default_timer()
p = []
w = []
d = []
with open("dataPY.txt","r") as data:
    for n in range(4):
        s=(data.readline()).split()
        p.append(int(s[0]))
        w.append(int(s[1]))
        d.append(int(s[2]))

wektorIndeksow=range(0,len(p))
listaPermutacji=list(itertools.permutations(wektorIndeksow))
sumaCzasuMin = 99999999
sumaKarMin = 99999999
permutacjaMin = ()
for permutacja in listaPermutacji:
    sumaKar=0
    sumaCzasu=0
    for proces in permutacja:
        sumaCzasu+=p[proces]
        sumaKar=sumaKar + max(0, (sumaCzasu-d[proces])*w[proces])
        
    if sumaKar<sumaKarMin:
        permutacjaMin = permutacja
        sumaCzasuMin = sumaCzasu
        sumaKarMin = sumaKar
        numerPermutacji = listaPermutacji.index(permutacja)
print(permutacjaMin)
print(sumaCzasuMin)
print(sumaKarMin)
stop = timeit.default_timer()
print('Time: ', stop - start)