#docstring is used to document the function
# Note: should be right below the function definition
def square(n):
    '''Takes a number and returns the square of n'''
    print(n**2)
square(5)

#can also print doc-string
def square(n):
    '''Takes a number and returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

#also PEP8 -> Python Enhancement Proposal
