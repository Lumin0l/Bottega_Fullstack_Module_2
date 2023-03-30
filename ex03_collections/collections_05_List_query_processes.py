# len(), negative indexes and index()
tags = ['python', 'development', 'tutorials', 'code']

# len() gives you the ammount of indexes in a list (or a string)
number_of_tags = len(tags)
print(number_of_tags)
# In our case it will print 4, because it counts the total ammount.

# Negative index. Same as in strings, negative index starts from the end. It starts in '1', not in '0'.
last_item = tags[-1]
print(last_item)

# We can also know the index of elements with 'index'
index_of_last_element = tags.index(last_item) # We can pass it as an independet var, or as 'code', the content.
print(index_of_last_element)
