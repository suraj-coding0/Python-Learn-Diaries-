# Inheritance in python

# When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

# Python Inheritance Syntax
# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#   Body of derived class

# Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.

##### Types of inheritance:

# 1.Single inheritance
# 2.Multiple inheritance
# 3.Multilevel inheritance
# 4.Hierarchical Inheritance
# 5.Hybrid Inheritance

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()


# Add the __init__() Function

# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).

# class Student(Person):
#   def __init__(self, fname, lname):
    #add properties etc.

'''class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)'''


# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)