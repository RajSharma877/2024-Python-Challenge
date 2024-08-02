a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if b == 0:
    raise ZeroDivisionError("Dont divide by zero")

else:
    print(f"Division is {a/b}")

# Custom exceptions are used to minimize errors in code and prevent the abnormal termination of program.
# But sometimes we want the developers to know that they are making critical mistakes so to crash the program we raise the exceptions.
# Raising exceptions also used in designing new module in any program such that whenever we use we would be aware of its functionalities and syntax.
