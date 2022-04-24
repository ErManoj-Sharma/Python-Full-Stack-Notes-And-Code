class Brain:
    def getbrain(self):
        print('brain is still working ')

class Car:
    def __init__(self,cname):
        self.cname=cname
    def getcar(self):
        print('car is runnig ')

class Person:
    def __init__(self,pname):
        self.pname=pname
        self.b=Brain()
        print('person is ready ')
        print('brain is ready ')
        self.c1=''
    def hascar(self,c):
        self.c1=c
        print('person purhcase car')

p=Person('Manoj')
c=Car('BMW')
p.hascar(c)
print(p.pname)
p.b.getbrain()
print(p.c1.cname)
p.c1.getcar()
print(Brain.mro())
print()
del p           # deleting main object
print('deleting main object')
print(c.cname)
c.getcar()
# p.b.getbrain()