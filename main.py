class proces:
    p=0
    q=0
    r=0
    def __init__(self, prepare, mill, cool):
        self.p = prepare  # przygotowanie
        self.q = mill  # obrobka
        self.r = cool  # stygniecie
    wage = 0
    startProces = 0
    startMilling = 0
    endMilling = 0
    endProces = 0
    #________________|   Millling   |_____________________ 
    #|start          |prepare       |endMilling           |endProces
    def printStart(self):
        print(self.start)

    def setWage(self, parP, parQ, parR):
        self.wage = parP*self.p + parQ*self.q + parR*self.r
    def setTSbyProcesStart(self,startProcesTime):
        self.startProces = startProcesTime
        self.startMilling = self.startProces + self.p 
        self.endMilling=self.startMilling+self.q
        self.endProces=self.endMilling+self.r
    def setTSbyMillingStart(self,startMillingTime):
        offset = 0
        if(startMillingTime-self.p<0):
            offset= self.p - startMillingTime
        self.startMilling = startMillingTime + offset
        self.startProces = self.startMilling - self.p 
        self.endMilling = self.startMilling + self.q
        self.endProces=self.endMilling+self.r


class procesList:
    def __init__(self):
        self.mainList = []
        self.duration = 0

    def addProcesToList(self, proces):
        self.mainList.append(proces)

    def sortListByWage(self, parP, parQ, parR):
        parP=parP/max(singleProces.p for singleProces in self.mainList)
        parQ=parQ/max(singleProces.q for singleProces in self.mainList)
        parR=parR/max(singleProces.r for singleProces in self.mainList)
        for singleProces in self.mainList:
            singleProces.setWage(parP, parQ, parR)
        self.mainList.sort(key=lambda singleProces: singleProces.wage)
    
    def setListTimeStamps(self):
        self.mainList[0].setTSbyProcesStart(0)
        #print('-------')
        for idx,singleProces in enumerate(self.mainList[1:]):
            singleProces.setTSbyMillingStart(self.mainList[idx].endMilling)
    def printListTimeStamps(self):
        for singleProces in self.mainList:
            print(singleProces.startProces," ",singleProces.startMilling," ",singleProces.endMilling," ",singleProces.endProces," ")
    def ListTimeLength(self):
        return max(singleProces.endProces for singleProces in self.mainList)



y = procesList()
y.mainList.clear()
with open('./dane.txt', 'r') as reader:
    for line in reader:
        p = int(line.split(" ")[0])
        q = int(line.split(" ")[1])
        r = int(line.split(" ")[2])
        x = proces(p, q, r)
        y.addProcesToList(x)
minmalnaDlugosc = 1000000000000000
minimalP = 10000000000000
minimalQ = 10000000000000
minimalR = 10000000000000
propP = 100
propQ = 100
propR = 100
for idxQ in range(propQ +1):
    for idxR in range(propR +1):
        for idxP in range(propP +1):
            y.sortListByWage(idxP/propP,idxQ/propQ,idxR/propR)
            y.setListTimeStamps()
            if(y.ListTimeLength()<minmalnaDlugosc):
                minmalnaDlugosc = y.ListTimeLength()
                minimalP=idxP/propP
                minimalR=idxR/propR
                minimalQ=idxQ/propQ
print(minmalnaDlugosc)
print(minimalP)
print(minimalQ)
print(minimalR)

#y.printListTimeStamps()
#print(y.ListTimeLength())
# print(y.mainList)
