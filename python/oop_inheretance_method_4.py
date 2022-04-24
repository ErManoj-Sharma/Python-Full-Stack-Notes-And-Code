class Animal:
    def eat(self):
        print('animal is eating')
    def sleep(self):
        print('animal is sleeping')
    def breathe(self):
        print('animal is breathing')
class Tiger(Animal):
    def eat(self):
        print('tiger is hunting and eating')
class Eagle(Animal):
    def eat(self):
        print('eagle is flying and eating')
class Shark(Animal):
    def eat(self):
        print('shark is swiming and eating')
t=Tiger()
e=Eagle()
s=Shark()

t.eat()
t.sleep()
t.breathe()
print()
e.eat()
e.sleep()
e.breathe()
print()
s.eat()
s.sleep()
s.breathe()