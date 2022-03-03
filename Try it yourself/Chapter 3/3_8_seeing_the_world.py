"""
Think of at least five places in the world you’d like to
visit.
	•	Store the locations in a list. Make sure the list is not in alphabetical order.
	•	Print your list in its original order. Don’t worry about printing the list neatly,
	just print it as a raw Python list.
	•	Use sorted() to print your list in alphabetical order without modifying the
	actual list.
	•	Show that your list is still in its original order by printing it.
	•	Use sorted() to print your list in reverse alphabetical order without changing the order of 
		the original list.
	•	Show that your list is still in its original order by printing it again.
	•	Use reverse() to change the order of your list. Print the list to show that its
	order has changed.
	•	Use reverse() to change the order of your list again. Print the list to show
	it’s back to its original order.
	•	Use sort() to change your list so it’s stored in alphabetical order. Print the
	list to show that its order has been changed.
	•	Use sort() to change your list so it’s stored in reverse alphabetical order.
	Print the list to show that its order has changed.
"""

# First point
# Create the list
places_to_visit = ['malacias','mitad del mundo','plaza de venecia','piramides','notredam']

# Second point
# Print the raw list
print ('Raw list:')
print (places_to_visit)

# Third point
# Print the list with an alphabetical order, without modify the original list
print ('\nOrdered list temporaly:')
print (sorted(places_to_visit))

# Fourth point
# Print the original list
print ('\nOriginal list:')
print (places_to_visit)

# Fifth point
# Print the list in reverse alphavetical order, without the original list
print ('\nList in reverse order:')
print (sorted(places_to_visit, reverse = True))

# Sixth point
# Print the original list again
print ('\nOriginal list again:')
print (places_to_visit)

# Seventh point
# Change the order list to reverse
places_to_visit.reverse()
# Print the list changed
print ('\nReverse list:')
print (places_to_visit)

# Eighth point
# Revert again the list
places_to_visit.reverse()
# Print the list as the original list
print ('\nOriginal list (I show it again):')
print (places_to_visit)

# Ninth point
# Use sort() method for ordering list
places_to_visit.sort()
# Print the order list in alphabetical way
print ('\nOrdered list:')
print (places_to_visit)

# Tenth point
# Ordering the list in inverse way
places_to_visit.reverse()
# Print the list in reverse alphabetical order
print ('\nList in reverse alphabetical order:')
print (places_to_visit)


