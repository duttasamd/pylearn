# class Employee :
#     pass
#
# # Even an empty class can be initialized.
# print(Employee()) # <__main__.Employee object at 0x10303b550>

# ================================================================================================================

# Free form. Classes can have methods that expect the implementor to add certain attributes that are not declared
# in the class definition.


class Employee :
    def tostring(self):
        return '{} {}'.format(self.first_name, self.last_name)


emp1 = Employee()

emp1.first_name = "Samrat"
emp1.last_name = "Dutta"
emp1.email = "samrat@dutta.com"

emp2 = Employee()

emp2.first_name = "Sam"
emp2.last_name = "D"
emp2.email = "sam@d.com"

print(emp1.first_name)
print(emp2.first_name)

print(emp1.tostring())
print(emp2.tostring())

# ======================================================================================

# Constructors and the __str__ method for prettifying the string representation.
# We look at the __repr__ method later.


class Student :

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return '{} {}. Email : {}'.format(self.first_name, self.last_name, self.email)


st1 = Student('stu1', 'dent1', 'stu1@dent1.com')
st2 = Student('stu2', 'dent2', 'stu2@dent2.com')

print(st1)
print(st2)

# ========================================================================================

# Class variables. [Equivalent to static variables.]
# Let us redefine the Employee class.

class Employee :
    num_of_employee = 0
    hike = 30

    def __init__(self, fn, ln, pay):
        Employee.num_of_employee += 1
        self.first_name = fn
        self.last_name = ln
        self.pay = pay

    def __str__(self):
        return '{} {}\'s pay is: {}'.format(self.first_name, self.last_name, self.pay)

    def raisepay(self):
        self.pay = self.pay + (Employee.hike/100)*self.pay

emp1 = Employee("emp", "1", 300)
emp2 = Employee("emp", "2", 300)

print(emp1)
emp1.raisepay()
print(emp1)

Employee.hike = 40

print(emp2)
emp2.raisepay()
print(emp2)

print(emp1.hike)

print("==========================================================================")

# print namespace of employee object. Variables in the object.

print(emp1.__dict__)

# print namespace of the class.

print(Employee.__dict__)

print("==========================================================================")

print("Printing hikes.")
print("emp1", emp1.hike)
print("emp2",  emp2.hike)

print(Employee.hike)

Employee.hike = 50

print("Changed Employee.hike to 50")
print("emp1", emp1.hike)
print("emp2", emp2.hike)

print(Employee.hike)


emp1.hike = 60 # creates a new instance variable called hike and overrides the class variable.
print("Changed emp1.hike to 60")


print("emp1", emp1.hike)
print("emp2", emp2.hike)

print(Employee.hike)

print("num employees :", Employee.num_of_employee)
print("==========================================================================")

