'''A function is defined like this'''

def sum(x, y):
    return(x + y)

''''Non-keyword arguments in a function'''

def minus(x, y = 1):
    return (x - y)

#If user doesn't give y argument, by default 1 is assigned to it

'''Keyword arguments in a function'''

def multiply(x,y):
    return (x * y)
print(multiply(y = 10, x = 9))

#This method allows us to change the order of arguments passe

'''Functional programming is a general concept which states that 
the code should be contained in functions. Functional programming 
allows us to reuse the code as many number of times we want. It 
not only makes the code efficient but also maintainable. Functional 
programming can be implemented by the use of functions in our code.'''
