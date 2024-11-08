
import re

# pattern = "sure"
# pattern = "was"
pattern = r"[A-Z]+yclone"

text = '''
Returns a cyclone match if the specified characters are at the beginning of the string Returns a match where the specified Cyclone characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string") Returns a match where the specified characters are Myclone present, but NOT at the Dyclone beginning (or at the end) of a word (the "r" in the beginning is making sure that Pyclone the string is being treated hyclone Syclone as a "raw string")
'''

# match = re.search(pattern, text)  # Stop In Firt Match
# print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])