

import reactangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

reactangle_area = reactangle.area(length, width)
print("The area of the rectangle is:", reactangle_area)

rectangle_perimeter = reactangle.perimeter(length, width)
print("The perimeter of the rectangle is:", rectangle_perimeter)
