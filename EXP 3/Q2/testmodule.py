# Import the airth module from the AIRT_OP package
from AIRT_OP import airth

# Test the functions
print(airth.add(5, 3))  # Output: 8
print(airth.sub(10, 2))  # Output: 8
print(airth.mul(4, 6))  # Output: 24
print(airth.div(12, 3))  # Output: 4

# Try dividing by zero (will raise an error)
# print(airth.div(10, 0))
