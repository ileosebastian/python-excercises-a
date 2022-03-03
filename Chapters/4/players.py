
# List of players:
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print Complete list:
print ('Complete list: ' + str(players))

print ('\n0 to 3')
print (players[0:3])

print ('\n1 to 4')
print (players[1:4])

print ('\nWithout starting index:')
print (players[:4])

print ('\nOmmit the end of the list:')
print (players[2:])


# List of players:
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print Complete list:
print ('\n\nComplete list: ' + str(players))
# -------------> At negative indices
print (players[-3:])


print ('\n\nUsing for loop in a slice')

print ("Here are the first three players on my team:")

for player in players[:3]:
    print (player.title())