try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a / b)

except ZeroDivisionError as z:
    print("Infinite")
