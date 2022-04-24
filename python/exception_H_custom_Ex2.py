class MinBalException(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message
class NegAmtException(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message

bal=5000
amt=int(input('enter amonunt to withdraw : '))
try:
    if(amt>bal):
        raise MinBalException('ammount is grather than balance ')
    elif(amt<0):
        raise NegAmtException('ammount is negative')
    else:
        bal=bal-amt
        print('updated balance is : ',bal)
except MinBalException as e:
    print(e)
except NegAmtException as e:
    print(e)
print('program terminated normally')