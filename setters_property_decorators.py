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

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


dark = Employee ("Dark" , "Duniya")
web = Employee ("Web" , "Duniya")

print(dark.explain())
print(web.explain())

dark.fname = "US"

print(dark.email)

dark.email = "dark.1908@dw.net"

print(dark.email)

del dark.email

print(dark.email)

print("\nHere comes an error because the email has been deleted using del function\n")
web.email = "web.1908@dw.net"

print(web.email)

print("\nFor learn how to run and access setters & property decorators , open this file in your editor and learn about this file")
print("\nThank You\n")