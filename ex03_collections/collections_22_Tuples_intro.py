# Tuples are similar to list, but not quite.
# The syntax is different: List uses [], Dictionaries use {} and Tuples use ().

post = ('Python Basics', 'Intro: guide to python', 'Some cool content here')

# Tuples have a cool feature that is 'unpacking'
title, sub_heading, content = post

# That would trigger a query engine that would have the same result as:
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print (title)
print(sub_heading)
print(content)

# Why use a Tuple vs a List:

# List: is mutable.
# Tuple: is IMmutable.

# Like strings, tuples are fixed, so you should decide when storing data based on if the data is dynamic or needs to be fixed.

# Tuples can't be sorted or altered in any case by other functions, it will trigger an error. That way the data stored in a tuple will be fixed throughout the program.

