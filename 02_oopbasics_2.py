# Regular methods and class methods and static methods
# ====================================================

class Employee :

    num_of_employees = 0
    hike = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employees += 1


    # use and attribute to denote class methods.
    # Class methods do not take in self as the default first argument.

    @classmethod
    def set_hike(cls, amount):
        cls.hike = amount


emp1 = Employee("First", "Emp", 1000)
emp2 = Employee("Second", "Emp", 1000)

print(Employee.hike)
print("emp1", emp1.hike)
print("emp2", emp2.hike)

print("Setting new hike!")

Employee.set_hike(40)
print(Employee.hike)
print("emp1", emp1.hike)
print("emp2", emp2.hike)


print("==========================================================================")

# Class methods as an alternative constructor.

# Data in the form of : Rajesh-Mukherjee-1900
# Viren-Banjerjee-900
# fn, ln, pay = ("Viren-Banjerjee-900").split("-")

class Student:

    num_of_students = 0
    bonus = 0

    def __init__(self, first, last, bonus):
        self.first = first
        self.last = last
        self.bonus = bonus
        Student.num_of_students += 1


    # use and attribute to denote class methods.
    # Class methods do not take in self as the default first argument.

    @classmethod
    def set_bonus(cls, amount):
        cls.bonus = amount

    @classmethod
    def from_str(cls, datastr):
        fn, ln, bonus = datastr.split("-")
        return cls(fn, ln, bonus)


fn, ln, hike = ("Viren-Banjerjee-900").split("-")

stu1 = Student(fn, ln, hike)

stu2 = Student.from_str("Rajesh-Mukherjee-1900")

print("stu1", stu1.first, stu1.last)
print("stu2", stu2.first, stu2.last)

print("==========================================================================")
# Static methods belong in a class but do not use any static attributes of the class.

class Employee :

    num_of_employees = 0
    hike = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employees += 1


    # use the @classmethod attribute to denote class methods.
    # Class methods do not take in self as the default first argument.

    @classmethod
    def set_hike(cls, amount):
        cls.hike = amount

    # use the @staticmethod attribute to denote static methods.
    # static methods do not have any mandatory parameters.
    @staticmethod
    def is_workday(day):
        if day.weekday() >= 5:
            return False

        return True


import datetime

date = datetime.date(2016, 7, 10) #Sunday

print(Employee.is_workday(date))

