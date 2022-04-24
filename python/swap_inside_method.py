
#when we sen values to method , method work on copies of values , actual values doesnot modifed
# because x,y are copies so whatever change we make on them will not reflect on actual parameter
#  x,y are deleted with acivation record
#
class demo:
    def __init__(self):
        self.a=10
        self.b=10
    def swap(self,x,y):             # x,y are formal parameter
        temp=x
        x=y
        y=temp
        print("value after swapping inside method  ")
        print(x)
        print(y)
a=10
b=20
print("values before swaping ")
print(a)
print(b)
d1=demo()
d1.swap(a,b)                # a,b are actual parameter
print("after swapping")
print(a)
print(b)
