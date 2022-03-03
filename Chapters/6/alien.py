
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Accessing values
new_points = alien_0['points'] - 1
print("You just earned " + str(new_points) + " points!")

# Adding a new key-value pairs
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

# With an empty set
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying values
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + ".")

# Another example
alien_0 = {'x-position': 0, 'y-position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x-position']))

if alien_0['speed'] == 'low':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# New position
alien_0['x-position'] = alien_0['x-position'] + x_increment

print("New x-position: " + str(alien_0['x-position']))

# Removing values
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']

print(alien_0)

# Using simililar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python', # <--- IMPORTANT THE COMMA for a good practice
    }

print("Sara's favorite language is " +
    favorite_languages['sarah'].title() +
    "."
)