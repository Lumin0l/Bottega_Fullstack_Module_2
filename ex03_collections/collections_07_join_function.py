# To use as an example, we are going to use a google search, because it is a string that gets requested to the google servers.

# https://www.google.com/search?q=python+development+tutorial
uri = 'https://www.google.com/search?q=' # search terms come after the '='. Let's immitate that. Uri is another way of refering to pages.

# We're going to pick the three original words from the search.
tags = ['python', 'development', 'tutorial']

# Let's create a variable to use and add based on the list.
formatted_tags = '+'.join(tags) # we use the 'join' function. It takes a list as argument, and before that it takes a delimiter, in our case '+' but could be ', ' or ' ' or whatever.
print(formatted_tags)

# So now let's put them togeter to make the proper uri
finished_uri = f'{uri}{formatted_tags}' # We can do that wit {uri} + {formatted_tags} or as we have, with the 'f' for format.
print(finished_uri)
finished_uri_two = uri + formatted_tags 
print(finished_uri_two)

