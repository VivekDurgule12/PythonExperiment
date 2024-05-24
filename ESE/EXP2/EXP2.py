"""
Exp 2. Write a program to demonstrate use of different datatypes
(range, string, list, dictionary, set, and tuples) in python
1. Write a program to implement various methods for modifying set.
1. add () 2. remove() 3.discard() 4.pop() 5.clear()







"""

# 1. Write a program to implement various methods for modifying set. 1. add () 2. remove() 3.discard() 4.pop() 5.clear()
"""
Set={1,2,3,4,5,6}
# print(Set.add(7))
# print(Set.remove(6))
# print(Set.discard(4)) 
# print(Set.pop()) 
# print(Set.clear()) 

print(Set)
"""

"""
2. Write a Python script to perform following operations:

"""

# 1. Merge two Python dictionaries.
"""
dic={'a':1, 'b':2}
dic1={'c':3,'d':4}
print(dic| dic1)
"""

# 2. Iterate over dictionaries using for loops.
"""
 dic={'a':1, 'b':2,'c':3,'d':4}

for D in dic: print(D)

for D in dic.values(): print(D)

for key,value in dic.items(): print(key,value)
"""

# 3. Sum of all the items in a dictionary
"""
dic={'a':1, 'b':2,'c':3,'d':4}

Sum=0
for IsSum in dic.values():
    Sum += IsSum

print(IsSum)
"""

# 4. Multiply all the items
"""
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

Multy = 1
for value in dic.values():
    Multy *= value

print(Multy)
"""


# 5. Remove element from a dictionary
"""
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic.pop('c')
print(dic)  # Output: {'a': 1, 'b': 2, 'd': 4}
"""

# 6. Sort a given dictionary by key
"""
dic = {'b': 2, 'a': 1, 'd': 4, 'c': 3}

Sorted= {key:dic[key] for key in sorted((dic.keys()))}
print(Sorted)
"""

# 7. Get the maximum and minimum value
"""
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(max(dic.values()))
print(min(dic.values()))
"""

# 8. Remove duplicates from Dictionary
"""
dic = {'b': 2, 'a': 1, 'd': 4, 'c': 3, 'a': 1}
Ogn={key:value for key,value in dic.items()}
print(Ogn)
"""



# 3. Write a python program to create, append and remove lists in python
"""
Vivek = []

Vivek.append(1)
Vivek.append(2)
Vivek.append(3)

print(Vivek)

Vivek.remove(2)

print(Vivek)
"""

# 4. Write a program to peform various string operations.

Str = "VivekDurgule!2"

# Convert the string to lowercase
lowercase_str = Str.lower()
print("Lowercase:", lowercase_str)

# Convert the string to uppercase
uppercase_str = Str.upper()
print("Uppercase:", uppercase_str)

# Capitalize the string
capitalized_str = Str.capitalize()
print("Capitalized:", capitalized_str)

# Check if the string ends with '2'
ends_with_2 = Str.endswith('2')
print("Ends with '2':", ends_with_2)

# Replace '!' with a space
replaced_str = Str.replace('!', ' ')
print("Replaced '!' with space:", replaced_str)

# Split the string by '!'
split_str = Str.split('!')
print("Split by '!':", split_str)
