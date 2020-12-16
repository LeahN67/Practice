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




