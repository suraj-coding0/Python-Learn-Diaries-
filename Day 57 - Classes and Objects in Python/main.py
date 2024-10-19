class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):       # Wo object jisper ye method call ho rha hai
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()        #A Data Prints
b.info()        #B Data Prints
c.info()        #Default Data Print
