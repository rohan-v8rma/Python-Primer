'''     
            INDEX
    1. Lambdas
    2. Mapping function
    4. Lambda functions and Mapping combined
    5. Filters
    6. Filters and Lambdas combined
'''
#1. Lambdas
print("\n1. Lambdas\n")
'''
In Python, an anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword in Python, 
anonymous functions are defined using the lambda keyword.
These functions are throw-away functions, i.e. they are just needed where 
they have been created. Lambda functions are mainly used in 
combination with the functions filter(), map() and reduce().

The general syntax of a lambda function is quite simple:
lambda argument_list: expression

The argument list consists of a comma separated list of arguments and the expression 
is an arithmetic expression using these arguments. You can assign the function to a 
variable to give it a name.'''


t = 4
result = (lambda x : x**2)(t)
print(result)
#OR
print((lambda x : x**2)(4))

print((lambda x,y : x-y)(2, 5))
#arguments are specified in a comma separated collection after the lambda function


#2. Easiest way of using Lambdas
print("\n2. Easiest way of using Lambdas\n")

#In this way, arguments can be given similar to functions

result6 = lambda x, y: x + y
print(result6(2,3))


# 3. Mapping function
print("\n3. Mapping function\n")
'''The advantage of the lambda operator can be seen when it is used in combination with 
the map() function. Map() is a function with two arguments:

r = map(<func>, <seq>)

The first argument <func> is the name of a function and the second a sequence 
(e.g. a list) <seq>. ]
map() executes the function <func> with all the elements of the sequence 
<seq> as arguments. 
#! It returns a "map object" with the elements being changed to the 
return values of the function <func>, with the elements passed as arguments.

#! It is necessary that we convert the map object to a list in order to view its elements
'''
def add_2(x):
    return x + 2
list0 = [10, 20, 30, 40 ,50]

result1 = list(map(add_2, list0)) 
print(result1)

result2 = list(map(str, list0)) #str is also a function
print(result2)

result3 = list(map(print, list0))
print(result3)
#* Since print() function doesn't return any value(just uses sys.stdout to display)
#* None values are assigned to all the elements. 
#* But, all the elements of the list are passed as arguments to print(),
#* and then printed during mapping




#4. Lambda functions and Mapping combined
print("\n4. Lambda functions and Mapping combined\n")

list_1 = [4,5,6]
list_2 = [1,2,3,7]

result4 = list(map(lambda x,y : x + y, list_1, list_2))
# Since list_1 and list_2 have different lengths, 
# so the shortest list will be considered as the benchmark length.
# Meaning the result will have only 3 elements

result5 = list(map(lambda x: str(x), list_1))
print(result4)
print(result5)

# 5. Filters
print("\n5. Filters\n")
'''The function filter(<expression>, <list>) offers an elegant way to filter out/choose all 
the elements of <list>, for which the Truth value of the <expression> is 1.
The Truth Value of the <expression> is evaluated for each element of <list>.
'''

#Example:
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]

result7 = filter(lambda x: x % 2, fibonacci)
print(list(result7))
# [1, 1, 3, 5, 13, 21, 55]
# Even numbers are not in this list because their remainders when divided by 2 are 0 
# whose Truth Value is False

result8 = filter(lambda x: x % 2 == 0, fibonacci)
print (list(result8))
# [0, 2, 8, 34]

# 6. Filters and Lambdas combined
print("\n6. Filters and Lambdas combined\n")

second = [1,2,3,4,5,6,7,8]
result5 = list(filter(lambda x : x % 2 == 0, second))
print(result5)


