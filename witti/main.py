import numpy
import re
p = []
w = []
d = []
with open("data.txt","r") as data:
    for n in range(10):
        s=(data.readline()).split()
        p.append(s[0])
        w.append(s[1])
        d.append(s[2])





