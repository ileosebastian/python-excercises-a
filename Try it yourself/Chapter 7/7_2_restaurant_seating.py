"""
    Write a program that asks the user how many people are in their dinner group.
    If the answer is more than eight, print a message saying they’ll have to wait 
    for a table. Otherwise, report that their table is ready.
"""

seatings_number = int(input("Hola, cuantas personas van a comer? "))

if seatings_number > 8:
    print("Por favor, espere por una mesa mas grande.")
elif seatings_number > 1:
    print("La mesa esta lista")