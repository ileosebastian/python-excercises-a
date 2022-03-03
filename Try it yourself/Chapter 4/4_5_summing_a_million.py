"""
Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
"""

many_numbers = list(range(1,1000001))

print ("Minimun value: " + str(min(many_numbers)))

print ("Maximun value: " + str(max(many_numbers)))

print ("Summation: " + str(sum(many_numbers)))
