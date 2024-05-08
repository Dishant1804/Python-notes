# list
# It is mutable which means that it's elements can be modified
# it is similar to array with reference to other languages
# It can contain the elements of different datatype
# Duplicates are allowed in list
x = ["apple", "banana", "orange", "kiwi", "melon", "mango"]
print(x)

# accessing the items in the list
# using subscript operator we can access the elements. [start_index : end_index] end index is not included
print("This returns the last element", x[-1])  # refers to the last element in the list
print("This is the accesing of list", x[2:5])

# The important functions of list are
# append : adds an element to end of the list
x.append("pineapple")
print("appended : ", x)

# copy : Returns a shallow copy of the list
y = x.copy()
print("This is the copy of x : ", y)

# clear : Removes all elements from the list
y.clear()
print("all the elements of y are removed : ", y)

# count : Returns the number of occurrences of a specified element
count = x.count("apple")
print("the elements in x are : ", count)

# index : Returns the index of the first occurrence of a specified element
index = x.index("orange")
print("The index of orange is : ", index)

# insert : Inserts an element at a specified position
insert = x.insert(4, "strawberry")
print("strawberry inserted at index 4 : ", x)

# length : returns the number of elements from the set
print("The length of the list is : ", len(x))

# pop : Removes and returns the element at a specified index (default is the last element)
x.pop()
print("the elemnet popped is : ", x)

# remove : Removes the first occurrence of a specified element
x.remove("apple")
print("The element removed is : ", x)

# reverse : Reverses the order of elements in the list
x.reverse()
print("The reverse of the list is : ", x)

# sort : Sorts the elements of the list in ascending order
x.sort()
print("The sorted list is : ", x)

# slice : Lists support slicing using the syntax list[start:stop:step/difference]
sliced = x[0:2:1]
print("The sliced value is : ", sliced)
