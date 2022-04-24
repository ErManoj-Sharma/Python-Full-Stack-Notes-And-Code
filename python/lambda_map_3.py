
l=[]
i=0
while(i<=4):
    data=int(input("enter no :"))
    l.insert(i,data)
    i=i+1

k=list(map(lambda data:data+10 ,l))
print(k)