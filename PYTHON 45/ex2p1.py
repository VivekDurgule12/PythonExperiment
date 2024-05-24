def modify_set():

    my_set = {1, 2, 3, 4, 5}

    my_set.add(6)
    print("After adding 6:", my_set)

    my_set.remove(3)
    print("After removing 3:", my_set)

    my_set.discard(2)
    print("After discarding 2:", my_set)

    popped_element = my_set.pop()
    print("Popped element:", popped_element)
    print("After popping an element:", my_set)

    my_set.clear()
    print("After clearing the set:", my_set)

modify_set()
