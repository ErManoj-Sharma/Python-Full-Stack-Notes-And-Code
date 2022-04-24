class Plane:
    def takeoff(self):
        print('plane took off')
    def fly(self):
        print('plane flying')
    def land(self):
        print('plane landing')

class Cargo(Plane):
    def cargo(self):
        print('carry cargo')

class Passenger(Plane):
    def passenger(self):
        print('carry passenger')

class fighter(Plane):
    def weapon(self):
        print('carry weapon')

c1=Cargo()
c1.takeoff()
c1.fly()
c1.cargo()
c1.land()
print()

f1=fighter()
f1.takeoff()
f1.fly()
f1.weapon()
f1.land()
print()

p1=Passenger()
p1.takeoff()
p1.fly()
p1.passenger()
p1.land()

