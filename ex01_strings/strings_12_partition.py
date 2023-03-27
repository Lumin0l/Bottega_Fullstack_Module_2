# Introduction to collections
# Strings can be connected and broken

heading = "Python: An Introduction" # lets say I want to brake it in header and subheader

header, _, subheader = heading.partition(': ') # it takes the element you give as partition, and returns a 'touple collection', different strings and will assign them to what whe marked.

"""
The convention to store elements you don't wanna use is the "_", that's why we stored the partition element there.
"""

print(header)
print(subheader)
print(_)

"""
Note that it will only partition on the first instance the element happens.
If you have "Python: an introduction and Python: continuation" it will only break up the first ': '
"""




