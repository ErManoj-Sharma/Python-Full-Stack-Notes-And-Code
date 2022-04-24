def operation(num):
    return num+10

l=[]
i=0
while(i<=4):
    data=int(input("enter no :"))
    l.insert(i,data)
    i=i+1

i=0
while(i<=4):
    result=operation(l[i])
    print(result," ",end=' ')
    i=i+1