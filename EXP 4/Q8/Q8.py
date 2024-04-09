def search():
    file = open("student.dat","rb")
    try:
        while True:
            record = pickle.load(file)
            if record[0] == 1005:
                print(record)
    except EOFError:
        pass
    file.close()