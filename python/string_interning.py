#firstly we store string data in gloal dictinary
#if data is not present then we allocate memory to it and return address .
#if data is present in global dictionary then we didnot allocate new memory to data .
#we will return address/reference existing data . ie is called string Interning .

str1="manoj"
str2="aarav"
str3="eukst"
str4="manoj"
str5="aarav"
str6="eukst"
str7="manoj"
str8="aarav"
str9="eukst"
print(id(str1))
print(id(str4))
print(id(str7))
# str1,4,7 have same id as they are pointing same data .
print(id(str2))
print(id(str5))
print(id(str8))
# str2,5,8 have same id as they are pointing same data
print(id(str3))
print(id(str6))
print(id(str9))
#str 3,6,9 have same id as they are pointing same data .
