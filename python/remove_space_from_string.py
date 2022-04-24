str=input("Enter the string : ")
newstr=""
i=0
while(i<=len(str)-1):
    data=str[i]
    if(data==" "):
        i=i+1
    else:
        newstr=newstr+data          # string concatenation
        i=i+1

print(newstr)