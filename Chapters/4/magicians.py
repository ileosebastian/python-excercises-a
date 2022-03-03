

magicians = ['alice','david','carolina']

# A simple for loop
for magician in magicians:
	print (magician)

# Use sigular name in temporal variable in for loop.
# And use plural name in lists.
# cats = ['minino', 'niki', 'mancha', 'chiki']
# for cat in cats: .... etc.



# More work in for loops

# for loop that to print more information
for magician in magicians:
	print (magician.title() + ', that was a great trick!')
	# We can use the temporal variable in the idented lines
	print ("I can't wait to see your next trick, " + magician.title() + '\n')
# Line without identation, this line it excecute out of the loop
print ("Thank you, everyone. That was a great magic show!")


for magician in magicians:
	print (magician)


print ("I can't wait to see your next trick, " + magician.title() + ".\n")