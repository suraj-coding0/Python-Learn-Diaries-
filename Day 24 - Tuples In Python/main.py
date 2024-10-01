tup = (1,)
print(type(tup), tup)

tup = (1,5,8,9,7,83,7,9,1,3)
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[-2])
# print(tup[18])
print(len(tup))


num = int(input("enter the number:"))
if num in tup:
    print("yes", num, "is present in this tuple")
else:
    print("no", num, "is not available in this tuple")

tup2 = tup[2:6]         #slicing
print(tup2)

print(tup[:5])


country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])


country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:            #in keyword
    print("Germany is present.")
else:
    print("Germany is absent.")



animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])       #jump index