# The REAL MF SPLIT

# It is used for case where you do NOT have a SINGLE clear differentiation element
tags = 'python,coding,programming,development'

# Let's say we want to get the different elements

list_of_tags = tags.split(',')
# if we do this: "tags = tags.split(',')" it will return a list, and couse an error

print(list_of_tags) # lists are basically arrays

# We can also use it to break the type of the vars into new ones

list_of _just_1_thing = tags.split() # this will break the sentece and put it into an array, but since there is no differentiator, it will only have 1 element

# The heading from before could be split like this
heading = 'Python: An introduction'
heading_list = heading.split(': ')
print(heading_list)

"""
Partition returns a 'touple'
Split returns a 'list'
"""
