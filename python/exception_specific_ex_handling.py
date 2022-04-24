try:
    a=int(input('Enter no : '))
    b=int(input('Enter no : '))
    res=a/b
    print(res)
except ZeroDivisionError as e:
    print('Denometer cannot be zero')
except ValueError as e:
    print('enter valid input')
except Exception as e:
    print('other exception is occured')
print('program ended normally ')
