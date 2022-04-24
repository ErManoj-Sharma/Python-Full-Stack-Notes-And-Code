class demo:
    x=99
    def __init__(self):
        self.a=10
        self.b=20
    def instancemethod1(self):
        print(self.a)
        print(self.b)
        print(" inside instance method : ",demo.x)
    @staticmethod
    def staticmethod1():            #static method decleration
        print(demo.x)

d1=demo()
d1.instancemethod1()
demo.staticmethod1()                # static method calling