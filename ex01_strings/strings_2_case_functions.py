# sentence = 'The quick brown fox jumped'
# sentence -> variable
# 'The quick brown fox jumped' -> string
# = -> assignment

sentence = 'The quick brown fox jumped'
sentence_two = sentence.upper() # This makes all uppercase

print(sentence)
print(sentence_two)

sentence = 'the quick brown fox jumped'.capitalize() # This makes the first letter capital
print(sentence)

sentence = 'the quick brown fox jumped'.title() # This makes every first letter capital
print(sentence)

sentence = 'the Quick Brown fOx jumped'
print(sentence.lower()) # This makes all lowercase