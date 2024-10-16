# with open('file.txt', 'r') as f:
#   print(type(f))
#   # Move to the 10th byte in the file
#   f.seek(5)     #leave the data before 5 word 

#   # Read the next 5 bytes
#   print(f.tell())
#   data = f.read(3)     #count the data after 5 words
#   print(data)



with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
  print(f.read())