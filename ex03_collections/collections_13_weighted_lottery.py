# Exercise that simulates a tricked lottery. It is an intro to dictionaries.
import numpy as np

real_weights = {
        'winning': 1,
        'break_even': 2,
        'losing': 3
        }

# Solution
# After importing the numpy library we make a container:

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weight.items():
        for _ in range(weight): # underscore in a for loop means that it is a var that is not going to be used. In this case it's only a counter.
            container_list.append(name)
    return np.random.choice(container_list)

print(weighted_lottery(real_weights))
