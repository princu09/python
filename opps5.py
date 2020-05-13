class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f" Name is {self.name}.\n Salary is {self.salary}. \n role is {self.role}. "

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # return cls(params[0] , params[1] , params[2])

        return cls(*string.split("-"))


dark = Employee("dark", 120000, "owner")
web = Employee("web", 90000, "ceo")
karan = Employee.from_str("Karan-480-student")

print(karan.no_of_leaves)

# dark.change_leaves(34)

# print(dark.no_of_leaves)
