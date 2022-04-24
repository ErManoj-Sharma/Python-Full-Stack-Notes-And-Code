#wap tp count no of word, lines, char in a file take input from user

fname=input('enter file name : ')
fptr=open(fname,'r')                    #file open
data=fptr.readlines()
#print(data)
linecount=len(data)
wordcount=0
charcount=0
for x in data:
    tchar=len(x)
    wordlist=x.split()
    tword=len(wordlist)
    wordcount=wordcount+tword
    charcount=charcount+tchar

print("no of lines in file : ",linecount)
print("no of words in file : ",wordcount)
print("no of char in file  :  ",charcount )