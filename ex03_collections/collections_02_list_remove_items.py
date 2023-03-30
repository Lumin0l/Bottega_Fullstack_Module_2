# There are different ways of removing elements from a list

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

# The first is remove
users.remove('jordan')
print(users)

# Second would be 'popping'
popped_user = users.pop() # we create another var to showcase, because 'pop' removes the last item of the list and returns it, so now it's going to be into popped_user.
print(f'users after pop: {users}')
print(f'popped item: {popped_user}')
# Use Cases: it's a way to iterate arrays using the last element, so a million.

# Third would be 'delete' or del
del users[0] # You need to index the element to be deleted
print(users)



