class Parent:
    def __init__(self):
        self.a=10

class Child(Parent):
    def __init__(self):
        Parent.__init__(self) # Parent Class Constructor call inside child class
        self.b=20
class Grand_Child(Child):
    def __init__(self):
        Child.__init__(self)
        self.c=30

c1=Grand_Child()
print(c1.c)
print(c1.b)
print(c1.a)