string = 'ringa ringa roses'
sub = 'ringa'
string0 = '''She said, "What is your name?"'''
#Using triple quotes in defining a string, we can use quotes in a string and get them printed


'''Concatenating a string'''

print("\nMethods of concatenating a string\n")

'''1. Using concatenation operator(+)'''
print("hello" + "world")
'''2. Using comma separation(,)'''
print("hello", "world")
'''3. Placing strings next to each other'''
print("hello" "world")


'''Unpacking a string'''
a, b, c, d = "spam"
#This will assign each letter of "spam" to the 4 variables
#Giving more or less variables than the number of letters will give an error

print(string0)
string = string.capitalize()
print(string)
#this function capitalizes a string

print(string.find('ringa', 0, 12))
#this function checks the given index range for the given substring
#upper limit not inclusive

string = 'ringaringaringa'
print(string.count('ringa'))
#this function is used to count the occurrences of the substring in the main string
#we can also write the indices we want to check in like (<substring>, <start>, end>)

#1
print('1.',string.isdigit())
#this function checks whether the string contains only digits in the string and returns either true or false

#2
num = "123"
print('2.', num.isdigit())
#this will return True

#3
print('3.', "73".isdecimal())
#4
print('4.', "73.1".isdecimal())
#this command checks whether the string contains a number with base 10, NOT whether the number has a decimal place

#5
print('5.', string.isalnum())
#this function checks the string and returns either true or false

#6
print('6.', string.istitle())
#this function checks whether all words in the string are capitalized or not

#7


string = string.swapcase()
print(string)
#this swaps the case of every letter in a string

string = string.lower()
print(string)
#converts all letters to lower case

print(string.partition('in'))
#this creates a tuple containing 3 elements and the string is divided by the substring
#present in the argument

print(string.count('ringa', 0, 4))
#counts the number of occurrences of a string in a substring

print(string.strip())
#removes any whitespaces before or after string
#can be used as lstrip or rstrip too

print(string.replace('ringa','Ringa'))
#this function replaces every occurrence of the first argument with the second argument

print(string.replace(' ',''))
#Easy way of replacing white spaces.

'''SLICING'''

print("\nSlicing\n")

print(string[2])
#prints character at a specific index. 
#If the index is not in the string, an error is returned >> String Index Out of Range

print(string[0:5])
#prints the substring starting from 0 and upto but NOT INCLUDING 5
#If the index is out of range, no error will be given. If no letters are between that range, a blank line would be printed

print(string[0:5:2])
#prints the substring starting from 0 and upto but NOT INCLUDING 5 
#but it takes every second character


'''Membership Operators and Membership Checking'''

print("\nMembership Operators\n")

print(sub in string)
#returns true or false based on whether substringt is preent on string or not 
'''
startswith() and endswith() are string methods that check the
starting or ending letters of a string.
We get a true or false as a return.

SYNTAX:
<string_name>.startswith(<substring>[,starting_pos [, end_pos]])
Similarly for endswith() method
'''
print(string.startswith("ringa"))
print(string.endswith("RosEs"))


'''Text Alignment'''

print("\nText Alignment\n")
string = 'wassup'

#Aligning text to center

print(string.center(20,'*'))
#the first argument specifies the total width of the original string with the fill characters.
#the second argument is the fill character.
#if no second arguemnt is given, it will assume a space character

#Aligning text to right

print(string.rjust(20))

#Aligning text to left

print(string.ljust(20,'^'))

