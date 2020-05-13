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
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class programmer(Employee):
    def __init__(self, aname, asalary, arole , languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f" Programmers Name is {self.name}.\n Salary is {self.salary}. \n role is {self.role}.\nThe Language are {self.languages}."

dark = Employee("dark", 120000, "owner")
web = Employee("web", 90000, "ceo")

shubham = programmer("shubham" , 555 , "programmer" , ["python"])
karan = programmer("karan" , 777 , "programmer" , ["python" , "cpp"])

print(karan.printprog ())