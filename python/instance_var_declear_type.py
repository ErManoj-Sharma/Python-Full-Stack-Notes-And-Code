class student:
    def __init__(self):
        self.name="manoj"  # instance varible decleared inside init method
        self.age=22
    def display(self):
        print(self.name)
        print(self.age)
        self.marks=99    # instance variable declered outside init method
        print(self.marks)
        print(self.location)
s1=student()
print(s1.name)
print(s1.age)
s1.location="bhilwara"   # instance varible declered outside class
print(s1.location)
s1.display()