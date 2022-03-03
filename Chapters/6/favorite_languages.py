# Poll of favorite languages for code
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print()

# using a key method
for name in favorite_languages.keys():
    print(name.title())

    # .key() it's equals to "for name in favorite_languages"

print("\nExample:")

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print("\tHi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title())


# Another example:
print()
if 'erin' not in favorite_languages.keys():
    print("Erin, please take a poll!")

# Dictionary's keys in order
# Using sorted() function
print()
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for talking the poll.")

# Dictionary's values with .values() method
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Values shown a unique time, using set() method:
print("\tUsing set() method")
for language in set(favorite_languages.values()):
    print(language.title())

print(set(favorite_languages.values()))


# # Something that is my
# var = "Someone"

# for char in var:
#     print(char, end='\t\t')

print("\n--------------------------")
favorite_languages = {
    'jen': ["python", "ruby"],
    'sarah': ['c'],
    'edward': ["ruby", "go"],
    'phil': ["python", "haskell"],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is " + languages[0].title())
    else:
        # print(str(len(languages)))
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())