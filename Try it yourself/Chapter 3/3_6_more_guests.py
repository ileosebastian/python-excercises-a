"""
You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
	•	Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
	statement to the end of your program informing people that you found a
	bigger dinner table.
	•	Use insert() to add one new guest to the beginning of your list.
	•	Use insert() to add one new guest to the middle of your list.
	•	Use append() to add one new guest to the end of your list.
	•	Print a new set of invitation messages, one for each person in your list
"""

# -------------------------------- excercise 3_4
# List of person that I could invite to dinner
invited_people = ['duval zambrano','rosa amelia','carlina linares']

# Dedicated messages for each person invited 
message_1 = "I want to eat the dinner with you, dear grandfather " + invited_people[0].title()
message_2 = "I want to eat the dinner with you, dear grandmother " + invited_people[1].title()
message_3 = "I want to eat the dinner with you, dear " + invited_people[-1].title() 

# Pring the messages
# New:
print ("\tInitial guests:")
print (message_1 + '\n' + message_2 + '\n' + message_3)


# -------------------------------- excercise 3_6
# First point
print ('\n\tI found a new bigger dinner table.')
print ('\n\tFor this reason, I invite new people for this dinner. The new guest are as follow:')

# Second point
invited_people.insert(0, 'anthony intriago')
# Third point
invited_people.insert(3, 'galina demera')
# Fourth point
invited_people.append('brian')


# Fifth point
message_1 = "I want to eat the dinner with you, dear " + invited_people[0].title() + '.'
message_2 = "I want to eat the dinner with you, dear grandfather " + invited_people[1].title() + '.'
message_3 = "I want to eat the dinner with you, dear grandmother" + invited_people[2].title() + '.'
message_4 = "I want to eat the dinner with you, dear " + invited_people[3].title() + '.'
message_5 = "I want to eat the dinner with you, dear girlfriend " + invited_people[-2].title() + '.'
message_6 = "I want to eat the dinner with you, dear " + invited_people[-1].title() + '.'  
print (message_1 + '\n' + message_2 + '\n' + message_3 + '\n' + message_4 + '\n' + message_5 + '\n' + message_6)
