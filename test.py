class Person:
    def __init__(self):
        self._name = None
        self._age = None

    @property
    def get_attributes(self):
        return f'Name : {self._name} , age : {self._age}'

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter 
    def name(self , value):
        self._name = value

    @age.setter
    def age(self , value):
        self._age = value

obj = Person()
obj.name = "Priya"
obj.age = 23
print(obj.get_attributes)

        