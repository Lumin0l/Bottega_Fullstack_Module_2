# You can also nest elements in Tuples

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

# My try:
'''
nested_tuple = (
        'a' = [1, 2, 3],
        'b' = [4, 5, 6],
        'c' = [7, 8, 9]
        )
print(nested_tuple)

'''
# Solution
# Apparently they do it in 2 steps.

tags = ['python', 'coding', 'tutorial']
post += (tags,) # Remember the comma at the end of the element.

print(post)

# We will be able to index it too:
print(post[-1][1]) # This should output 'coding': index 1 on the last element of the tuple.

