def int_input(prompt):
    while True:
        try:
            age = int(input(prompt))
            return age
        except ValueError as e:
            print("Not a proper integer! Try it again")

age = int_input("Age of your dog? ")
print("Age of the dog: ", age)
