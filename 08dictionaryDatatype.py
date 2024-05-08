# dictionary
# Dictionaries are used to store data values in key:value pairs
# Dictionaries are mutable, allowing the addition, modification, and removal of key-value pairs
x = {
    "name": "john",
    "age": 19,
    "year": 2004,
}
print(x)

# accessing the particular element from the dict
print(x["age"])

# Some of the important functions of dictionary are
# copy : Returns a shallow copy of the dictionary
y = x.copy()
print("This is the copy of dictionary : ", y)

# clear : Removes all key-value pairs from the dictionary
y.clear()
print("This is the cleared dictonary : ", y)

# get : Returns the value for a given key; if the key is not present, returns a default value or None
print("This the get method of the dictonary : ", x.get("name"))

# items : Returns a view of all key-value pairs as tuples
print("This the key value pairs of the dictonary : ", x.items())

# keys : Returns a view of all keys in the dictionary
print("The keys of the dictonary are : ", x.keys())

# pop : Removes and returns the value for a specified key. Raises an error if the key is not present
print("This is the pop method : ", x.pop("year"))

# popitem : Removes and returns an arbitrary key-value pair as a tuple. Raises an error if the dictionary is empty
print("This is the popped item : ", x.popitem())

# values : Returns a view of all values in the dictionary
print("This are the values of the dictionary : ", x.values())

# update : Updates the dictionary with key-value pairs from another dictionary or iterable
x.update({"sex": "male"})
print(x)
