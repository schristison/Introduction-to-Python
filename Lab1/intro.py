print('Hello World')

name = 'Sandie'
last_name = 'Cee'
age = 99
found = False
average = 48.75

print(name)
print(last_name)
print(found)
print(average)

print(21 + 21)
print(age - 1)
print(78 * 121)
print(123 / 32)
print(10 % 3) # % = modulus operator (returns the residue of the division)

def test():
    print("inside the function")
    print("this too")
    print('outside the function')

def separator():
    print('----------------------------------------------------')


test()

separator()

print(name + last_name)
print(10 * name)

separator()
print(name + str(23)) # str converts the number into a string

separator()

if(age < 90):
    print('You are still young')
elif(age == 90):
    print('You are on the border line')
else:
    print('Sorry bud, you are officially old')