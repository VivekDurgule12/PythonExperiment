def AMCount(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            count_a = content.lower().count('a')
            count_m = content.lower().count('m')
            total_count = count_a + count_m
            print(f"A or a: {count_a}")
            print(f"M or m: {count_m}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the file name 'STORY.TXT'
AMCount("STORY.TXT")
