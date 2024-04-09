def count_letter():
    file = open("Q5/article.txt","r")
    data = file.read()
    count = 0
    for letter in data:
        if letter.isupper():
            count+=1
    print(count)
    file.close()

count_letter()