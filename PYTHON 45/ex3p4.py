def print_numbers():
    for num in range(8):
        if num == 3 or num == 6:
            continue
        print(num, end="")

print_numbers()
