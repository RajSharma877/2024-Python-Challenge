class Employee:
    a = 1

    #     A class method is a method which is bound to the class and not the object of the class.
    # @classmethod decorator is used to create a class method.
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    # Getter method
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    # Setter method
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45

e.name = "Raj Sharma"
print(e.fname, e.lname)
e.show()  # Prints instance attribute

# self => object -> method
# cls => class -> object -> method
