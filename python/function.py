#method outside class is known as function

def add(x,y):           # with parameter with return
    sum=x+y
    return sum

def sub(x,y):
    diff=x-y
    print(" difference is :",diff )
def mul():
    a=10
    b=20
    product=a*b
    return product
def div():
    a=20
    b=10
    div1=a/b
    print("division is : "div1)

m=10
n=20

# function calling
sum1= add(m,n)
sub(m,n)
product1=mul()
div()