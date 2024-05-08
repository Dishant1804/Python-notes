# Arithmetic operator
# + - * / % are the usual operators supported by python

# Exponentiation ** 
x = 10
y = 3
print(x ** y)

# floor division // returns the floor value after division
print(x // y)

# Assignment Operartor
# = += -= *= /= %= //= **= these are few of common assignmnet operators supported by python

# comaparision operator
# == != <= >= > < these are the comaprision operators suppoorted in python

# logical oprators
# and operator
age = 19
name = "John"
if age > 18 and age < 50:
    print("Valid driver")

# or operator
if age > 18 or age < 20:
    print("you can drive the car")

# not operator  
if not (age < 5 and age < 10):
    print("you can drive dude")

# idenetity operator
# They are used to compare the objects,that if they are actually the same object, with the same memory location
x = [1, 2, 3]
y = [1, 2, 3]
z = x

# is operator
print("is operator", x is y)
print("is operator", x is z)

# is not operator
print("is not operator", x is not y)
print("is not operator", x is not z)

# Membership operator
# they are used to test if a sequence is presented in an object

# in operator
fruits = ['apple', 'banana', 'orange']
print("in operator", 'apple' in fruits)
print("in operator", 'grape' in fruits)

# in not operator
print("in not operator", 'apple' not in fruits)
print("in not operator", 'grape' not in fruits)
