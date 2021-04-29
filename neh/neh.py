import numpy as np
import re
import itertools
import timeit
start = timeit.default_timer()


with open("daneSolo.txt","r") as data:
    s=(data.readline()).split()
    N = int(s[0]) #zadania
    M = int(s[1]) #maszyny
    dane = np.zeros((N,M))
    for n in  range(N):
        s=(data.readline()).split()
        for m in range(M):
            dane[n,m]=(int(s[m]))
   

def timeToEnd(queue):
    endingTimes=np.zeros((len(queue),M))
    endingTimes[0,0]=dane[0,0]
    for task in range(len(queue)-1):
        task = task +1
        endingTimes[task,0]=dane[queue[task],0]+endingTimes[task-1,0]
    for machine in range(M-1):
        machine = machine +1
        endingTimes[0,machine]=dane[queue[0],machine]+endingTimes[0,machine-1]
    

    for machine in range(M-1):
        machine+=1
        for task in range(len(queue)-1):
            task+=1
            endingTimes[task,machine] = max(endingTimes[task-1,machine],endingTimes[task,machine-1])+dane[task,machine]
    
    time = endingTimes[len(queue)-1,M-1]
    return(time)

myQ=[]
myQH=[]
choosedQ=[]
myTasks=list(range(N))

for task in range(N):
    choosedTask=myTasks[0]
    for leftTask in myTasks:
        if timeToEnd([leftTask]) >timeToEnd([choosedTask]):
            choosedTask=leftTask
   
   
    bigTask=myTasks.pop(myTasks.index(choosedTask))
    choosedQ = myQ.copy()
    choosedQ.insert(0,bigTask)
   
    for position in range(len(myQ)+1):
        myQH = myQ.copy()
        
       
        myQH.insert(position,bigTask)
       
        if timeToEnd(choosedQ)>timeToEnd(myQH):
            choosedQ=myQH.copy()
    myQ=choosedQ.copy()
   
print("Najlepsze rozwiązanie: ",[x+1 for x in myQ])
print("Długosc tego rozwiązania: ",timeToEnd(myQ))