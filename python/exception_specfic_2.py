try:
    a=int(input('Enter no : '))
    b=int(input('Enter no : '))
    res=a/b
    print(res)
except (ZeroDivisionError,ValueError) as e:
    #print('Denometer cannot be zero')
    print(e.__str__()) #method 1
    print()
    print(e)            #method 2
except Exception as e:
    print('other exception is occured')
print('\nprogram ended normally ')