# Split in python
url = 'https://google.com'

# strip
print(url.strip('https://')) # it will cut the input from anywhere

# lstrip: 'left strip'
print(url.lstrip('https://')) # will cut from the left

# rstrip: 'right strip'
print(url.rstrip('.com')) # will cut from the right

# Cleanup
print('--cleanup--')
url = url.lstrip('https://')
url = url.rstrip('.com')
print(url)

