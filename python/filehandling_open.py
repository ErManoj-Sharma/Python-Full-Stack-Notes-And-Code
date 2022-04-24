fname=input('enter file name : ')
fptr=open(fname,'w')                    #file open
for i in range(5):
    data=input("enter name : ")
    fptr.write(data+"\n")   #fptr.write(data)
fptr.close()            #file close
print('data written on file ')