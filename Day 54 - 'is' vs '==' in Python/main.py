# In Python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that you should be aware of.

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # exact location of object in memory
print(a == b) # value


a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True