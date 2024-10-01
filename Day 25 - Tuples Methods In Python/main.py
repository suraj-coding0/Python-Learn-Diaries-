# Tuples are immutable, (not changeable)
#  if you want to add, remove or change tuple items, then first you must convert the tuple to a list. 
# Then perform operation on that list and convert it back to tuple.

#### Tuples ####
#we can convert tuple into list then change the data and then again convert list into tuple
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)


# we can directly concatenate two tuples without converting them to list.
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)


# we can directly concatenate two tuples without converting them to list.
num = (1,3,6,2,8,4)
name = ("suraj","Kiran","mohit","vishal","sandeep",)
combo = num + name
print(combo)


Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 3, 2, 1)
res = Tuple1.count(3)          #The count() method of Tuple returns the number of times the given element appears in the tuple.
print('Count of 3 in Tuple1 is:', res)

# tuple.index(element, start, end)
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 4)
res1 = Tuple.index(4)           #The Index() method returns the first occurrence of the given element from the tuple.
print('First occurrence of 3 is', res1)

res = len(Tuple1) 
print(res)