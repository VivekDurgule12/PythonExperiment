def display_pattern():
    for i in range(4):
        for j in range(i+1):
            print("*", end="\t")
        print()

display_pattern()
