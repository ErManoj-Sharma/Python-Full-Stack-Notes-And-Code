import re
str="ram rama ramaa ramaaa ramaaaa"
pattern="rama*"
res=re.finditer(pattern,str)
print(res)
for data in res:
    print(data.start(),end=' ')
    print(data.end(),end=' ')
    print(data.group())