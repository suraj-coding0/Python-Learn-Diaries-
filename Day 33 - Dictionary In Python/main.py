#Dictionaries are ordered collection of data items.
#They store multiple items in a single variable.
#Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

dict = {
    "Suraj": "Human being",
    "Chair": "object",
    "Virat Kohli":"Cricketer"
}

print(dict["Virat Kohli"])

dict2 = {
    344:"Harry",
    56:"Suraj",
    311:"Kiran",
    535:"Rohit",
    489:"Vishal"
}

print(dict2[311])

info = {'name':'Kiran', 'age':19, 'eligible':True}
print(info["age"])
print(info.get('eligible'))
print(info.keys())      #show all keys 
print(info.values())    #show all values

# info1 = {'name':'Karan', 'age':19, 'eligible':True}
# print(info1["age2"])           #if key does not exist in dictionary then show errors
# print(info1.get('eligible2'))  #if key does not exist in dictionary then sshow none

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")