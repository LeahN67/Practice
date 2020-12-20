#Functions, Lambdas, and Map/Reduce
def say_hello(speaker, person_to_greet, greeting = "Hello"):
    print(f'{greeting} {person_to_greet}, this is {speaker}.')

say_hello("Leah","Pauline")
say_hello("Pauline","Leah","Goodbye")
say_hello(speaker="Leah",person_to_greet="Pauline",greeting="Goodbye")

#A function is a way to capture code that is commonly executed

def process_string(str):
    t = str.strip() #Remove spaces at the beginning and at the end of the string
    return t[0].upper()+t[1:]
str= process_string("hello")
print(f'{str}')

#Maps
#The map function takes a list and applies a function to each member of the list and returns a second list that is the same size as the first

l = ['   apple  ', 'pear ', 'orange', 'pine apple  ']
print(list(map(process_string, l)))

#Comprehension

l = ['   apple  ', 'pear ', 'orange', 'pine apple  ']
l2 = [process_string(x) for x in l]
print(l2)
#While a map function always creates a new list of the same size as the original, the filter function creates a potentially smaller list.
#Map
def greater_than_five(x):
    return x>5

l = [ 1, 10, 20, 3, -2, 0]
print(list(map(greater_than_five, l)))

#Filter
def greater_than_five(x):
    return x>5

l = [ 1, 10, 20, 3, -2, 0]
l2 = list(filter(greater_than_five, l))
print(l2)

#Lambda
#A lambda is essentially an unnamed function.

l = [ 1, 10, 20, 3, -2, 0]
l2 = list(filter(lambda x: x>5, l))
print(l2)

#Reduce
from functools import reduce
l = [ 1, 10, 20, 3, -2, 0]
result = reduce(lambda x,y:x+y,l)
print(result)

