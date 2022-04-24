# method (function without parameter & with return value )

class calculator:
    def __init__(self):
        self.x=2
        self.y=3
    def add(self):
        num1=30
        num2=45
        result=num1+num2
        return result

c1=calculator()
c= c1.add()
print("sum is ",c)