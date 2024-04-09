def count_words():
    file = open("poem.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word =="the" or word =="The":
            count += 1
    print(count)
    file.close()

count_words()