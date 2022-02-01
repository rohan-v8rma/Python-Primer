#TUPLES
'''
        INDEX
1. Creating a tuple from a sequence
2. Slicing a Tuple
3. Special Tuple functions
4. Unpacking a Tuple
'''

tpl1 = ('a', 'b', 'c', 'd', 'e')

#1. Creating a Tuple from a sequence

tpl2 = tuple('xyz')

tuple3 = 1,2,3,4,5
print(tuple3)
'''Interesting way of creating a tuple.
Spaces don't matter between commas and elements'''

#2. Slicing a Tuple

print(tpl1[0:4:2])
'''this function returns the every second element of the tuple from 0
upto but not including 4'''

#3. Special Tuple functions

print(tpl1.index('d'))
'''this function returns the index of a specified element'''

print(max(tpl1))
'''this function returns the element with the maximum value'''

print(min(tpl1))
'''this function returns the element with the minimum value'''

print(tpl1.count('a'))
'''this function counts the occurrence of a specified element in a tuple'''

#4. Unpacking a Tuple

z,x,y,w,v = tpl1 
#this method assigns each variable a corresponding value in the tuple.
## the number of elements of the tuple and the no. of variables should be same
