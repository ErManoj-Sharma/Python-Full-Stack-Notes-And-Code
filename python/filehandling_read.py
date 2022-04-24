fname=input('enter file name : ')
fptr=open(fname,'r')                    #file open
data=fptr.readlines()# read()   #read(15)  #readline
    #read &return all lines of file
print()
print(data)

fptr.close()            #file close
