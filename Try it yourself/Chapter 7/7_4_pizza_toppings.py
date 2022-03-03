"""
    Write a loop that prompts the user to enter a series of pizza toppings until
    they enter a 'quit' value. As they enter each topping, print a message 
    saying you’ll add that topping to their pizza.
"""

prompt = "\nIngrese un ingrediente nuevo a la pizza, por favor: "
prompt += "\n(Escriba 'salir' para salir del programa)  "

while True:
    topping = input(prompt)

    if topping.lower() == 'salir':
        print("Su pizza ya estuvo.")
        break
    else:
        print("Le agregaremos " + topping.lower() + " ahora a su pizza!")