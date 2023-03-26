'''
Python is 0 started like 0:
    'The quick brown fox jumped'
    0 -> T
    1 -> h
    2 -> e
    ...
'''

starter_sentence = 'The quick brown fox jumped'
print(starter_sentence[7]) # It's a 'c'

'''
They are immutable, that is you can't do this:
    starter_sentence[7] = 'B'

The system won't allow that, string is fixed as declared, you can show or copy elements
but not manipulate it.

Important for machine learning, because the data 'can't change'.
'''

# Ranges

# Noob way of creating a new sentence
first = starter_sentence[0]
second = starter_sentence[1]
third = starter_sentence[2]

new_sentence = first + second + third
print(new_sentence)

# Cool way
first_word = starter_sentence[0:3] # '0:3' means: starting in '0' to the range (':') of '3' (range meaning not included, so it will copy 'T' + 'h' + 'e')
cool_new_sentence = first_word
print(cool_new_sentence)

# What if we wanted to manipulate it, change 'The' with 'Thy'
new_sentence_changed = 'Thy' + starter_sentence[3:] # We start in 3 (' ') and by not adding anything, it automatically goes to the end.
print(new_sentence_changed)
