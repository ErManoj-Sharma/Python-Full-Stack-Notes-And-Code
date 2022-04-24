def outerfunction():
    print("inside outerfunction")
    def innerfunction():
        print("inside inner function")
    innerfunction()
    innerfunction()

outerfunction()
print()
outerfunction()
print()
#innerfunction() if we call inner function outside the outerfunction then
#it will give error NameError