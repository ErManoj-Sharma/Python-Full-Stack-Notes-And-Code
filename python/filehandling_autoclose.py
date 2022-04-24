with open('data.txt','w') as fptr:
    for i in range(5):
        n=input("Enter a name : ")
        fptr.write(n)
    print("name written in file ")
print(fptr.closed)