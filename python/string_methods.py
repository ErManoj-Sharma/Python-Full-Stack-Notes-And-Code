#1 relace method
str="python is cool"
str1=str.replace("is","will be ")
print(str1)

#2 startswith endswith

str2="if you think you can ,you will"
print(str2.startswith("if"))
print(str2.startswith("manoj"))
print(str2.endswith("will"))

#3 count
print(str2.count("you"))
print(str2.count("can"))

str3="you"
str4="rabbbit"
print(str3 in str2)
print(str4 in str2)

#4
str5="when there is will,man,there is will a way"
print(str5.find("will"))
print(str5.rfind("will"))

print(str5.index("will"))
print(str5.rindex("will"))

print(str5.find("lion"))
#print(str5.index("lion")) # value error