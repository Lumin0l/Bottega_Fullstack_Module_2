# You may want to sort a list and not change the original one.

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

# We can sort it and then call the original list
sale_prices.sort()
print(sale_prices) # this will sort the OG and print it sorted.

# What if we want to store that in a different var?
sale_prices_4sorted = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices_4sorted)
print(f'sorted: {sorted_list}')
print(f'unsorted: {sale_prices_4sorted}')
