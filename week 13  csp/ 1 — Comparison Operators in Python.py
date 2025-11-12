# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False, equal to
print(a != b)   # True, not equal to
print(a > b)    # False, greater than
print(a < b)    # True, less than
print(a >= b)   # False, greater than equal to
print(a <= b)   # True, less than or equal to


#predict the output of the following comparisons:
10 > 5 #true
7 == 2 * 3 + 1 #true
8 != 8 #false
4 <= 2 + 2 #true

# Write 3 examples that result in True and 3 that result in False.

# Create a simple grade-checking condition:
grade=89
if grade>=90: print(True)
else: print(False)
10==9
30-20>=19
# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
gradepass=int(input("What is your score"))
if gradepass>=60: print("you passed")
else: print("you failed")

password=input("Enter you password")
if len(password)>=8 and any(char.isdigit() for char in password): print("valid")
else:print("invalid")