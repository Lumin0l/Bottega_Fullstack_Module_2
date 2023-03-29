# A couple of lessons back I failed to turn a float into an int, let's see how.

from decimal import Decimal

product_cost = 88.80
commission_rate = 0.08
qty = 450

# Just type the type name bro
product_cost = int(product_cost)
print(product_cost)

# Same with all others
print(float(qty))

# That's how decimal worked in the one before
print(Decimal(commission_rate))
