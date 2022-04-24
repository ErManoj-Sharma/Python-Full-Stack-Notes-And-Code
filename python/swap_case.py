str=input("enter string 1 : ")
i=0
newstr=''
while(i<=len(str)-1):
    data=str[i]
    asciivalue=ord(data)
    if(asciivalue>=65 and asciivalue<=90):
        asciivalue = asciivalue + 32
        data = chr(asciivalue)
        newstr=newstr+data
    elif((asciivalue>=97 and asciivalue<=122)):
        asciivalue=asciivalue-32
        data=chr(asciivalue)
        newstr = newstr + data
    i=i+1

print("string in swapcase : ",newstr)

