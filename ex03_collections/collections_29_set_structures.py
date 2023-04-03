# Not used very much, but they appear from time to time:
# A set is more or less a mix between dict and list

# Syntax:
# Dict with no pairs:
tags = {
  'python',
  'coding',
  'tutorials',
  'data'
}
print(tags)

# Why use a set? When all elements inside are unique, you can't allow duplicates. It will ignore any duplicate data.
# Uniqueness
tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}
print(tags) 

# You can't index Sets, so tags[0] will trigger an error.

# We can query though:
query_one = 'python' in tags # This will give as a boolean True/False
print(query_one)



