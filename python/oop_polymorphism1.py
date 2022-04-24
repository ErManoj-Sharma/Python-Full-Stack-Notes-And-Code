class Tiger:
    def eat(self):
        print('tiger is hunting and eating')

    def sleep(self):
        print('tiger is sleeping')
class Deer:
    def eat(self):
        print('deer is  eating')

    def sleep(self):
        print('deer is sleeping')
class Monkey:
    def eat(self):
        print('monkey is eating')

    def sleep(self):
        print('monkey is sleeping')
def allowanimal(ref):
    ref.eat()
    ref.sleep()

t=Tiger()
d=Deer()
m=Monkey()
allowanimal(t)
print()
allowanimal(d)
print()
allowanimal(m)