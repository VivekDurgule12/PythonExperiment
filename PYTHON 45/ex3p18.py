def display_pattern():
    for i in range(6, 2, -1):
        for j in range(i):
            print(j, end="\t")
        print()

    print()

    for i in range(5, 0, -1):
        for j in range(i):
            print(j, end="\t")
        print()

display_pattern()
