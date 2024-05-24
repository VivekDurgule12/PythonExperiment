"""
Exp1. Demonstrate installation steps and different ways of invoking
python file.

"""

# 1. Write a program to find the type of triangle. Input sides from user.
"""

# Triangle Type Finder
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

"""

# 2. Write a program to display 
""" 
electricity bill. Input no of units from user.
# Electricity Bill Calculator
units = float(input("Enter number of units: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2
else:
    bill = 100 * 1.5 + 100 * 2 + (units - 200) * 3

print(f"Electricity Bill:{bill:.2f}")
"""

# 3. Write a program to find the location of point in graph.
"""
Point Location Finder
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print("Point is in the First Quadrant")
elif x < 0 and y > 0:
    print("Point is in the Second Quadrant")
elif x < 0 and y < 0:
    print("Point is in the Third Quadrant")
elif x > 0 and y < 0:
    print("Point is in the Fourth Quadrant")
elif x == 0 and y == 0:
    print("Point is at the Origin")
elif x == 0:
    print("Point is on the Y-axis")
else:
    print("Point is on the X-axis")
"""




# 4. Write a program to check whether given triplet is pythagoriantriplet. Input three numbers from user.
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

sides = sorted([a, b, c])
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("The triplet is a Pythagorean triplet")
else:
    print("The triplet is not a Pythagorean triplet")

"""

# 5. Write a program to find the distance between two points. 

"""
# Distance Between Two Points
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance:.2f}")

"""