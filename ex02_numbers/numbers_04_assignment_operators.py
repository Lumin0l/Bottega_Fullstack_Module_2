# The symbols for assignment

total = 100 # how could we add 10 to it?

total = total + 10 # isn't this a bit redundant?

total += 10 # this is better.

# We should have 120 by now

# Let's put it as it was

total -= 20

# 100 again

# Let's multiply it

total *= 2

# Back to normal

total /= 2 # it will turn it into a float, for some reason.
print(f'division is: {total}')

# Let's turn it back to plain int with floor division


total //= 1
print(f'floor division: {total}') # hm this doesnt't work, I guess there has to be some remainder for floor division to get rid of

# Le't try again:

total += 101
print(f'to be devided: {total}')
total //= 2
print(f'second attempt: {total}')

# So, floor division does eliminate the remainder, but it keeps it as a float

# Let's do the rest in one go

total **= 2
total %= 100

print(f'final total: {total}')
