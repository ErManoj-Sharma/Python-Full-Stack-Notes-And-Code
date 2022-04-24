class Animal:
    def eat(self):
        print('animal is eating')
    def sleep(self):
        print('animal is sleeping')
    def breathe(self):
        print('animal is breathing')
class Tiger(Animal):
    pass
class Eagle(Animal):
    pass
class Shark(Animal):
    pass
t=Tiger()
e=Eagle()
s=Shark()

t.eat()
t.sleep()
t.breathe()

e.eat()
e.sleep()
e.breathe()

s.eat()
s.sleep()
s.breathe()