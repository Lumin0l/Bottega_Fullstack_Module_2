# How to use the get function and why
# Imagine we want to have a featured team, but it's not in the dictionary:
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}

# "featured_team = teams['mets']" -> if we were to leave this, the program would crash. The user can't always know what there is in dictionaries, it can't break every time they pick something wrong.
# To protect from that we have the get function:

featured_teams = teams.get('mets', 'no featured team') # get takes 2 args, what we are looking for in the dict and the backup in case it doesn't find it. Can be anything, a string, an int...

print(featured_teams)

# It's kind of an alternative, shorter "if... else...".

