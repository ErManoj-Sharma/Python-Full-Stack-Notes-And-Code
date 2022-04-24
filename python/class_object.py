class student:
    def __init__(self):
        self.name="manoj"
        self.age=22
        self.marks=100
        self.location="bhilwara"

    def study(self):
        print("student is studying ")
s1=student()
print(s1)                       # printing address of object

print(s1.name)
print(s1.age)                   # accessing data through object
print(s1.marks)

s1.study()                      # calling method

s2=s1                           # copying object to another object

print(s1)                       # printing both objects address ( both are same)
print(s2)

s3=s1                           #creating one more address variable of same object

s4=student()                    # creating one more object ( returned address is stored in s4)

print(s1)
print(s2)                       # s1,s2,s3 have same address
print(s3)
print(s4)                       # s4 has different address

s1.name="eukst"                 # name changed by s1 address variable

print(s1.name)
print(s2.name)                  # all adrress variale pointing to same address so, change will happend to other variable also
print(s3.name)
print(s4.name)                  # s4 doesnot change , because it points to other object








