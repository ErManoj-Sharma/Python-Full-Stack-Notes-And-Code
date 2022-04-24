class Calculator:
    def add(self,*value):                       # *value works as array , it is not array but works like same
        i=0
        sum=0
        while(i<=len(value)-1):
            sum=sum+value[i]
            i=i+1
        return sum

c1=Calculator()
a=10
b=20
c=30
d=40
e=50

sum1=c1.add(a,b)
sum2=c1.add(a,b,c)
sum3=c1.add(a,b,c,d)
sum4=c1.add(a,b,c,d,e)

print(sum1)
print(sum2)
print(sum3)
print(sum4)
