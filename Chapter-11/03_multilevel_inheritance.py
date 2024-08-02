class Employee:  # Base class
    a = 1


class Programmer(Employee):  # Child class inheriting from base class
    b = 2


class Manager(
    Programmer
):  # Grand child class inheriting from child class as well as grand parent class
    c = 3


o = Employee()
print(o.a)
# print(o.b) # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)
