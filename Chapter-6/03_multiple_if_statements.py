a = int(input("Enter age: "))

# If statement 1
if a % 2 == 0:
    print("a is even")
# End of if statement 1

# If statement 2
if a >= 18:
    print("You are above the age of consent")
    print("Good for you")

elif a < 0:
    print("You are entering an invalid negative age")

elif a == 0:
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age of consent")

# End of if statement 2

print("End of program")
