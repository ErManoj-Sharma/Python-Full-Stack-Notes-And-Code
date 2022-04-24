str=input("enter string 1 : ")
i=0
newstr=''
while(i<=len(str)-1):
    data=str[i]

    asciivalue=ord(data)            # ord() method convert character to ascii value
    if(asciivalue>=97 and asciivalue<=122):
        newstr=newstr+data
    else:
        asciivalue=asciivalue+32
        data=chr(asciivalue)        # chr() method convert ascii value to character
        newstr = newstr + data
    i=i+1

print("string in lowercase : ",newstr)

