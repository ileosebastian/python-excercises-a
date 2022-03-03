"""
You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
	•	Start with your program from Exercise 3-6. Add a new line that prints a
	message saying that you can invite only two people for dinner.
	•	Use pop() to remove guests from your list one at a time until only two
	names remain in your list. Each time you pop a name from your list, print
	a message to that person letting them know you’re sorry you can’t invite
	them to dinner.
	•	Print a message to each of the two people still on your list, letting them
	know they’re still invited.
	•	Use del to remove the last two names from your list, so you have an empty
	list. Print your list to make sure you actually have an empty list at the end
	of your program.
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
 

# -------------------------------- excercise 3_7
# First point
print ("\n\tThe dinner table won't arrive in time. For this reason, I can only invite two people.")

# Second point
print ("\tSorry, I can’t invite you in this time my dear " + invited_people.pop().title() + '.')
print ("\tSorry, I can’t invite you in this time my dear " + invited_people.pop().title() + '.')
print ("\tSorry, I can’t invite you in this time my dear " + invited_people.pop().title() + '.')
print ("\tSorry, I can’t invite you in this time my dear " + invited_people.pop().title() + '.')

# Third point 
print ("The people stills invite to my dinner are: " + invited_people[0].title() + ' and ' + invited_people[1].title())

# Fourth point
del invited_people[0]
del invited_people[0]
print (invited_people)
del invited_people