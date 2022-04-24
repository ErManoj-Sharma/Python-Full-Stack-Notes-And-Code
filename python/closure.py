def outer():
    print(' inside outer')
    def inner():
        print('inside inner ')
    print(inner)
    return inner

ref1=outer()
print(ref1)
ref1()
