'''
Frozenset is a new class that has the characteristics of a set, 
but its elements cannot be changed once assigned. While tuples are 
immutable lists, frozensets are immutable sets.

Sets being mutable are unhashable, so they can't be used as 
dictionary keys. On the other hand, frozensets are hashable and 
can be used as keys to a dictionary.

Also sets can't store other sets since sets are mutable as well
'''


frozen_a = frozenset([1,2,3,4])
frozen_b = frozenset([4,5,6,7])
print(frozen_a)
#frozenset() can be used with any iterable (list, tuple, set etc.)
'''
This data type supports methods like copy(), difference(), 
intersection(), isdisjoint(), issubset(), issuperset(), 
symmetric_difference() and union(). 

Being immutable, it does not have methods 
that add or remove elements.

'''