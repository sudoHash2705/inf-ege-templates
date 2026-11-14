from itertools import*
words = list(product("АГИНРТ",repeat = 6))
count = 0
for word in words:
    count+=1
    word = "".join(word)
    if count%2==1 and word[0]!="А" and word[0]!="И" and word[0]!="Г" and word.count("А")==1:
        print(count)
    
