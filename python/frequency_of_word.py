str="ramu is playing ramu is sleeping ramu is eating ramu is bathing"
wordlist=str.split()
dict={}
for word in wordlist:
    if (dict.get(word)):
        value=dict[word]
        value=value+1
        dict[word]=value
    else:
        dict[word]=1
for key,value in dict.items():
    print(key,' : ',value)
    