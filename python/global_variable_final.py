def fun1():
    global a
    a,b=999,10
    print(a)
    print(b)
def fun2():
    a=888
    c=20
    print(a)
    print(c)
def fun3():
    global a
    a=777
    d=30
    print(a)
    print(d)
fun1()
fun2()
fun3()
print(a)