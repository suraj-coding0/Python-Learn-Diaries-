#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# Before Python 3.6 we had to use the format() method.
# F-string allows you to format selected parts of a string.
# To specify a string as an f-string, simply put an f in front of the string literal, like this:


price = 49                  #format () method
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3                #Placeholders and Modifiers
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

def myconverter(x):             #Perform Operations in F-Strings
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

price = 59                      #Perform Operations in F-Strings
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

# letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Harry"

# print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")


price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
print(type(txt.format()))


print(f"{2 * 30}")
print(type(f"{2 * 30}"))


val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")


import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")