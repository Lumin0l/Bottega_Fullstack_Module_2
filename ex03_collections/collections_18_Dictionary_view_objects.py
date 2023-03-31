# They allow us to view the values on the dictionaries.

players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}
# As can be seen, as long as the punctiation is correct it doesb't matter how you structure dicts.
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

# Let's view the keys with '.keys'
print(players.keys())
# Now the values
print(players.values())
# And the whole items, that are shown as tuples
print(players.items())

# The stuff shown by .keys(), .values() and .items() are 'view objects', dynamic views on the dictionary entries, that is, if the dict changes, the views change too.
# These are 'view objects' not lists, so they can't be treated as such:
# This will show an error -> print(player.values()[0]. View objects do not support indexing.

# We can get access to the values though. Let's first see WHAT IS A VIEW:
# If all questions or calls to dictionaries should happen the usual way, we could run into problems, because things could be changed when viewd.
# With views, if something changes any value in the dictionary, the 'view object' will manifest it without intervening.

# In order to manipulate it, we can cast them as lists:
print(list(players.values())[1])

# We can make copies by declaring variables and that way we make it 'thread safe', changes will happen in the var, not in the dict.
player_names = list(players.copy().values())
print(player_names)

# How we work with nested items
team_groupings = teams.items()
print(team_groupings) # this, even if it is an independent var, it still holds the type 'dict object'.
# Because its a dict object, we have to manipulate it with the functions that allow us to work with them.
'''
len(dictview) -> Returns number of entries
iter(dictview) -> Returs an iterator of the keys, values or items. It will basically show the content as is.
reversed(dictview) -> Returns a reverse iterator over the keys, values or items.
sorted(dictview) -> Returns a sorted list over the keys, values or items.
list(dictview) -> Returns a list over the keys, values or items. This is the "casting" function
'''





