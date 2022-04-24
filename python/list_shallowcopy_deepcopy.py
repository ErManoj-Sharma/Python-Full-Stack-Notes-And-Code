a=[1,2,3,4,5]

print('shallow copy')
a1=a
print(a)
print(a1)
print(id(a))
print(id(a1))
print(a is a1)

print()
print('deep copy')
b=a.copy()
print(a)
print(b)
print(id(a))
print(id(b))
print(a is b)
b.insert(5,8)
print(a)
print(b)



