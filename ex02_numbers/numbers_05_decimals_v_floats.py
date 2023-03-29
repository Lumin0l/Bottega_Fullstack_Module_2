# Floats are nice and all, but if you want more precision you should use decimals by importing the library that includes them
# First let's import decimals

from decimal import Decimal # import the Decimal class from the decimal library

product_cost = 88.40 # technically python will read this as 88.4, because it eliminates trailing 0s
commision = 0.08 # or 8 %

# To learn the real cost, cost + commision
product_cost += (commision * product_cost)
print(f'product cost is: {product_cost}')

# Let's introduce a quantity of products and multiply them to see how much all costs

qty = 450
print(f'total cost of everything: {product_cost * qty}') # With float it looses all other numbers and rounds it to 42962.4

# Let's do all as decimals now:

product_cost = Decimal(88.40)
commission = Decimal(0.08)
qty = 450

product_cost += product_cost * commission
print(f'new product price with decimals: {product_cost}')
print(f'new total cost with decimals: {product_cost * qty}') # now it will be 42962.40000000000282883716451. Much more precise.
