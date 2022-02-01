'''
            INDEX
    INTRO - What are *args and **kwargs?
    1. *args variable
    2. **kwargs variable
    3. How to use *args and **kwargs with a list or dictionary.
'''
# What are *args and **kwargs?

'''First of all, it is not necessary to write *args or **kwargs. 
Only the * (asterisk) is necessary. 
We could have also write *var and **vars. 
Writing *args and **kwargs is just a convention. 

They can be called "spreading" or "packing" operators.

*args and **kwargs make the function flexible.
'''

# 1. *args variable
print("\n1. *args variable\n")
'''
*args is used to send a non-keyworded variable length argument list 
to the function.

SYNTAX: def(argument_1, *<variable_name>): ...
'''
def add_all(*list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum += number
    print(sum)

add_all(1, 2, 3, 4)
add_all(23, 21, 4, 14, 61, 99)

'''As we can see, we are entering a variable number 
of arguments into the function, and we are getting no error.'''


# 2. **kwargs variable
print("\n2. **kwargs variable\n")
'''
**kwargs is used to send a keyworded variable length of arguments 
to a function.

SYNTAX: def(argument_1, **<variable_name>): ...
'''
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

greet_me(name_1 = "rohan", name_2 = "soham")


#3. How to use *args and **kwargs with a list or dictionary.
print("\n3. How to use *args and **kwargs with a list or dictionary.\n")
'''
In the cases below, the operators are 'spreading' the sequences.
In cases when they are used in the function definition,
they 'pack' the sequences.
'''

tuple_1 = [1,2,3]
tuple_2 = [4,5,6]

tuple_3 = [*tuple_1, *tuple_2]
print(tuple_3)

dictionary_1 = {"name" : "Rohan"}
dictionary_2 = {"age" : 19, "roll no" : 20}

dictionary_3 = {**dictionary_1, **dictionary_2}
print(dictionary_3)
