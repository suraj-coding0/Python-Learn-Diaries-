# x = (1, 2, 3, 4)
# dir(x)
# print(dir(x))             # Dir Method
# print(x.__add__)


class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.version = 1

    
p = Person("John", 30)
print(p.__dict__)           #__Dict__ Object

print(help(Person))         # Help Object