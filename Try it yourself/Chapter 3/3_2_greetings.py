"""
Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each 
message should be the same, but each message should be personalized with the person’s name.
"""

# the list of my friends
names = ['barcia','Anibal','Nahin','Stefano','Jesus','Brian']

# storing the messages for each person's name
message_barcia = 'Hello, my friend ' + names[0].title() + '!'
message_anibal = 'Hello, my friend ' + names[1] + '!'
message_nahin = 'Hello, my friend ' + names[2] + '!'
message_stefano = 'Hello, my friend ' + names[3] + '!'
message_jesus = 'Hello, my friend ' + names[4] + '!'
message_brian = 'Hello, my friend ' + names[-1] + '!'

# printing the messages
print (message_barcia)
print (message_anibal)
print (message_nahin)
print (message_stefano)
print (message_jesus)
print (message_brian)
