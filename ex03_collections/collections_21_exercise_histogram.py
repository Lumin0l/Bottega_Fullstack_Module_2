# Each dollar needs to be a sell.
"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

# We need to create a dictionary with a program that takes an imput and prints dollars according to it.
# No user imput, no imput, in fact no imput.


go = '$' * 20
fa = '$' * 42
tw = '$' * 10
ou = '$' * 12

printout = {
        'g': go,
        'f': fa,
        't': tw,
        'o': ou
        }
print(printout)

# I made the correct assigning, I think, I don't know how to apply the propper view. Let's see the solution.

# Solution

sales = {
        'google': 20,
        'facebook': 42,
        'twitter': 10,
        'offline': 12,
    }

print('g ' + sales['google'] * '$')
print('f ' + sales['facebook'] * '$')
print('t ' + sales['twitter'] * '$')
print('o ' + sales['offline'] * '$')


