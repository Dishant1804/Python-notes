# single line string
a = "Hello world"
print(a)

# multi line string
a = """This is multiline statement
in python"""
print(a)

# get the char at particular index
a = "Hello, World!"
print("this is the character at particular position", a[1])

# looping over string gives array of chars
for x in "banana":
    print(x)

# length function returns the length of the given string
a = "Hello, World!"
print(len(a))

# checking the words in string returns a boolean value
txt = "This is a statement"
print("This" in txt)

# slicing of string [start_index : end_index] the end index is not included. default start index is 0
b = "Hello, World!"
print(b[2:5])
print(b[1:-2])

# uppercase the string
a = "hello"
print(a.upper())

# lowercase the string
a = "HELLO"
print(a.lower())

# strip : removes the whitespaces in beginning and end
a = " hello world..! "
print(a.strip())

# replace : replaces te element in the string. it accepts 2 arguments (word_to_replace , word_to_replace_it )
a = "Hello, World!"
print(a.replace("World", "Dishant"))

# split : splits the list into substrings. It accepts the argument which is the seperator
a = "hello, World"
print(a.split(","))

# concate the strings
a = "hello"
b = "world"
print(a + " " + b)

# format : method to insert numbers in string
age = 25
month = 10
txt = "I am John and my age is {} and {} month"
print(txt.format(age, month))

# another exaample with index number
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
