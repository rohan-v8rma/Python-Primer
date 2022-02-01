#Modules
'''Module Functions'''

'''To show all available functions in a module'''

#print(dir(<module name>))

'''To display all docstrings along with module name, functions' name and constants'''

#help(<module name>)

'''Importing a module'''

#Importing an entire module : 

import random

#Assigning an alias to an imported module : 

import statistics as stat

#Importing selected objects from a module : from <module name> import <object name>

'''After importing select objects from a module, we need not prefix the object with
the module name and we can use it by itself'''

from time import sleep
print('sleeping')
sleep(1.5)

'''If you want to import all objects from a module but still not use the module name
as a prefix, use:'''

#from <module> import *


'''Random Module'''

print(random.randint(1,6))
#it returns a random integer from lower limit to upper limit including upper limit


print(random.randrange(3,60,5))
#it returns random numbers from range start to stop with step value
## upper limit is not included

print(random.random())
#it returns a value from 0 upto but not including 1  

'''Statictics Module'''


seq = [1,45,6,6,423,6,7,5,467,7]
#this can be either a list or a tuple

print(stat.mean(seq))
#it returns mean of the sequence

print(stat.mode(seq))
#it returns mode of the sequence

print(stat.median(seq))
#it returns median of sequence
