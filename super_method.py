class A:
    classvar1 = "I am in Super class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's contructor"
        self.classvar1 = "Instant var in class A"
        self.special =  "special"

class B(A):
    classvar2 = "I am in class B"

    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's contructor"
        self.classvar1 = "Instant var in class B"

        print(super().classvar1)


a = A()
b = B()

print(b.special , b.var1 , b.classvar1)

print("\n \nfor more learn about super method open this file code in your code editor and learn it")