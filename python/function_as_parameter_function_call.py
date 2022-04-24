def fun1():
    print("inside fun1 ")
def fun2(x,y):
    print("inside fun2 : ",x+y)
def display(ptr3,ptr4):
    print()
    print("in display ")
    ptr3()
    e,f=40,50
    ptr4(e,f)

fun1()
a,b,c,d=10,20,30,40
fun2(a,b)
ptr1=fun1
ptr2=fun2
print()
ptr1()
ptr2(c,d)

display(ptr1,ptr2)