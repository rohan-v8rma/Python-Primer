'''Itertools'''

import itertools

#Product

l1 = [5,4]
l2 = [3,2]
l3 = [6,7]
print(list(itertools.product(l1,l2,l3)))
#returns all possible combinations of arrays selecting one element from each array

#Permutations

list_of_permutation = list(itertools.permutations('abcd', 2))
print(list_of_permutation)

#Combinations with no repetition of elements

list_of_combination = list(itertools.combinations('abcd', 2))
print(list_of_combination)

#Combinations with repetition of elements

list_of_combination_with_repetition = list(itertools.combinations_with_replacement('abcd', 2))
print(list_of_combination_with_repetition)
