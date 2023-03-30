# Exercise to find the median

import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

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

# Do it manually
# My try

sorted_list = sorted(sale_prices)
print(f'the sorted list: {sorted_list}')
i = len(sorted_list)
print(i)
median = (i//2) # at first I did '(i//2) + 1', but even if len shows the total index, when indexing we start in 0, so (i//2) is enough
print(sorted_list[median])

# Their solution
sale_prices_two = [
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

sorted_list_two = sorted(sale_prices_two)
num_of_sales = len(sorted_list)
median = sorted_list[math.floor(num_of_sales/2)]
print(median)

# So, almost the same. Good by me.
