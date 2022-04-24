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

e=Employee("manoj",22,15000,"bhilwara")
e1=Employee("aarav",7,10000,"goa")

f=open("serial.txt","wb")
pickle.dump(e,f)
pickle.dump(e1,f)
print("object stored in file successfully")
f.close()
