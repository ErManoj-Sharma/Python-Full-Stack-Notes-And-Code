
# finding ASCII value of char by ord( ) method
#ord method return ASCII value of input charcter
#using ord() method in fr loop
str="Manoj"
for char in str:
    print("the ASCII value of ",char,"is",ord(char))
#using ord method in while loop
stri="EUKST"
i=0
while(i<=len(stri)-1):
    print("the ASCII value of ",str[i]," is ",ord(str[i]))
    i=i+1


