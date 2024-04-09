def count_words():
    file = open("Q5/article.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word[-1] == 'e':
            count+=1
    print(count)
    file.close()

count_words()