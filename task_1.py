# Creating a List
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Adding an element to the list
my_list.append(6)
print("List after adding an element:", my_list)

# Removing an element from the list
my_list.remove(2)
print("List after removing an element:", my_list)

# Modifying an element in the list
my_list[0] = 10
print("List after modifying an element:", my_list)

# Creating a Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nOriginal dictionary:", my_dict)

# Adding a key-value pair to the dictionary
my_dict['d'] = 4
print("Dictionary after adding a key-value pair:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict['b']
print("Dictionary after removing a key-value pair:", my_dict)

# Modifying a value in the dictionary
my_dict['a'] = 10
print("Dictionary after modifying a value:", my_dict)

# Creating a Set
my_set = {1, 2, 3, 4, 5}
print("\nOriginal set:", my_set)

# Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(2)
print("Set after removing an element:", my_set)

# Sets are unordered collections, so modifying a specific element is not directly possible.
# However, you can remove and re-add elements as needed.

# Example of removing and re-adding an element
my_set.discard(3)  # remove element if it exists
my_set.add(10)     # add new element
print("Set after removing and adding an element:", my_set)
