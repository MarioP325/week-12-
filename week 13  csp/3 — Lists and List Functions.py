# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are ordered collections of items
#lists are mutable meaning they can be changed
#lists are created using brackets []
# Examples:
list_list=[1,2,3,4,5]
print(list_list)
print(type(list_list))
#instead of creating multiple variables we can create a list in order to simplify the process when we need to manage multiple items
#performance task answer
#acessing elements
print(list_list[0])
print(list_list[1:4])
print(list_list[0:])
#modifying list
list_list.append(6)
print(list_list)
list_list.append( 7)
print(list_list)
list_list.extend([8,9,10,11,12,13,14])
print(list_list)
list_list.extend(list(range(15,500)))
print(list_list)
list_list.extend(list(range(501,1101)))
print(list_list)
# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.