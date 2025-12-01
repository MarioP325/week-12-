# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

list1=[1,2,3]
list2=[4,5,6]
nested_list=[list1, list2]
print(nested_list[1][2]) #output 6
fruits=["apple", "orange", "banana", "coconut"]
vegetables=["celery", "carrots", 'potatoes']
meats=["chicken", "fish", "turkey"]
groceries=[fruits,vegetables,meats]
print(groceries[2][2])
for collection in groceries :
    for food in collection:
            print(food, end=" ")
            print()

num_pad= ((1,2,3),
          (4,5,6),
          (7,8,9),
          ("*", 0, "#"))
for row in num_pad:
      print(row)
      for num in row:
            print(num, end=" ")
            print()

matrix= [
      [1,2,3],
      [4,5,6],
      [7,8,9]
]
print(matrix[2][2])
#list comprehension
example_list=[row[0] for row in matrix]


# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are ordered collections of items
#lists are mutable meaning they can be changed
#lists are created using brackets []
# Examples:
# list_list=[1,2,3,4,5]
# print(list_list)
# print(type(list_list))
# #instead of creating multiple variables we can create a list in order to simplify the process when we need to manage multiple items
# #performance task answer
# #acessing elements
# print(list_list[0])
# print(list_list[1:4])
# print(list_list[0:])
# #modifying list
# list_list.append(6)
# print(list_list)
# list_list.append( 7)
# print(list_list)
# list_list.extend([8,9,10,11,12,13,14])
# print(list_list)
# list_list.extend(list(range(15,500)))
# print(list_list)
# list_list.extend(list(range(501,1138)))
# print(list_list)

new_list=['a','b','c']
print(new_list)
new_list.append('d')
print(new_list)
#romiving items on list
removed_item=new_list.pop()#d
#removes last item by default
print(removed_item)
remove_second_item=new_list.pop(1)#b
print(remove_second_item)
print(new_list)#a,c

#sorting a list
numbers=[4,2,5,1,3]
numbers.sort()
print(numbers) # [1,2,3,4,5]
#reversing
numbers.reverse()
print(numbers)
#inserting
numbers.insert(2,10)
print(numbers)

third_list=[7,8,9]
third_list[0]=6
print(third_list)
third_list[-1]=10
print(third_list)

import random
random_list=random.sample(range(1,1000), 100)
print(random_list)
print(sorted(random_list))
sorted_list=sorted(random_list)
#.append(item) - adds an item to the end of the list
# .pop(index) - removes and returns the item at the specified index
# .sort() -sorts the list in ascending order
#.reverse() - reverses the order of the list
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