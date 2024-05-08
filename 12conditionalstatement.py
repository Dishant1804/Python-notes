# The indentation matters in python especially in if-else statements
# if there is nothing to execute when the if condition is staisfied we can use pass so that if does not give error

a = 10
b = 20

# use of pass
if a < b:
    pass

# if
if b > a:
    print("true")

# if-else
if b < a:
    print("true")
else:
    print("false")

# Elif
if a > b:
    print("a is greater than b")
elif a == b - 10:
    print("a equals b")

# short hand if
if b > a: print("a is greater than b")

# short hand if else
print("b") if a < b else print("a")

# nested if
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
