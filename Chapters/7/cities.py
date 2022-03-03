prompt = "\nPor favor, ingrese el nombre de una ciudad que haya visitado: "
prompt += "\n(Escriba 'quit' cuando usted haya finalizado.)  "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("Me encantaria ir a " + city.title() + "!")