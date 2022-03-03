"""
Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:

    •	Add a new pizza to the original list.

    •	Add a different pizza to the list friend_pizzas.

    •	Prove that you have two separate lists. Print the message, My favorite
    pizzas are:, and then use a for loop to print the first list. Print the message,
    My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
    Make sure each new pizza is stored in the appropriate list.
""" 

# Initial (Init)
my_pizzas = ['neapolitan pizza', 'chicago pizza', 'St. Louis Pizza']

friend_pizzas = my_pizzas[:]

# First point
my_pizzas.append('peppenori pizza')

# Second point
friend_pizzas.insert(1, 'hawaiian pizza')

# Third point
print ("\n\tMy favorite pizzas are:")
print (my_pizzas)

print ("\n\n\tMy friend's favorite pizzas are:")
print (friend_pizzas)

print ("\n\nmy_pizzas size: " + str(len(my_pizzas)) + " and friend_pizzas size: " + str (len (friend_pizzas)))