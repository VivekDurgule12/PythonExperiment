def display_pattern():
    for i in range(6, 0, -1):
        for j in range(i):
            print("*", end="\t")
        print()

display_pattern()
