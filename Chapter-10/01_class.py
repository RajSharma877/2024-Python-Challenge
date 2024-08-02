# A class is a blueprint or a template.
class Employee:
    # This are class attributes
    language = "Python"
    salary = "150000"


# Object instantiation
raj = Employee()
raj.name = "Raj"
print(raj.name, raj.salary, raj.language)  # accessing class attributes via object

riya = Employee()
riya.name = "Riya"  # This is an instance attribute
print(riya.name, riya.language, riya.salary)

# Here name is object attribute and salary and language are class
# attributes as they directly belong to the class
