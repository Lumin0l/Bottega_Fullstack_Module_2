# How to make collections inside dictionaries
teams = {
        "astros": ["Altuve", "Correa", "Bregman"], # We put a list, but it can be anything really.
        "angels": ["Trout", "Pujols"],        
        "yankees": ["Judge", "Stanton"],
        }

print(teams["astros"])

# We can do all we want to do with the elements, like slicing and so on.
print(teams["astros"][1:])

# You can also store these in variables as is:
yankees = teams['yankees']
print(yankees)
