'''
                        SETS
                                            
Set is a list but only with unique elements. Also it is unordered.

All elements of a set should be IMMUTABLE/hashable. So a set can only contain
booleans, integers, floats, strings, and tuples.

NOTE:
We have to use <var_name> = set() in order to create an empty set.
If we use <var_name> = {}, this will create an empty dictionary
'''
list1 = ['a','b','c']

#Conversion from list to set

set1 = set(list1)
print(f"set1 is = {set1}\n")


#METHODs that require re-assignment 


#Union of 2 or more sets
'''
SYNTAX:
<var_name> = <set 1>.union(<set 2>[,<set 3>,[...]])
'''
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union_of_sets = set_a.union(set_b)
print(f"The union of sets A and B = {union_of_sets}")

#Intersection of 2 or more sets
'''
SYNTAX:
<var_name> = <set 1>.intersection(<set 2>[,<set 3>,[...]])
'''
intersection_of_a_and_b = set_a.intersection(set_b)
print(f"The intersection of sets A and B = {intersection_of_a_and_b}\n")

set_c = {4, 20}
intersection_of_a_b_and_c = set_a.intersection(set_b, set_c)
print(f"The intersection of sets A, B and C = {intersection_of_a_b_and_c}\n")

#Difference of 2 sets

a_b = set_a.difference(set_b) # Set A - Set B
print(f"\nSet A - Set B = {a_b}")

b_a = set_b.difference(set_a) # Set B - Set A
print(f"\nSet B - Set A = {b_a}\n")

#Creating a set using a dictionary

dictionary = {1 : "rohan", 2 : "soham", 3 : "mayhul"}
set2 = set(dictionary)
#all keys of the dictionary are added into a set
print(set2,'\n')

set2 = set(dictionary.values())
#all values of the dictionary are added into a set
print(set2,'\n')

set2 = set(dictionary.items())
#all key-value pairs of the dictionary, which are stored in tuples are added into a set
print(set2,'\n')



#METHODs that mutate Sets without changing the storage address and no need of re-assignment


#Addition of an element

set1.add('d') #only one element can be added at a time
print(f"set1 is = {set1}\n")


#Removal of elements

#remove()
set1.remove('b')
print(f"set1 is = {set1}\n")

#discard()
set1.discard('b')
'''
Difference between discard and remove is that if the element to be remove isn't present 
in the set, discard doesn't raise an error while remove does
'''

#pop()
'''Since a set is unordered, pop randomly removes an element and returns it'''

print("Element removed is", set1.pop())
'''
What this command means is that, first, set1.pop() is executed.
set1 has been mutated without the need of re-assignment.

After that, the pop() method returns the value which is removed from the set.
This returned value is printed as a result of being enclosed in print() function.
'''
print(f"\nset1 is = {set1}\n")


#Emptying a set

set1.clear()
print(f"set1 is = {set1}\n")





