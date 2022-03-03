"""
    Start with the program you wrote for Exercise 6-1 (page 102).
    Make two new dictionaries representing different people, and store all three 
    dictionaries in a list called people. Loop through your list of people. As you 
    loop through the list, print everything you know about each person.
"""

person_0 = {
    'fname': "Leo",
    'lname': "Intriago",
    'age': 20,
}
person_1 = {
    'fname': "Pepe",
    'lname': "Alcivar",
    'age': 20,
}
person_2 = {
    'fname': "Pepe",
    'lname': "Alcivar",
    'age': 20,
}

people = [person_0, person_1, person_2]

i = 1
for person in people:
    print("\nPersona #" + str(i))
    info = list(person.values())
    full_name = info[0] + " " + info[1]
    age = info[2]
    print("Nombres:", full_name, ". Edad:", age)
    i = i + 1