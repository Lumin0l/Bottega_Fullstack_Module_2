# How to add elements to the end of a list.

tags = ['python', 'development', 'tutorials', 'code']

# Nope: bad practices
tags[-1] = 'programming' # this will replace the las, not add up.
print(tags)

tags = ['python', 'development', 'tutorials', 'code']
tags.extend('programming') # this will add 'programming' as independent chars
print(tags)

# Yep: proper ways
tags = ['python', 'development', 'tutorials', 'code']

tags.extend(['programming']) # by using [] we add a new element and will properly be indexed
print(tags)

# it does not return anything, for that we need to use '+'
tags = ['python', 'development', 'tutorials', 'code']
new_tags = tags + ['programming']
print(new_tags)




