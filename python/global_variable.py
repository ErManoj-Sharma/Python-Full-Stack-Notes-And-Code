a=999  #global variable
def fun1():
    b=20                #local variable of fun1
    print(b)
    print("inside fun1 : ",a) #printing global variable in function

def fun2():
    c=10                #local variable of fun2
    print(c)
    print("inside fun2 : ",a)       # #printing global variable in function

fun1()      #calling fun1
fun2()      #calling fun2
print(a)    #print gloabal variable

#so, global variable can be access from any part of program