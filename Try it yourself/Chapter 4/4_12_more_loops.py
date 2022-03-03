"""
All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.
"""


# -----------> by 'foods.py' program

my_foods = ['pizza', 'falafel', 'carrot cake']

# Make a copy of entire list
friend_foods = my_foods[:]


my_foods.append('cannoli')
friend_foods.append("ice cream")


print ("My favorite foods are:")

# foods.py: print (my_foods)

# From 4_12:
for my_food in my_foods:
    print (my_food.title())



print ("\nMy friend's favorite foods are:")

# foods.py: print (friend_foods)

# From 4_12:
for friend_food in friend_foods:
    print (friend_food.title())