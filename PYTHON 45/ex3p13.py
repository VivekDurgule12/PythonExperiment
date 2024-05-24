def multiplication_table(number):
    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number}x{i}={result}")

# Get the number from the user
num = int(input("Input a number: "))

multiplication_table(num)
