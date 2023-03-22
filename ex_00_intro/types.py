
#    Booleans: true/false value.  
#    Numbers: complex, python has very good uses for numbers and will have it's own section.
#    Strings: arrays of chars, normally wrapped in "" or ''.
#    Bytes and byte arrays: self explanatory.
#    None: most languages that dynamically allocate have a None type. You can use it to assign values to things that you don't know what they will be yet.
#    Lists: structure. Kind of like a list.
#    Tuples: structures.
#    Sets: structures.
#    Dictionaries: (it's yellow because I don't know vim yet LoL)
#

# Example program that uses data types

meal_completed = True
sub_total = 100
tip = sub_total * 0.2 # result will automatically be a float in python

total = sub_total + tip

receipt = "Your total is: " + str(total) # it will convert the var to a str

print(receipt)





