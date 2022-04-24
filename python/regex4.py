import re
str="ramu is faster at running than rohan"
pattern1="^ramu"
pattern2="rohan$"
print()

res1=re.findall(pattern1,str)
res2=re.findall(pattern2,str)
print(res1)
print(res2)
print()

res1=re.search(pattern1,str)
res2=re.search(pattern2,str)
print(res1)
print(res2)
