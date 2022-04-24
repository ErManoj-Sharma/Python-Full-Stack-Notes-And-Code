def even(x):
    if(x%2==0):
        return True
    else:
        return False
l=[]
i=0
while(i<=4):
    num=int(input("enter no:"))
    l.insert(i,num)
    i=i+1

print(l)
#by filter function
k=list(filter(even,l))
print(k)

# by while loop
i=0
while(i<=4):
    status=even(l[i])
    if(status==True):
        print(l[i]," ",end=' ')
    i=i+1