class proces:
    def __init__(self,prepare,mill,cool):
        self.p = prepare #przygotowanie
        self.q = mill #obrobka
        self.r = cool #stygniecie
    wage =  0
    start = 0
    endMilling = start + q
    endProces = endMilling + r
    def printStart(self):
        print(self.start)
    def setWage(self,parP,parQ,parR):
        self.wage = parP*self.p + parQ*self.q + parR*self.r
class procesList:
    def __init__(self):
       self.mainList=[]
       self.duration = 0
    def addProcesToList(self,proces):
        self.mainList.append(proces)
    def sortListByWage(self,parP,parQ,parR):
        for singleProces in self.mainList:
            singleProces.setWage(parP,parQ,parR)
        self.mainList.sort(key=lambda singleProces: singleProces.wage)


y=procesList()
y.mainList.clear()
with open('./dane.txt','r') as reader:
    for line in reader:
        p = int(line.split(" ")[0])
        q = int(line.split(" ")[1])
        r = int(line.split(" ")[2])
        x = proces(p,q,r)
        y.addProcesToList(x)
y.sortListByWage(1,0,0)
for singleProces in y.mainList:
    print(singleProces.p) 

test = proces(10,10,10)
print('----------')
print(test.endMilling)
print(test.endProces)
print(test.start)
test.start=20
print(test.endMilling)
print(test.endProces)
print(test.start)
#print(y.mainList)