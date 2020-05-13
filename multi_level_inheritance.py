class Dad:
    basketball = 6

class Son(Dad):
    dance = 1
    basketball = 9 
    def isdance(self):
        return f"Yes I dance {self.dance} no of times."

class GrandSon(Son):

    dance = 6
    guitar = 1
    
    def isdance(self):
        return f"Jackson yeah ! " \
            f"Yes i dance awesomely {self.dance} no of times."

darry = Dad()
larry = Son()
harry = GrandSon()

print(harry.basketball)