#
# Example file for working with functions
#

# Define a basic function
def func1():
    print("I am a function")

# Function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ",arg2)

# Function that returns a value
def cube(x):
    return x*x*x

# Function with default value for an argument
def power(num,x=1):
    result=1
    for i in range(x):
        result=result*num
    return result

# Function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# Examples
""" func1()                 # Prints correctly
print(func1())              # Prints correctly, and then 'None' -- no return value
print(func1)                # Prints memory address?
 """
""" func2(10,20)            # prints correctly
print(func2(10,20))         # prints correctly, and then 'None' -- no return value
print(cube(3))              # returns 27 -- as there is a return value
 """
""" print(power(2))         # prints correcty, using default x value
print(power(2,3))           # prints correctly, given x value overwrites default value
print(power(x=3,num=2))     # prints correctly, as long as value names are given, Python can sort accordingly
"""   
print(multi_add(4,5,10,4))  # prints correctly, static parameters can be added as well, but variable parameter key ALWAYS has to be last listed   