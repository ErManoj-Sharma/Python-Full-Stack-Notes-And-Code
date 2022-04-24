class Radio:
    def turnon(self,x):
        if(x==1):
            print('radio is on ')
        else:
            print('radio is off')
class Car:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.r=Radio()

c1=Car(40,100)
print(c1.min)
print(c1.max)
c1.r.turnon(1)