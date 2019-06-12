# magic methods and dunder methods

# __repr__ & __str__
# __repr__ is a representation of the object meant for other software developers to see.
# __str__ is a more user friendly version.
# When __str__ is not present, __repr__ is the fallback


class Employee :

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = float(pay)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)


emp1 = Employee("Nick", "Julia", 1800)

print(emp1)

print("=============================================================================")

class Employee :

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = float(pay)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "Employee : {} {}, Email: {}.{}@mail.com".format(self.first, self.last, str.lower(self.first), str.lower(self.last))


emp1 = Employee("Nick", "Julia", 1800)

print(emp1)

print("repr:", repr(emp1))

print("str:", str(emp1))

print("=============================================================================")


class Employee :

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = float(pay)

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        else:
            return self.pay + other


emp1 = Employee("Nick", "Julia", 1800)
emp2 = Employee("Jacky", "Chan", 1000)
emp3 = Employee("Micky", "Lee", 2000)

print(emp1 + emp2) # Only 2. 3 dont work

print(emp1 + (emp2 + emp3)) # This works

# print(emp1 + emp2 + emp3) # This doesn't work

print("=============================================================================")

class Employee :

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = float(pay)

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        else:
            return self.pay + other

    def __radd__(self, other):
        return self.__add__(other)


emp1 = Employee("Nick", "Julia", 1800)
emp2 = Employee("Jacky", "Chan", 1000)
emp3 = Employee("Micky", "Lee", 2000)

print(emp1 + emp2 + emp3) # This works now.

print("=============================================================================")

class Employee :

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = float(pay)

    def __len__(self):
        return len(self.first + self.last) + 1


emp1 = Employee("Nick", "Julia", 1800)
print(len(emp1))

# Property attributes to have getter setters
print("=============================================================================")

class Employee :

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = str.lower(first) + "." + str.lower(last) + "@mail.com"

    def __str__(self):
        return "{} {}. Email: {}".format(self.first, self.last, self.email)

emp2 = Employee("John", "Smith")
print(emp2)

emp2.first = "Jim"
print(emp2) # Changing the first name did not change the email automatically. We need that funcationality.

print("=============================================================================")
# The solution is to use property attributes

class Employee :

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = str.lower(first) + "." + str.lower(last) + "@mail.com"

    @property
    def email(self):
        return str.lower(self.first) + "." + str.lower(self.last) + "@mail.com"

    def __str__(self):
        return "{} {}. Email: {}".format(self.first, self.last, self.email)


emp2 = Employee("John", "Smith")
print(emp2)

emp2.first = "Jim"
print(emp2)


print("=============================================================================")
# Setters and Deleters

class Employee :

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = str.lower(first) + "." + str.lower(last) + "@mail.com"

    @property
    def email(self):
        return str.lower(self.first) + "." + str.lower(self.last) + "@mail.com"

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    @full_name.setter
    def full_name(self, fullname):
        fn, ln = fullname.split(' ')
        self.first = fn
        self.last = ln

    @full_name.deleter
    def full_name(self):
        print("Deleting name for: {} {}".format(self.first, self.last))
        self.first = None
        self.last = None

    def __str__(self):
        return "{} {}. Email: {}".format(self.first, self.last, self.email)


emp2 = Employee("John", "Smith")
print(emp2)

emp2.full_name = 'Jim Carry'
print(emp2)

del emp2.full_name
print(emp2.first)
