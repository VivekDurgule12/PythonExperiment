def display_pattern():
    for i in range(4):
        for j in range(i+1):
            print(j, end="\t")
        for j in range(i):
            print("\t", end="")
        print()

display_pattern()
