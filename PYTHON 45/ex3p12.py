def sum_integers(a, b):
    sum_of_numbers = a + b
    if 15 <= sum_of_numbers <= 20:
        return 20
    else:
        return sum_of_numbers

# Get the two integers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = sum_integers(num1, num2)
print("The result is:", result)
