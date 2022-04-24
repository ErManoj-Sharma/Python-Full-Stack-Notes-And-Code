x=10
def fun1():
    x=99
    def fun2():
        x=777
        print(x," in local scope")
    fun2()
    print(x," in enclosed scope")
fun1()
print(x," in global scope")