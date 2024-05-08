# while loop
i = 1
while i < 6:
    print("This is while loop : ", i)
    i += 1

# while else is supported in python
i = 1
while i < 6:
    print("while else loop : ", i)
    i += 1
else:
    print("i is no longer less than 6")

# break with while
i = 1
while i < 6:
    print("This is while with break : ", i)
    if i == 3:
        break
    i += 1

# continue with while
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print("This is while with continue : ", i)
