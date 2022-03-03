"""
    Use a dictionary to store people’s favorite numbers.
    Think of five names, and use them as keys in your dictionary. 
    Think of a favorite number for each person, and store each as a value in your 
    dictionary. 
    Print each person’s name and their favorite number. 
    For even more fun, poll a few friends and get some actual data for your program.
"""

people_favorite_numbers = {
    'joseph': 16,
    'aury': 5,
    'gaston': 7,
    'amelia': 55,
    'jesus': 666
}

print("People's favorite number poll." + "\n" +
    "\t" + "Joseph: " + str(people_favorite_numbers['joseph']) +
    "\t" + "Aury: " + str(people_favorite_numbers['aury']) +
    "\t" + "Gaston: " + str(people_favorite_numbers['gaston']) +
    "\t" + "amelia: " + str(people_favorite_numbers['amelia']) +
    "\t" + "Jesus: " + str(people_favorite_numbers['jesus'])
)
