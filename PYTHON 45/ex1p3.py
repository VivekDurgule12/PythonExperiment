def find_point_location():
    x = float(input("Enter the x-coordinate: "))
    y = float(input("Enter the y-coordinate: "))

    if x > 0 and y > 0:
        print("The point lies in the first quadrant.")
    elif x < 0 and y > 0:
        print("The point lies in the second quadrant.")
    elif x < 0 and y < 0:
        print("The point lies in the third quadrant.")
    elif x > 0 and y < 0:
        print("The point lies in the fourth quadrant.")
    elif x == 0 and y != 0:
        print("The point lies on the y-axis.")
    elif x != 0 and y == 0:
        print("The point lies on the x-axis.")
    else:
        print("The point is at the origin (0, 0).")

find_point_location()
