def count_uppercase_characters(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            print(f"Total number of uppercase characters in the file '{file_name}': {uppercase_count}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the file name 'sample.txt'
count_uppercase_characters("sample.txt")
