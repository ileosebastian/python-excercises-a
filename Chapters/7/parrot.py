# message = input("Digame algo, y se lo repetire: ")
# print(message)

# prompt = "\nDigame algo, y se lo repetire: "
# prompt += "\nEscriba 'quit' para cerrar el programa. "

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

prompt = "\nDigame algo, y se lo repetire: "
prompt += "\nEscriba 'quit' para cerrar el programa. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)