"""
Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner.
"""

# I use the excercise 3_4...
# List of person that I could invite to dinner
invited_people = ['duval zambrano','rosa amelia','carlina linares']

# Dedicated messages for each person invited 
message_1 = "I want to eat the dinner with you, dear grandfather " + invited_people[0].title()
message_2 = "I want to eat the dinner with you, dear grandmother " + invited_people[1].title()
message_3 = "I want to eat the dinner with you, dear " + invited_people[-1].title() 

# Pring the messages
print (message_1 + '\n' + message_2 + '\n' + message_3)


# This excercise:
print ('\nThe number of people I invited is' + str(len(invited_people)))




