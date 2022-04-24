import pickle
class Employee:
    def __init__(self,name,age,salary,location):
        self.name=name
        self.age=age
        self.salary=salary
        self.location=location
    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
        print(self.location)

f=open("serial.txt","rb")
e=pickle.load(f)
a=pickle.load(f)
e.display()
a.display()
f.close()