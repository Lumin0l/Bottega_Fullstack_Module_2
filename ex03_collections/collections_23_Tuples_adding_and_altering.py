# We said that Tuples they are immutable, but can be manipulated in different ways, same as strings were, creating a new one.

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')
print(post)

# Let's say we wanna add something else. We could just add it to the var like:
# post = ('Python Basics', 'Intro guide to python', 'Some cool python content', 'ADDITION')
# But in reality that is rarely going to be done, data comes from the outside and through many processes.

# We add things like in strings, with '+':
post = post + ('addition',) # For Tuples you need extra steps: add () and a ',' at the end of the elements so python processes them as Tuple elements.
print(post)

# There is syntactic sugar for this too:
post += ('second addition',)
print(post)

# ID function:

# 'id' shows the memmory location for each element, including the tuple itself:
print(f'This is the id: {id(post)}')

# He introduced this concept to show that when we don't add anything, you get the same 'id', but when we 'add stuff to the tupple' the id changes.
# That is because we don't really add anything, we create a new var in a new location with the addition.

