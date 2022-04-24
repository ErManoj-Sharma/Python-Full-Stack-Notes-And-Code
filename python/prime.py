#t = int(input())
#while (t > 0):
#    prime = True
#    a = int(input("enter no :"))
#    if (a == 1):
#        print('no')
#    else:
#        for i in range(2, a):
#            if (a % i == 0):
#                prime = False
#       if (prime == True):
#        else:
#            print('no')
#    t = t - 1



d=int(input())
n=int(input())
def sum(d,n):
    add=0
    p=d*n
    while(p>0):
        add=add + p
        p=p-1
    print(add)
sum(d,n)