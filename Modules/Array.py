import array

'''Array module is used to create arrays in python. 
They are different from lists. Further explanation 
can be seen in Datatypes basics in Python revision'''

'''This module defines an object type which can 
compactly represent an array of basic values: 
characters, integers, floating point numbers'''

'''We have to specify beforehand which datatype we
will be storing in the array using a 'type code'
at the time of creation of the array'''

arr1 = array.array('i',[1,3,4])
#There are numerous type codes and the initializer
#list is optional

print(array.typcodes)
#this gives all the type codes concatenated in the
#form of a string

print(arr1.typecode)
#this gives us the typecode character used in creating this 
#specific array

arr1.append(2)
#this functions appends the given element to the list

print(arr1)