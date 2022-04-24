a=999  #global variable
def fun1():
    global a
    a=888
    b=20                #local variable of fun1
    print(b)
    print("inside fun1 a(local) : ",a) #printing global variable in function

def fun2():
    global a
    a=777
    c=10                #local variable of fun2
    print(c)
    print("inside fun2 a(local) : ",a)       # #printing global variable in function

print("before entering in any function a(global):",a)
fun1()      #calling fun1
fun2()      #calling fun2
print(" value of a(global)",a)