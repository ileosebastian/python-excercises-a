"""
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

	•	 If the alien is green, print a message that the player earned 5 points.

	•	 If the alien is yellow, print a message that the player earned 10 points.

	•	 If the alien is red, print a message that the player earned 15 points.
	
	•	 Write three versions of this program, making sure each message is printed
	for the appropriate color alien.

"""

alien_color = ['green', 'yellow', 'red']

"""
-3, 0 are equivalents to 'green'
-2, 1 are equivalents to 'yellow'
-1, 2 are equivalents to 'red'
"""
i = 1 # They can be: -3, -2, -1; 0, 1, 2

if alien_color[i] == 'green':
	points = 5
elif alien_color[i] == 'yellow':
	points = 10
elif alien_color[i] == 'red':
	points = 15

print("Player earned " + str(points) + " points!")
