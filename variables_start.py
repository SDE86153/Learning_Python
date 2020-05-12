#
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)

# Re-declaring the variable works
f="abc"
print(f)

# ERROR: variables of different types cannot be combined
# print("this is a string " + 123)    # Doesnt work!
print("this is a string " + str(123)) 

# Global vs. local variables in functions
def someFunction():
    global f
    f="def"
    print(f)

someFunction()
print(f) # If commented out, the output of f will be 'abc' and then 'def'

del f
print(f) # Will throw an error because this variable no longer exists