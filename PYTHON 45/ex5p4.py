def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            this_count = content.count("this")
            these_count = content.count("these")
            print(f"The word 'this' occurs {this_count} times in the file '{file_name}'.")
            print(f"The word 'these' occurs {these_count} times in the file '{file_name}'.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


count_words_in_file("article.txt")
