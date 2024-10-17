#______MAP_______

# def cube(x):
#     return x*x*x

# print(cube(5))

l = [1,2,4,6,4,3]
# newlist = []
# for items in l:
#     newlist.append(cube(items))
# print(newlist)

newl = list(map(lambda x: x*x*x, l))
print(newl)

#______FILTER_______

def filter_function(k):
    return k>3
#jin value ke liye filter_function true return karega wo output me aajayega.
newnewl = list(filter(filter_function, l))
print(newnewl)


#______Reduce_______

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8] # first two value ko add karte rahna hai 
result = reduce(lambda x, y: x + y, numbers)
print(result)

