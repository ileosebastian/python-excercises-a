"""
Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:

    •	Print the message, The first three items in the list are:. Then use a slice to
    print the first three items from that program’s list.

    •	Print the message, Three items from the middle of the list are:. Use a slice
    to print three items from the middle of the list.

    •	Print the message, The last three items in the list are:. Use a slice to print
    the last three items in the list.
"""

# --------------> program 'numbers.py'


# Print a list of numbers, from 1 to 4
for value in range(1,5):
	print (value)

# Or from 1 to 5
print ('\n')
for value in range(1,6):
	print (value)

# list of numbers automatly
numbers = list(range(1,6))
print (numbers)

# -------------------> this excercise:
# First Point
print ("\nThe first three items in the list of numbers are:")
print (numbers[0:3])

print ("Three items from the middle of the list of numbers are:")
print (numbers[2:])

print ("The last three items in the list of numbers are:")
print (numbers[-3:])
