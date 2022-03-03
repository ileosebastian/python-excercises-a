"""
Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.

    • Use a loop to print a sentence about each river, such as The Nile runs
    through Egypt.

    • Use a loop to print the name of each river included in the dictionary.
    
    • Use a loop to print the name of each country included in the dictionary.
""" 

long_rivers = {
    'yellow river' : 'china',
    'llena' : 'russia',
    'Tocantins Araguaia': 'brazil',
    }

print("\t\t\tThe river majors of the world.")
# First point
for river, country in sorted(long_rivers.items()):
    print("The " + river + " runs through " + country + ".")

# Secon point
print()
for river in sorted(long_rivers.keys()):
    print(river.title())

# Third point
print()
for country in sorted(long_rivers.values()):
    print(country.title())