# Common functions to merge and interact with sets
tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

# There are some duplicate elements there. 

# How to merge sets:
merged_tags = tags_one | tags_two # It's done with the '|'. it will keep the uniqueness.
print(merged_tags) # It will eliminate the duplicates.



# Tags in tags_one but not in tags_two.
# That is, we want to have a "master" dict and add the elements it doesn't share with the second.
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one) # it will only print 'python', because everything else inside 'tags_one' is shared with 'tags_two'

# Tags found in both:
# The opposite, the elements that are shared with the two sets.
universal_tags = tags_one & tags_two 
