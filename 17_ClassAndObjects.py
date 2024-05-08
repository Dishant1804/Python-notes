# class is declared using class keyword
class Demo():
    x = 10


# obj is the reference object used to access the elements of the class
obj = Demo()
print(obj.x)


# __init__() is nothing but just default constructor in python which is used to det the initial values of the class
# it is automatically called when the class is being used to create the new object
# self is the required attribute as it is responsible for setting the reference of the instance which is created
class checking_init():
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj_of_init = checking_init("John", 26)
print(obj_of_init.name, obj_of_init.age)


# __str__() is used to format the output of the code which the f before a string in the return statement is used to
# create a formatted string, also known as an f-string. #F-strings provide a concise and convenient way to embed
# expressions inside string literals.
class checking_str():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name : {self.name} , Age : {self.age}"


obj_of_str1 = checking_str("John Doe", 35)
obj_of_str2 = checking_str("Garry white", 26)
print("This is obj 1 ", obj_of_str1, "\nThis is obj 2 ", obj_of_str2)


# methods inside class
class creating_methods:
    def foo(self):
        print("This is the method")

    def add(self, x, y):
        return x + y


obj_of_creating_method = creating_methods()
print("The sum of 10 and 20 is : ", obj_of_creating_method.add(10, 20))
