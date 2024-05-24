def dictionary_operations():
    
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    merged_dict = {**dict1, **dict2}
    print("Merged dictionary:", merged_dict)


    print("\nIterating over the merged dictionary:")
    for key, value in merged_dict.items():
        print(f"Key: {key}, Value: {value}")

    
    values = merged_dict.values()
    total_sum = sum(values)
    print(f"\nSum of all values: {total_sum}")

    
    total_product = 1
    for value in values:
        total_product *= value
    print(f"Product of all values: {total_product}")

   
    removed_key = 'b'
    if removed_key in merged_dict:
        del merged_dict[removed_key]
        print(f"\nDictionary after removing '{removed_key}': {merged_dict}")
    else:
        print(f"Key '{removed_key}' not found in the dictionary.")

dictionary_operations()
