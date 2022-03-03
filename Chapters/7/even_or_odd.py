number = input("Ingrese un numero, y le dire si es par o impar: ")
number = int(number)

if number%2 == 0:
    print("\nEl numero", number, "es par.")
else:
    print("\nEl numero " + str(number) + " es impar.")