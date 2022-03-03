"""
    We’re now working with examples that are complex enough that they can be 
    extended in any number of ways. Use one of the example programs from this 
    chapter, and extend it by adding new keys and values, changing the context 
    of the program or improving the formatting of the output.
"""

# I know to code this exercise, and I've done these features in a lot of giving 
# examples programs for this book
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