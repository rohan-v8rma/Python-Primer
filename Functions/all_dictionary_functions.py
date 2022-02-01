#DICTIONARIES

dictionary = {'name' : "rohan", 'age' : 17, 'height' : 186, 'salary p.a.' : '10 Cr'}
d2 = {'name' : "soham", 'age' : 17, 'height' : 176, 'salary p.a.' : '10 Cr', 'gender' : 'm'}


#1. Obtaining a value associated with a particular key

print(dictionary['salary p.a.'])

# OR #

print(dictionary.get('wrong key','No value found'))
'''
this method allows us to get value of a KEY
if key is not present, instead of getting traceback, error message specified is returned
'''
#2. Updating the value of a particular key

dictionary['salary p.a.'] = '50 Cr'

#3. Updating values of multiple keys

dictionary.update(d2)
'''
this function replaces values of first dictionary with values from second dictionary
if a key in d2 is not present in dictionary, it will be added   
'''

#4. This method returns all the keys of the dictionary in a list
print(dictionary.keys()) 

#5. This method returns all the values of the dictionary in a list

print(dictionary.values())

#6. This method returns all the key value pairs of the dictionary, each of which is stored in a tuple, inside a list

print(dictionary.items())

#7. Unpacking dictionary items in a for statement
print("\n Unpacking dictionary items in a for statement\n")
'''
We can unpack the item tuple in a for statement

Tuple Unpacking (each value of the tuple is assigned to a variable)
tuple = [1,2,3,4]
a,b,c,d = tuple

'''


for key, value in dictionary.items():
    print(key, value)

#8. Membership operators in dictionaries
print("\n Membership operators in dictionaries\n")

print('name' in dictionary)
'''
it will return either True or False based on presence of the key
'''
print('50 Cr' in dictionary.values())
'''
it will return either True or False based on presence of the value
'''
#9. Pretty Printing a dictionary
print("\n  Pretty Printing a dictionary\n")

import json
print(json.dumps(dictionary, indent = 3)) 

#10. Deleting elements(key-value pairs) from a dictionary
print("\n Deleting elements(key-value pairs) from a dictionary\n")
del dictionary['age']
'''NOTE that del is a keyword, not a function'''

# or #
   
print(dictionary.pop('name'),'\n')
'''
First pop() method is executed, then the value is returned.
After that the returned value is printed using print() function.
'''
# or #

dictionary.clear()
'''
this clears all key value pairs. 
'''

#10. fromkeys() method
'''
The fromkeys() method returns a dictionary with the collection of keys all mapped to a specified value.

The collection of keys can be enclosed in lists, tuples or sets.
The default value is 'None' datatype. We can specify a specific value as  
SYNTAX:
<dictionary name> = dict.fromkeys(<collection of keys>[, <specified value>])
'''
collection = (1,2,3,4)

print(dict.fromkeys(collection))
print(dict.fromkeys(collection, {"hello", "world"}))

