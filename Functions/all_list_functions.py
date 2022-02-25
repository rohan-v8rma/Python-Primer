# LISTS
'''
                            INDEX
    1. Creating lists from sequences
    2. Creating lists from inputs using for loop
    3. Creating a list using multiple for loops
    4. Splitting a string at multiple delimiters
    5. Creating strings from lists 
    6. Printing a comma separated list in one line of code
    7. Creating lists using range function
    8. Multiplying a List with an integer
    9. Slicing
    10. Membership Operators
    11. Obtaining index of a specified element 
    12. Counting occurrence of a specified element of a list #IMPORTANT
    13. Sorting the Order of Elements of a List using various conditions
    14. Special list functions
    15. Adding elements to a list
    16. Spreading a list using *args
    17. Removing elements from a list
    18. Deleting/Clearing a list
    19. Unpacking a List
    
'''
term = 'h'
list3 = ['t','i','g']
string = 'hello    world'

'''1. Creating lists from sequences'''

list1 = list('hello')
#list1 = ['h', 'e', 'l', 'l', 'o']

list2 = list('hello world')
#list2 = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

list3 = string.split()
#list3 = ['hello', 'world']

list4 = string.split(' ')
#list4 = ['hello','','','','','world']

'''2. Creating lists from inputs using for loop'''

length_of_list = 2
#list_1 = [int(input("Enter an element ---> ")) for iter_var in range(length_of_list)]

'''3. Creating a list using multiple for loops'''

list_1 = ['1','1','1','1']
list_2 = ['2','3','4','5']
list_3 = [a+b for a in list_1 for b in list_2]

'''4. Splitting a string at multiple delimiters'''
print("\n Splitting a string at multiple delimiters\n")
import re 
text = 'hello, my name*is\'rohan'
list71 = re.split(',|\*|\'',text)
print(list71)
#list71 = ['hello', ' my name', 'is', 'rohan']

'''5. Creating strings from lists'''
print('\n Creating strings from lists\n')

word = ''.join(list1)
#the prefix of join specifies the separator between the elements of the list
#only works if the elements in list1 are string (str) types
#if there are any integers in the list1

word_1= ''.join([str(element) for element in list1])
#Beware we still cannot use join if there are tuples or lists inside list1
print(word)

'''6. Printing a comma separated list in one line of code'''
print("\n Printing a comma separated list in one line of code\n")

print(','.join(list1))

'''7. Creating lists using range function'''

list5 = list(range(7))
#l5 = [3,4,5,6]

list6 = list(range(3,8))
#l6 = [3,4,5,6,7]

'''8. Multiplying a List with an integer'''
print("\n Multiplying a List with an integer\n")

list7 = [1,1,1,1,1]
print(list7 * 2)
'''this results in formation of a list which has the elements of l4 but twice over.

If we want to multiply each element numerically by 2,
use a combination of lambdas and mapping
or use list comprehension
'''

'''9. Slicing'''

print(list1[0:4])
#prints the list from 0 upto but not including 4

print(list1[0:5:2])
#prints the list starting from 0 and upto but NOT INCLUDING 5 
#but it takes every second element


'''10. Membership Operators'''

print(term in list1)
#returns true or false depending on whether the term is present in list1 or not
#It only checks the elements of the list. 
#It can't be used to check whether a certain list is a subset of it.

'''11. Obtaining index of a specified element'''

print(list1.index('e'))
# it returns the index of the first matched item from the list


'''12. Counting occurrence of a specified element of a list'''

print(list1.count('l'))
# it returns the value of number of occurrences of specified element


'''13. Sorting the Order of Elements of a List using various conditions'''
print("\nSorting the Order of Elements of a List\n")

list10 = sorted(list1)
#sorted() function is used to assign a sorted list to another variable


'''
SYNTAX : <list_name>.sort([key = <sorting_condition>], [reverse = True])
this method mutates the list directly(since lists are mutable) instead of re-assigning it

The default procedure for sorting strings inside is to compare using 
comparison operators '<>' of python. 

When we compare strings using '<>', strings are arranged according to 
the lower ASCII value of the first character. If first characters match, second
characters are compared and so on.

#! We can change the procedure for sorting by specifying a key. 

#! If we add reverse = True, it will sort in descending order

NOTE We can't use sorted() function or sort() method with lists that contain
more than one data type.
'''
list0 = ["ABD", "abc", "aBe"]
print(list0, "<--- unsorted list")

list0.sort()
print(list0)

list0.sort(reverse = True)
print(list0)


list0.sort(key = str.lower)
#* this will sort the list according to 'lowercase' of the elements of the list
#* which means the strings will be compared in lowercase, but the original strings
#* will be displayed in the list. 
print(list0)

list0.reverse()
#this reverses the list

list12 = list1[-1::-1]
#this way of slicing is used to assign the reverse of a list to a variable



'''14. Special list functions'''

#print(max(list1))
#this function returns the element with the maximum value

#print(min(list1))
#this function returns the element with the minimum value

'''15. Adding elements to a list'''

#these functions can be executed on their own. list1 doesn't have to be reassigned
# this is because lists are mutable datatypes
list1.append('y')   
#it adds an element to the last index

list1.insert(1, 't')
#it adds an element to a specific index

list1.extend(list3)
#it adds another list to the end of the first list

'''16. Spreading a list using *args'''
print("\n Spreading a list using *args\n")

#instead of using extend it is better to use
list25 = [*list1, *list3]
# * operators spread a list
print(list25)


'''17. Removing elements from a list'''
##these functions can be executed on their own. list1 doesn't have to be reassigned to change it.

list1.pop(1)
#it removes an element at a specific index given in the argument

del list1[3:8:2]
#this deletes a range of indices. We can choose a step as well. 

list1.remove('o')
#it removes the first occurrence of a specified element 

'''18. Deleting/Clearing a list'''

list1.clear() 
#it empties a list but doesn't delete it

del list1 
#it deletes the whole list

'''19. Unpacking a List'''

a,b,c,d = [1,2,3,4]
