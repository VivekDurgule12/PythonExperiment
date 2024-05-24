def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            total_words = len(words)
            print(f"Total number of words in the file '{file_name}': {total_words}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


count_words_in_file("sample.txt")
