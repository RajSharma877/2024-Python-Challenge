"""
Sometimes we want to write the logic n no. of times which increases the lines of code and complexity of code.
So to wrap the logic which is performing the same role we can use functions.
Functions are a way in Python to wrap your piece of code and instructing it what to perform.
To invoke a function or get the desired result we need to perform function call
"""

# Function definition
def avg():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))

    average = (a + b + c) / 3

    print(average)


# Function call
avg()
