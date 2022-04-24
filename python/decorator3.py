def print_msg():
    msg='hello everyone'
    return msg

def outer(print1):
    print('inside outer')
    def inner():
        print('inside inner')
        ref1=print1
        msg1=ref1()
        newstr=msg1.upper()
        print(newstr)
    return inner

ptr1=outer(print_msg)
ptr1()
print('program end')