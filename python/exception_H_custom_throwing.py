#creating custom exception and throwing
class AlessthanBException(Exception):
    def __init__(self):             #definig exception
        print('subtraction not possible')
a=int(input('enter no :'))
b=int(input('enter no :'))
try:
    if(a<b):
        e=AlessthanBException() #throwing custom exception
        raise e
    else:
        print(a-b)
except AlessthanBException as e:
    print('Subtarction not possibel as a<b')

    print(e)        # no output
    print(e.__str__())  # no output
print('program terminated normally')
