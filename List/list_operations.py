# Initializing a List
list1 = [1,2,3]

# Accessing a value from list
print(list1[0])
print(list1[1])
print(list1[2])

# Iterating over list
for i in list1:
    print(i)

# Length of a list Using len()
print(len(list1))

# Adding an element to list
list1.append(4)

# Remove last element of list
a = list1.pop()
print('value =',a)
print(list1)

# Remove value at specific index
a = list1.pop(1)
print(list1)

# Using del()
del list1[1]
print(list1)

# Clear all values in list
list1.clear()
print(list1)

list1.append(5)
print(list1)

# Insert value at specific index
list1.insert(1,4)
print(list1)

# Sort list
list1.sort()
print(list1)

# Remove a specific value from list
list1.remove(4)
print(list1)

# Count of a specific value in list
print(list1.count(5))

# Extend the list using extend() and + operator
list1.extend([1,2,3])
print(list1)
list1 = list1+[6,7,8]
print(list1)

# Reverse of list
list1.reverse()
print(list1)

# Get index of an element from list
print(list1.index(5))

# Copy an array
list2 = list1.copy()
print(list2)

# Update value of a specific index
list2[0] = 0
print(list2)