
b1 = open("b1.txt", 'w')
b2 = open("b2.txt", 'w')
a = open("a.txt",'r')
count = 1
for i in a:
    if count % 2 == 0:
        b1.write(i.upper())
    else:
        b2.write(i.lower())
    count = count + 1
b1.close()
b2.close()
a.close()
