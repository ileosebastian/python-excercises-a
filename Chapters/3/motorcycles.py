

# I make a list of motorcycles
motorcycles = ['honda','yamaha','suzuki']

# Print the list
print (motorcycles)


""" ------------------------------ MODIFY LIST
# I change the first element
motorcycles[0] = 'ducati'
print (motorcycles)

motorcycles[-1] = False
print (motorcycles)
"""

""" ------------------------------ INSERT ELEMENTS IN THE LIST
# Appending element to the end
motorcycles.append('ducati')
# The list has a new element: ducati
print (motorcycles)



# Empty list
motorcycles = []

# Append the elements into the list
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

# Print the list made with append method
print (motorcycles)


# Insert a new element en the position 0
motorcycles.insert(1,'ducati')

# Print the list with the element inserted
print (motorcycles)
"""

""" ------------------------------ REMOVING ELEMENTS IN THE LIST

# Remove a know item using a know index 
#del motorcycles[0] # the first item
del motorcycles[1] # the second item
print (motorcycles)



# Remove an item using pop method
popped_motorcycle = motorcycles.pop()

# Print the original list and list with the item removed
print (motorcycles)
print (popped_motorcycle)



# Remove the last item as a last owned
last_owned = motorcycles.pop()

# Print the last owned bought
print ("\nThe last motorcycle I owned was a " + last_owned.title() +'.')



# Remove any item with on any position
first_owned = motorcycles.pop(0)

# Print statement that to describe the first motorcycle I ever owned
print ('\nThe first motorcycle I owned was a ' + first_owned.title() + '.')


# Remove using remove method

# List general for this topic
motorcycles = ['honda','yamaha','suzuki','ducati']
print (motorcycles)

# Remove item 'ducati', without knowing the index
motorcycles.remove('ducati')
print (motorcycles)


# Defining a variable for remove an item in the list
motorcycles = ['honda','yamaha','suzuki','ducati']
print (motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)

# Print tha list without item 'ducati'
print (motorcycles)

# Print a statement as example
print ('\nA ' + too_expensive.title() + ' motorcycle is too expensive for me.')

"""



""" ------------------------------ AVOIDING ERRORS...
"""

motorcycles = []
print (motorcycles[-1]) # This is an error about IndexError

