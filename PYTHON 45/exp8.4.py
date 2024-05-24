# Rectangle class
class Rectangle:
    def _init_(self, length: float, width: float):
        """
        Initialize a Rectangle instance.

        :param length: The length of the rectangle.
        :param width: The width of the rectangle.
        """
        self.length = length
        self.width = width

    def compute_area(self) -> float:
        """
        Compute the area of the rectangle.

        :return: The area of the rectangle (length * width).
        """
        return self.length * self.width
