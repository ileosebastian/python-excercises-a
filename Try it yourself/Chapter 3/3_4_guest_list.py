"""
 If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
"""
# List of person that I could invite to dinner
invited_people = ['duval zambrano','rosa amelia','carlina linares']

# Dedicated messages for each person invited 
message_1 = "I want to eat the dinner with you, dear grandfather " + invited_people[0].title()
message_2 = "I want to eat the dinner with you, dear grandmother " + invited_people[1].title()
message_3 = "I want to eat the dinner with you, dear " + invited_people[-1].title() 

# Pring the messages
print (message_1 + '\n' + message_2 + '\n' + message_3)