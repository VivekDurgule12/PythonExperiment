def string_operations():
   
    sample_string = "Hello, World! This is a sample string for string operations."

   
    print("1. Length of the string:", len(sample_string))

    
    print("2. Uppercase:", sample_string.upper())

    
    print("3. Lowercase:", sample_string.lower())

  
    substring = "string"
    print("4. Count of 'string':", sample_string.count(substring))

    
    new_string = sample_string.replace("sample", "modified")
    print("5. Replaced 'sample' with 'modified':", new_string)

    
    words = sample_string.split()
    print("6. Split into words:", words)

    
    joined_string = "-".join(words)
    print("7. Joined with '-':", joined_string)

   
    prefix = "Hello"
    print("8. Starts with 'Hello'?", sample_string.startswith(prefix))

   
    suffix = "operations."
    print("9. Ends with 'operations.'?", sample_string.endswith(suffix))

string_operations()
