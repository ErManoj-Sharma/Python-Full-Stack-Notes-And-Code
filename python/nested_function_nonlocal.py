def fun1():
    a=99
    def fun2():
        a=777
        print(a," local scope")
    fun2()
    print(a," non local scope")

fun1()
print()
#now using nonlocal
def fun3():
    a=99
    def fun4():
        nonlocal a #nonlocal points to non local copy of a so
        #pvm not create local copy of a and use non local copy
        # for operation
        a=777
        print(a," local scope")
    fun4()
    print(a," non local scope")

fun3()