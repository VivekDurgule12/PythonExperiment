import math

class Circle:
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        """
        Compute the area of a circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Compute the perimeter (circumference) of a circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius
