#eval() function python
'''eval is a built-in- function used in python,
eval function parses the expression argument
and evaluates it as a python expression.'''


# 1.Using eval() for numerical expressions

x = 2
f = "x**2 + 2*x + 3"
#this is will be stored as a string
print(f)

f = eval("x**2 + 2*x + 3")
#this will be seen as a python expression
#and the value of x will be substituted.
print(f)

'''eval() function is useful when we want
a numerical expression in one line
as input from the user'''


# 2.Using eval() to input different data types

'''eval() function can also be used to receive
input of dictionaries, lists, tuples etc. because
they will be seen as the data types they are
according to python syntax, rather than as a string'''

tuple_1 = "(1,2,3)"
#when input() function is written as it is
tuple_1 = eval("(1,2,3)")
#when input() function is enclosed in eval()

'''We can't use in-built functions like
tuple(), list(), set() and dict() in all cases
because of some complexities occurring
when using quotes
'''
