def outer(print1):              #
    print('inside outer')       #
    def inner():                #
        print('inside inner')   # decorator
        ref1=print1             #
        msg1=ref1()             #
        newstr=msg1.upper()     #
        print(newstr)           #
    return inner                #

@outer
def print_msg():
    print('inside print_msg')
    msg='hello everyone'
    return msg
print_msg()