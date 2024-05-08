# tuple
# They are immutable hence they cannot be modified
# It can contain the elements of different datatype
x = ("apple", "banana", "cherry", "kiwi", "melon", "mango")
print(x)

# using subscript operator we can access the elements. [start_index : end_index] end index is not included
print("This returns the last element : ", x[-1])  # refers to the last element in the tuple
print("This is the accesing of tuple : ", x[2:5])

# The important functions of tuple are
# count :  Returns the number of occurrences of a specified element
count = x.count("banana")
print("The count of the elements of tuple is : ", count)

# index :  Returns the index of the first occurrence of a specified element
index = x.index("cherry")
print("The index of cherry is : ", index)

# length : returns the number of elements from the set
print("The length of the tuple is : ", len(x))

# reverse : You can use slicing to achieve a reversed tuple: reversed_tuple = tuple(original_tuple[::-1])
reversed = tuple(x[::-1])
print("The reversed tuple is : ", reversed)

# slice : Similar to lists, tuples also support slicing using the syntax tuple[start:stop:step/difference]
sliced = x[::1]
print("The tuple after slicing is : ", sliced)
