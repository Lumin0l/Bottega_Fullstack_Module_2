# We can use multiple values as keys for dicts, including metadata.

# Here we have all the types of collections:
# This way we can enbed metadata for specific uses, we can use counters or indexes we can use later, for example.
priority_index = {
    (1, 'premier'): [1, 34, 12],
    (1, 'mvp'): [84, 22, 24],
    (1, 'standard'): [93, 81, 3],
}

print(list(priority_index.keys())) # Here we see all.

# We could add limiters and stuff to our decisions when used as tuples







