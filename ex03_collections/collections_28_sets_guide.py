# This will allow us to merge our lists into a set of tuples
# Very helpful tool for machine-learning and data science

positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis'] # They should be well sorted or else there can be a problem.

# To assign every 'position' with it's correspondent 'player' we use zip:
scoreboard = zip(positions, players)

print(scoreboard) # This will print a zip object: <zip object at 0x7f3eaac2b300>, need to cast it as a list:
print(list(scoreboard)) # See: [('2b', 'Altuve'), ('3b', 'Bregman'), ('ss', 'Correa'), ('dh', 'Gattis')]





