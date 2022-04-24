import re
fptr=open("data.txt","r")
data=fptr.read()
pattern1="rama*"
res=re.findall(pattern1,data)
print(res)
print()
pattern="[0-9]{10}"
res=re.findall(pattern,data)
print(res)
print()
pt="[a-z A-Z 0-9 _ -]+@[a-z A-Z 0-9 _ -]+\.com"
res=re.findall(pt,data)
print(res)
print()
pat="@[a-z A-Z 0-9]+"
res=re.findall(pat,data)
print(res)


