#  Inheritance

class Employee :

    num_of_employees = 0
    hike = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = float(pay)
        Employee.num_of_employees += 1

    def __str__(self):
        return "{} {} earns {}".format(self.first, self.last, self.pay)

    def raisepay(self):
        self.pay += (self.hike/100) * self.pay

    @classmethod
    def set_hike(cls, amount):
        cls.hike = amount

    @classmethod
    def from_str(cls, datastr):
        fn, ln, pay = datastr.split("-")
        return cls(fn, ln, float(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() >= 5:
            return False

        return True


class Developer(Employee):
    pass


d1 = Developer.from_str("Rakesh-Kuthrapalli-100")

print("Dev:", d1)

e1 = Employee.from_str("Jiji-Buffon-100")

print("Emp:", e1)

# print(help(Developer))
Employee.set_hike(20)

e1.raisepay()
d1.raisepay()

print("Raised pays!")
print("Dev:", d1, "pay raised by {}%".format(d1.hike))
print("Emp:", e1, "pay raised by {}%".format(e1.hike))

Developer.set_hike(30)
Employee.set_hike(20)

e1.raisepay()
d1.raisepay()

print("Raised pays again but nonuniformly!")
print("Dev:", d1, "pay raised by {}%".format(d1.hike))
print("Emp:", e1, "pay raised by {}%".format(e1.hike))


print("==========================================================================")
# Different constructors. Using super()

class Developer(Employee):

    def __init__(self, fn, ln, pay, programming_lang):
        super().__init__(fn, ln, pay)
        # Employee.__init__(self, fn, ln, pay)  ## This also works. But it is not recommeded.

        self.programming_lang = programming_lang

    def __str__(self):
        return super().__str__() + " Lang: " + self.programming_lang

d2 = Developer("David", "Nam", 678, "Java")

print(d2)

print("==========================================================================")

class Manager(Employee):

    def __init__(self, fn, ln, pay, employees=None):
        super().__init__(fn, ln, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)


    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def __str__(self):
        des = super().__str__()
        counter = 0
        for emp in self.employees:
            counter += 1
            des += "\n{}. {} {}".format(counter, emp.first, emp.last)
        return des


d1 = Developer("Kento", "Bento", 100, "Java")
d2 = Developer("Loki", "Kuku", 120, "Python")

m1 = Manager("P", "K", 1000)
print(m1)

m2 = Manager("New", "Manager", 1500, [d1])
print(m2)

print("Adding employee d2")
m2.add_employee(d2)

print(m2)

print("Removing Employee d1")
m2.remove_employee(d1)

print(m2)

print("==========================================================================")
# isinstance and issubclass

print("m1 is instance of Manager:", isinstance(m1, Manager))
print("m1 is instance of Employee:", isinstance(m1, Employee))
print("m1 is instance of Developer:", isinstance(m1, Developer))

print("==========================================================================")

print("m1's class is subclass of Manager:", issubclass(m1.__class__, Manager))
print("m1's class is subclass of Employee:", issubclass(m1.__class__, Employee))
print("m1's class is subclass of Developer:", issubclass(m1.__class__, Developer))
