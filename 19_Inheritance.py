class Animal:
    def __init__(self, name):
        self._name = name

    def speak(self):
        pass  # this is the abstract method which is to be overridden


class Dog(Animal):
    def speak(self):
        return f"{self._name} says woof"


class Cat(Animal):
    def speak(self):
        return f"{self._name} says meow"


obj_dog = Dog("brudo")
obj_cat = Cat("coconut")
print(obj_dog.speak())
print(obj_cat.speak())
