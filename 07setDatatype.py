# set
# They are mutable, allowing addition and removal of elements.
# It contains only unique elements , duplicate values are not allowed in set
# They are unordered collections, meaning the elements do not have a specific order.
# It can contain the elements of different datatype
x = {
    "car",
    "bike",
    "scooty"
}
y = {
    "car",
    "truck"
}
print(x)

# The important functions of set are
# add : Adds an element to the set. If the element is already present, it does nothing
x.add("truck")
print(x)

# copy : Returns a shallow copy of the list
z = x.copy()
print(z)

# clear : Removes all elements from the list
z.clear()
print(z)

# difference : Returns a new set containing elements that are present in the first set but not in the others
diff = x.difference(y)
print(diff)

# discard : Removes a specified element from the set but does not raise an error if the element is not present
discardedElement = x.discard("bike")
print(discardedElement)

# intersections : Returns a new set containing common elements between two or more sets
intersected = x.intersection(y)
print(intersected)

# length : Returns the number of elements in the set
print(len(x))

# pop : Removes a specified element from the set. Raises an error if the element is not present
x.pop()
print(x)

# union : Returns a new set containing all unique elements from the sets being unioned
union = x.union(y)
print(union)
