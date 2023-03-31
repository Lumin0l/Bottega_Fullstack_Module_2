# How to make a list of dictionaries
teams = [
        {'astros': {
                    '2B': 'Altuve',
                    'SS': 'Correa',
                    '3B': 'Bregman',
                }
            }, 
        {'angels': {
                    'OF': 'Trout',
                    'DH': 'Pujols',
                }
            },
        ]
# This is ugly as hell, it takes practice (or a propper text editor), but this is how it's done.
# In our case, it works like a regular list, because it is a regular list.
angels = teams[1].get('angels', 'Team not found')
print(angels)



