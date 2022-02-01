import re 
'''
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - The word boundary \b matches on a change from a \w (a word character) to a \W a non word character, or from \W to \w.
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String


|       - Either Or
'''



#Matching Brackets
print("\nMatching Brackets\n")
'''
[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets

RANGES like 'a-z' and CHARACTERS like 'a' 'b' 'c' '-' '+' can be placed in these matching brackets []
Inside these brackets, (+?.*) characters don't have special meaning
'''
pattern = re.compile(r"[+-=]\w")

# NOTE that the default quantifier for matching brackets is 1. 
# Meaning if no quantifier is mentioned, then out of all the characters present in the 
# matching brackets, only 1 can be present in the matched string

string = "+=totj"
match_object = pattern.search(string)
print(string[match_object.start() : match_object.end()])


#Group
print("\nGroup\n")
'''
( )     - Group

Capturing groups are a way to treat multiple characters as a single unit. They are created by placing the characters to be grouped inside a set of parentheses.
'''

pattern_0 = re.compile(r"(a-z)")
string_0 = "a-z"
#match_object_0 = pattern._ 
#Quantifiers
print("\nQuantifiers\n")

'''
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)

Quantifiers can be placed after a character or group of characters enclosed in () or [] to indicate 
how many occurrences of the given character or group of characters should be observed in the string.
'''
