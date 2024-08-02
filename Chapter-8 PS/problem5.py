def pattern(n):
    if n == 0:
        return  # This return statement means leave the function block and stop the execution of function
    print("*" * n)
    pattern(n - 1)


pattern(5)
