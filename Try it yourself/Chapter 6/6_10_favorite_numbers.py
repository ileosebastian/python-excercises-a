"""
    Modify your program from Exercise 6-2 (page 102) so 
    each person can have more than one favorite number. Then print each person’s 
    name along with their favorite numbers.
"""

people_favorite_numbers = {
    'joseph': [16, 22, 43, 77],
    'gaston': [21, 33, 66, 0],
    'amelia': [1, 2 , 3],
    'jesus': [666],
    'priscila': [71, 69],
    'josebska': [300, 400, 2111],
    }

i = 1
for person_name, numbers in  people_favorite_numbers.items():
    print("\nPersona #" + str(i))
    if len(numbers) == 1:
        print("\tEl numero favorito de {0} es: {1}".
              format(person_name.title(), numbers[0])
              )
    else:
        print("\tLos numeros favoritos de {0} son: ".format(person_name.title()))
        for number in numbers:
            print("\t\t", str(number))
    i = i + 1