# for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print("This is for loop : ", x)

# for with break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print("This is for with break  : ", x)
    if x == "banana":
        break

# for with continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print("This is for with continue : ", x)

# for loop with range
# range accepts 3 argumnets, (start_index, end_index, difference) default start is 0 and end index is not included
# default difference is 1
for x in range(6):
    print("This for loop in range : ", x)

# for else loop
for x in range(6):
    print("This is for else loop : ", x)
else:
    print("Finally finished!")
