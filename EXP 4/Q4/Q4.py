def count_words():
    file = open("Q4/article.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word =="this" or word =="These":
            count += 1
    print(count)
    file.close()

count_words()