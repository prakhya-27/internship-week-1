# Creating a List
n=int(input('enter no. of elements u want in ur list: '))
my_list = [int(input()) for i in range(n)]
print("Original list:", my_list)

# Adding an element to the list
ele_to_append = int(input('enter the element you would like to append:\n'))
my_list.append(ele_to_append)
print("List after adding an element:", my_list)

# Removing an element from the list
ele_to_remove=int(input('enter element you owuld like to remove:\n'))
my_list.remove(ele_to_remove)
print("List after removing an element:", my_list)

# Modifying an element in the list
ele_to_modify=int(input('enter element you would like to modify:\n'))
ele_to_add = int(input("enter the new element \n"))
index=next(i for i in range(len(my_list)) if my_list[i]==ele_to_modify)
my_list[index] = ele_to_add
print("List after modifying an element:", my_list)


# Creating a Dictionary
ele=int(input('enter no. of elements in dictionery:\n'))
my_dict = {i:int(input('enter element:')) for i in range(ele)}
print("\nOriginal dictionary:", my_dict)

# Adding a key-value pair to the dictionary
key_add=int(input('enter key of element where you want to add new element:\n'))
ele_to_add_dic=int(input('enter element you want to add in dictionery'))
my_dict[key_add] = ele_to_add_dic
print("Dictionary after adding a key-value pair:", my_dict)

# Removing a key-value pair from the dictionary
key = int(input('enter key of the element you want to delete:'))
del my_dict[key]
print("Dictionary after removing a key-value pair:", my_dict)

# Modifying a value in the dictionary
key_mod=int(input('enter key of element u want to modify:\n'))
ele_to_mod_dic = int(input('enter element you would like to modify:\n'))
my_dict[key_mod] = ele_to_mod_dic
print("Dictionary after modifying a value:", my_dict)

# Creating a Set
num_of_ele=int(input('enter no. of elements in the set:\n'))
my_set = {int(input('enter element: ')) for i in range(num_of_ele)}
print("\nOriginal set:", my_set)

# Adding an element to the set
ele_add_set=int(input('enter element you would like to enter into set:\n'))
my_set.add(ele_add_set)
print("Set after adding an element:", my_set)

# Removing an element from the set5
ele_to_rem=int(input('enter element to remove:\n'))
my_set.remove(ele_to_rem)
print("Set after removing an element:", my_set)

# Sets are unordered collections, so modifying a specific element is not directly possible.
# However, you can remove and re-add elements as needed.

# Example of removing and re-adding an element
rem1=int(input('enter element to remove:\n'))
add1=int(input('enter element you want to add:\n'))

my_set.discard(rem1)  # remove element if it exists
my_set.add(add1)     # add new element
print("Set after removing and adding an element:", my_set)
