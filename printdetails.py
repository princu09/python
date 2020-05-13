class Employee:
    
    def __init__(self, aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f" Name is {self.name}.\n Salary is {self.salary}. \n role is {self.role}. "

dark = Employee("dark", 120000 , "owner")

# web = Employee()

# dark.name = "dark"
# dark.salary = "150000"
# dark.role = "owner"

# web.name = "web"
# web.salary = "120000"
# web.role = "ceo"


print(dark.printdetails())