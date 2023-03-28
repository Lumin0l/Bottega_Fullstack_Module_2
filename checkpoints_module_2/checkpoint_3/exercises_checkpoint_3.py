# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

string = 'Hello, I am a string'
number = 42
lst = [1, 2, 3]
boolean = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.

index = string[0:3]

# Exercise 3: Use an index to grab the first element from your list.

index_list = lst[0]

# Exercise 4: Create a new number variable that adds 10 to your original number.

number_second = number + 10

# Exercise 5: Use an index to get the last element in your list.

last_element_lst = lst[-1]


# Exercise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'
split_names = names.split(',')

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

first_word = string[:5]
first_word_upper = first_word.upper()

new_string = first_word_upper + string[5:]
print(new_string)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

print(f"My number is: {number}")

# Exercise 9: Print “hello world”.

print("Hello world")
