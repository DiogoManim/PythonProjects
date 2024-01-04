# Data Types

# String

print("Hello"[0])       # output -> H

'''
 This method of pulling out a particular element from a string is 
 called subcripting, and the number determines which character to pull out.
'''

print("Hello"[4])       # output -> o

print("123" + "345")    # output -> 123345

''' Since the type of these values is String and not Int, the result is also a String '''

# Integer

print(123)              # output -> 123

print(123 + 345)        # output -> 468

''' This prints out the actual numbers instead of Strings, because the type is Int '''

'''
    Tip: When writing a large number like 123.456.789 we tend to separate it with dots 
    or commas. In Python, this can be written with an underscore '_' so it can be more
    readable for us.
'''

i = 123456789
j = 123_456_789

print(i == j)           # output -> True

''' This way we can verify it represents the same. '''

# Float / Floating Point Number

''' Simply a number with decimal values '''

pi = 3.14159

# Boolean

True
False

# Type Error, Type Checking and Type Conversion

num_char = len(input("What is your name? "))

# print("Your name has " + num_char + " characters.")

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

''' 
    This commented print line would give us an error on the terminal, since the num_char
    variable is of type 'int' instead of 'str'. We can only concatenate strings with 
    strings, so as we can only add integers with integers.
'''

print(type(num_char))       # output -> <class 'int'>

''' This type function returns the type of the variable num_char. '''

a = float(123)
print(type(a))

print(70 + float("100.5"))  # output (type float) -> 170.5

print(str(70) + str(100))   # output (type string) -> 70100

'''
    This is casting. We are changing the types of the variables or explicitly defining
    them with the type we want.
'''