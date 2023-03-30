# Python by default sorts stuff in their index value

tags = ['python', 'development', 'tutorials', 'code']
print(tags)

# In python, strings are mutable, so we can change it.
# Knowing that, we can sort them alphabetically with 'sort'
tags.sort()
print(f'sorted tags: {tags}')

# You can also sort backwards
tags.sort(reverse=True) # we introduce an input of reverse and boolean 'True', so it complies with the 'if' that has inside, I guess.
print(f'reverse sort tags: {tags}')
# This is useful for dates, for example, in case you want to sort them new-old or old-new...

# Sorting ints
# Sorting ints goes by value: small to big. If you want big-small, reverse.
totals = [234, 1, 543, 2345]
totals.sort()
print(f'totals sorted: {totals}')
totals.sort(reverse=True)
print(f'totals sorted reverse: {totals}')

