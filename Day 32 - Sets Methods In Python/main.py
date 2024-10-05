# s1 = {1,4,2,8,4,5}
# s2 = {6,3,2,8,10,1,7}

# print(s1.union(s2))              #union
# print(s1.intersection(s2))       #intersection

# s1.update(s2)        # all s2 data add in s1 set
# print(s1, s2)


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
# print(cities)


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Berlin", "Delhi"}
# cities3 = cities.difference(cities2)
# print(cities3)


# *********************************************

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}         #atleast one element can match then cannot disjoint(false)
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))


cities = {"Tokyo", "Kabul", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kabul",}                   
print(cities.issuperset(cities2))               #all cities2 element available in cities
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities)) 


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")              #add Method
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)              #update Method
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")               #remove Method
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Seoul")               #discard Method
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()                   #random value pop
print(cities)
print(item)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities                           #delete set
# print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()                        #clear all element
print(cities)


info = {"Carla", 19, False, 5.9}        #check if item exists
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")