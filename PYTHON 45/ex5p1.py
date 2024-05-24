def read_file_line_by_line(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception
