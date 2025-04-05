#Python Math Module
#The math module provides various mathematical functions.

import math
print(math.sqrt(7))
print(abs(-5))
print(pow(8,5))

#Working with NaN (Not a Number)
#In Python, NaN represents undefined or unrepresentable values, often resulting from mathematical errors (e.g., dividing by zero).

nan_value = float('nan')
print(nan_value)  # Output: nan

# Checking if a value is NaN
if math.isnan(nan_value):
    print("This is NaN")

#Working with Infinity
#Python's math.inf represents positive infinity.
positive_infinity = math.inf
print(positive_infinity)  # Output: inf

# Checking if infinity is greater than a large number
print(positive_infinity > 999999999999999999999)  # Output: True