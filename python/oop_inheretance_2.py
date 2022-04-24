class Parent:
    def __init__(self):
        self.a=10

class Child(Parent):
    def __init__(self):
        Parent.__init__(self) # Parent Class Constructor call inside child class
        self.b=20

c1=Child()
print(c1.b)
print(c1.a)