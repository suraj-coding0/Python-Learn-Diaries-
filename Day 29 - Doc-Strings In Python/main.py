# Python Comments vs Docstrings
#python comments:Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.
#python docstrings:As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.

# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)


#print Zen Of Python(poem)
import this

