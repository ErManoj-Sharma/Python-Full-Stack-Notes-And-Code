class Cargoplane:
    def takeoff(self):
        print('plane took off')
    def fly(self):
        print('plane flying')
    def land(self):
        print('plane landing')
    def cargo(self):
        print('carry cargo')

class Passengerplane:
    def takeoff(self):
        print('plane took off')
    def fly(self):
        print('plane flying')
    def land(self):
        print('plane landing')
    def passenger(self):
        print('carry passenger')

class fighterplane:
    def takeoff(self):
        print('plane took off')
    def fly(self):
        print('plane flying')
    def land(self):
        print('plane landing')
    def weapon(self):
        print('carry weapon')
c1=Cargoplane()
c1.takeoff()
c1.fly()
c1.cargo()
c1.land()
print()

f1=fighterplane()
f1.takeoff()
f1.fly()
f1.weapon()
f1.land()
print()

p1=Passengerplane()
p1.takeoff()
p1.fly()
p1.passenger()
p1.land()

