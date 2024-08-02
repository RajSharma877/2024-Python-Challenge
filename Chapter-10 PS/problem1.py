class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Raj", 1200000, 246002)
print(p.name, p.salary, p.pin, p.company)
g = Programmer("Gaurav", 1200000, 246002)
print(g.name, g.salary, g.pin, g.company)
