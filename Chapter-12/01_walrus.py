"""
The walrus operator (:=) in Python is a new assignment operator introduced in Python 3.8. 
It allows you to assign values to variables as part of an expression. 
This can make certain types of code more concise and can help avoid repeating calculations.
"""

# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3
