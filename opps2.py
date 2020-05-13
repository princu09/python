class Employee:
    no_of_leaves = 8
    pass

dark = Employee()
web  = Employee()
 
dark.name = "dark"
dark.salary = "150000"
dark.role = "owner"

web.name = "web"
web.salary = "120000"
web.role = "ceo"

print(dark.__dict__)
print(web.__dict__)