class Employee:
    def __init__(self , fname , lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@dw.net"

    def explain(self):
        return f"The employee name is {self.fname} {self.lname}."

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Error : Email is not found , please set your email first using setter"
        return f"{self.fname}.{self.lname}@dw.net"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]


skillf = Employee("skill", "f")
print(skillf.email)

# print("\nHere i print a id which store in backhand\n")
# print(id("This is id\n"))

# print("\nHere i print a dir which store in backhand\n")
# print(dir("This is id"))

#-----------------------Here i import inpect module and print all members----------------------------------

import inspect
# print(inspect.getmembers(skillf))

print("\n-------------------------------------------------------------------------------------------------------------------")
print("Note : open this file and comment out one by one line and learn it all commands its very important in python")
print("\nIf you learn more about inspect module a pdf availbe in this folder.")
print("\nFor learn how to run and access object_introspection , open this file in your editor and learn about this file")
print("\nThank You\n")
