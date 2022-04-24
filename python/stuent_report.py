class Student:
    def __init__(self,name,smarks,mmarks,emarks):
        self.name=name
        self.smarks=smarks
        self.mmarks=mmarks
        self.emarks=emarks
        self.sum=smarks+emarks+mmarks

    def display(self):
        print("Student name  : ",self.name)
        print("maths marks   : ",self.mmarks)
        print("science marks : ",self.smarks)
        print("english marks : ",self.emarks)
        print("Total marks   : ",self.sum)
s1=Student("manoj",90,80,70)
s2=Student("Aarav",10,20,30)
s3=Student("Abhi",50,60,80)

s1.display()
print("\n")
s2.display()
print("\n")
s3.display()
print("\n")
if((s1.sum>s2.sum) and(s1.sum>s3.sum)):
    print("first is ",s1.name," with marks ",s1.sum)
elif((s2.sum>s1.sum) and (s2.sum>s3.sum)):
    print(" first is ",s2.name," with marks ",s2.sum)
elif((s3.sum>s1.sum) and (s3.sum>s2.sum)):
    print("first is ",s3.name," with marks ",s3.sum)