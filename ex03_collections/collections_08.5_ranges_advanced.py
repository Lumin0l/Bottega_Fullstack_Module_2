# They work slightly different and technically when working with lists 'ranges' are called 'slices'

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

# Let's delomitate all except the first and last
tag_range_middle = tags[1:-1]
print(tag_range_middle)

# We can add a third collumn and create an 'interval'
tag_range_interval = tags[:-1:2] # this means ''-> start from the beginning, '-1'-> all the way to the end, '2'-> take 1 out of every 2.
print(tag_range_interval)

# Reversing the whole list
tag_range_reverse = tags[::-1]
print(tag_range_reverse)
# Why not use '.sort'? The difference lays in how python works, usinf '.sort' we arrange it only alphabetically. With '::-1' we reverse the indexes.
# Also, '.sort' will arrange the tags in a certain list, but doesn't return anything, so you can't assign it other variables.

# I'll try to imitate '::-1' easier
tag_range_reverse_mine = tags[-1:0]
print(f'normal: {tags}')
print(f'mine  : {tag_range_reverse_mine}')
# Okay, so ranges normally only go left to right. You can delimit them to some spot starting on the right, but you can't run the array starting on the right.
