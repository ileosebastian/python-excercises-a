"""
You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
	•	Start with your program from Exercise 3-4. Add a print statement at the
	end of your program stating the name of the guest who can’t make it.
	•	Modify your list, replacing the name of the guest who can’t make it with
	the name of the new person you are inviting.
	•	Print a second set of invitation messages, one for each person who is still
	in your list.
"""

# -------------------------------- excercise 3_4
# List of person that I could invite to dinner
invited_people = ['duval zambrano','rosa amelia','carlina linares']

# Dedicated messages for each person invited 
message_1 = "I want to eat the dinner with you, dear grandfather " + invited_people[0].title()
message_2 = "I want to eat the dinner with you, dear grandmother " + invited_people[1].title()
message_3 = "I want to eat the dinner with you, dear " + invited_people[-1].title() 

# Pring the messages
print (message_1 + '\n' + message_2 + '\n' + message_3)


# -------------------------------- excercise 3_5
# First point
print ('\n\tThe guest ' + invited_people[1] + 'can’t make it.')

# Second point
replacement_person = 'anthony intriago'
print ('\tAs a change, this guest has been replace for ' + replacement_person.title())
invited_people[1] = replacement_person

# Third point
message_2 = "I want to eat the dinner with you, dear " + invited_people[1].title()
print (message_1 + '\n' + message_2 + '\n' + message_3)




