# Same as with strings, good to revise and develop

tags = ['python', 'development', 'tutorials', 'code']

# If no item is set as starter, starts from the beginnig
tag_range_beginning = tags[:3]
print(tag_range_beginning)

# Same if we put no delimiter, it will go to the end.
tag_range_end = tags[1:]
print(tag_range_end)

# How to select limits for the end
tag_range_delimited = tags[:-1] # all except the last one, or '-1'
print(tag_range_delimited)

# For learning's sake
tag_all = tags[:] # this means all. It's good to know how it operates.
print(tag_all)

