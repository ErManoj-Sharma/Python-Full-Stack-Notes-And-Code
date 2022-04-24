class Animal:
    def eat(self):
        print('animal is eating')
    def sleep(self):
        print('animal is sleeping') #inhereted method
    def breathe(self):
        print('animal is breathing')   #inhereted method
class Tiger(Animal):
    def eat(self):
        print('tiger is hunting and eating')    #method overiding
    def run(self):
        print('tiger is running')           #specialize method
class Eagle(Animal):
    def eat(self):
        print('eagle is flying and eating')  #method overiding
    def fly(self):
        print('eagle is flying ')       #specialize method
class Shark(Animal):
    def eat(self):
        print('shark is swiming and eating')  #method overiding
    def swim(self):
        print('shark is swiming')     #specialize method
t=Tiger()
e=Eagle()
s=Shark()

t.eat()
t.run()
t.sleep()
t.breathe()
print()
e.eat()
e.fly()
e.sleep()
e.breathe()
print()
s.eat()
s.swim()
s.sleep()
s.breathe()
print(Shark.mro())