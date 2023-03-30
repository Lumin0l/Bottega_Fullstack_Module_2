# Slicing is critical, let's keep working with it

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

# Most of the time, you won't really know all the list since they will be very long. So normally you won't hardcode stuff.
# For that we have the slice class, to create vars by slicing.

slice_obj = slice(2) # this is the same as doing '[:2]'
print(slice_obj) # this will only print the range -> 'none, 2, none'

# By doing that obj, we save and lock a method or a set slice, so now we can call the object into lists:
print(tags[slice_obj]) # This will be the same as doing 'tags[:2]', but now we've 'locked the value in a variable'

# You can lock the whole process
slice_obj_two = slice(1, 4, 2) # This will start in index 1, until index 4, every 2 indexes.
print(tags[1:4:2])
print(tags[slice_obj_two])

# With the 'slice' object we can also do extra things like start ot stop or step, to know the structure:
print(slice_obj_two.start) # what is the starting index
print(slice_obj_two.stop) # what is the delimiter
print(slice_obj_two.step) # what is the stepping system

