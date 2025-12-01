# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:
temperature= int(input("What is the temperature outside today"))
if temperature>10 and temperature<=60:
    print("the temperature is cold outside")
elif temperature>=70 and temperature<80:
    print("The temperature is warm out today")
elif temperature<=110 and temperature>=90:
    print("The temperature is hot out today")
elif temperature<-10 or temperature>110:
    print("Extreme temperature please beware!!!") 
