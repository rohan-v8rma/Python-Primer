# Functools Module

import functools

list_1 = [1,2,3,4,5]

# Reduce method
'''
SYNTAX:
functools.reduce(<reducer function>, <sequence>[, <initial-value>])

This method reduces a sequence to a single value.

The previous value received from the calculation is involved in the computation
along with the current element.
By default, since there is no previous value when starting the reduce process,
the first element is taken as the previous value, and the values for the current 
element are taken from the second element onwards.

Otherwise, we can specify an initial value to be used as the first previous value
as the last argument of the method. This way the reduction will start by taking 
the current element from the first element onwards.
'''
print(functools.reduce(lambda x, y: x + y,list_1,10))
#this function will calculate ((((((10 + 1) + 2) + 3) + 4) + 5))
