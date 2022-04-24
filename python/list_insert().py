i=0
l=[]
while True:
    num=int(input('Enter no to add in list : '))
    l.insert(i,num)
    i=i+1

    print('Want to add more :1'
          '\nno element to add : 2 ')
    choice=int(input('Enter your choice (1/2) : '))
    if choice==1:
        continue
    elif choice==2:
        break
    else:
        print('invalid choice ')
        break

print(l)