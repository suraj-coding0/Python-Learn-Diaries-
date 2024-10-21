class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id 

    #make method name of showdetail
    def showDetails(self):
        print(f"The Name Of Employee is: {self.name} and id is: {self.id}")

class programmer(employee):
    def showLanguage(self):
        print("The Default Language Is Python")


e1 = employee("Suraj Maurya", 400)
e1.showDetails()
e2 = programmer("Rohan Das", 600)
e2.showDetails()
e2.showLanguage()