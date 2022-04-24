class Parent:
    def __init__(self):
        self.a=10

class Child(Parent):
    def __init__(self):
        self.b=20

c1=Child()
print(c1.b)
print(c1.a) #AttributeError: 'Child' object has no attribute 'a'
# in python Parent Class constructor is not called
# automatcially . it is duty of prgrammer to call
# it mannually .