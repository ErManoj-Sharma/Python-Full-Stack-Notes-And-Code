import re
str='hi ram hi ramu hi ramuuuuuuuuu '
pattern = 'ramu*'
res=re.search(pattern,str)
print("output of search : ",res)
res1=re.match(pattern,str)
print("output of match : ",res1)
res2=re.findall(pattern,str)
for x in res2:
    print(x)


print()
print( "New String")
str1='ram hi ramu hi ramuuuuuuuuu '
pattern = 'ram*'
res=re.search(pattern,str1)
print(res)
res1=re.match(pattern,str1)
print(res1)
res2=re.findall(pattern,str)
for x in res2:
    print(x)
