a=int(input('enter no :'))
b=int(input('enter no :'))
try:
    if(a<b):
        e=Exception() #calling existing exception
        raise e     #mannual throwing exception by using class exception
    else:
        print(a-b)
except Exception as e:
    print('Subtarction not possibel as a<b')
print('program terminated normally')

