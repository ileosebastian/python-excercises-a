"""
Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

	•	Modify your program to print a statement about each animal, such as
	A dog would make a great pet.

	•	Add a line at the end of your program stating what these animals have in
	common. You could print a sentence such as Any of these animals would
	make a great pet!
"""

# Opinion: It's a similar exercise than 4_1. Therefore, I'm going to do the same.

animals = ['tiger','panther','cat']

for animal in animals:
	print (animal.title())
	print ("The " + animal + " it's a great feline." + '\n')

print ("These are felines and it's great animals!")
