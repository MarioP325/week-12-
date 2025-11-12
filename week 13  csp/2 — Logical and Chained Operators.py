# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True

#score calculator
score=int(input("enter your score"))
if 90 <= score<=100:print("A")
elif 80 <= score<=89: print("B")
elif 70 >= score<=79: print("C")
elif 60>= score<=69: print("D")
else:   print("F")
# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
num=int(50)
if num>=50 and num<=100: print("true")
else:print("false")
# Write an expression that checks if a number is NOT equal to 0 and greater than 10.
if  num!=0 and num>10:print("true")
# Use chained comparison to check if 3 < 4 < 5.
if 3 < 4 < 5: print("true")
else: print("loser")
# Challenge: Create a password rule using logical operators:

password=input("Enter password")
if len(password)>=5 and len(password)<=10:print("valid")
else: print("invalid")