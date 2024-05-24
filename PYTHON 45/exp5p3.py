def count_word_occurrence(file_name, word):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            word_count = content.lower().count(word.lower())
            print(f"The word '{word}' occurs {word_count} times in the file '{file_name}'.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


count_word_occurrence("notes.txt", "the")
