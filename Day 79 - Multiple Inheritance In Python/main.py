# Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.

### Syntax:- 
''' class ChildClass(ParentClass1, ParentClass2, ParentClass3):
    # class body '''

### Example:-
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"the name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"the dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

obj = DancerEmployee("kathak", "Kiran")
print(obj.name)
print(obj.dance)

obj.show()          # Jo First Pe Hoga Wo Pahle Print Hoga

print(DancerEmployee.mro()) 