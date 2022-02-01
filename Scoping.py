#This is our global scope 





#Problems with variables in global scope

'''
Suppose we have a constant which we have to use in two functions.
(In some other languages, it is easy as we can just use const data type)

In python we can't define constants in the same file, we need to keep
constants in a separate .py file and import that file.

(NOTE : We name constants in CAPITALS as a convention so that we don't
by mistake use them with mutating functions)

So, if we keep the constant and the functions, all in the global scope,
it is possible that the value of the constant is mutated by mistake in 
some function, affecting the output of other functions as well. For example:
'''
LIST = ['a','b','c']

def func1():
    LIST.pop()
    #pop() function mutates LIST while keeping it at the same contiguous memory location
    #If we had reassigned LIST, we would still have the original LIST at the other memory location
    #which is why we would receive the original value only as output
def func2():
    print(LIST)
func1()
func2()

'''
The key takeaway from this is to practice scope separation.

Let's see 
'''

def func3():
    #LIST1.pop()
    '''
    Now this command will not work since LIST1 is not in an outer or same scope.
    
    LIST1 is in the local scope of the main(), not in the global scope, 
    where func3() and func4() lie.
    '''
def main():
    LIST1 = ['p','q','r']
    #global LIST1
    #If we write this command, 
# <--- scope of LIST1 will change to here
    func3()
main()