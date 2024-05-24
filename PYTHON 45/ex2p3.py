def list_operations():

    my_list = [1, 2, 3, 4, 5]
    print("Initial list:", my_list)


    my_list.append(6)
    my_list.append(7)
    print("List after appending elements:", my_list)

   
    element_to_remove = 3
    if element_to_remove in my_list:
        my_list.remove(element_to_remove)
        print(f"List after removing {element_to_remove}:", my_list)
    else:
        print(f"Element {element_to_remove} not found in the list.")

list_operations()
