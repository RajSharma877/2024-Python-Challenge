class Employee:  # Base class
    company = "ITC"

    def show(self):
        print(
            f"The name of the Employee is {self.name} and the salary is {self.salary}"
        )


# This is a bad practice to access one class method or attributes in another class.
# As the program grows the complexity will be also growing.
# The best method to provide modularity and the consistent way of maintaining state of variables between different classes is Inheritance
# Inheritance is the programming approach where we can access all methods and variables declared in parent class in derived class


# class Programmer:
#     company = "ITC Infotech"

#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):  # Derived or child class
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)
