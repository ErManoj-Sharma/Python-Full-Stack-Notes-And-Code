def fun1():
    print("inside fun 1")
def fun2(x,y):
    print("inside fun 2 : ",x+y)

fun1()
a,b=10,20
fun2(a,b)      #function call with function name

ptr1=fun1       #function assignment to variable
ptr2=fun2

ptr1()          #function call with variable name
c,d=30,40
ptr2(c,d)