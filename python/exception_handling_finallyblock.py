def fun2():
    print('establish connection with database in fun 2 ')
    try:
        res=10/0
        print(res)
    except Exception as e:
        print('exception caught in fun2 ')
        raise e
    finally:
        print('disconnect Database in fun 2')

def fun1():
    print('establish connection with databse in fun 1')
    try:
        fun2()
    except Exception as e:
        print('exception handles in fun1 ')
        raise e
    finally:
        print('disconnect db in fun 1 ')

print('program start')
try:
    fun1()
except Exception as e:
    print('Exception handled in main')
print('program terminated normaly')

