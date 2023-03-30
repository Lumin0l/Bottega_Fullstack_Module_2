# How to mix and nest lists

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users] # see how you can put a list inside another list.

print(mixed_list)

user_list = mixed_list.pop() # we'll remove the las element with 'pop', that element is a list in our case, so now we have it in an independent var.

print(user_list)

# Best practices:
# It is not advised to do mixed lists because it could be problematic for different actions with the lists
# They would use nested lists to keep them in one way, but separate.

nested_list = [[users], [ids], [mixed_list[:2]]]
print(nested_list)
