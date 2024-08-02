class Employee:  # Base class
    def __init__(self):
        print("Constructor of Employee class")

    a = 1


class Programmer(Employee):  # Child class inheriting from base class
    def __init__(self):
        print("Constructor of Programmer class")

    b = 2


class Manager(
    Programmer
):  # Grand child class inheriting from child class as well as grand parent class
    def __init__(self):
        super().__init__() 
        print("Constructor of Manager class")
    c = 3

# Before super() if we want to call the constructor of any class we have to manually call them by creating objects
# But in a particular scenario when we want to access the constructor from base class and child class we can use super() method
# super() method is used to access the methods of a super class in the derived class.

# o = Employee()
# print(o.a)
# # print(o.b) # Shows an error as there is no b attribute in Employee class

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)
