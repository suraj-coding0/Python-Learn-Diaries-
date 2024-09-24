#strings are immutable

a = "suraj"
b = "Maurya"
print(a)
print(len(a))
print(a.upper())  #The upper() method
print(b.lower())  #The lower() method

# str2 = " Silver Spoon "
# print(str2.strip)         #The strip() method

str3 = "Hello !!!"
print(str3.rstrip("!"))  #The rstrip() method
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

name = "suraj maurya i am learning python"
print(name.replace("suraj", "Ananya"))  #the replace method

print(name.split(" "))  #the split method

blogheading = "introDuctIon to pyThon"
print(blogheading.capitalize())  #the Capitalize method

heading = "welcome to the console"
print(heading.center(40, "."))  #the center method
print(len(heading.center(40)))
print(len(heading))

title = "i am a boy i am pursuing bca i am from delhi"
print(title.count("am"))  #the count method

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))  #the endswitch() method
print(str1.endswith("to", 4, 10))

str1 = "He's name is ram. He is an honest man."
print(str1.find("ish"))  #the find() method
# print(str1.index("ish"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())  #the isalnum() method
str1 = "Welcome00"
print(str1.islower())  #the islower() method

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
str2 = "we wish you a merry christmas\n"
print(str2.isprintable())  #the isprintable() method

str1 = "        "  #using Spacebar
print(str1.isspace())
str2 = "        "
print(str2.isspace())  #the isspace() method

str1 = "World health Organization"
print(str1.istitle())  #the istitle() method

str1 = "WORLD HEALTH ORGANIZATION"
print(str1.isupper())  #the isupper method

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))  #the startswith() method

str1 = "Python is a Interpreted Language"
print(str1.swapcase())  #the swapcase() method

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())  #the title() method
