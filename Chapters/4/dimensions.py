# ########## One exercice for 4_15 ##########

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# TypeError: dimensions[0] = 250

print('Using for loop')
for dimension in dimensions:
    print(dimension)

print("\nOriginal dimension:")
for dimension in dimensions:
    print(dimension)

print("\nModified dimensions:")

dimensions = (400, 100)
for dimension in dimensions:
    if dimension == 400:
        print("Soy el 400!")

    print(dimension)
