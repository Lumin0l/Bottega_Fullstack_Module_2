# As stated, very much like arrays.

# Let's say we received several names from a sql database

users = ['Kristine', 'Tiffany', 'Jordan'] # This is the structure of how they are declared.
print(users)

# These strings are immutable, but lists are NOT. You can delete and add stuff as you want like this:

# Adding items in a specific place
users.insert(0, 'Anthony') # This will add it where you state, without replacing anything. In our case it will turn 'users[3]' into 'users[4] with 'Anthony' in the beginning.
print(users)

# Adding items at the end
users.append('Ian')
print(users)

# Quering them, or getting access to them
# Just index it bro
print(users[2])

# Reassign values
users[3] = 'Mary'
print(users)

