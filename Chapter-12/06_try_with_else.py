try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:  # This else block will execute if the code inside try block runs successfully
    print("Program ends")
