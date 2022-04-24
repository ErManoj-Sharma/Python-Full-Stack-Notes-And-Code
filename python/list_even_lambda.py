
l=[]
i=0
while(i<=4):
    num=int(input("enter no:"))
    l.insert(i,num)
    i=i+1

print(l)
#by filter function
k=list(filter(lambda x:x%2==0,l))
print(k)
