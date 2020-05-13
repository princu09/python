class Employee:
    no_of_leaves = 8
    
    def __init__(self, aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f" Name is {self.name}.\n Salary is {self.salary}. \n role is {self.role}. "

    @classmethod
    def change_leaves(cls , newleaves):
        cls.no_of_leaves = newleaves
        
dark = Employee("dark", 120000 , "owner")
web = Employee("web", 90000 , "ceo")

dark.change_leaves(34)

print(dark.no_of_leaves)