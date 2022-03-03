"""
    Make a dictionary called favorite_places. Think of three 
    names to use as keys in the dictionary, and store one to three favorite places 
    for each person. To make this exercise a bit more interesting, ask some friends 
    to name a few of their favorite places. Loop through the dictionary, and print 
    each person’s name and their favorite places.
"""

favorite_places = {
    'juan': ["Pensilvania", "Alaska", "las vegas", "australia"],
    'pedro': ["peru"],
    'gabriel': ["italia", "noruega", "argentina", ],
    'ethan': ["espania", "francia", "italia"],
    'eduarda': ["cololmbia", "ecuador"],
    'matrioska': ["mexico", "monaco", "luxemburgo", "tokio"],
    }

i = 1
for person_name, places in  favorite_places.items():
    print("\nPersona #" + str(i))
    if len(places) == 1:
        print("\tEl lugar favorito de {0} es: {1}".
              format(person_name.title(), places[0].title())
              )
    else:
        print("\tLos lugares favoritos de {0} son: ".format(person_name.title()))
        for place in places:
            print("\t\t", place.title())
    i = i + 1
        