class farmer:
    rate=5
    def __init__(self,principle,time):
        self.principle=principle
        self.time=time

    def calcsi(self):
        si=self.principle*self.time*farmer.rate/100
        print(si)

f1=farmer(10000,2)
f2=farmer(20000,3)
f3=farmer(30000,10)

f1.calcsi()
f2.calcsi()
f3.calcsi()

