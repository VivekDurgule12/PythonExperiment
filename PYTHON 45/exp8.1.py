class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."

# Example usage
calculator = Calculator()

result = calculator.add(7, 5)
print("7 + 5 =", result)

result = calculator.subtract(34, 21)
print("34 - 21 =", result)

result = calculator.multiply(54, 2)
print("54 * 2 =", result)

result = calculator.divide(144, 2)
print("144 / 2 =", result)

result = calculator.divide(45, 0)
print("45 / 0 =", result)
