a = 89  # Global variable which can be accessed in any function or anywhere in this code


def fun():
    global a  # global keyword can make changes the value of the global variable by local variable's value
    # ‘global’ keyword is used to modify the variable outside of the current scope.
    a = 3  # Local variable bound to this function
    print(a)


fun()
print(a)
