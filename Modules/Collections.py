'''Collections - high performance container data types'''

import collections

#Counter()

count_1 = dict(collections.Counter(['red','blue','red','green']))
count_2 = dict(collections.Counter('fjfskjfsjf')) 
print(count_1)
print(count_2)

#setting count of an element to 0 does not remove it. del removes it entirely

count_1['red'] = 0    #'red' still exists
del count_1['red']    #now 'red' does not exist

#elements()
#this function returns the elements which are listed in that amount and in that order

count_3 = collections.Counter(a = 4, b = 3, c = 2, d = 1)
list1 = list(count_3.elements())
print(list1) 

#most_common()
#whatever argument is given, it will return those many most common elements

count_4 = collections.Counter('fjfskjfsjf')
print(count_4.most_common()[0][1])
print(count_4)
