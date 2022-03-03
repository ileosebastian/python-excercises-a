"""
    Make several dictionaries, where the name of each dictionary is the 
    name of a pet. In each dictionary, include the kind of animal and the owner’s 
    name. Store these dictionaries in a list called pets. Next, loop through your list 
    and as you do print everything you know about each pet.
"""

niki = {
    'kind': "gato",
    'owner_name': "Leo "
}

satanas = {
    'kind': "perro",
    'owner_name': "bruja del 71"
}   

maclein = {
    'kind': "perro",
    'owner_name': "Leo Gaston"
}   

don_gato = {
    'kind': "gato",
    'owner_name': "auronplay"
}   

bethovenn = {
    'kind': "perro",
    'owner_name': "alguien de una peli"
}   

pets = [niki, satanas, maclein, don_gato, bethovenn]

i = 1
for pet in pets:
    print("\nMascota #" + str(i))
    print("\tTipo de mascota:", pet['kind'])
    print("\tNombre del duenio:", pet['owner_name'].title())

    i = i + 1
