
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

#----------this is add operator dunder method------------------------

    def __add__(self , other):
        return self.salary + other.salary

#----------this is truediv operator dunder method------------------------

    def __truediv__(self , other):
        return self.salary / other.salary

#----------this is repr operator dunder method------------------------

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

#----------this is str operator dunder method------------------------

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


emp1 = Employee("Harry" , 3450 , "Programmer")
emp2 = Employee("Rohan" , 50 , "Cleaner")

print("\nThis is add operator dunder method value")
print(emp1 + emp2)

print("\nThis is truediv operator dunder method value")
print(emp1 / emp2)

print("\nOpen Code Editor and comment  define (def __str__(self):) Then change below this line \n")

print("↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓")

print(str(emp1))

print("\nMapping Operators to Functions pdf in this folder check it.")