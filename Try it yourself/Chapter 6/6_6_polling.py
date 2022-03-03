"""
Use the code in favorite_languages.py (page 104).

    • Make a list of people who should take the favorite languages poll. Include
    some names that are already in the dictionary and some that are not.

    • Loop through the list of people who should take the poll. If they have
    already taken the poll, print a message thanking them for responding.
    If they have not yet taken the poll, print a message inviting them to take
    the poll.

"""

# Poll of favorite languages for code
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

people = [
    'jen',
    'ben',
    'konan',
    'edward',
    'pepito',
    ]

for name in people:
    print(name.title())

    if name in favorite_languages.keys():
        print("\tHi " + name.title() + ", thank you for responding the poll.")
    else:
        print("\tHey " + name.title() + ", please to take the poll.")