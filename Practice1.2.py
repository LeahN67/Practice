print("Hello World")
print("""Print 
Multiple 
Lines""")
print('Hello World')
print(42.5)
print(42)
a = 10
b = "ten"
print(a)
print(b)

a = 10
print(a)
a = a + 1
print(a)

a=10
print(f'The value of a is {a}') #use of f-strings. The f-string is denoted by placing an "f" just in front of the opening single or double quote that begins the string.

b=23
print(f'Your balance is: {b}')

a=10
print(f'The value of a plus 5 is: {a+5}')

a=5
print(f'The value of a is:{a}')
print('The value of a is:{}'.format(a))
print('The value of a is:' + str(a))
print('The value of a is:%d'%(a))

a=5
if a>5:
    print('The variable a is greater than 5.')
else:
    print('The value is not greater than 5.')

a=5
b=6
if a==5:#assign values
    print('The value of a is 5')
    if b==6:#shows equality
        print('The value of b is 6')
    elif a==6:
        print('The value of a is 6')

for x in range(0,10):
    print(x)

acc=0
for x in range(0,10):
    acc+=x
    print(f'Adding {x}, so far the sum is {acc}')

print(f'Final sum is:{acc}')





