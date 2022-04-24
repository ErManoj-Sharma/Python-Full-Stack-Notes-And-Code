def fun1():
    a=10
    def fun2():
        b=20
        print(a,"inside fun2")
        print(b,"inside fun2")
    fun2()
    print(a,"outside fun2 , inside fun1")
    #print(b)        # error b not defined
# we canot access value of inner function outside the inner function
fun1()