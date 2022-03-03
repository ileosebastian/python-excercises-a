"""
    Ask the user for a number, and then report whether the number is a multiple
    of 10 or not.
"""

number = int( input("Ingrese un numero, por favor: ") )

if number%10 == 0:
    print("El numero " + str(number) + " es multiplo de 10.")
else:
    print("El numero", number, "no es multiplo de 10.")