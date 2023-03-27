# Filter through stuff with 'find', 'index' and 'in'

sentence = 'The quick brown fox jumped over the lazy dog'

# Find
finding = sentence.find('quick') # it returns the position where this is in the sentence (like substr in c)
print(finding) # in our case it will be 4

# Index
indexing = sentence.index('quick') # Same as find will return the index
# indexing_false = sentence.index('not here') # Problem is, find will return -1 if it doesn't fin anything, index will return an error
print(indexing)

# In
inning = 'fox' in sentence # it will just say it's true
inning_false = 'not here' in sentence # it will just say it's false
print(inning)
print(inning_false)

"""
So,
'Find' will tell you where the word/char is and won't stop the program if false.
'Index' will tell you where the word/char is and stop the program if it's nowhere.
'In' will tell you if there is a word/char or not.
"""
