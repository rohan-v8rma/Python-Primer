'''
A regular expression (sometimes called a rational expression) is a 
sequence of characters that define a search pattern, mainly for use 
in pattern matching with strings, or string matching, 
i.e. “find and replace”-like operations.

Regular expressions are a generalized way to match patterns with 
sequences of characters.

Python implements a standards-compliant regular expression module, 
which is called 're'.

Note that we have to compile strings into regular expression objects,
using compile() method before we can use 're' methods on them. 
'''



import re

#* compile() method
pattern = re.compile("o")
'''
Now, 'd' is a regex object and it can be checked whether 'd'
is contained in a string
'''


#* search() method 
'''
SYNTAX : <regex_object>.search(string[, pos[, endpos]])

Only the first match is identified
'''
print("\nsearch() method\n")
print(pattern.search("dog"))
print(pattern.search("dog", 2))


#* match() method
'''
SYNTAX : <regex_object>.match(string[, pos[, endpos]])

This method only checks for a match at the start of a string
'''
print("\nmatch() method\n")
print(pattern.match("og"))


#* fullmatch() method
'''
SYNTAX : <regex_object>.fullmatch(string[, pos[, endpos]])

This method checks whether the regex_object provided matches 
the string exactly. If not, None is returned. 
'''

print("\nfullmatch() method\n")

pattern_1 = re.compile("o[gh]")
#Here [gh] indicates that either 'g' or 'h' should be present

print(pattern_1.fullmatch("ogre", 0, 2))
print(pattern_1.fullmatch("or"))

'''
match(), search() and fullmatch() return match objects if a match is found
and None data type if not.

truth value of the match object is 1 and that of None is 0,
so it is easy to test whether a match has been found using if statement
'''


#* findall() method
'''
SYNTAX : <regex_object>.findall(string[, pos[, endpos]])

This method returns all strings which contain the pattern/regex_object,
contained in a list
'''
print("\nfindall() method\n")
print(pattern_1.findall("\nog\noh\nog"))


#* finditer() method
'''
finditer() gives us an iterable object containing match objects

SYNTAX : <regex_object>.finditer(string[, pos[, endpos]])
'''
print("\nfinditer() method\n")
print(pattern_1.finditer("\nog\noh\nog"))




#* start() and end() method
print("\nstart() and end() method\n")
'''
The start() and end() method are usable on the objects obtained from 
search(), match(), fullmatch() (MATCH OBJECTS) and 
finditer() (ITERABLE OBJECT containing MATCH OBJECTS)
Note that start() and end() only work when these objects are returned,
not when 'None' datatype is returned by these methods

start() gives us the starting index of the match.

end() gives us the (ending index + 1) of the match.

So we can directly use both these indices in slicing in order to obtain
the matched portion of the string
'''
#! a. methods returning single match object (search(), match() and fullmatch())
string_0 = "hog"
match_object = pattern_1.search(string_0)  #pattern_1 is o[gh]
print(string_0[match_object.start() : match_object.end()],"\n")


#! b. methods returning iterable match object (finditer())
string_1 = "\nog\noh\nog"
iterable_match_object = pattern_1.finditer(string_1)  #pattern_1 is o[gh]
for match in iterable_match_object:
    print(match)
    print(string_1[match.start() : match.end()])