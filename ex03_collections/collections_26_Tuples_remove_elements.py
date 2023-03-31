# Let's see how to remove elements from tuples

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# By deffinition a tuple can't be altered, so you need to create new vars to remove stuff.
# There is keywords and methods though:

# Remove from the end
post = post[:-1] # so, the post is the post up until the last element.
print(post)

# Remove from the beginning works the same
post = post[1:] 
print(post)

# Remove specific elements (messy and not recommended)
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')
post = list(post) # We cast it as a list. This will trigger warnings because tuples should not be changed and can affect other porcesses.
post.remove('Some cool python content') # We use delete.
post = tuple(post) # We recast it back into a tuple.
print(post)



