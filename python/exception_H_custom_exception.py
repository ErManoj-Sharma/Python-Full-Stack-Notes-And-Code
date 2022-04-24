#steps to create custom Exception
# 1 create class for custom exception
# 2 inherit exception class
# 3 pass error messaege in constructor
# 4 override __str__() method


class AlessthanBException(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message

a=int(input('enter no :'))
b=int(input('enter no :'))
try:
    if(a<b):
        raise AlessthanBException('subtraction not possible because A is less than B')
    else:
        print(a-b)
except AlessthanBException as e:
    print(e)        # giving output
    print(e.__str__())  # giving  output
print('program terminated normally')
