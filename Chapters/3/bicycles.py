

# list of a few kinds bicycles
bicycles = ['trek', 'cannondale','redline','specialized']

# print the general list
print (bicycles)

# print the first element of the list
print (bicycles[0])

# print the first element of the list with a string method
print (bicycles[0].title())

# print bicycles kind in the index 1 and 3 (3th and 4th position)
print (bicycles[1])
print (bicycles[3])

# print the last element in the list of bicycles
print (bicycles[-1])

# print the second element from the end of the list
print (bicycles[-2])

# print a message with a value of list
message = 'My first bicycle was a ' + bicycles[2].title() + '.'
print (message)
