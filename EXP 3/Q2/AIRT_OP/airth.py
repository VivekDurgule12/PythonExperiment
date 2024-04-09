def add(x, y):
  """Adds two numbers and returns the sum."""
  return x + y

def sub(x, y):
  """Subtracts two numbers and returns the difference."""
  return x - y

def mul(x, y):
  """Multiplies two numbers and returns the product."""
  return x * y

def div(x, y):
  """Divides two numbers and returns the quotient (assuming y != 0)."""
  if y == 0:
    raise ZeroDivisionError("Division by zero")
  return x / y
