def outer(print1):              #
          #
    def inner():                #
                                # decorator
        ref1=print1             #
        msg1=ref1()             #
        newstr=msg1.upper()     #
        print(newstr)           #
    return inner                #

@outer
def morning():
    msg='good morning'
    return msg
@outer
def afternoon():
    msg='good afternoon'
    return msg
@outer
def evening():
    msg='good evening'
    return msg
@outer
def night():
    msg='good night'
    return msg

morning()
afternoon()
evening()
night()