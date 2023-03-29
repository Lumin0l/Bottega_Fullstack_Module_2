# How to create manual exponent function, that is, replicate 'math.pow()'
# Tools given: reduce.

from functools import reduce

# My approach:
# I tried to understand what reduce did, but there were lambdas and stuff I didn't understand

def my_function(base, exponent):
    return(base ** exponent)

print(f'my function: {my_function(2, 3)}')

# Solution 1:
# Iterative approach

def manual_exponent(num, exp): # pretty 42 approach. Take number and create an index, multiply num by itself index times - 1 and done.
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1
    
    return total # pretty

print(f'solution number one: {manual_exponent(2, 3)}')

# Solution 2:
# Functional approach

def manual_exponent_two(num, exp):
    computed_list = [num] * exp # this will create a list of 'num' 'exp times: if you have '[1] * 4' it will create [1, 1, 1, 1] list.
    
    return (reduce(lambda total, element: total * element, computed_list)) # this is just weird

print(f'solution number two: {manual_exponent_two(2, 3)}')

'''
reduce: reduce takes a function as an argument and then a list. With the lambda we are passing total and element. With the computed_list we pass the list we created.
Every time you call the lambda function, that is, every time in the list. It's going to take the total and multiply it by the element: total = total * elemet as many times as the list goes on.
'''

