#In python we can raise custom error if the program is not behaving in the certain way

#there are various kinds of errors such as NameError, IndexError, TypeError, SyntaxError, LogicalError, etc.
number1 = int(input("Enter the number between 5 and 10 : "))

if(number1 < 5 or number1 > 10):
    raise ValueError("Value is not between 5 and 10")
else : 
    print("You have entered : " , number1)

# Define a custom exception
class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

# Example usage
def example_function(x):
    if x < 0:
        raise MyCustomException("x should be a positive number")

try:
    example_function(-1)
except MyCustomException as e:
    print(f"Caught custom exception: {e}")
