# def keyword is used to declare a function in python
def foo():
    print("This is the user defined function")


foo()


# arguments and parameters can also be passed in python
# age_of_person is known as function parameter
def age(age_of_person):
    print("The age you hav entered is : ", age_of_person)


age(19)  # 19 which is passed to the function is known as argument


# default parameter value in python
# if no parameter is sent by user the default parameter will get executed
def country(country="india"):
    print("I am from this country : ", country)


country("sweden")


# there is no need to specify the datatype of the parameter in python
def food(fruits):
    for x in fruits:
        print(x)


fruits = ["pineapple", "apple", "strawberry", "kiwi"]
food(fruits)
