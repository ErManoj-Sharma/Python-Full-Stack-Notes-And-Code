a=int(input('Enter Numerator :'))
b=int(input('Enter Denometer : '))
try:
    res=a/b
    print(res)
except Exception as e:
    print('exception is handled ')


print('program terminated normally')