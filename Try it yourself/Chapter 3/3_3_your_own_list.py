"""
Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
"""

# My own list of the vehicles
favorite_transaportations = ['Ford car','Honda motorcycle','Harley motorcycle','Hundai car']

# storing messages as statement
message_ford = 'I would like to own a ' + favorite_transaportations[0] + '.'
message_honda = 'I would like to own a ' + favorite_transaportations[1] + '.'
message_harley = 'I would like to own a ' + favorite_transaportations[-2] + '.'
message_hundai = 'I would like to own a ' + favorite_transaportations[-1] + '.'

# printing the messages in sequecy
print (message_ford)
print (message_honda)
print (message_harley)
print (message_hundai)
