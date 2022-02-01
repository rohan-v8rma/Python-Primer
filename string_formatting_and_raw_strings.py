
#*       RAW STRINGS
'''
A Python raw string is a normal string, prefixed with a r or R.
This makes the python interpreter treat characters such as backslash ('\')
as a literal character. 
This also means that this character will not be treated as a escape character.
(An escape sequence is a sequence of characters that does not represent itself
when used inside a character or string literal, but is translated into another
character or a sequence of characters that may be difficult or impossible to
represent directly.
The entire escape sequence is considered as string of length one.)

This is useful compiling regular expression object since a lot of backslashes may be
used in those statements which shouldn't be confused with python escape sequences.

In regular expression objects, we use escape sequences which are specific to regular expressions. 
If we were to use python strings, we would have to denote backslashes using '\\'.
'''
print(r"\n\t")

#*       STRING FORMATTING

'''
WHICH STRING FORMATTING METHOD IS BEST?

f-strings are faster and better than both %-formatting and str.format(). 
f-strings expressions are evaluated are at runtime, and we can also 
embed expressions inside f-string, using a very simple and easy syntax. 
The expressions inside the braces are evaluated in runtime and then 
put together with the string part of the f-string and then 
the final string is returned.
But f-strings are only good for Python 3.6+
'''

#* Formatting strings using f-strings
'''
PEP 498 introduced a new string formatting mechanism known as Literal String Interpolation or 
more commonly as F-strings (because of the leading f character preceding the string literal). 
The idea behind f-strings is to make string interpolation simpler.

To create an f-string, prefix the string with the letter “ f ”. 
The string itself can be formatted in much the same way that you would with str.format(). 
F-strings provide a concise and convenient way to embed python expressions inside string 
literals for formatting.

Just enclose the text you want to be considered as a python expression in curly brackets {}.
'''
print("\nUsing f-strings\n")
#! a. Formatting string with F-Strings

name = "Rohan"

print(f"Hello world, my name is {name}")

#! b. Arithmetic operations using F-strings
'''
If we enclose arithmetic operations within curly brackets in f-strings, they will 
be evaluated.l
'''
num_1 = 20
num_2 = 35

print(f"The average of {num_1} and {num_2} is {(num_1 + num_2)/2}")

#! c. Lambda expressions in F-strings

num_3 = 2
print(f"The output of the function f(x) = x^2 + 2x + 1 at x = {num_3} is {(lambda x : x**2 + 2*x + 1)(num_3)}")

#! d. Float Precision using F-strings

num_4 = 210.3939
print(f"The floating point number is {num_4:.3f}")
#This signifies 3 floating point digits to be represented by rounding, not truncating




#* Formatting strings using format() method
print("\nformat() METHOD\n")
num = [45,46,47]
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "Numbers : {0},{1},{2}".format(num[0], num[1], num[2])
#empty placeholders:
txt4 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)
print(txt4)

#Use "%" to convert the number into a percentage format:

txt = "You scored {:%}"
print(txt.format(0.25))

#Or, without any decimals:

txt = "You scored {:.0%}"
print(txt.format(0.25))

