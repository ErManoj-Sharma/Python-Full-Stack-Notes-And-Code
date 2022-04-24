# method (function with parameter & with return value )

class calculator:
    def __init__(self):
        self.x=2
        self.y=3
    def add(self,num1,num2):
        result=num1+num2
        return result

c1=calculator()
a=20
b=20
c= c1.add(a,b)
print("sum is ",c)