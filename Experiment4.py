# List operations using inbuilt methods

# Creating a sample list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Display the original list
print("Original List:", my_list)

# Append an element to the end of the list
my_list.append(8)
print("After Append:", my_list)

# Insert an element at a specific index
my_list.insert(2, 7)
print("After Insert:", my_list)

# Remove the first occurrence of a specific element
my_list.remove(1)
print("After Remove:", my_list)

# Pop an element at a specific index
popped_element = my_list.pop(3)
print("Popped Element:", popped_element)
print("After Pop:", my_list)

# Extend the list with another list
extension_list = [0, 2, 4, 6]
my_list.extend(extension_list)
print("After Extend:", my_list)

# Reverse the order of elements in the list
my_list.reverse()
print("After Reverse:", my_list)

# Sort the list in ascending order
my_list.sort()
print("After Sort (Ascending):", my_list)

# Sort the list in descending order
my_list.sort(reverse=True)
print("After Sort (Descending):", my_list)

# Find the index of a specific element
index_of_5 = my_list.index(5)
print("Index of 5:", index_of_5)

# Count occurrences of a specific element
count_of_5 = my_list.count(5)
print("Count of 5:", count_of_5)

# Create a shallow copy of the list
copy_of_list = my_list.copy()
print("Shallow Copy:", copy_of_list)

# Clear all elements from the list
my_list.clear()
print("After Clear:", my_list)
