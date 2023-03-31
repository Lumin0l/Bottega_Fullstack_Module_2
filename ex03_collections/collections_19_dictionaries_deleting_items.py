
# How to delete stuff

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

# One of the most straighforward ways is with 'del'

del teams['astros']
print(teams)

# This is fine if you know 100% that a key exists and want to delete. If it doesn't exist you will get an error. 
# Just like the .get function helps with this when looking to find elements, for deleting we have 'pop'.
teams.pop('astros', 'No team found with that name')

# You can use pop to save and store the deleted things because it has a return.
removed_team = teams.pop('yankees', 'no team found')
print(removed_team)



