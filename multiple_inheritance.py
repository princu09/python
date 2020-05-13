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

class Player:
    no_of_games = 4

    def __init__(self ,name ,game):
        self.name = name 
        self.game = game 
    
    def printdetails(self):
        return f" Name is {self.name}.\n Game is {self.game}. "

class CoolProgrammer(Employee,Player):
    pass

dark = Employee("dark", 120000, "owner")
web = Employee("web", 90000, "ceo")


shubham = Player("shubham" , ["cricket"])
karan = CoolProgrammer("Karan" , 8999 , "CoolProgrammer" )

det = karan.printdetails()

print(det)