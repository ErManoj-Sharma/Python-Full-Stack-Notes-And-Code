import re
str="Ramu89Vishal1234Suraj459"
pattern="[0-9]"
patternn="[0-9]+"

replace="@"
res=re.sub(pattern,replace,str)
print(res)
print()
res=re.subn(pattern,replace,str)
print(res)
print()
res=re.sub(patternn,replace,str)
print(res)
print()
str1="Ramu 89 vishal 1324 suraj 456"
res=re.split(patternn,str1)
print(res)

print()

###ERROR
str2="Ramu 89 vishal 1324 suraj 456"
pat="[]*[0-9]*[]"
re=re.split(pat,str2)

print(re)
