"""
Exp. 3: Program to demonstrate Use of Statements in Python
Problem Statements
-------------------------------------------------------------------------------------------------










16. Write a Python program to print alphabet pattern 'U'.
Expected Output:
* *
* *
* *
* *
* *
* *
 ***

17. Write a Python program to print alphabet pattern 'Z'.
Expected Output:
*******
 *
 *
 *
 *
*
*******

18. Write a Python program to calculate a dog's age in dog's years. Note: For the
first two years, a dog year is equal to 10.5 human years. After that, each dog
year equals 4 human years.
Expected Output:
Input a dog's age in human years: 15
The dog's age in dog's years is 73

19. Write a Python program to check whether an alphabet is a vowel or
consonant.
Expected Output:
Input a letter of the alphabet: k
k is a consonant.

20. Write a Python program to convert month name to a number of days.
Expected Output:
List of months: January, February, March, April, May, June, July, August
, September, October, November, December
Input the name of Month: February
No. of days: 28/29 days

21. Write a Python program to sum of two given integers. However, if the sum is
between 15 to 20 it will return 20.

22. Write a Python program to check a string represent an integer or not.
Expected Output:
Input a string: Python
The string is not an integer.

23. Write a Python program to check a triangle is equilateral, isosceles or
scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:
Input lengths of the triangle sides:
x: 6
y: 8
z: 12
Scalene triangle

24. Write a Python program that reads two integers representing a month and
day and prints the season for that month and day.
Expected Output:
Input the month (e.g. January, February etc.): july
Input the day: 31
Season is autumn

25. Write a Python program to display astrological sign for given date of birth.
Expected Output:
Input birthday: 15
Input month of birth (e.g. march, julyetc): may
Your Astrological sign is : Taurus

26. Write a Python program to display the sign of the Chinese Zodiac for given
year in which you were born.
Expected Output:
Input your birth year: 1973
Your Zodiac sign : Ox

27. Write a Python program to find the median of three values.
Expected Output:
Input first number: 15
Input second number: 26
Input third number: 29
The median is 26.0

28. Write a Python program to get next day of a given date.
Expected Output:
Input a year: 2016
Input a month [1-12]: 08
Input a day [1-31]: 23
The next date is [yyyy-mm-dd] 2016-8-24

29. Write a Python program to calculate the sum and average of n integer
numbers (input from the user). Input 0 to finish.

30. Write a Python program to create the multiplication table (from 1 to 10) of a
number.
Expected Output:
Input a number: 6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60

31. Write a Python program to construct the following pattern, using a nested
loop number.
Expected Output:
1
22
333
4444
55555
666666
7777777
88888888
999999999

32. Write a program to display following pattern
*
* *
* * *
* * * *

33. Write a program to display following pattern
0
0 1
 0 1 2
 0 1 2 3

34. Write a program to display following pattern
* * * * * *
* * * * *
* * * *
* * *
* *
*

35. Write a program to display following pattern
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
0
Note:
[Every student of each Batch should solve minimum 7 problem statements]
"""

#1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# for i in range (1500,2700,1):
#     if i %7== 0 and i %5==0:
#         print(i)
    
"""
2. Write a Python program to convert temperatures to and from celsius,
fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in
fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""

# celsius = float(input("Enter temperature\in celsius: "))
# fahrenheit = (celsius * 1.8) + 32
# Answer = (str(celsius )+ " degree Celsius\is equal to " + str(fahrenheit )+ " degree Fahrenheit.")
# print(Answer)


"""
3. Write a Python program to construct the following pattern, using a nested for
loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
# row =5
# for i in range(1 , row *2):
#     if i <= row:
#         print("* " * i )
#     else:
#         print ("* " * (row *2 -i))
   
"""
4. Write a Python program that accepts a word from the user and reverse it
"""

# String = "Vivek"
# for i in range(len(String) -1 , -1 , -1):
#     print(String[i],end=" ")
    
"""
5. Write a Python program to count the number of even and odd numbers from a
series of numbers. Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""

# for i in range(Beginning, Ending + 1):
#     if i % 2 == 0:
#         Even += 1
#     else:
#         Odd += 1     

# print("Even in Numbers =", Even)
# print("Odd in Numbers =", Odd)
"""
6. Write a Python program that prints all the numbers from 0 to 7 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5 7
"""
# Number=(1,2,3,4,5,6,7)
# for i in Number:
#     if i == 3 or i == 6:
#         continue
#     else:
#         print(i,end=" ")

"""
7. Write a Python program which iterates the integers from 1 to 50. For multiples
of three print "Fizz" instead of the number and for the multiples of five print
"Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz
"""

# def Iterates(Numbers): 
#     if Numbers >= 0:
#         Iterates(Numbers-1)
#         if Numbers % 3==0:
#             print("Buzz")
#         elif Numbers % 5 == 0:
#             print("FizzBuzz")
#         print(Numbers,end=" ")

# Numbers=int(input("Enter Number = "))
# print(Iterates(Numbers))

"""
8. Write a Python program which takes two digits m (row) and n (column) as
input and generates a two-dimensional array. The element value in the i-th row
and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.
Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""
# rows, columns = 3, 4
# arr = [[i*j for j in range(columns)] for i in range(rows)]
# print(arr)

"""
9. Write a Python program that accepts a sequence of lines (blank line to
terminate) as input and prints the lines as output (all characters in lower case).
"""

# String =input("Enter String: ")

# if String==String.islower():
#     String.isupper()
# elif String==String.isupper():
#     String.islower()
# else:
#     print("please Enter a String ")

# print(String)

"""
10. Write a Python program which accepts a sequence of comma separated 4
digit binary numbers as its input and print the numbers that are divisible by 5 in a
comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010
"""

"""
11. Write a Python program that accepts a string and calculate the number of
digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2
"""

# def CalculateChar(Text):
#     Letters=0
#     Digit=0
#     for char in Text:
#         if char.isalpha():
#             Letters+=1
#         elif char.isdigit():
#             Digit+=1

#     return Letters , Digit
    
# input=input("Enter a String : ")
# Letters,Digit = CalculateChar(input)
# print(f"The Letters {Letters}, The Digit{Digit}")


"""
12. Write a Python program to check the validity of password input by users
Validation :
 At least 1 letter between [a-z] and 1 letter between [A-Z].
 At least 1 number between [0-9].
 At least 1 character from [$#@].
 Minimum length 6 characters.
 Maximum length 16 characters.
# """
# import re

# def PasswordCheking(Password):
#     SpecialSym =['$', '@', '#', '%']
#     val = True

#     if not any(char in SpecialSym for char in Password):
#         print('Password should have at least one of the symbols $@#')
#         val = False
#     if val:
#         return val
    
#     if len(Password)<8:
#         return False
#     if not re.search("[a-z]",Password):
#         return False
#     if not re.search("[A-Z]",Password):
#         return False
#     if not re.search("[0-9]",Password):
#         return False
#     return True

# UserInput=input("Enter Password :")

# if PasswordCheking(UserInput):
#     print("Valid passWord")
# else:
#     print("Invalid Password")

"""
13. Write a Python program to find numbers between 100 and 400 (both
included) where each digit of a number is an even number. The numbers
obtained should be printed in a comma-separated sequence.
"""

# items = []

# for i in range(100, 401):

#     s = str(i)
#     if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
    
#         items.append(s)

# print(",".join(items)) 


"""
12. Write a Python program to check the validity of password input by users
Validation :
 At least 1 letter between [a-z] and 1 letter between [A-Z].
 At least 1 number between [0-9].
 At least 1 character from [$#@].
 Minimum length 6 characters.
 Maximum length 16 characters.


"""
# # Import the 're' module for regular expressions
# import re

# # Prompt the user to input a password and store it in the variable 'p'
# p = input("Input your password")

# # Set 'x' to True to enter the while loop
# x = True

# # Start a while loop that continues until 'x' is True
# while x:  
#     # Check conditions for a valid password:
#     # Password length should be between 6 and 12 characters
#     if (len(p) < 6 or len(p) > 12):
#         break
#     # Password should contain at least one lowercase letter
#     elif not re.search("[a-z]", p):
#         break
#     # Password should contain at least one digit
#     elif not re.search("[0-9]", p):
#         break
#     # Password should contain at least one uppercase letter
#     elif not re.search("[A-Z]", p):
#         break
#     # Password should contain at least one special character among '$', '#', '@'
#     elif not re.search("[$#@]", p):
#         break
#     # Password should not contain any whitespace character
#     elif re.search("\s", p):
#         break
#     else:
#         # If all conditions are met, print "Valid Password" and set 'x' to False to exit the loop
#         print("Valid Password")
#         x = False
#         break

# # If 'x' remains True, print "Not a Valid Password"
# if x:
#     print("Not a Valid Password")

"""
14. Write a Python program to print alphabet pattern 'L'.
Expected Output:
*
*
*
*
*
*
*****
"""

# for i in range(5):
#         print('*')

# print('*' * 4)



"""
15. Write a Python program to print alphabet pattern 'T'.
Expected Output:
*****
 *
 *
 *
 *
 *
 *

"""

# for i in range(5):
#         if i == 0:
#             print('*' * 5)
#         else:
#             print(' ' * (5 // 2) + '*')

