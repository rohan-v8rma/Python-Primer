#      Memory Mutation in Python

# 1. Mutable data types
print("\n1. Mutable data types\n")

variable_1 = ["hello"]
variable_2 = variable_1
variable_2 += ["world"]

print(variable_1)
# Expected Output : ["hello"]
'''We expected this output since we thought variable_2 was a
new separate variable.'''

# Actual Output : ["hello", "world"]

print(variable_2)
# Output : ["hello", "world"]

'''
Whenever you assign a variable to another variable 
of mutable datatype, any changes to the data are 
reflected by both variables. 
The new variable is just an alias for the old variable. 
This is only true for mutable datatypes. 
'''


# 2. Functions and Mutable Data Types
print("\n2. Functions and Mutable data types\n")

def add_to(num, target=[]):
    target.append(num)
    return target

print(add_to(1))
# Expected Output: [1]
# Output: [1]

print(add_to(2))
# Expected Output: [2]
# Output: [1, 2]

print(add_to(3))
# Expected Output: [3]
# Output: [1, 2, 3]

'''In Python the default arguments are evaluated(compiled) once when
the function is defined, not each time the function is called.

We should never define default arguments of mutable type unless
we are aware of this behaviour.
'''

# Solution around this problem

def add_to(element, target = None):
    '''Since this default argument is immutable, 
    it is evaluated everytime we don't enter the second argument'''
    target = []
    target.append(element)
    return target

print(add_to(1))
# Desired Output: [1]
# Output: [1]

print(add_to(2))
# Desired Output: [2]
# Output: [2]