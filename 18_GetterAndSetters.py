# getters and setters

class person():
    # The initial value is set to none
    def __init__(self):
        self._name = None  # The underscore before the variable name is naming convention for protected variables
        self._age = None

    # The property annotation is known as decorator which converts this method into getter method implicitly
    @property
    def get_attribute(self):
        return f"Name : {self._name} , Age : {self._age}"

    # We have to define the name and age property so that we can set their value
    # These are actually the getter methods which are used to give the output
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # The setters are formed when we add the annotation with the method_name.setter
    # remember that we had defined the _name in getter method which is used here
    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value


obj_person = person()
obj_person.name = "John"
obj_person.age = 30

# the parenthesis are not used when we are defining the property annotation above the method
attribute = obj_person.get_attribute  # here parenthesis is not needed

print(attribute)
