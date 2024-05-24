def get_integer_input(prompt):
    while True:
        try:
            n = int(input(prompt))
            return n
        except ValueError:
            print("Error: Invalid input, input a valid integer.")

# Usage
n = get_integer_input("Input an integer: ")
print("Input value:", n)
