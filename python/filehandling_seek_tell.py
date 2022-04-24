fptr=open("emp.txt",'r')
print(fptr.tell()) #default tell() is at 0 position
print(fptr.read())
print()

fptr.seek(10)
print(fptr.tell())
print(fptr.read())
print()

fptr.seek(15)
print(fptr.tell())
print(fptr.read())
print()

fptr.seek(25)
print(fptr.tell())
print(fptr.read())
print()

fptr.seek(7)
print(fptr.tell())
print(fptr.read())
