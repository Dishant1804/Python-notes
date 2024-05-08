x = "hi"  # The variable created outside the function has global scope


def foo():
    x = 10  # The variable created inside the local function has local scope
    global y  # The variable created using global keyword will have global scope even if it is created inside a fn
    y = "hello"
    print("The value of x in function is : ", x)
    print("The value of y in function is : " + y)


foo()

print("The value of x is : " + x)
print("The value of y is : " + y)
