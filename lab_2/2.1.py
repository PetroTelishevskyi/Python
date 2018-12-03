try:
    f = open('text.txt','r')
    lines = f.read()
    for i in lines:
        word = lines.split()
    words = []
    for j in word:
        words.append(len(j))
    e = min(words)
    for k in word:
        if len(k) == e:
            print (k)
    f.close()
except:
    print("can't open file")
    f.close()
