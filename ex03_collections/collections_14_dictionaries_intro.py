# Introduction to dictionaries

# They are made with curly bracers
players = {
        "ss": "Correa", # 'ss' is the key and 'correa' is the content
        "2b": "Altuve",
        "3b": "Bregman",
        "DH": "Gattis",
        "OF": "Springer",
        }

print(players)

# Like in an old timey dictionary, we have to go through keys to find what we look for. 
# It means we work with the keys INSTEAD of the indexes:

second_base = players['2b']
print(second_base)

# If we try to open some key that it doesn't exist, it will show an error.
# third_base = players['asd'] -> this will show an error.
# It is case sensitive, so watch out.
