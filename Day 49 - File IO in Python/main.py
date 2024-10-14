# File Input/output Function

# *** Open And Read The File  Of Using 'R  Keyword ***
f = open('myfile.txt', 'r')   #read mode is default if we remove "r keyword" file also read
# print(f)

text = f.read()
print(text)
# f.close()


# *** Creating A New File Of Using 'W' Keyword ***
f = open('myfile2.txt', 'w')   
f.write("Hello, World!")        #write Content
f.close()

# *** Append A New Content In File Of Using 'A' Keyword ***
f = open('myfile2.txt', 'a')   
f.write("My Name Is Suraj Maurya")
f.close()


with open('myfile2.txt', 'a') as f:
  f.write("Hey I am inside with")