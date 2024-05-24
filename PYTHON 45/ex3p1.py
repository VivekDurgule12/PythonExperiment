def find_numbers():
    numbers = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]
    return numbers

result = find_numbers()
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700:")
print(result)
