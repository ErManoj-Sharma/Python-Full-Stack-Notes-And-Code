class cal:
    def arthops(self,x,y):
        res1=x+y
        res2=x-y
        res3=x*y
        res4=x/y
        return res1,res2,res3,res4

c1=cal()
a,b=10,20
x1,x2,x3,x4=c1.arthops(a,b)
print(x1)
print(x2)
print(x3)
print(x4)