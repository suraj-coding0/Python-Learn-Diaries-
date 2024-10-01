list = [1,3,4,3,8,2,3,5,6,3]
print(list)
# list.append(7)              #appends items to the end of the existing list
# print(list)
# list.sort()                  #sorts the list in ascending order
# print(list)              
# list.sort(reverse=True)      #print the list in descending order
# print(list)
# list.reverse()               #This method reverses the order of the list.
# print(list)
# print(list.index(2))         #This method returns the index of the first occurrence of the list item.
# print(list.count(3))         #Returns the count of the number of items with the given value.


colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()          #Returns copy of the list.
print(colors)
print(newlist)

list.insert(1,100)              #inserts an item at the given index
print(list)                 


m = [900, 1000, 1100]
list.extend(m)                  # adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
print(list)

# You can simply concatenate two lists to join two lists.

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)                 