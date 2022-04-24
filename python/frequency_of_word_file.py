f=open('empp.txt','r')
data=f.readlines()
print(data)

dict = {}
for line in data:
    print(line)
    wordlist = line.split()
    print(wordlist)
    for word in wordlist:
        if (dict.get(word)):
            value = dict[word]
            value = value + 1
            dict[word] = value
        else:
            dict[word] = 1
print()
for key, value in dict.items():
    print(key, ' : ', value)
