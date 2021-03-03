friends = ["Bob", "Zoey", "Hank", "Bri", "Allen"]
numbers = [2, 4, 6, 8]

# Friend at index 0
print(friends[0])

# Access the last index
print(friends[-1])

# Indexes 1 and greater
print(friends[1:])

# Indexes from 1 up to but not including 3
print(friends[1:3])

# Add a list to the end of a list
# List can have different datatypes in it
friends.extend(numbers)
print(friends)

# Insert will add an element to the list at a specific index. Previous and all elements will be pushed up 1 accordingly.
friends.insert(1, "Jay")
print(friends)

# Count occurences of value in list
print(friends.count("Jay"))

# Sorting with list
# Will throw error if list contains different datatypes in a single list
print(friends)