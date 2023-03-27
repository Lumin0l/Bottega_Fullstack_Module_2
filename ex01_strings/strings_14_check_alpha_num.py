# Useful when working with apis, normally the api data comes in strings, thats why we have been manipulating strings
api_data = '5'
greeting = 'hi'

# When working with apis, many times you'll receive queries that need to return an int, but the data from the api comes as a string: '5'.

# To deal with that, like in C: isalpha, isnumeric... They return true or false.

print('isalpha') # 100% is aplhabetic, meaning, if there is a space it would return false
print(api_data.isalpha())
print(greeting.isalpha())

print('\nisnumeric')
print(api_data.isnumeric())
print(greeting.isnumeric())




