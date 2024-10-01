#list is a type of datatype
#list are changeable
marks = [1,2,3,5,"suraj", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])


print(marks[-3]) # Negative index
print(marks[len(marks)-3]) # Positive index
print(marks[6-3]) # Positive index
print(marks[3]) # Positive index


if 18 in marks:           #check item present in the list.
    print("yes")
else:
    print("no")


if "suraj" in marks:
    print("yes")
else:
    print("no")


# Same thing applies for strings as well!
if "raj" in "Suraj Maurya":
  print("Yes")
else:
    print("no")


print(marks)
print(marks[:])       #python automatic take all list
print(marks[2:5])
print(marks[3:])
print(marks[:5])
print(marks[1:-3])
print(marks[1:6:2])    #jump index


# list comprehension
lst = [i for i in range(10)]
print(lst)

lst = [i*i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)