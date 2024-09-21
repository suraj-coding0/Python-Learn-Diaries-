# a = "Suraj"
# b = "Maurya"
# print(a + b)

# x = 1
# y = 2                 #this is integer value
# print(x + y)

x = "1"
y = "2"  #convert into integer then add
print(int(x) + int(y))

#explicit typecasting

string = "15"
number = 7
string_number = int(
    string)  #throws an error if the string is not a valid integer
sum = number + string_number
print("The Sum of both the numbers is: ", sum)

#implicit typecasting

a = 7  #this is integer
print(type(a))

b = 3.0  #this is float
print(type(b))

# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
