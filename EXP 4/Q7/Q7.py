def AMcount():
    file = open('Q7/article.txt','r')
    data = file.read()
    counta=0
    countm=0
    for letter in data:
        if letter == 'A' or letter =='a':
            counta += 1
        elif letter == 'M' or letter =='m':
            countm += 1

    file.close()
    print('A or a:',counta)
    print('M or m:',countm)

AMcount()