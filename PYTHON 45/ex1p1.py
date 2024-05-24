def find_triangle_type():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Equilateral triangle")
        elif a == b or a == c or b == c:
            print("Isosceles triangle")
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Right-angled triangle")
        else:
            print("Scalene triangle")
    else:
        print("Not a triangle")

find_triangle_type()
