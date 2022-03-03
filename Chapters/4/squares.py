# ########## Two exercice for 4_15 ##########

# --------- LIKE A BEGINNER
squares = []

for value in range(1, 11):
    # square = value**2
    squares.append(value**2)

print ('Like a beginner: ' + str(squares))

print (type(squares))
""" My aport
n = 1
for square in squares:
	print (str(n) + ':= ' + str(square))
	n+=1
"""


# --------- LIKE A PRO
squares = [value**2 for value in range(1, 11)]
print ('Like a pro: ' + str(squares))