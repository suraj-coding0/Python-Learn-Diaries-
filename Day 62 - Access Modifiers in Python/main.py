class Employee:
    def __init__(self):
        self.__name = "Suraj Maurya"

a = Employee()

#***** Public Access Modifier ****** 
# print(a.name)    #Access Name In Public Access Modifier
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)



#***** Private Access Modifier ****** 
# print(a.__name)   # Cannot Be Accessed Directly
print(a._Employee__name)  # Can Be Accessed Indirectly
print(a.__dir__())     # Show All Mathods.

# Example:-
class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())




#***** Protected Access Modifier ****** 
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())
print(dir(obj))