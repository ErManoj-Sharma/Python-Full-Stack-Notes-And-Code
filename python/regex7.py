import re
f=open("data1.txt","r")
data=f.readlines()
pattern="^.....$"

for x in data:
    res=re.search(pattern,x)
    if(res):
        print(res)
f.close()