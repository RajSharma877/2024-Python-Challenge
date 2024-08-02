# A class is a blueprint or a template.
class Employee:
    # This are class attributes
    language = "Python"
    salary = "150000"


# Object instantiation
raj = Employee()
raj.language = "JavaScript"
print(raj.salary, raj.language)  # accessing class attributes via object

# Note: Instance attributes, take preference over class attributes during assignment &
# retrieval.