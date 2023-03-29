# Automating processes with the math library

import math # python is famous for how math works in it, this is the first step here

loss = -20.25
product_cost = 89.99

print(abs(loss)) # will print the absolute value of the var: without the '-'. It's in the core of python, no need for math lib.

# this is how we use libraries: you call the library 'math' and then with '.' you call the function in that lib.

print(math.floor(product_cost)) # math.floor will remove the right side of the '.'. You could also do it with 'int()', but this is more intentional.

# Ceiling

print(math.ceil(product_cost)) # This rounds the number upwards. Even if it's 89.1 it will return 90.

# Round 

print(round(product_cost)) # Just rounds

# Square root

print(math.sqrt(product_cost)) # Gives you the square root

print(math.pow(5, 2)) # This thing does '5 ** 2', but since it is a math function it will return more accurate numbers.

