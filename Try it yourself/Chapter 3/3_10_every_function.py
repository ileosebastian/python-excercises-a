"""
Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, 
or anything else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.
"""


# My list:
superheroes = ['batman','wonderwoman','captain america','spiderman', 'superman','hulk']

print ('List of the superheroes: ' + str(superheroes).title())

print ('\nList of superheroes in alphabetical order: ')
print ('\t' + str(sorted(superheroes)).title())

print ('\nList of superheroes in reverse alphabetical order: ')
print ('\t' + str(sorted(superheroes, reverse = True)).title())

print ('\nMy favorite superheroe is ' + str(superheroes[0]).title())

print ('\n\tI hate the superheroe ' + str(superheroes.pop()).title() + '. For this reason, I remove it to the list.')

print ('\nThen, the list is currently: ')
print ('\t' + str(superheroes).title())

print ('\tI love other superheroes, for this reason, I insert new superheroes to the list.')

superheroes.insert(3,'catwoman')
superheroes.append('starfire')
superheroes.insert(1,'cyborg')
superheroes.append('spaw')

print ('\nThe list is, then, as the follow:')
print ('\t' + str(superheroes).title())

print ('\nHowever, I consider that ' + str(superheroes[4]).title() + ' is a ridiculous superhero.')
print ('\nFor this reason, I think modify this position for a better superhero.')


# If you modify the item of the 4 position, can't ordered using sort()
superheroes[4] = 'flash'

print ('\nThen, the list is the follow:')
print ('\t' + str(superheroes).title())

print ('\nList of superheroes has been sorted permanently...')
# superheroes.sort(reverse = True)
superheroes.sort()

print ('And is the follow: ')
print ('\t' + str(superheroes).title())

print ('\nNow, I want to superhero Superman...')
superheroes.remove('superman')

print ('The list is the follow: ')
print ('\t' + str(superheroes).title())

print ('\nList in reverse order of permanent way:')
superheroes.reverse()

print ('\t' + str(superheroes).title())

print ('\nNow, I think that this was a fuck decition xd')
print ("I'm go to back at the ordered list without reverse it.")
superheroes.reverse()

print ('And is the follow: ')
print ('\t' + str(superheroes).title())