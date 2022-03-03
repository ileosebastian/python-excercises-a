"""
5-1Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test.
	•	 Look closely at your results, and make sure you understand why each line
	evaluates to True or False.

	•	 Create at least 10 tests. Have at least 5 tests evaluate to True and another
	5 tests evaluate to False.
"""

# Test 1
game = 'god of war'

print("Is game == 'Mario Bros'? I predict False.")
print(game == 'Mario Bros')

# Test 2
animals = ['cat', 'dog', 'rabbit', 'perico']

print("\nIs 'cat' in the animals list? I predict True.")
print('cat' in animals)

# Test 3
age = 15

print("\nIs age >= 18? I predict False.")
print(age >= 18)

# Test 4
requests = ['gabriel', 'daniel', 'anibal', 'jose']

requests.append('leo')

print("\nIs 'Leo' in the requests list? I predict True")
print('leo' in requests)

# Test 5
book = 'Dracula'

print("\nIs book == 'The Raven'? I predict False.")
print(book == 'The Raven')

# Test 6
number_magic = 44

print("\nIs number magic == 44? I predict True.")
print(number_magic == 44)

# Test 7
beatles = ['Jhons Lenon', 'Paul Mccartney', 'Ringo Starr', 'George Harrison']

print("\nIs 'Yoko Ono' in the beatles? I predict, in fact, False.")
print('Yoko Ono' in beatles)

# Test 8contries
latin_america = ('Ecuador', 'Colombia', 'Peru', 'Brazil', 'Mexico', 'Argentina')

print("\nIs 'USA' not in latin amercia? I predict True")
print('USA' not in latin_america)

# Test 9
languages = ['english', 'french', 'german', 'spanish']

print("\nIs 'russian' in languages? I predict False.")
print('russian' in languages)

# Test 10
number_1 = 666
number_2 = 777

number = 700

print("\nI predict True")
print(number >= number_1 and number <= number_2)
