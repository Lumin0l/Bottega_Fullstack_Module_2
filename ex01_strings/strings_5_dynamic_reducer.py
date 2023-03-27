import operator
from functools import reduce


"""
Sketch: dynamic_reducer([1, 2, 3] '+') = 6
Sketch: dynamic_reducer([1, 2, 3] '-') = -4
Sketch: dynamic_reducer([1, 2, 3] '*') = 6
Sketch: dynamic_reducer([1, 2, 3] '/') = ?
"""

# My try:
"""
dynamic_reducer([list], operator)
    list = input("what are the numbers")
    operator = input("what is the operator")
    if operator != '+' or opertator != '-' or operator != '*' or operator != '/'
        return(print("error, wrong operator"))

# I get to here, I don't know how to manipulate arrays in python
"""
# Solution:

def dynamic_reducer(collection, op): # we can't use 'operator' because it's inside the library :/
    # This is how you create dictionaries in python
    operators = {
       "+": operator.add, # Here we call the 'operator' library, and inside of that the '.add' operation included
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.truediv,
    }
    
    return reduce((lambda total, element: operators[op](total, element)), collection) # The reduce function has a 'lambda' and the numbers (collection) as input.
# I don't know man, I guess future Imanol will understand more, once he knows what lambdas and dictionaries are

print(dynamic_reducer([1, 2, 3], '+'))
print(dynamic_reducer([1, 2, 3], '-'))
print(dynamic_reducer([1, 2, 3], '*'))
print(dynamic_reducer([1, 2, 3], '/'))




