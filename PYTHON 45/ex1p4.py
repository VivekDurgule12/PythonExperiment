def is_pythagorean_triplet():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))

    # Ensure a is the largest number
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a

    if a**2 == b**2 + c**2:
        print(f"The triplet ({a}, {b}, {c}) is a Pythagorean triplet.")
    else:
        print(f"The triplet ({a}, {b}, {c}) is not a Pythagorean triplet.")

is_pythagorean_triplet()
