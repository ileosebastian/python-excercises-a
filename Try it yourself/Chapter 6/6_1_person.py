"""
    Use a dictionary to store information about a person you know.
    Store their first name, last name, age, and the city in which they live. 
    You should have keys such as first_name, last_name, age, and city. 
    Print each piece of information stored in your dictionary.
"""
my_favorite_person = {
    'first_name': 'Carlina',
    'last_name': 'Linares',
    'age': 21,
    'city': 'Portoviejo',
    }

print(
    "Firt name: " + my_favorite_person['first_name'].title() + "\n" +
    "Last name: " + my_favorite_person['last_name'].title() + "\n" +
    "Age: " + str(my_favorite_person['age']) + "\n" +
    "City: " + my_favorite_person['city'].title()
)