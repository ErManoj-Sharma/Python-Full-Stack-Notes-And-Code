fname=input('enter file name : ')
fptr=open(fname,'a')                    #file open
for i in range(3):
    name=input("enter name : ")
    id=input("Enter id : ")
    loc=input("Enter location : ")
    salary=input("Enter salary : ")
    data=id+" "+name+" "+loc+" "+salary+" \n"
    fptr.write(data)   #fptr.write(data)
fptr.close()            #file close
print('data written on file ')