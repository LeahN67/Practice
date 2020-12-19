#LISTS AND TUPLES...
l=['a','b','c','d']
t=('a','b','c','d')

print(l)
print(t)

#lists are mutable...
l[2]='changed'
print(l)
#Tuple cannot be changed ,meaning it is immutable...
#t[2]='changed'~This would lead to an error...
#print(t)

#for-each statement
for s in l:
    print(s)

for r in t:
    print(r)

#enumerate function
#Python is zero based
for i,l in enumerate(l):
    print(f'{i}:{l}')

for h,t in enumerate(t):
    print(f'{h}:{t}')
#Tuples do not allow the program to add additional objects after definition...
#add and have duplicates in lists...
c=[]
c.append('a')
c.append('b')
c.append('c')
c.append('c')
print(c)

#allow you to access an element by its index number
print(c[1])
#insert...
c.insert(0,'a0')
print(c)
c.insert(1,'b1')
print(c)
#Remove...
c.remove('b')
print(c)
#Delete at index...
del c[0]
print(c)

#SETS...
#A Python set holds an unordered collection of objects, but sets do not allow duplicates.
s=set()
s={'a','b','c','d'}
s=set(['a','b','c','d'])
print(s)
#A Python set holds an unordered collection of objects, but sets do not allow duplicates.
# Manually add items, sets do not allow duplicates
# Sets add, lists append.
c=set()
c.add('a')
c.add('b')
c.add('c')
c.add('c')
print(c)

#MAPS/DICTIONARIES/HASH TABLES...
d={'name': "Jeff", 'Address': "123 Main"} #Dictionary
print(d)
print(d['name'])

if 'name' in d:
    print("Name is defined")
    if 'Age' in d:
        print("Age is defined")
    else:
        print("Age is undefined")

#access the directory and provide a default value
d.get('unknown_key', 'default')
#access the individual keys and values of a dictionary.
print(f'Keys:{d.keys()}')
print(f'Values:{d.values()}')


# Python list & map structures
customers= [{"Name":"Jeff & Tracy Heaton","Pets":["Wynton", "Cricket",
        "Hickory"]},{"Name":"John Smith", "Pets":["Rover"]}, {"Name":"John Doe"}]
print(f'Our Customers are :{customers}')

for customer in customers:
    print(f"{customer['Name']}:{customer.get('pets','no pets')}")

#More Advanced Lists
a=[1,2,3,4,5,6]
b=[7,8,9,0,1,2]
print(zip(a,b))

print(list(zip(a,b)))

for x,y in zip(a,b):
    print(f'{x}-{y}=',(x-y))

a=[1,2,3,6,7,8,5]
for i,x in enumerate(a):
    if x>5:
        a[i]=5
print(a)

lst=[x*10 for x in range(2,10)]
print(lst)

text={'Leah','Toto','Mum'}
lookup={key:value for (value,key) in enumerate(text)}
print(lookup)

print(f'The column number of Leah is: {lookup["Leah"]}')

#An Introduction to JSON
import json
json_string = '{"first":"Jeff","last":"Heaton"}'
obj = json.loads(json_string)
print(f"First name: {obj['first']}")
print(f"Last name: {obj['last']}")


python_obj = {"first":"Jeff","last":"Heaton"}
print(json.dumps(python_obj))














