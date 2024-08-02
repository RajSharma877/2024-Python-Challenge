# A class is a blueprint or a template.
class Employee:
    # This are class attributes
    language = "Python"
    salary = "150000"

    # self refers to the instance of the class. It is automatically passed with a function call
    # from an object. self parameter is compulsory whenever we create a method in class.
    # Whether we use self parameter or not it will be passed to the function always
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    #  Sometimes we need a function that does not use the self-parameter. We can define a
    #  static method like this
    @staticmethod  # decorator to mark greet as a static method
    def greet():
        print("Good morning")


# Object instantiation
raj = Employee()
raj.language = "JavaScript"  # This is an instance attribute
print(raj.salary, raj.language)  # accessing class attributes via object

raj.greet()
raj.getInfo()
# Employee.getInfo(raj)
