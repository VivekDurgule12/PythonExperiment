def binary_divisible_by_5(binary_sequence):
    numbers = binary_sequence.split(',')
    divisible_by_5 = [num for num in numbers if int(num, 2) % 5 == 0]
    return ','.join(divisible_by_5)

# Sample Data
binary_input = '0100,0011,1010,1001,1100,1001'

result = binary_divisible_by_5(binary_input)
print("Numbers divisible by 5:", result)
