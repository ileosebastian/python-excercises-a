"""
Store a person’s name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
	Print the name once, so the whitespace around the name is displayed.
	Then print the name using each of the three stripping functions, lstrip(),
	rstrip(), and strip().
"""

# I store a variable, called person_name, a string that content a sentence with various messages. 
person_name = "      leo intriago  & carlina linares,    " + "\n" + "     \tlove within.     " 

print (person_name) # I print the content of variable

print ("Using lstrip: \n"+ person_name.lstrip()) # I print and strip the whitespaces from left

print ("Using rstrip: \n"+ person_name.rstrip()) # I print and strip the whitespaces from right

print ("Using strip: \n"+ person_name.strip()) # I print and strip all the whitespaces 

