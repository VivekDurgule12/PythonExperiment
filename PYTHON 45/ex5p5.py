def count_words_ending_with_e(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
            words_ending_with_e = [word for word in words if word.endswith('e')]
            count = len(words_ending_with_e)
            print(f"Total number
