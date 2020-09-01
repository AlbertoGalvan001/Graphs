# Summing Values from a Dictionary
# Given an object/dictionary with keys and values that consist of both strings and integers,
# design an algorithm to calculate and return the sum of all of the numeric values.
# Verbalize your thought process as much as possible before writing any code.

# Run through the UPER problem solving framework while going through your thought process.

# Example
# {
# "cat" : "bob",
# "dog" : 23,
# 19 : 18,
# 90 : "fish"
# }
# Running your algorithm should output 41, the sum of the values 23 and 18.

# After creating your algorithm in your favorite IDE,
# submit the output that you get using the following inputs:

# instantiate a variable to hold this on:
def addValues(myDict):
# iterate through dict
    total = 0
    for value in myDict.values():
        if type(value) == int:
            total += value    
    return total
        


myDict = {
"cat" : "bob",
"dog" : 23,
19 : 18,
90 : "fish"
}

print(addValues(myDict))
# check value to see if numeric.
# if numeric, add value to the sum.
# return sum