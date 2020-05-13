
# Public -
# Protected -
# Private -

class Employee:
    no_of_leaves = 8
    var = 10
    _protec = 56
    __pr = 98

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

emp = Employee("harry", 343, "Programmer")

print("\nIf you print any public var using this command print(emp.var)")
print("This is a public var number",emp.var)

print("\nIf you print any protected var using this command print(emp._protec)")
print("This is a protected var number",emp._protec)

print("\nIf you print any protected var using this command print(_emp._Employee__pr)")
print("This is a private var number",emp._Employee__pr)

print("\n for learn more about this file open this public_private_protected_access_specifiers.py file in your python editor and learn its all data.")