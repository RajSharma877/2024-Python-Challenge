class Employee:
    a = 1

    #     A class method is a method which is bound to the class and not the object of the class.
    # @classmethod decorator is used to create a class method.
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


e = Employee()
e.a = 45
e.show()  # Prints instance attribute

# self => object -> method
# cls => class -> object -> method
