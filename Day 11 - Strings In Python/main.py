# In python, anything that you enclose between single or double 
# quotation marks is consider as a string.

Name = "Suraj"
Friend1 = "Rohit"
Friend2 = 'Vishal'
#Friend3 = Sandeep   #throw error because not enclosed in double quotes
Friend3 = "Sagar"
Friend4 = "Mohit"

print(Name)
print(Friend1, Friend2, Friend3, Friend4) 

#when We Use Triple Quotes Then Print As It Is.
apple = '''He said,
Hi Suraj
hey I'm good
I want to eat an apple'''

print(apple)

print("Hello, " + Name)
#print indexing
print(Name[0])
print(Name[1])
print(Name[2])
print(Name[3])
print(Name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop\n")
for character in apple:
    print(character)